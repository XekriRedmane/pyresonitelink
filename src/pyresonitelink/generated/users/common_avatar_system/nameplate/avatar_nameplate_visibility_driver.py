"""Generated component: AvatarNameplateVisibilityDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarNameplateVisibilityDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """AvatarNameplateVisibilityDriver is used to drive the visibility of nameplates during certain scenarios.

    Category: Users/Common Avatar System/Nameplate

    **Behavior**: This disables the target of ``Visible`` when nameplates are hidden locally through the nameplate visibility facet on the Home tab of the Dash Menu. This also drives the visibility of nameplates for other reasons, like when visibility of default nameplates is needed locally. It also hides the target nameplate during certain render contexts, like when a user is taking a picture with hide nameplates during pictures setting turned on.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AvatarNameplateVisibilityDriver"

    def __init__(self, always_show_to_contacts: primitives.Bool | None = None, visible: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            always_show_to_contacts: Initial value for AlwaysShowToContacts.
            visible: Initial value for Visible.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if always_show_to_contacts is not None:
            self.always_show_to_contacts = always_show_to_contacts
        if visible is not None:
            self.visible = visible

    @property
    def always_show_to_contacts(self) -> primitives.Bool | None:
        """Show to contacts regardless of whether it should be hidden or not."""
        member = self.get_member("AlwaysShowToContacts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @always_show_to_contacts.setter
    def always_show_to_contacts(self, value: primitives.Bool) -> None:
        """Set the AlwaysShowToContacts field value."""
        member = self.get_member("AlwaysShowToContacts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AlwaysShowToContacts", fields.FieldBool(value=value)
            )

    @property
    def visible(self) -> str | None:
        """The boolean to drive for nameplate visiblity (like the active of the nameplate slot)"""
        member = self.get_member("Visible")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visible.setter
    def visible(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the Visible reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Visible")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Visible",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

