"""Generated component: ProtoFluxWireManager."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.wire_type import WireType
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.stripe_wire_mesh import StripeWireMesh
from pyresonitelink.generated._types.mesh_renderer import MeshRenderer
from pyresonitelink.generated._types.mesh_collider import MeshCollider
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProtoFluxWireManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ProtoFluxWireManager component is used to drive the visual elements of protoflux wires which connect protoflux nodes.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxWireManager"

    def __init__(self, connect_point: str | Slot | None = None, type_: WireType | str | None = None, width: primitives.Float | None = None, start_color: primitives.ColorX | None = None, end_color: primitives.ColorX | None = None, delete_highlight: primitives.Bool | None = None, wire_mesh: str | StripeWireMesh | None = None, renderer: str | MeshRenderer | None = None, collider: str | MeshCollider | None = None, target_position: str | IField[primitives.Float3] | None = None, target_tangent: str | IField[primitives.Float3] | None = None, target_orientation: str | IField[primitives.FloatQ] | None = None, target_width: str | IField[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            connect_point: Initial value for ConnectPoint.
            type_: Initial value for Type.
            width: Initial value for Width.
            start_color: Initial value for StartColor.
            end_color: Initial value for EndColor.
            delete_highlight: Initial value for DeleteHighlight.
            wire_mesh: Initial value for _wireMesh.
            renderer: Initial value for _renderer.
            collider: Initial value for _collider.
            target_position: Initial value for _targetPosition.
            target_tangent: Initial value for _targetTangent.
            target_orientation: Initial value for _targetOrientation.
            target_width: Initial value for _targetWidth.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if connect_point is not None:
            self.connect_point = connect_point
        if type_ is not None:
            self.type_ = type_
        if width is not None:
            self.width = width
        if start_color is not None:
            self.start_color = start_color
        if end_color is not None:
            self.end_color = end_color
        if delete_highlight is not None:
            self.delete_highlight = delete_highlight
        if wire_mesh is not None:
            self.wire_mesh = wire_mesh
        if renderer is not None:
            self.renderer = renderer
        if collider is not None:
            self.collider = collider
        if target_position is not None:
            self.target_position = target_position
        if target_tangent is not None:
            self.target_tangent = target_tangent
        if target_orientation is not None:
            self.target_orientation = target_orientation
        if target_width is not None:
            self.target_width = target_width

    @property
    def connect_point(self) -> str | None:
        """The point this is supposed to be pointing to."""
        member = self.get_member("ConnectPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @connect_point.setter
    def connect_point(self, target: str | Slot | None) -> None:
        """Set the ConnectPoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ConnectPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ConnectPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def type_(self) -> WireType | None:
        """The type of wire this is supposed to be showing."""
        member = self.get_member("Type")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return WireType(member.value)
        return None

    @type_.setter
    def type_(self, value: WireType | str) -> None:
        """Set Type. The type of wire this is supposed to be showing."""
        member = self.get_member("Type")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Type",
                members.FieldEnum(value=str(value)),
            )

    @property
    def width(self) -> primitives.Float | None:
        """The width this wire should be."""
        member = self.get_member("Width")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @width.setter
    def width(self, value: primitives.Float) -> None:
        """Set the Width field value."""
        member = self.get_member("Width")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Width", fields.FieldFloat(value=value)
            )

    @property
    def start_color(self) -> primitives.ColorX | None:
        """The color this wire should start at. usually used for async impulse wires."""
        member = self.get_member("StartColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @start_color.setter
    def start_color(self, value: primitives.ColorX) -> None:
        """Set the StartColor field value."""
        member = self.get_member("StartColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StartColor", fields.FieldColorX(value=value)
            )

    @property
    def end_color(self) -> primitives.ColorX | None:
        """The end color this wire should end at. usually used for async impulse wires."""
        member = self.get_member("EndColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @end_color.setter
    def end_color(self, value: primitives.ColorX) -> None:
        """Set the EndColor field value."""
        member = self.get_member("EndColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EndColor", fields.FieldColorX(value=value)
            )

    @property
    def delete_highlight(self) -> primitives.Bool | None:
        """Whether to delete the highlight visual."""
        member = self.get_member("DeleteHighlight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @delete_highlight.setter
    def delete_highlight(self, value: primitives.Bool) -> None:
        """Set the DeleteHighlight field value."""
        member = self.get_member("DeleteHighlight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DeleteHighlight", fields.FieldBool(value=value)
            )

    @property
    def wire_mesh(self) -> str | None:
        """The stripe mesh this is modifying."""
        member = self.get_member("_wireMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @wire_mesh.setter
    def wire_mesh(self, target: str | StripeWireMesh | None) -> None:
        """Set the _wireMesh reference by target ID or StripeWireMesh instance."""
        target_id: str | None = target.id if isinstance(target, StripeWireMesh) else target  # type: ignore[assignment]
        member = self.get_member("_wireMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_wireMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.StripeWireMesh'),
            )

    @property
    def renderer(self) -> str | None:
        """The renderer of the stripe mesh this is modifying."""
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
    def collider(self) -> str | None:
        """The collider of this stripe mesh visual."""
        member = self.get_member("_collider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider.setter
    def collider(self, target: str | MeshCollider | None) -> None:
        """Set the _collider reference by target ID or MeshCollider instance."""
        target_id: str | None = target.id if isinstance(target, MeshCollider) else target  # type: ignore[assignment]
        member = self.get_member("_collider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_collider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MeshCollider'),
            )

    @property
    def target_position(self) -> str | None:
        """The field to drive with the target position for the stripe mesh."""
        member = self.get_member("_targetPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_position.setter
    def target_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _targetPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_targetPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def target_tangent(self) -> str | None:
        """The field to drive with the target tangent for the stripe mesh."""
        member = self.get_member("_targetTangent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_tangent.setter
    def target_tangent(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _targetTangent reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_targetTangent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetTangent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def target_orientation(self) -> str | None:
        """The field to drive with the target orientation for the stripe mesh."""
        member = self.get_member("_targetOrientation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_orientation.setter
    def target_orientation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _targetOrientation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_targetOrientation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetOrientation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def target_width(self) -> str | None:
        """The field to drive with the target width for the stripe mesh."""
        member = self.get_member("_targetWidth")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_width.setter
    def target_width(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the _targetWidth reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_targetWidth")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetWidth",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

