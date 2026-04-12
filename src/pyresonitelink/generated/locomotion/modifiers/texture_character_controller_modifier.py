"""Generated component: TextureCharacterControllerModifier."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.character_controller_parameter import CharacterControllerParameter
from pyresonitelink.generated._enums.mode import Mode
from pyresonitelink.generated._enums.color_channel import ColorChannel
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextureCharacterControllerModifier(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The TextureCharacterControllerModifier component reacts to character controllers that collide with mesh colliders in its children hiearchy. It starts by finding what the contact triangle and point on the mesh collider a character controller hit was. That point is mapped to what part of a texture the character controller hit. Finally, the texture data in ``Texture`` is used to determine what the value should be used for Modifying the character controller that hit that mesh collider.

    Category: Locomotion/Modifiers

    Attach to the same slot as a mesh collider for best results. A packed
    texture of RBGA can be used and reused for this component to save on
    resources and modify 4 different values on 4 different instances of this
    component to allow for Modifying 4 different character controller
    properties at the same time.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TextureCharacterControllerModifier"

    def __init__(self, parameter: CharacterControllerParameter | str | None = None, modification_mode: Mode | str | None = None, min_value: primitives.Float | None = None, max_value: primitives.Float | None = None, channel: ColorChannel | str | None = None, texture: str | IAssetProvider[Texture2D] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            parameter: Initial value for Parameter.
            modification_mode: Initial value for ModificationMode.
            min_value: Initial value for MinValue.
            max_value: Initial value for MaxValue.
            channel: Initial value for Channel.
            texture: Initial value for Texture.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if parameter is not None:
            self.parameter = parameter
        if modification_mode is not None:
            self.modification_mode = modification_mode
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value
        if channel is not None:
            self.channel = channel
        if texture is not None:
            self.texture = texture

    @property
    def parameter(self) -> CharacterControllerParameter | None:
        """The parameter of the contacting character controller to modify."""
        member = self.get_member("Parameter")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CharacterControllerParameter(member.value)
        return None

    @parameter.setter
    def parameter(self, value: CharacterControllerParameter | str) -> None:
        """Set Parameter. The parameter of the contacting character controller to modify."""
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
        """How to modify the parameter on the contacting character controller."""
        member = self.get_member("ModificationMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Mode(member.value)
        return None

    @modification_mode.setter
    def modification_mode(self, value: Mode | str) -> None:
        """Set ModificationMode. How to modify the parameter on the contacting character controller."""
        member = self.get_member("ModificationMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ModificationMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def min_value(self) -> primitives.Float | None:
        """When the mapped value on ``Texture`` maps to a value of 0, what should the value be for the character controller modification?"""
        member = self.get_member("MinValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_value.setter
    def min_value(self, value: primitives.Float) -> None:
        """Set the MinValue field value."""
        member = self.get_member("MinValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinValue", fields.FieldFloat(value=value)
            )

    @property
    def max_value(self) -> primitives.Float | None:
        """When the mapped value on ``Texture`` maps to a value of 100% brightness or 1, what should the value be for the character controller modification?"""
        member = self.get_member("MaxValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_value.setter
    def max_value(self, value: primitives.Float) -> None:
        """Set the MaxValue field value."""
        member = self.get_member("MaxValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxValue", fields.FieldFloat(value=value)
            )

    @property
    def channel(self) -> ColorChannel | None:
        """The channel to use on ``Texture`` when getting a value for UV contact points."""
        member = self.get_member("Channel")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ColorChannel(member.value)
        return None

    @channel.setter
    def channel(self, value: ColorChannel | str) -> None:
        """Set Channel. The channel to use on ``Texture`` when getting a value for UV contact points."""
        member = self.get_member("Channel")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Channel",
                members.FieldEnum(value=str(value)),
            )

    @property
    def texture(self) -> str | None:
        """The texture to use for character controller modification data."""
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the Texture reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

