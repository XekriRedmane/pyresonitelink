"""Generated component: BlitToDisplay."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture import ITexture
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BlitToDisplay(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """BlitToDisplay is a component that is able to make a user's game window display a 2d texture of any kind (including render textures) and is also able to create new game windows to display images as well. 

This component takes no regard for permissions at the time of writing. This component generates new windows without confirmation. New windows generated are created on new monitors or the main monitor, and are made to fit the screen. 

Combining this with DisplayInfo allows for getting the size of the user's screen, which can be used to adjust the texture displayed by this component to better fit the generated window.

    Category: Rendering

    **Behavior**: Disabling this component does not disable its effects. Setting ``TargetUser`` to null does though. New windows created by this component will close the game if closed. It is unknown if this is a bug. This component can and will blind desktop users if ``DisplayIndex`` is set to 0 and ``TargetUser`` targets a desktop user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BlitToDisplay"

    def __init__(self, texture: str | IAssetProvider[ITexture] | None = None, display_index: primitives.Int | None = None, background_color: primitives.ColorX | None = None, flip_horizontally: primitives.Bool | None = None, flip_vertically: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture: Initial value for Texture.
            display_index: Initial value for DisplayIndex.
            background_color: Initial value for BackgroundColor.
            flip_horizontally: Initial value for FlipHorizontally.
            flip_vertically: Initial value for FlipVertically.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if texture is not None:
            self.texture = texture
        if display_index is not None:
            self.display_index = display_index
        if background_color is not None:
            self.background_color = background_color
        if flip_horizontally is not None:
            self.flip_horizontally = flip_horizontally
        if flip_vertically is not None:
            self.flip_vertically = flip_vertically

    @property
    def target_user(self) -> members.SyncObject | None:
        """The user to display the image on their screen for. Using the local user does work."""
        member = self.get_member("TargetUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @target_user.setter
    def target_user(self, value: members.SyncObject) -> None:
        """Set TargetUser. The user to display the image on their screen for. Using the local user does work."""
        self.set_member("TargetUser", value)

    @property
    def texture(self) -> str | None:
        """The texture to display to the screen. A render texture may be used here."""
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | IAssetProvider[ITexture] | None) -> None:
        """Set the Texture reference by target ID or IAssetProvider[ITexture] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture>'),
            )

    @property
    def display_index(self) -> primitives.Int | None:
        """which game window to display ``Texture`` to. If the window number doesn't exist, one is created automatically. If 0 is used, the main game window will be used."""
        member = self.get_member("DisplayIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @display_index.setter
    def display_index(self, value: primitives.Int) -> None:
        """Set the DisplayIndex field value."""
        member = self.get_member("DisplayIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisplayIndex", fields.FieldInt(value=value)
            )

    @property
    def background_color(self) -> primitives.ColorX | None:
        """The color to display behind the image."""
        member = self.get_member("BackgroundColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @background_color.setter
    def background_color(self, value: primitives.ColorX) -> None:
        """Set the BackgroundColor field value."""
        member = self.get_member("BackgroundColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BackgroundColor", fields.FieldColorX(value=value)
            )

    @property
    def flip_horizontally(self) -> primitives.Bool | None:
        """flip the image horizontally before displaying to the screen."""
        member = self.get_member("FlipHorizontally")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flip_horizontally.setter
    def flip_horizontally(self, value: primitives.Bool) -> None:
        """Set the FlipHorizontally field value."""
        member = self.get_member("FlipHorizontally")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FlipHorizontally", fields.FieldBool(value=value)
            )

    @property
    def flip_vertically(self) -> primitives.Bool | None:
        """flip the image vertically before displaying to the screen."""
        member = self.get_member("FlipVertically")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flip_vertically.setter
    def flip_vertically(self, value: primitives.Bool) -> None:
        """Set the FlipVertically field value."""
        member = self.get_member("FlipVertically")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FlipVertically", fields.FieldBool(value=value)
            )

