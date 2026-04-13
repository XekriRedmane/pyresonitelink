"""Generated component: SubmeshCharacterControllerModifier."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._enums.character_controller_parameter import CharacterControllerParameter
from pyresonitelink.generated._enums.mode import Mode
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SubmeshCharacterControllerModifier(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The SubmeshCharacterController is a component able to change properties of a Person or NPC locomotion (Character Controller) walking on a mesh based on what submesh of the mesh they are walking on.

    Category: Locomotion/Modifiers

    Attach to the same slot as a mesh collider with a mesh set to static and
    IsCharacterCollider in order for this to work.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SubmeshCharacterControllerModifier"

    def __init__(self, parameter: CharacterControllerParameter | str | None = None, modification_mode: Mode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            parameter: Initial value for Parameter.
            modification_mode: Initial value for ModificationMode.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if parameter is not None:
            self.parameter = parameter
        if modification_mode is not None:
            self.modification_mode = modification_mode

    @property
    def parameter(self) -> CharacterControllerParameter | None:
        """The parameter to modify"""
        member = self.get_member("Parameter")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CharacterControllerParameter(member.value)
        return None

    @parameter.setter
    def parameter(self, value: CharacterControllerParameter | str) -> None:
        """Set Parameter. The parameter to modify"""
        member = self.get_member("Parameter")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Parameter",
                members.FieldEnum(value=str(value)),
            )

    @property
    def modification_mode(self) -> Mode | None:
        """How to modify the parameter."""
        member = self.get_member("ModificationMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Mode(member.value)
        return None

    @modification_mode.setter
    def modification_mode(self, value: Mode | str) -> None:
        """Set ModificationMode. How to modify the parameter."""
        member = self.get_member("ModificationMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ModificationMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def values(self) -> members.SyncList | None:
        """What value to use when modifying for each sub mesh. In order of submesh number."""
        member = self.get_member("Values")
        if isinstance(member, members.SyncList):
            return member
        return None

    @values.setter
    def values(self, value: members.SyncList) -> None:
        """Set Values. What value to use when modifying for each sub mesh. In order of submesh number."""
        self.set_member("Values", value)

