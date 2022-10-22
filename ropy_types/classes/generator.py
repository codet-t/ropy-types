from ropy_types.util.ApiTrackerModel import ApiTracker, RobloxClass, RobloxClassFunctionParameter, RobloxEnum, RobloxMemberFunction, RobloxMemberProperty
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
    "Tuple": "tuple[Any]",
    "void": "None",
    "Dictionary": "dict[Any, Any]",
    "Objects": "list[Instance]", # special case because Instance could also be Self,
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
    def get_class_by_name(cls, name: str, api_tracker: ApiTracker ) -> RobloxClass | None:
        return next((roblox_class for roblox_class in api_tracker["Classes"] if roblox_class["Name"] == name), None)

    @classmethod
    def generate_class(cls, _class: RobloxClass, api_tracker: ApiTracker) -> str:
        # generate the class
        class_string = f"class {_class['Name']}"
        if _class["Superclass"] == "<<<ROOT>>>":
            class_string += f":\n"
        else:
            class_string += f"({_class['Superclass']}):\n"

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
                class_string += f"\t{member['Name']}: '{_class['Name']}'\n"
                continue;

            class_string += f"\t{re.sub('[^0-9a-zA-Z]+', '', member['Name'])}: {cls.convert_py_type(member['ValueType']['Name'])}\n"

        same_name_properties_names: list[str] = [];
        # now we generate the same-named properties
        for member in same_name_properties:
            same_name_properties_names.append(member["Name"]);

            if member['ValueType']["Name"] == _class["Name"]:
                class_string += f"\t{member['Name']}: '{_class['Name']}'\n"
                continue;

            class_string += f"\t{re.sub('[^0-9a-zA-Z]+', '', member['Name'])}: {cls.convert_py_type(member['ValueType']['Name'])}\n"

        if(_class["Name"] == "Instance"):
            # @classmethod
            #    def new(cls, className: str, parent: Self | None = None) -> Any:
            #       if not className in __InstanceClasses__:
			#           raise Exception(f"Invalid class name: {className}")
            #       return __InstanceClasses__[className]()
		
            class_string += f"\t@classmethod\n"
            class_string += f"\tdef new(cls, className: str, parent: Self | None = None) -> Any:\n"
            class_string += f"\t\tif not className in __InstanceClasses__:\n"
            class_string += f"\t\t\traise Exception(f\"Invalid class name: {{className}}\")\n"
            class_string += f"\t\treturn __InstanceClasses__[className]()\n\n"

        # check the functions
        for member in _class['Members']:
            if member['MemberType'] != "Function":
                continue;
            
            # generate the function
            class_string += f"\t@abstractmethod\n"
            class_string += f"\tdef {member['Name']}"
            
            if cls.is_method_overloading(_class, api_tracker, member):
                class_string += f"{_class['Name']}"

            class_string += f"({cls.generate_params(member['Parameters'], _class, same_name_properties_names)})"

            # check if member['ReturnType']['Name'] is equal to class name
            # special case:
            if member['ReturnType']['Name'] == "Objects":
                if _class['Name'] == "Instance":
                    class_string += f" -> list[Self]"
                else:
                    class_string += f" -> list[Instance]"
            elif member["ReturnType"]["Name"] == _class["Name"]:
                class_string += f" -> Self"
            else:
                if cls.convert_py_type(member['ReturnType']['Name']) in same_name_properties_names:
                    class_string += f" -> '{cls.convert_py_type(member['ReturnType']['Name'])}'"
                else:
                    class_string += f" -> {cls.convert_py_type(member['ReturnType']['Name'])}"

            class_string += ":"

            if cls.is_method_overloading(_class, api_tracker, member):
                class_string += f" # Overloading + Overriding"

            class_string += "\n\t\tpass\n\n"
        

        # add a pass
        class_string += "\n\tpass\n\n"

        # return the class
        return class_string

    @classmethod
    def issubclass(cls, api_tracker: ApiTracker, roblox_class: RobloxClass, superclass_name: str) -> bool:
        superclass = cls.get_class_by_name(roblox_class["Superclass"], api_tracker);
        is_instance = False;
                
        while superclass and superclass["Name"] != superclass_name:
            superclass = cls.get_class_by_name(superclass["Superclass"], api_tracker);

        if superclass and superclass["Name"] == superclass_name:
            is_instance = True;

        return is_instance

    @classmethod
    def is_method_overloading(cls, _class: RobloxClass, api_tracker: ApiTracker, member: RobloxMemberFunction) -> bool:
        parent_class = cls.get_class_by_name(_class["Superclass"], api_tracker)
        parent_method_found = False
        while parent_class is not None and not parent_method_found:
            for parent_member in parent_class["Members"]:
                if parent_member["MemberType"] != "Function":
                    continue;

                if parent_member["Name"] != member["Name"]:
                    continue;

                    # check if the parameters are the same of the parent class's function member
                if len(parent_member["Parameters"]) != len(member["Parameters"]):
                    parent_method_found = True;
                    return True;
                
            parent_class = cls.get_class_by_name(parent_class["Superclass"], api_tracker)

        return False

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
    def generate_instance_classes_map(cls, api_tracker: ApiTracker) -> str:
        # generate the instance classes map
        instance_classes_map_string = "__InstanceClasses__: dict[str, Type[Instance]] = {\n"

        for roblox_class in api_tracker["Classes"]:
            # check if the class is an instance
            is_instance = cls.issubclass(api_tracker, roblox_class, "Instance")

            if is_instance:
                instance_classes_map_string += f"\t\"{roblox_class['Name']}\":"
                instance_classes_map_string += f" {roblox_class['Name']},\n"

        instance_classes_map_string += "}\n\n"

        return instance_classes_map_string

    @classmethod
    def generate_builtin_variables(cls, api_tracker: ApiTracker) -> str:
        # workspace = Workspace()
        # script = LuaSourceContainer()
        # game = DataModel()
        # shared = Array()
        # plugin = Plugin()

        result = "workspace: Workspace = Workspace()\n"
        result += "script: LuaSourceContainer = LuaSourceContainer()\n"
        result += "game: DataModel = DataModel()\n"
        result += "shared: Array = Array()\n"
        result += "plugin: Plugin = Plugin()\n"
        result += "\n"

        return result;

    @classmethod
    def generate_string(cls, api_tracker: ApiTracker) -> str:
        # this is the string that will be returned
        api_tracker = cls.sort_model(api_tracker)
        generated_string = "from typing_extensions import Self\n"
        generated_string += "from typing import Any, Callable, Type\n"
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
            generated_string += cls.generate_class(_class, api_tracker)
        
        generated_string += cls.generate_instance_classes_map(api_tracker)
        generated_string += cls.generate_builtin_variables(api_tracker)

        return generated_string;