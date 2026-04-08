"""Generated component: HyperlinkDisplayInterface."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.user_ref import UserRef
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class HyperlinkDisplayInterface(GeneratedComponent, IItemMetadataSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.HyperlinkDisplayInterface.

    Category: Utility/Entity Interfaces
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.HyperlinkDisplayInterface"

    def __init__(self, item_name: str | IField[primitives.String] | None = None, spawning_user: str | UserRef | None = None, spawning_user_id: str | IField[primitives.String] | None = None, is_instance: primitives.Bool | None = None, url: str | IField[str] | None = None, url_string: str | IField[primitives.String] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            item_name: Initial value for ItemName.
            spawning_user: Initial value for SpawningUser.
            spawning_user_id: Initial value for SpawningUserID.
            is_instance: Initial value for IsInstance.
            url: Initial value for Url.
            url_string: Initial value for UrlString.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if item_name is not None:
            self.item_name = item_name
        if spawning_user is not None:
            self.spawning_user = spawning_user
        if spawning_user_id is not None:
            self.spawning_user_id = spawning_user_id
        if is_instance is not None:
            self.is_instance = is_instance
        if url is not None:
            self.url = url
        if url_string is not None:
            self.url_string = url_string

    @property
    def item_name(self) -> str | None:
        """Target ID of the ItemName reference (targets IField[primitives.String])."""
        member = self.get_member("ItemName")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @item_name.setter
    def item_name(self, target: str | IField[primitives.String] | None) -> None:
        """Set the ItemName reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ItemName")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ItemName",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def spawning_user(self) -> str | None:
        """Target ID of the SpawningUser reference (targets UserRef)."""
        member = self.get_member("SpawningUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spawning_user.setter
    def spawning_user(self, target: str | UserRef | None) -> None:
        """Set the SpawningUser reference by target ID or UserRef instance."""
        target_id: str | None = target.id if isinstance(target, UserRef) else target  # type: ignore[assignment]
        member = self.get_member("SpawningUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpawningUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UserRef'),
            )

    @property
    def spawning_user_id(self) -> str | None:
        """Target ID of the SpawningUserID reference (targets IField[primitives.String])."""
        member = self.get_member("SpawningUserID")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @spawning_user_id.setter
    def spawning_user_id(self, target: str | IField[primitives.String] | None) -> None:
        """Set the SpawningUserID reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SpawningUserID")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SpawningUserID",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

    @property
    def is_instance(self) -> primitives.Bool | None:
        """The IsInstance field value."""
        member = self.get_member("IsInstance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_instance.setter
    def is_instance(self, value: primitives.Bool) -> None:
        """Set the IsInstance field value."""
        member = self.get_member("IsInstance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsInstance", fields.FieldBool(value=value)
            )

    @property
    def url(self) -> str | None:
        """Target ID of the Url reference (targets IField[str])."""
        member = self.get_member("Url")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @url.setter
    def url(self, target: str | IField[str] | None) -> None:
        """Set the Url reference by target ID or IField[str] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Url")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Url",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Uri>'),
            )

    @property
    def url_string(self) -> str | None:
        """Target ID of the UrlString reference (targets IField[primitives.String])."""
        member = self.get_member("UrlString")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @url_string.setter
    def url_string(self, target: str | IField[primitives.String] | None) -> None:
        """Set the UrlString reference by target ID or IField[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("UrlString")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UrlString",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<string>'),
            )

