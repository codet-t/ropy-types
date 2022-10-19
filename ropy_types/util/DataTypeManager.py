from ropy_types.util.ApiTrackerModel import ApiTracker

class DataTypeManager:
    @classmethod
    def get(cls, api_tracker: ApiTracker) -> list[str]:
        datatypes: list[str] = [];

        for _class in api_tracker["Classes"]:
            for _member in _class["Members"]:
                if _member["MemberType"] == "Property":
                    if _member["ValueType"]["Category"] == "DataType":
                        if _member["ValueType"]["Name"] not in datatypes:
                            datatypes.append(_member["ValueType"]["Name"]);
                            
        return datatypes;