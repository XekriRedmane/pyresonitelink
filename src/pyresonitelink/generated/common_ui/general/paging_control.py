"""Generated component: PagingControl."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PagingControl(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.PagingControl.

    Category: Common UI/General
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PagingControl"

    def __init__(self, items_per_page: primitives.Int | None = None, total_items: primitives.Int | None = None, has_more_items: primitives.Bool | None = None, skip_items: primitives.Int | None = None, no_items_label: primitives.String | None = None, paging_info_label: primitives.String | None = None, total_pages: primitives.Int | None = None, remaining_items: primitives.Int | None = None, label: str | IField[primitives.String] | None = None, previous_enabled: str | IField[primitives.Bool] | None = None, next_enabled: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            items_per_page: Initial value for ItemsPerPage.
            total_items: Initial value for TotalItems.
            has_more_items: Initial value for HasMoreItems.
            skip_items: Initial value for SkipItems.
            no_items_label: Initial value for NoItemsLabel.
            paging_info_label: Initial value for PagingInfoLabel.
            total_pages: Initial value for TotalPages.
            remaining_items: Initial value for RemainingItems.
            label: Initial value for _label.
            previous_enabled: Initial value for _previousEnabled.
            next_enabled: Initial value for _nextEnabled.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if items_per_page is not None:
            self.items_per_page = items_per_page
        if total_items is not None:
            self.total_items = total_items
        if has_more_items is not None:
            self.has_more_items = has_more_items
        if skip_items is not None:
            self.skip_items = skip_items
        if no_items_label is not None:
            self.no_items_label = no_items_label
        if paging_info_label is not None:
            self.paging_info_label = paging_info_label
        if total_pages is not None:
            self.total_pages = total_pages
        if remaining_items is not None:
            self.remaining_items = remaining_items
        if label is not None:
            self.label = label
        if previous_enabled is not None:
            self.previous_enabled = previous_enabled
        if next_enabled is not None:
            self.next_enabled = next_enabled

    @property
    def items_per_page(self) -> primitives.Int | None:
        """The ItemsPerPage field value."""
        member = self.get_member("ItemsPerPage")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @items_per_page.setter
    def items_per_page(self, value: primitives.Int) -> None:
        """Set the ItemsPerPage field value."""
        member = self.get_member("ItemsPerPage")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ItemsPerPage", fields.FieldInt(value=value)
            )

    @property
    def total_items(self) -> primitives.Int | None:
        """The TotalItems field value."""
        member = self.get_member("TotalItems")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_items.setter
    def total_items(self, value: primitives.Int) -> None:
        """Set the TotalItems field value."""
        member = self.get_member("TotalItems")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalItems", fields.FieldInt(value=value)
            )

    @property
    def has_more_items(self) -> primitives.Bool | None:
        """The HasMoreItems field value."""
        member = self.get_member("HasMoreItems")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @has_more_items.setter
    def has_more_items(self, value: primitives.Bool) -> None:
        """Set the HasMoreItems field value."""
        member = self.get_member("HasMoreItems")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HasMoreItems", fields.FieldBool(value=value)
            )

    @property
    def skip_items(self) -> primitives.Int | None:
        """The SkipItems field value."""
        member = self.get_member("SkipItems")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @skip_items.setter
    def skip_items(self, value: primitives.Int) -> None:
        """Set the SkipItems field value."""
        member = self.get_member("SkipItems")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SkipItems", fields.FieldInt(value=value)
            )

    @property
    def no_items_label(self) -> primitives.String | None:
        """The NoItemsLabel field value."""
        member = self.get_member("NoItemsLabel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @no_items_label.setter
    def no_items_label(self, value: primitives.String) -> None:
        """Set the NoItemsLabel field value."""
        member = self.get_member("NoItemsLabel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoItemsLabel", fields.FieldString(value=value)
            )

    @property
    def paging_info_label(self) -> primitives.String | None:
        """The PagingInfoLabel field value."""
        member = self.get_member("PagingInfoLabel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @paging_info_label.setter
    def paging_info_label(self, value: primitives.String) -> None:
        """Set the PagingInfoLabel field value."""
        member = self.get_member("PagingInfoLabel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PagingInfoLabel", fields.FieldString(value=value)
            )

    @property
    def total_pages(self) -> primitives.Int | None:
        """The TotalPages field value."""
        member = self.get_member("TotalPages")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_pages.setter
    def total_pages(self, value: primitives.Int) -> None:
        """Set the TotalPages field value."""
        member = self.get_member("TotalPages")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalPages", fields.FieldInt(value=value)
            )

    @property
    def remaining_items(self) -> primitives.Int | None:
        """The RemainingItems field value."""
        member = self.get_member("RemainingItems")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @remaining_items.setter
    def remaining_items(self, value: primitives.Int) -> None:
        """Set the RemainingItems field value."""
        member = self.get_member("RemainingItems")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RemainingItems", fields.FieldInt(value=value)
            )

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
    def previous_enabled(self) -> str | None:
        """Target ID of the _previousEnabled reference (targets IField[primitives.Bool])."""
        member = self.get_member("_previousEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @previous_enabled.setter
    def previous_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _previousEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_previousEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_previousEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def next_enabled(self) -> str | None:
        """Target ID of the _nextEnabled reference (targets IField[primitives.Bool])."""
        member = self.get_member("_nextEnabled")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @next_enabled.setter
    def next_enabled(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _nextEnabled reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_nextEnabled")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_nextEnabled",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    async def next_page(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Call the NextPage sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "NextPage", {"button": button, "eventData": event_data}, debug,
        )

    async def previous_page(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Call the PreviousPage sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PreviousPage", {"button": button, "eventData": event_data}, debug,
        )

    async def next_page_0(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the NextPage sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "NextPage", {}, debug,
        )

    async def previous_page_0(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the PreviousPage sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "PreviousPage", {}, debug,
        )

