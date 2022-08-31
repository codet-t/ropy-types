from typing import Any, Callable, Optional
from typing_extensions import Self

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .Actor import Actor

class Instance:
    def __init__(self, ClassName: str, Parent: Self | None = None):
        self.ClassName = ClassName
        self.Parent = Parent
        self.Archivable: bool = True
        self.Name: str = ClassName
        self.AncestryChanged = Connectable();
        self.AttributeChanged = Connectable();
        self.Changed = Connectable();
        self.ChildAdded = Connectable();
        self.ChildRemoved = Connectable();
        self.DescendantAdded = Connectable();
        self.DescendantRemoving = Connectable();
        self.Destroying = Connectable();

    @classmethod
    def new(cls, ClassName: str, Parent: Self | None = None) -> Self:
        return Instance(ClassName, Parent)

    def ClearAllChildren(self) -> None:
        pass

    def Clone(self) -> Self:  # type: ignore
        pass

    def Destroy(self) -> None:
        pass

    def FindFirstAncestor(self, InstanceName: str) -> Self | None:
        pass

    def FindFirstAncestorOfClass(self, ClassName: str) -> Self | None:
        pass

    def FindFirstAncestorWhichIsA(self, ClassName: str) -> Self | None:
        pass

    def FindFirstChild(self, InstanceName: str) -> Self | None:
        pass

    def FindFirstChildOfClass(self, ClassName: str) -> Self | None:
        pass

    def FindFirstChildWhichIsA(self, ClassName: str) -> Self | None:
        pass

    def FindFirstDescendant(self, InstanceName: str) -> Self | None:
        pass

    def GetActor(self, Name: str) -> Optional['Actor']:
        pass

    def GetAttribute(self, Name: str) -> Any:
        pass

class Connectable:
    def Connect(self, Function: Callable[[], Any]):
        pass