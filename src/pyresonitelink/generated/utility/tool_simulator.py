"""Generated component: ToolSimulator."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itool import ITool
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ToolSimulator(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ToolSimulator.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ToolSimulator"

    def __init__(self, tool: str | ITool | None = None, simulating_user: str | User | None = None, primary: bool | None = None, secondary: bool | None = None, strength: np.float32 | None = None, axis: primitives.Float2 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tool: Initial value for Tool.
            simulating_user: Initial value for SimulatingUser.
            primary: Initial value for Primary.
            secondary: Initial value for Secondary.
            strength: Initial value for Strength.
            axis: Initial value for Axis.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if tool is not None:
            self.tool = tool
        if simulating_user is not None:
            self.simulating_user = simulating_user
        if primary is not None:
            self.primary = primary
        if secondary is not None:
            self.secondary = secondary
        if strength is not None:
            self.strength = strength
        if axis is not None:
            self.axis = axis

    @property
    def tool(self) -> str | None:
        """Target ID of the Tool reference (targets ITool)."""
        member = self.get_member("Tool")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tool.setter
    def tool(self, target: str | ITool | None) -> None:
        """Set the Tool reference by target ID or ITool instance."""
        target_id: str | None = target.id if isinstance(target, ITool) else target  # type: ignore[assignment]
        member = self.get_member("Tool")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Tool",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ITool'),
            )

    @property
    def simulating_user(self) -> str | None:
        """Target ID of the SimulatingUser reference (targets User)."""
        member = self.get_member("SimulatingUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @simulating_user.setter
    def simulating_user(self, target: str | User | None) -> None:
        """Set the SimulatingUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("SimulatingUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SimulatingUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def primary(self) -> bool | None:
        """The Primary field value."""
        member = self.get_member("Primary")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @primary.setter
    def primary(self, value: bool) -> None:
        """Set the Primary field value."""
        member = self.get_member("Primary")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Primary", fields.FieldBool(value=value)
            )

    @property
    def secondary(self) -> bool | None:
        """The Secondary field value."""
        member = self.get_member("Secondary")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @secondary.setter
    def secondary(self, value: bool) -> None:
        """Set the Secondary field value."""
        member = self.get_member("Secondary")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Secondary", fields.FieldBool(value=value)
            )

    @property
    def strength(self) -> np.float32 | None:
        """The Strength field value."""
        member = self.get_member("Strength")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @strength.setter
    def strength(self, value: np.float32) -> None:
        """Set the Strength field value."""
        member = self.get_member("Strength")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Strength", fields.FieldFloat(value=value)
            )

    @property
    def axis(self) -> primitives.Float2 | None:
        """The Axis field value."""
        member = self.get_member("Axis")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @axis.setter
    def axis(self, value: primitives.Float2) -> None:
        """Set the Axis field value."""
        member = self.get_member("Axis")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Axis", fields.FieldFloat2(value=value)
            )

