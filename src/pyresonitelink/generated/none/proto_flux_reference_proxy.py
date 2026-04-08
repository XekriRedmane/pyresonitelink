"""Generated component: ProtoFluxReferenceProxy."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.proto_flux_node import ProtoFluxNode
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.reference_proxy_source import ReferenceProxySource
from pyresonitelink.generated._types.isync_ref import ISyncRef
from pyresonitelink.generated._types.protoflux_arrow_manager import ProtofluxArrowManager
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ivalue import IValue
from pyresonitelink.generated._types.iui_grab_receiver import IUIGrabReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProtoFluxReferenceProxy(GeneratedComponent, IUIGrabReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxReferenceProxy.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxReferenceProxy"

    def __init__(self, node: str | ProtoFluxNode | None = None, element_name: primitives.String | None = None, label: str | IField[primitives.String] | None = None, proxy_visual: str | Button | None = None, ref_proxy_source: str | ReferenceProxySource | None = None, node_reference: str | ISyncRef | None = None, arrow: str | ProtofluxArrowManager | None = None, connect_point: str | Slot | None = None, current_name: str | IValue[primitives.String] | None = None, self_hovering: str | IValue[primitives.Bool] | None = None, target_hovering: str | IValue[primitives.Bool] | None = None, arrow_manager_enabled: str | IField[primitives.Bool] | None = None, arrow_renderer_enabled: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            node: Initial value for Node.
            element_name: Initial value for ElementName.
            label: Initial value for _label.
            proxy_visual: Initial value for _proxyVisual.
            ref_proxy_source: Initial value for _refProxySource.
            node_reference: Initial value for NodeReference.
            arrow: Initial value for Arrow.
            connect_point: Initial value for ConnectPoint.
            current_name: Initial value for _currentName.
            self_hovering: Initial value for _selfHovering.
            target_hovering: Initial value for _targetHovering.
            arrow_manager_enabled: Initial value for _arrowManagerEnabled.
            arrow_renderer_enabled: Initial value for _arrowRendererEnabled.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if node is not None:
            self.node = node
        if element_name is not None:
            self.element_name = element_name
        if label is not None:
            self.label = label
        if proxy_visual is not None:
            self.proxy_visual = proxy_visual
        if ref_proxy_source is not None:
            self.ref_proxy_source = ref_proxy_source
        if node_reference is not None:
            self.node_reference = node_reference
        if arrow is not None:
            self.arrow = arrow
        if connect_point is not None:
            self.connect_point = connect_point
        if current_name is not None:
            self.current_name = current_name
        if self_hovering is not None:
            self.self_hovering = self_hovering
        if target_hovering is not None:
            self.target_hovering = target_hovering
        if arrow_manager_enabled is not None:
            self.arrow_manager_enabled = arrow_manager_enabled
        if arrow_renderer_enabled is not None:
            self.arrow_renderer_enabled = arrow_renderer_enabled

    @property
    def node(self) -> str | None:
        """Target ID of the Node reference (targets ProtoFluxNode)."""
        member = self.get_member("Node")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @node.setter
    def node(self, target: str | ProtoFluxNode | None) -> None:
        """Set the Node reference by target ID or ProtoFluxNode instance."""
        target_id: str | None = target.id if isinstance(target, ProtoFluxNode) else target  # type: ignore[assignment]
        member = self.get_member("Node")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Node",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxNode'),
            )

    @property
    def element_name(self) -> primitives.String | None:
        """The ElementName field value."""
        member = self.get_member("ElementName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @element_name.setter
    def element_name(self, value: primitives.String) -> None:
        """Set the ElementName field value."""
        member = self.get_member("ElementName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ElementName", fields.FieldString(value=value)
            )

    @property
    def value_type(self) -> members.FieldEnum | None:
        """The ValueType member."""
        member = self.get_member("ValueType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @value_type.setter
    def value_type(self, value: members.FieldEnum) -> None:
        """Set the ValueType member."""
        self.set_member("ValueType", value)

    @property
    def label(self) -> str | None:
        """Target ID of the _label reference (targets IField[primitives.String])."""
        member = self.get_member("_label")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @label.setter
    def label(self, target: str | IField[primitives.String] | None) -> None:
        """Set the _label reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_label")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_label",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def proxy_visual(self) -> str | None:
        """Target ID of the _proxyVisual reference (targets Button)."""
        member = self.get_member("_proxyVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @proxy_visual.setter
    def proxy_visual(self, target: str | Button | None) -> None:
        """Set the _proxyVisual reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_proxyVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_proxyVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def ref_proxy_source(self) -> str | None:
        """Target ID of the _refProxySource reference (targets ReferenceProxySource)."""
        member = self.get_member("_refProxySource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ref_proxy_source.setter
    def ref_proxy_source(self, target: str | ReferenceProxySource | None) -> None:
        """Set the _refProxySource reference by target ID or ReferenceProxySource instance."""
        target_id: str | None = target.id if isinstance(target, ReferenceProxySource) else target  # type: ignore[assignment]
        member = self.get_member("_refProxySource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_refProxySource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ReferenceProxySource'),
            )

    @property
    def node_reference(self) -> str | None:
        """Target ID of the NodeReference reference (targets ISyncRef)."""
        member = self.get_member("NodeReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @node_reference.setter
    def node_reference(self, target: str | ISyncRef | None) -> None:
        """Set the NodeReference reference by target ID or ISyncRef instance."""
        target_id: str | None = target.id if isinstance(target, ISyncRef) else target  # type: ignore[assignment]
        member = self.get_member("NodeReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NodeReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ISyncRef'),
            )

    @property
    def arrow(self) -> str | None:
        """Target ID of the Arrow reference (targets ProtofluxArrowManager)."""
        member = self.get_member("Arrow")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @arrow.setter
    def arrow(self, target: str | ProtofluxArrowManager | None) -> None:
        """Set the Arrow reference by target ID or ProtofluxArrowManager instance."""
        target_id: str | None = target.id if isinstance(target, ProtofluxArrowManager) else target  # type: ignore[assignment]
        member = self.get_member("Arrow")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Arrow",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ProtofluxArrowManager'),
            )

    @property
    def connect_point(self) -> str | None:
        """Target ID of the ConnectPoint reference (targets Slot)."""
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
    def current_name(self) -> str | None:
        """Target ID of the _currentName reference (targets IValue[primitives.String])."""
        member = self.get_member("_currentName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_name.setter
    def current_name(self, target: str | IValue[primitives.String] | None) -> None:
        """Set the _currentName reference by target ID or IValue[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IValue) else target  # type: ignore[assignment]
        member = self.get_member("_currentName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IValue<string>'),
            )

    @property
    def self_hovering(self) -> str | None:
        """Target ID of the _selfHovering reference (targets IValue[primitives.Bool])."""
        member = self.get_member("_selfHovering")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @self_hovering.setter
    def self_hovering(self, target: str | IValue[primitives.Bool] | None) -> None:
        """Set the _selfHovering reference by target ID or IValue[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IValue) else target  # type: ignore[assignment]
        member = self.get_member("_selfHovering")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_selfHovering",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IValue<bool>'),
            )

    @property
    def target_hovering(self) -> str | None:
        """Target ID of the _targetHovering reference (targets IValue[primitives.Bool])."""
        member = self.get_member("_targetHovering")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_hovering.setter
    def target_hovering(self, target: str | IValue[primitives.Bool] | None) -> None:
        """Set the _targetHovering reference by target ID or IValue[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IValue) else target  # type: ignore[assignment]
        member = self.get_member("_targetHovering")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetHovering",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IValue<bool>'),
            )

    @property
    def arrow_manager_enabled(self) -> str | None:
        """Target ID of the _arrowManagerEnabled reference (targets IField[primitives.Bool])."""
        member = self.get_member("_arrowManagerEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @arrow_manager_enabled.setter
    def arrow_manager_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _arrowManagerEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_arrowManagerEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_arrowManagerEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def arrow_renderer_enabled(self) -> str | None:
        """Target ID of the _arrowRendererEnabled reference (targets IField[primitives.Bool])."""
        member = self.get_member("_arrowRendererEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @arrow_renderer_enabled.setter
    def arrow_renderer_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _arrowRendererEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_arrowRendererEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_arrowRendererEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

