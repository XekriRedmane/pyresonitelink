"""Generated component: VRIK."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VRIK(GeneratedComponent, IComponent, IWorldEventReceiver):
    """All weight values are 1-0, excluding clamps which are inverted 0-1.

    All weight values are 1-0, excluding clamps which are inverted 0-1. You
    can overdrive some of them with interesting results.

    **Introduction**: The VRIK component is used to configure Inverse Kinematics on an avatar, for posing joints based on the position of IK Targets such as a VR HMD, hand tracking, or Vive Trackers

This component is automatically configured when importing a mesh with a detectable humanoid rig, and generally should not be modified unless you know what you are doing.

Documentation on this component may take some time, as it is very complex, and not commonly used. The basis for this component seems to be the VRIK solver developed by Final IK.

    **IKSolverVR**: Most of the complexity in VRIK is actually stored in the IKSolverVR type. And even this is spread across multiple types.

    **BoneDrive**: Bonedrive fields use a combination of the ``defaultLocalPositions`` and ``defaultLocalRotations`` entries at this element's entry position in the list as well as VRIK position and rotation solved values to determine the final driven value.
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
        """Whether to update the VRIK regardless of whether or not the sync delegates are called by a VRIK avatar or similar sources. this can break systems still using a VRIKAvatar but can fix ones with a lack of such component."""
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
        """Clamps IK transforms to reasonable values and Resets IK every update."""
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
        """The actual solver that contains most of the fields of this component."""
        member = self.get_member("Solver")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @solver.setter
    def solver(self, value: members.SyncObject) -> None:
        """Set Solver. The actual solver that contains most of the fields of this component."""
        self.set_member("Solver", value)

    @property
    def component_initiated(self) -> primitives.Bool | None:
        """Marks this component as fully started and ready to solve IK transforms."""
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
        """A list of fields to drive with ``defaultLocalPositions`` and ``defaultLocalRotations`` plus transforms solved by the IK using ``defaultLocalPositions`` and ``defaultLocalRotations`` as a basis."""
        member = self.get_member("_drives")
        if isinstance(member, members.SyncList):
            return member
        return None

    @drives.setter
    def drives(self, value: members.SyncList) -> None:
        """Set _drives. A list of fields to drive with ``defaultLocalPositions`` and ``defaultLocalRotations`` plus transforms solved by the IK using ``defaultLocalPositions`` and ``defaultLocalRotations`` as a basis."""
        self.set_member("_drives", value)

