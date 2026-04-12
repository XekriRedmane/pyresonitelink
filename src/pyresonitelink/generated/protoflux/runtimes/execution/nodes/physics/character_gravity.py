"""Generated component: CharacterGravity."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.character_controller import CharacterController
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CharacterGravity(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Character Gravity`` node returns a referenced character controller gravity. The gravity output is used when you want the character controller's current gravity it is aiming for when simulating. The actual gravity is what the character controller is simulating now, and can be varied when using it dependiong on the settings on the character controller (specifically the gravity scale field).

    Category: ProtoFlux/Runtimes/Execution/Nodes/Physics

    You can use the actual gravity output of this node to control how
    gravity works for certain character controllers that need to have
    different values effect them in different ways (using both the user's
    transform scale and the component's gravity scale). You can set the
    simulating user's gravity scale to cubic and have their gravity be
    effected by their size. Using Linear will keep the gravity the same no
    matter the size of the user. (Tested on users jumping while changing the
    gravity scale field in the character controller component).
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Physics.CharacterGravity"

    def __init__(self, character: str | INodeObjectOutput[CharacterController] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            character: Initial value for Character.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if character is not None:
            self.character = character

    @property
    def character(self) -> str | None:
        """The character controller reference."""
        member = self.get_member("Character")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @character.setter
    def character(self, target: str | INodeObjectOutput[CharacterController] | None) -> None:
        """Set the Character reference by target ID or INodeObjectOutput[CharacterController] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Character")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Character",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.CharacterController>'),
            )

    @property
    def gravity(self) -> members.EmptyElement | None:
        """The current gravity from this character controller that it "should" try to simulate."""
        member = self.get_member("Gravity")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @gravity.setter
    def gravity(self, value: members.EmptyElement) -> None:
        """Set Gravity. The current gravity from this character controller that it "should" try to simulate."""
        self.set_member("Gravity", value)

    @property
    def actual_gravity(self) -> members.EmptyElement | None:
        """The ActualGravity member."""
        member = self.get_member("ActualGravity")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @actual_gravity.setter
    def actual_gravity(self, value: members.EmptyElement) -> None:
        """Set the ActualGravity member."""
        self.set_member("ActualGravity", value)

