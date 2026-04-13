"""Generated component: ProtoFluxOutputListManager."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.type_ import Type
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.proto_flux_node_visual import ProtoFluxNodeVisual
from pyresonitelink.generated._types.isync_list import ISyncList
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProtoFluxOutputListManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The ProtoFluxOutputListManager component is used to manage a list of outputs on a ProtoFlux visual.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.Visuals.ProtoFluxOutputListManager"

    def __init__(self, visual: str | ProtoFluxNodeVisual | None = None, list_: str | ISyncList | None = None, min_elements: primitives.Int | None = None, add_button_enabled: str | IField[primitives.Bool] | None = None, remove_button_enabled: str | IField[primitives.Bool] | None = None, output_type: Type | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            visual: Initial value for Visual.
            list_: Initial value for List.
            min_elements: Initial value for MinElements.
            add_button_enabled: Initial value for AddButtonEnabled.
            remove_button_enabled: Initial value for RemoveButtonEnabled.
            output_type: Initial value for OutputType.
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
        if output_type is not None:
            self.output_type = output_type

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
        """The list this is a visual for."""
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
        """The minimum elements allowed for the list."""
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
        """The enabled field of the add elements button."""
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
        """The enabled field of the remove elements button."""
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
        """A list of slots representing the UIX elements of the list of outputs."""
        member = self.get_member("_elements")
        if isinstance(member, members.SyncList):
            return member
        return None

    @elements.setter
    def elements(self, value: members.SyncList) -> None:
        """Set _elements. A list of slots representing the UIX elements of the list of outputs."""
        self.set_member("_elements", value)

    @property
    def output_type(self) -> Type | None:
        """The C# Type of the list of outputs for the list this is managing."""
        member = self.get_member("OutputType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Type(member.value)
        return None

    @output_type.setter
    def output_type(self, value: Type | str) -> None:
        """Set OutputType. The C# Type of the list of outputs for the list this is managing."""
        member = self.get_member("OutputType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "OutputType",
                members.FieldEnum(value=str(value)),
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

