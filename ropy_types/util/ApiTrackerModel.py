from typing import Dict, List, Literal, TypeAlias, Union

ApiTracker: TypeAlias = Union[Dict[
        Literal["Classes"], List[
            Dict[
                Literal["MemoryCategory"], str 
            ] | Dict[
                Literal["Name"], str
            ] | Dict[
                Literal["Superclass"], str
            ]
        ]
    ], Dict[
        Literal["Enums"], Dict[
            Literal["Name"], str
        ]
    ], Dict[
        Literal["Version"], int
    ]
]