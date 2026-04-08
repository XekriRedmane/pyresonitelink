"""Generated component: VRIK."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VRIK(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FinalIK.VRIK.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FinalIK.VRIK"

    def __init__(self, auto_update: primitives.Bool | None = None, fix_transforms_enabled: primitives.Bool | None = None, component_initiated: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            auto_update: Initial value for AutoUpdate.
            fix_transforms_enabled: Initial value for FixTransformsEnabled.
            component_initiated: Initial value for componentInitiated.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if auto_update is not None:
            self.auto_update = auto_update
        if fix_transforms_enabled is not None:
            self.fix_transforms_enabled = fix_transforms_enabled
        if component_initiated is not None:
            self.component_initiated = component_initiated

    @property
    def auto_update(self) -> primitives.Bool | None:
        """The AutoUpdate field value."""
        member = self.get_member("AutoUpdate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_update.setter
    def auto_update(self, value: primitives.Bool) -> None:
        """Set the AutoUpdate field value."""
        member = self.get_member("AutoUpdate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoUpdate", fields.FieldBool(value=value)
            )

    @property
    def fix_transforms_enabled(self) -> primitives.Bool | None:
        """The FixTransformsEnabled field value."""
        member = self.get_member("FixTransformsEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fix_transforms_enabled.setter
    def fix_transforms_enabled(self, value: primitives.Bool) -> None:
        """Set the FixTransformsEnabled field value."""
        member = self.get_member("FixTransformsEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FixTransformsEnabled", fields.FieldBool(value=value)
            )

    @property
    def solver(self) -> members.SyncObject | None:
        """The Solver member."""
        member = self.get_member("Solver")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @solver.setter
    def solver(self, value: members.SyncObject) -> None:
        """Set the Solver member."""
        self.set_member("Solver", value)

    @property
    def component_initiated(self) -> primitives.Bool | None:
        """The componentInitiated field value."""
        member = self.get_member("componentInitiated")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @component_initiated.setter
    def component_initiated(self, value: primitives.Bool) -> None:
        """Set the componentInitiated field value."""
        member = self.get_member("componentInitiated")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "componentInitiated", fields.FieldBool(value=value)
            )

    @property
    def drives(self) -> members.SyncList | None:
        """The _drives member."""
        member = self.get_member("_drives")
        if isinstance(member, members.SyncList):
            return member
        return None

    @drives.setter
    def drives(self, value: members.SyncList) -> None:
        """Set the _drives member."""
        self.set_member("_drives", value)

