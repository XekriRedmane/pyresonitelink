"""Generated component: SupporterCreditList."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.credit_type import CreditType
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SupporterCreditList(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The SupporterCreditList component is used to get a list of supporters currently supporting the game financially.

    Category: Cloud/Indicators
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SupporterCreditList"

    def __init__(self, credit_type: CreditType | str | None = None, separator: primitives.String | None = None, prefix: primitives.String | None = None, suffix: primitives.String | None = None, formatted_list: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            credit_type: Initial value for CreditType.
            separator: Initial value for Separator.
            prefix: Initial value for Prefix.
            suffix: Initial value for Suffix.
            formatted_list: Initial value for FormattedList.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if credit_type is not None:
            self.credit_type = credit_type
        if separator is not None:
            self.separator = separator
        if prefix is not None:
            self.prefix = prefix
        if suffix is not None:
            self.suffix = suffix
        if formatted_list is not None:
            self.formatted_list = formatted_list

    @property
    def credit_type(self) -> CreditType | None:
        """What kind of supporter level/category to get names from."""
        member = self.get_member("CreditType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CreditType(member.value)
        return None

    @credit_type.setter
    def credit_type(self, value: CreditType | str) -> None:
        """Set CreditType. What kind of supporter level/category to get names from."""
        member = self.get_member("CreditType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "CreditType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def separator(self) -> primitives.String | None:
        """How to separate the list of names."""
        member = self.get_member("Separator")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @separator.setter
    def separator(self, value: primitives.String) -> None:
        """Set the Separator field value."""
        member = self.get_member("Separator")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Separator", fields.FieldString(value=value)
            )

    @property
    def prefix(self) -> primitives.String | None:
        """What to put at the beginning of each name (Usually a color tag)"""
        member = self.get_member("Prefix")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @prefix.setter
    def prefix(self, value: primitives.String) -> None:
        """Set the Prefix field value."""
        member = self.get_member("Prefix")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Prefix", fields.FieldString(value=value)
            )

    @property
    def suffix(self) -> primitives.String | None:
        """What to put at the end of each name (Usually a color tag ender."""
        member = self.get_member("Suffix")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @suffix.setter
    def suffix(self, value: primitives.String) -> None:
        """Set the Suffix field value."""
        member = self.get_member("Suffix")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Suffix", fields.FieldString(value=value)
            )

    @property
    def formatted_list(self) -> primitives.String | None:
        """The resulting list."""
        member = self.get_member("FormattedList")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @formatted_list.setter
    def formatted_list(self, value: primitives.String) -> None:
        """Set the FormattedList field value."""
        member = self.get_member("FormattedList")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FormattedList", fields.FieldString(value=value)
            )

