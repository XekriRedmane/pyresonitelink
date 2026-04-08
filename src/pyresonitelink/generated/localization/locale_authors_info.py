"""Generated component: LocaleAuthorsInfo."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.locale_resource import LocaleResource
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocaleAuthorsInfo(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LocaleAuthorsInfo.

    Category: Localization
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocaleAuthorsInfo"

    def __init__(self, locale: str | IAssetProvider[LocaleResource] | None = None, credits_string: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            locale: Initial value for Locale.
            credits_string: Initial value for CreditsString.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if locale is not None:
            self.locale = locale
        if credits_string is not None:
            self.credits_string = credits_string

    @property
    def locale(self) -> str | None:
        """Target ID of the Locale reference (targets IAssetProvider[LocaleResource])."""
        member = self.get_member("Locale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @locale.setter
    def locale(self, target: str | IAssetProvider[LocaleResource] | None) -> None:
        """Set the Locale reference by target ID or IAssetProvider[LocaleResource] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Locale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Locale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.LocaleResource>'),
            )

    @property
    def credits_string(self) -> primitives.String | None:
        """The CreditsString field value."""
        member = self.get_member("CreditsString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @credits_string.setter
    def credits_string(self, value: primitives.String) -> None:
        """Set the CreditsString field value."""
        member = self.get_member("CreditsString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CreditsString", fields.FieldString(value=value)
            )

