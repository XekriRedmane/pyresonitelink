"""Generated component: ProtoFluxGlobalRefProxy."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.proto_flux_node import ProtoFluxNode
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.reference_proxy_source import ReferenceProxySource
from pyresonitelink.generated._types.isync_ref import ISyncRef
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.iui_grab_receiver import IUIGrabReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProtoFluxGlobalRefProxy(GeneratedComponent, IUIGrabReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxGlobalRefProxy.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxGlobalRefProxy"

    def __init__(self, node: str | ProtoFluxNode | None = None, element_name: primitives.String | None = None, label: str | IField[primitives.String] | None = None, proxy_visual: str | Button | None = None, ref_proxy_source: str | ReferenceProxySource | None = None, target_global_ref: str | ISyncRef | None = None, current_proxy: str | IGlobalValueProxy | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            node: Initial value for Node.
            element_name: Initial value for ElementName.
            label: Initial value for _label.
            proxy_visual: Initial value for _proxyVisual.
            ref_proxy_source: Initial value for _refProxySource.
            target_global_ref: Initial value for TargetGlobalRef.
            current_proxy: Initial value for _currentProxy.
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
        if target_global_ref is not None:
            self.target_global_ref = target_global_ref
        if current_proxy is not None:
            self.current_proxy = current_proxy

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
    def target_global_ref(self) -> str | None:
        """Target ID of the TargetGlobalRef reference (targets ISyncRef)."""
        member = self.get_member("TargetGlobalRef")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_global_ref.setter
    def target_global_ref(self, target: str | ISyncRef | None) -> None:
        """Set the TargetGlobalRef reference by target ID or ISyncRef instance."""
        target_id: str | None = target.id if isinstance(target, ISyncRef) else target  # type: ignore[assignment]
        member = self.get_member("TargetGlobalRef")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetGlobalRef",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ISyncRef'),
            )

    @property
    def current_proxy(self) -> str | None:
        """Target ID of the _currentProxy reference (targets IGlobalValueProxy)."""
        member = self.get_member("_currentProxy")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_proxy.setter
    def current_proxy(self, target: str | IGlobalValueProxy | None) -> None:
        """Set the _currentProxy reference by target ID or IGlobalValueProxy instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("_currentProxy")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentProxy",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy'),
            )

    async def on_proxy_button_pressed(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Call the OnProxyButtonPressed sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "OnProxyButtonPressed", {"button": button, "eventData": event_data}, debug,
        )

