"""Generated component: RectMesh."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iui_compute_component import IUIComputeComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RectMesh(GenericComponent[T], IUIComputeComponent, IWorldEventReceiver):
    """The RectMesh component takes in a value (either a dynamic value from an IAudioSource, or a min and max float value) and parameters for the generated rect mesh, then renders it onto the UIX.

}}

    Category: UIX/Graphics

    This can be used to make fancy audio visuals from a user's Audio Stream
    Controller.

    Parameterize with a value type::

        RectMesh[primitives.Float]
        RectMesh[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.RectMesh<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.UIX.RectMesh<>"

    @property
    def mesh(self) -> members.SyncObject | None:
        """The mesh parameters used to render this rect mesh."""
        member = self.get_member("Mesh")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @mesh.setter
    def mesh(self, value: members.SyncObject) -> None:
        """Set Mesh. The mesh parameters used to render this rect mesh."""
        self.set_member("Mesh", value)

    @property
    def materials(self) -> members.SyncList | None:
        """The material to render for this rect mesh."""
        member = self.get_member("Materials")
        if isinstance(member, members.SyncList):
            return member
        return None

    @materials.setter
    def materials(self, value: members.SyncList) -> None:
        """Set Materials. The material to render for this rect mesh."""
        self.set_member("Materials", value)

