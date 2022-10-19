from typing import List, Literal, TypeAlias, TypedDict

ThreadSafetyType: TypeAlias = Literal["None", "ReadOnly", "ReadWrite"]

class RobloxType(TypedDict):
    Name: str
    Category: str

class RobloxMemberSecurity(TypedDict):
    Read: Literal["PluginSecurity", "RobloxScriptSecurity", "LocalUserSecurity", "RobloxSecurity", "None"]
    Write: Literal["PluginSecurity", "RobloxScriptSecurity", "LocalUserSecurity", "RobloxSecurity", "None"]

class RobloxSerializationType(TypedDict):
    CanLoad: bool
    CanSave: bool

class RobloxMemberProperty(TypedDict):
    MemberType: Literal["Property"]
    Category: str
    Name: str
    Security: RobloxMemberSecurity
    Tags: List[str]
    ThreadSafety: ThreadSafetyType
    ValueType: RobloxType
    Serialization: RobloxSerializationType

class RobloxClassFunctionParameter(TypedDict):
    Name: str
    Type: RobloxType

class RobloxMemberFunction(TypedDict):
    MemberType: Literal["Function"]
    Name: str
    Parameters: List[RobloxClassFunctionParameter]
    Security: Literal["None"] | RobloxMemberSecurity
    ThreadSafety: ThreadSafetyType
    ReturnType: RobloxType

class RobloxMemberEvent(TypedDict):
    MemberType: Literal["Event"]
    Name: str
    Parameters: List[RobloxClassFunctionParameter]
    Security: Literal["None"] | RobloxMemberSecurity
    ThreadSafety: ThreadSafetyType

class RobloxMemberCallback(TypedDict):
    MemberType: Literal["Callback"]
    Name: str
    Parameters: List[RobloxClassFunctionParameter]
    Security: Literal["None"] | RobloxMemberSecurity
    ThreadSafety: ThreadSafetyType
    ReturnType: RobloxType

class RobloxClass(TypedDict):
    Members: List[RobloxMemberFunction | RobloxMemberProperty | RobloxMemberCallback | RobloxMemberEvent]
    MemoryCategory: str
    Name: str
    Superclass: str
    Tags: List[str] | None

class SingleEnum(TypedDict):
    Name: str
    Value: int

class RobloxEnum(TypedDict):
    Name: str
    Items: List[SingleEnum]

class ApiTracker(TypedDict):
    Classes: List[RobloxClass]
    Enums: List[RobloxEnum]
    DataTypes: List[str]
    Version: int