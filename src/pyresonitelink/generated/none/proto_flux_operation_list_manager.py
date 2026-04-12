"""Generated component: ProtoFluxOperationListManager."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.proto_flux_node_visual import ProtoFluxNodeVisual
from pyresonitelink.generated._types.isync_list import ISyncList
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProtoFluxOperationListManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ProtoFluxOperationListManager component is used for the visuals in the Sequence and Async Sequence nodes.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.Visuals.ProtoFluxOperationListManager"

    def __init__(self, visual: str | ProtoFluxNodeVisual | None = None, list_: str | ISyncList | None = None, min_elements: primitives.Int | None = None, add_button_enabled: str | IField[primitives.Bool] | None = None, remove_button_enabled: str | IField[primitives.Bool] | None = None, supports_async: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            visual: Initial value for Visual.
            list_: Initial value for List.
            min_elements: Initial value for MinElements.
            add_button_enabled: Initial value for AddButtonEnabled.
            remove_button_enabled: Initial value for RemoveButtonEnabled.
            supports_async: Initial value for SupportsAsync.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if visual is not None:
            self.visual = visual
        if list_ is not None:
            self.list_ = list_
        if min_elements is not None:
            self.min_elements = min_elements
        if add_button_enabled is not None:
            self.add_button_enabled = add_button_enabled
        if remove_button_enabled is not None:
            self.remove_button_enabled = remove_button_enabled
        if supports_async is not None:
            self.supports_async = supports_async

    @property
    def visual(self) -> str | None:
        """The ProtoFlux visual this is a part of."""
        member = self.get_member("Visual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual.setter
    def visual(self, target: str | ProtoFluxNodeVisual | None) -> None:
        """Set the Visual reference by target ID or ProtoFluxNodeVisual instance."""
        target_id: str | None = target.id if isinstance(target, ProtoFluxNodeVisual) else target  # type: ignore[assignment]
        member = self.get_member("Visual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Visual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxNodeVisual'),
            )

    @property
    def list_(self) -> str | None:
        """The list this is modifying."""
        member = self.get_member("List")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @list_.setter
    def list_(self, target: str | ISyncList | None) -> None:
        """Set the List reference by target ID or ISyncList instance."""
        target_id: str | None = target.id if isinstance(target, ISyncList) else target  # type: ignore[assignment]
        member = self.get_member("List")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "List",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ISyncList'),
            )

    @property
    def min_elements(self) -> primitives.Int | None:
        """The minimum number of items allowed in the list."""
        member = self.get_member("MinElements")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_elements.setter
    def min_elements(self, value: primitives.Int) -> None:
        """Set the MinElements field value."""
        member = self.get_member("MinElements")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinElements", fields.FieldInt(value=value)
            )

    @property
    def add_button_enabled(self) -> str | None:
        """The enabled field of the add element list."""
        member = self.get_member("AddButtonEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @add_button_enabled.setter
    def add_button_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the AddButtonEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("AddButtonEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AddButtonEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def remove_button_enabled(self) -> str | None:
        """The enabled field of the remove element list."""
        member = self.get_member("RemoveButtonEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @remove_button_enabled.setter
    def remove_button_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the RemoveButtonEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("RemoveButtonEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RemoveButtonEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def elements(self) -> members.SyncList | None:
        """The list of UI elements being used to display the elements in ``List``"""
        member = self.get_member("_elements")
        if isinstance(member, members.SyncList):
            return member
        return None

    @elements.setter
    def elements(self, value: members.SyncList) -> None:
        """Set _elements. The list of UI elements being used to display the elements in ``List``"""
        self.set_member("_elements", value)

    @property
    def supports_async(self) -> primitives.Bool | None:
        """Whether the elements support Async input/output."""
        member = self.get_member("SupportsAsync")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @supports_async.setter
    def supports_async(self, value: primitives.Bool) -> None:
        """Set the SupportsAsync field value."""
        member = self.get_member("SupportsAsync")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SupportsAsync", fields.FieldBool(value=value)
            )

    async def add_element(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Called when the add element button is touched.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "AddElement", {"button": button, "eventData": event_data}, debug,
        )

    async def remove_element(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Called when the remove element button is touched.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "RemoveElement", {"button": button, "eventData": event_data}, debug,
        )

