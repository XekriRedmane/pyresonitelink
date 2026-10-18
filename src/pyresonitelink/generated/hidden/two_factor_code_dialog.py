"""Generated component: TwoFactorCodeDialog."""

from __future__ import annotations

from typing import TYPE_CHECKING
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent

if TYPE_CHECKING:
    from pyresonitelink.generated.uix.interaction.text_field import TextField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TwoFactorCodeDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The TwoFactorCodeDialog component is used to accept and process a 2FA code from a user when logging into Resonite.

    Category: Hidden

    Not to be used by the user directly.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TwoFactorCodeDialog"

    def __init__(self, code: str | TextField | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            code: Initial value for _code.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if code is not None:
            self.code = code

    @property
    def code(self) -> str | None:
        """The text field used to enter the 2FA code."""
        member = self.get_member("_code")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @code.setter
    def code(self, target: str | TextField | None) -> None:
        """Set the _code reference by target ID or TextField instance."""
        target_id: str | None = target if target is None or isinstance(target, str) else target.id
        member = self.get_member("_code")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_code",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

