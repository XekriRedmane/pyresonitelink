"""Generated component: LocaleActiveDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocaleActiveDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LocaleActiveDriver.

    Category: Localization
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocaleActiveDriver"

    def __init__(self, target: str | IField[bool] | None = None, locale_code: str | None = None, match_main_language: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            locale_code: Initial value for LocaleCode.
            match_main_language: Initial value for MatchMainLanguage.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if locale_code is not None:
            self.locale_code = locale_code
        if match_main_language is not None:
            self.match_main_language = match_main_language

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[bool])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[bool] | None) -> None:
        """Set the Target reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def locale_code(self) -> str | None:
        """The LocaleCode field value."""
        member = self.get_member("LocaleCode")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @locale_code.setter
    def locale_code(self, value: str) -> None:
        """Set the LocaleCode field value."""
        member = self.get_member("LocaleCode")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocaleCode", fields.FieldString(value=value)
            )

    @property
    def match_main_language(self) -> bool | None:
        """The MatchMainLanguage field value."""
        member = self.get_member("MatchMainLanguage")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @match_main_language.setter
    def match_main_language(self, value: bool) -> None:
        """Set the MatchMainLanguage field value."""
        member = self.get_member("MatchMainLanguage")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MatchMainLanguage", fields.FieldBool(value=value)
            )

