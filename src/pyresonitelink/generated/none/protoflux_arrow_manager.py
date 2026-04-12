"""Generated component: ProtofluxArrowManager."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ivalue import IValue
from pyresonitelink.generated._types.arrow_mesh import ArrowMesh
from pyresonitelink.generated._types.mesh_renderer import MeshRenderer
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProtofluxArrowManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ProtofluxArrowManager component is used to drive and create the visuals for arrows pointing from/to variables and where they are being used.

    Not usually used by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.ProtofluxArrowManager"

    def __init__(self, connect_node: str | Slot | None = None, target_size: str | IValue[primitives.Float3] | None = None, target_offset: str | IValue[primitives.Float3] | None = None, arrow_mesh: str | ArrowMesh | None = None, renderer: str | MeshRenderer | None = None, target_vector: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            connect_node: Initial value for ConnectNode.
            target_size: Initial value for TargetSize.
            target_offset: Initial value for TargetOffset.
            arrow_mesh: Initial value for _arrowMesh.
            renderer: Initial value for _renderer.
            target_vector: Initial value for _targetVector.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if connect_node is not None:
            self.connect_node = connect_node
        if target_size is not None:
            self.target_size = target_size
        if target_offset is not None:
            self.target_offset = target_offset
        if arrow_mesh is not None:
            self.arrow_mesh = arrow_mesh
        if renderer is not None:
            self.renderer = renderer
        if target_vector is not None:
            self.target_vector = target_vector

    @property
    def connect_node(self) -> str | None:
        """The node the arrow should point to."""
        member = self.get_member("ConnectNode")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @connect_node.setter
    def connect_node(self, target: str | Slot | None) -> None:
        """Set the ConnectNode reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ConnectNode")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ConnectNode",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def target_size(self) -> str | None:
        """The size field of the target."""
        member = self.get_member("TargetSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_size.setter
    def target_size(self, target: str | IValue[primitives.Float3] | None) -> None:
        """Set the TargetSize reference by target ID or IValue[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IValue) else target  # type: ignore[assignment]
        member = self.get_member("TargetSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IValue<float3>'),
            )

    @property
    def target_offset(self) -> str | None:
        """The offset field of the target."""
        member = self.get_member("TargetOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_offset.setter
    def target_offset(self, target: str | IValue[primitives.Float3] | None) -> None:
        """Set the TargetOffset reference by target ID or IValue[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IValue) else target  # type: ignore[assignment]
        member = self.get_member("TargetOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IValue<float3>'),
            )

    @property
    def arrow_mesh(self) -> str | None:
        """The arrow mesh this is modifying."""
        member = self.get_member("_arrowMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @arrow_mesh.setter
    def arrow_mesh(self, target: str | ArrowMesh | None) -> None:
        """Set the _arrowMesh reference by target ID or ArrowMesh instance."""
        target_id: str | None = target.id if isinstance(target, ArrowMesh) else target  # type: ignore[assignment]
        member = self.get_member("_arrowMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_arrowMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ArrowMesh'),
            )

    @property
    def renderer(self) -> str | None:
        """The renderer rendering ``_arrowMesh``"""
        member = self.get_member("_renderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @renderer.setter
    def renderer(self, target: str | MeshRenderer | None) -> None:
        """Set the _renderer reference by target ID or MeshRenderer instance."""
        target_id: str | None = target.id if isinstance(target, MeshRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_renderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_renderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MeshRenderer'),
            )

    @property
    def target_vector(self) -> str | None:
        """The field for the target vector on the arrow mesh."""
        member = self.get_member("_targetVector")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_vector.setter
    def target_vector(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _targetVector reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_targetVector")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetVector",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

