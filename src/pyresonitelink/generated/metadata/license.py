"""Generated component: License."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class License(GeneratedComponent, IComponent, IWorldEventReceiver):
    """License is a legacy component, that has no functionality. We don't recommend using it. There is no standard for the formats, meaning or use of the properties within the component. Due to this different communities have used it for different items and purposes leading to a lot of confusion.

    Category: Metadata
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.License"

    def __init__(self, require_credit: primitives.Bool | None = None, credit_string: primitives.String | None = None, can_export: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            require_credit: Initial value for RequireCredit.
            credit_string: Initial value for CreditString.
            can_export: Initial value for CanExport.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if require_credit is not None:
            self.require_credit = require_credit
        if credit_string is not None:
            self.credit_string = credit_string
        if can_export is not None:
            self.can_export = can_export

    @property
    def require_credit(self) -> primitives.Bool | None:
        """There is no common standard for this value's meaning"""
        member = self.get_member("RequireCredit")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @require_credit.setter
    def require_credit(self, value: primitives.Bool) -> None:
        """Set the RequireCredit field value."""
        member = self.get_member("RequireCredit")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RequireCredit", fields.FieldBool(value=value)
            )

    @property
    def credit_string(self) -> primitives.String | None:
        """There is no common standard for this value's meaning"""
        member = self.get_member("CreditString")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @credit_string.setter
    def credit_string(self, value: primitives.String) -> None:
        """Set the CreditString field value."""
        member = self.get_member("CreditString")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CreditString", fields.FieldString(value=value)
            )

    @property
    def can_export(self) -> primitives.Bool | None:
        """There is no common standard for this value's meaning"""
        member = self.get_member("CanExport")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @can_export.setter
    def can_export(self, value: primitives.Bool) -> None:
        """Set the CanExport field value."""
        member = self.get_member("CanExport")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CanExport", fields.FieldBool(value=value)
            )

