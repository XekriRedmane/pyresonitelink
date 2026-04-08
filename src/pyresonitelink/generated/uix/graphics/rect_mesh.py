"""Generated component: RectMesh."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RectMesh(GenericComponent[T], IUIComputeComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.RectMesh<>.

    Category: UIX/Graphics

    Parameterize with a value type::

        RectMesh[primitives.Float]
        RectMesh[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.RectMesh<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.UIX.RectMesh<>"

    @property
    def mesh(self) -> members.SyncObject | None:
        """The Mesh member."""
        member = self.get_member("Mesh")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @mesh.setter
    def mesh(self, value: members.SyncObject) -> None:
        """Set the Mesh member."""
        self.set_member("Mesh", value)

    @property
    def materials(self) -> members.SyncList | None:
        """The Materials member."""
        member = self.get_member("Materials")
        if isinstance(member, members.SyncList):
            return member
        return None

    @materials.setter
    def materials(self, value: members.SyncList) -> None:
        """Set the Materials member."""
        self.set_member("Materials", value)

