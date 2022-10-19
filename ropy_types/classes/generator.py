from typing import Dict
from ropy_types.util.ApiTrackerModel import ApiTracker, RobloxClass, RobloxClassFunctionParameter, RobloxEnum, RobloxMemberProperty
import re

pytypes: Dict[str, str] = {
    "string": "str",
    "int64": "int",
    "double": "float",
    "Variant": "Any",
    "Function": "Callable[..., Any]",
    "Array": "list[Any]",
    "Tuple": "tuple[Any]",
}

pyenums: Dict[str, str] = {
    "None": "NONE",
    "True": "TRUE",
    "False": "FALSE",
    "Font": "FONT",
    "Platform": "PLATFORM",
    "Status": "STATUS",
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
    def generate_datatype(cls, _datatype: str) -> str:
        # generate datatype
        datatype = f"class {_datatype}:\n"
        datatype += f"\tpass\n\n"

        return datatype;

    @classmethod
    def generate_params(cls, _params: list[RobloxClassFunctionParameter], roblox_class: RobloxClass) -> str:
        # generate params
        params = "self"
        # example: self, a: int, b: str

        for param in _params:
            # check if param['Type']['Name'] is equal to class name
            if param["Type"]["Name"] == roblox_class["Name"]:
                params += f", {param['Name']}: Self"
            else:
                params += f", {param['Name']}: {cls.convert_py_type(param['Type']['Name'])}"

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

        # now we generate the same-named properties
        for member in same_name_properties:
            if member['ValueType']["Name"] == _class["Name"]:
                class_string += f"\t{member['Name']}: Self\n"
                continue;

            class_string += f"\t{re.sub('[^0-9a-zA-Z]+', '', member['Name'])}: {cls.convert_py_type(member['ValueType']['Name'])}\n"

        # check the functions
        for member in _class['Members']:
            if member['MemberType'] != "Function":
                continue;

            # generate the function
            class_string += f"\tdef {member['Name']}({cls.generate_params(member['Parameters'], _class)}):\n\t\tpass\n\n"
        

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
    def generate_string(cls, api_tracker: ApiTracker) -> str:
        # this is the string that will be returned
        generated_string = "from typing_extensions import Self\n"
        generated_string += "from typing import Any, Callable\n"
        generated_string += "from enum import Enum\n\n"

        # add the datatypes
        for datatype in api_tracker['DataTypes']:
            generated_string += cls.generate_datatype(datatype)

        # add the enums
        for enum in api_tracker['Enums']:
            generated_string += cls.generate_enum(enum)

        # add the classes
        for _class in api_tracker["Classes"]:
            generated_string += cls.generate_class(_class)

        return generated_string;