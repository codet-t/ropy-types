from ropy_types.util.ApiTrackerModel import ApiTracker, RobloxClass, RobloxClassFunctionParameter, RobloxEnum, RobloxMemberProperty
import re

primitive_types: list[str] = [
    "bool",
    "int",
    "float",
    "double",
    "string",
    "void",
]

pytypes: dict[str, str] = {
    "string": "str",
    "int64": "int",
    "double": "float",
    "Variant": "Any",
    "Function": "Callable[..., Any]",
    "Array": "list[Any]",
    "Tuple": "tuple[Any]",
    "void": "None",
    "Dictionary": "dict[Any, Any]",
    "Objects": "dict[int, Instance]", # special case because Instance could also be Self,
}

pyenums: dict[str, str] = {
    "None": "NONE",
    "True": "TRUE",
    "False": "FALSE",
    "Font": "FONT",
    "Platform": "PLATFORM",
    "Status": "STATUS",
}

py_keywords: dict[str, str] = {
    "class": "className",
    "from": "from_",
}

class Generator:
    @classmethod
    def convert_py_type(cls, _type: str) -> str:
        if _type in pytypes:
            return pytypes[_type]

        return _type
    
    @classmethod
    def convert_py_enum(cls, _enum: str) -> str:
        if _enum in pyenums:
            return pyenums[_enum]

        return _enum
    
    @classmethod
    def convert_py_keyword(cls, _keyword: str) -> str:
        if _keyword in py_keywords:
            return py_keywords[_keyword]

        return _keyword

    @classmethod
    def generate_datatype(cls, _datatype: str) -> str:
        # generate datatype
        datatype = f"class {_datatype}:\n"
        datatype += f"\tpass\n\n"

        return datatype;

    @classmethod
    def generate_params(cls, _params: list[RobloxClassFunctionParameter], roblox_class: RobloxClass, properties_with_the_same_name_as_class: list[str]) -> str:
        # generate params
        params = "self"
        # example: self, a: int, b: str

        for param in _params:
            # check if param['Type']['Name'] is equal to class name
            if param["Type"]["Name"] == roblox_class["Name"]:
                params += f", {param['Name']}: Self"
            else:
                if cls.convert_py_type(param['Type']['Name']) in properties_with_the_same_name_as_class:
                    params += f", {cls.convert_py_keyword(param['Name'])}: '{cls.convert_py_type(param['Type']['Name'])}'"
                else:
                    params += f", {cls.convert_py_keyword(param['Name'])}: {cls.convert_py_type(param['Type']['Name'])}"

        return params

    @classmethod
    def generate_class(cls, _class: RobloxClass) -> str:
        # generate the class
        class_string = f"class {_class['Name']}:\n"

        # check the properties first
        same_name_properties: list[RobloxMemberProperty] = [];

        for member in _class['Members']:
            if member['MemberType'] != "Property":
                continue;

            if member["Name"] == member['ValueType']["Name"]:
                same_name_properties.append(member)
                continue;

            # generate the property
            if member['ValueType']["Name"] == _class["Name"]:
                class_string += f"\t{member['Name']}: Self\n"
                continue;

            class_string += f"\t{re.sub('[^0-9a-zA-Z]+', '', member['Name'])}: {cls.convert_py_type(member['ValueType']['Name'])}\n"

        same_name_properties_names: list[str] = [];
        # now we generate the same-named properties
        for member in same_name_properties:
            same_name_properties_names.append(member["Name"]);

            if member['ValueType']["Name"] == _class["Name"]:
                class_string += f"\t{member['Name']}: Self\n"
                continue;

            class_string += f"\t{re.sub('[^0-9a-zA-Z]+', '', member['Name'])}: {cls.convert_py_type(member['ValueType']['Name'])}\n"

        # check the functions
        for member in _class['Members']:
            if member['MemberType'] != "Function":
                continue;
            
            # generate the function
            class_string += f"\t@abstractmethod\n"
            class_string += f"\tdef {member['Name']}({cls.generate_params(member['Parameters'], _class, same_name_properties_names)})"

            # check if member['ReturnType']['Name'] is equal to class name
            # special case:
            if member['ReturnType']['Name'] == "Objects":
                if _class['Name'] == "Instance":
                    class_string += f" -> dict[int, Self]"
                else:
                    class_string += f" -> dict[int, Instance]"
            elif member["ReturnType"]["Name"] == _class["Name"]:
                class_string += f" -> Self"
            else:
                if cls.convert_py_type(member['ReturnType']['Name']) in same_name_properties_names:
                    class_string += f" -> '{cls.convert_py_type(member['ReturnType']['Name'])}'"
                else:
                    class_string += f" -> {cls.convert_py_type(member['ReturnType']['Name'])}"
            class_string += ":\n\t\tpass\n\n"
        

        # add a pass
        class_string += "\n\tpass\n\n"

        # return the class
        return class_string

    @classmethod
    def generate_enum(cls, _enum: RobloxEnum) -> str:
        # generate the enum
        enum_string = f"class {cls.convert_py_enum(_enum['Name'])}(Enum):\n"

        # generate the items
        for member in _enum['Items']:
            enum_string += f"\t{cls.convert_py_enum(member['Name'])} = {member['Value']}\n"

        # add a pass
        enum_string += "\tpass\n\n"

        # return the enum
        return enum_string

    @classmethod
    def sort_model(cls, api_tracker: ApiTracker) -> ApiTracker:
        # sort classes such that only known classes are used inside of the class
        
        enum_names: list[str] = [];
        
        for enum in api_tracker['Enums']:
            enum_names.append(cls.convert_py_enum(enum['Name']))
        
        pytypes_names: list[str] = [];

        for pytype in pytypes:
            pytypes_names.append(pytype)

        known_classes: list[str] = primitive_types + api_tracker["DataTypes"] + enum_names + pytypes_names;
        all_mentioned: list[str] = [];

        for roblox_class in api_tracker["Classes"]:
            # check if any of its properties use unknown classes
            known_classes.append(roblox_class['Name'])

            for member in roblox_class['Members']:
                if member['MemberType'] != "Property":
                    continue;
                all_mentioned.append(member['ValueType']['Name'])

                if "?" in member['ValueType']['Name']:
                    member['ValueType']['Name'] = member['ValueType']['Name'].replace("?", "")
                    member['ValueType']['Name'] += "| None"
                    continue;

                if member['ValueType']['Name'] not in known_classes:
                    member['ValueType']['Name'] = "'" + member['ValueType']['Name'] + "'"
            
            # check if any of its functions use unknown classes
            for member in roblox_class['Members']:
                if member['MemberType'] != "Function":
                    continue;
                all_mentioned.append(member['ReturnType']['Name'])

                if "?" in member['ReturnType']['Name']:
                    member['ReturnType']['Name'] = member['ReturnType']['Name'].replace("?", "")
                    member['ReturnType']['Name'] += "| None"
                    continue;

                if member['ReturnType']['Name'] not in known_classes:
                    member['ReturnType']['Name'] = "'" + member['ReturnType']['Name'] + "'"

                for param in member['Parameters']:
                    all_mentioned.append(param['Type']['Name'])

                    if "?" in param['Type']['Name']:
                        param['Type']['Name'] = param['Type']['Name'].replace("?", "")
                        param['Type']['Name'] += "| None"
                        continue;

                    if param['Type']['Name'] not in known_classes:
                        param['Type']['Name'] = "'" + param['Type']['Name'] + "'"
            
            # check if any of its events use unknown classes
            for member in roblox_class['Members']:
                if member['MemberType'] != "Event":
                    continue;

                for param in member['Parameters']:
                    all_mentioned.append(param['Type']['Name'])

                    if "?" in param['Type']['Name']:
                        param['Type']['Name'] = param['Type']['Name'].replace("?", "")
                        param['Type']['Name'] += "| None"
                        continue;

                    if param['Type']['Name'] not in known_classes:
                        param['Type']['Name'] = "'" + param['Type']['Name'] + "'"

        # loop through all_mentioned and remove "?" if it exists
        for i in range(len(all_mentioned)):
            if "?" in all_mentioned[i]:
                all_mentioned[i] = all_mentioned[i].replace("?", "")

        # get all unknown classes
        unknown_classes: list[str] = [];

        for mentioned in all_mentioned:
            if mentioned not in known_classes and mentioned not in unknown_classes:
                unknown_classes.append(mentioned)

        api_tracker["RemainingClasses"] = unknown_classes

        return api_tracker;

    @classmethod
    def generate_string(cls, api_tracker: ApiTracker) -> str:
        # this is the string that will be returned
        api_tracker = cls.sort_model(api_tracker)
        generated_string = "from typing_extensions import Self\n"
        generated_string += "from typing import Any, Callable\n"
        generated_string += "from abc import abstractmethod\n"
        generated_string += "from enum import Enum\n\n"

        # add the datatypes
        for datatype in api_tracker['DataTypes']:
            generated_string += cls.generate_datatype(datatype)

        # add the remaining classes
        for remaining_class in api_tracker['RemainingClasses']:
            generated_string += cls.generate_datatype(remaining_class)

        # add the enums
        for enum in api_tracker['Enums']:
            generated_string += cls.generate_enum(enum)

        # add the classes
        for _class in api_tracker["Classes"]:
            generated_string += cls.generate_class(_class)

        return generated_string;