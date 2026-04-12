"""Generated component: LegacyUIStyle."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyUIStyle(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The LegacyUIStyle component is used in older content to specify what colors a UI should be depending on where it is. This should not be used in new content, and should be removed/replaced whenever possible.

    Category: Rendering/Visuals
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyUIStyle"

    def __init__(self, color: primitives.ColorX | None = None, user_parented_color: primitives.ColorX | None = None, private_color: primitives.ColorX | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            color: Initial value for Color.
            user_parented_color: Initial value for UserParentedColor.
            private_color: Initial value for PrivateColor.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if color is not None:
            self.color = color
        if user_parented_color is not None:
            self.user_parented_color = user_parented_color
        if private_color is not None:
            self.private_color = private_color

    @property
    def color(self) -> primitives.ColorX | None:
        """The normal color."""
        member = self.get_member("Color")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color.setter
    def color(self, value: primitives.ColorX) -> None:
        """Set the Color field value."""
        member = self.get_member("Color")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Color", fields.FieldColorX(value=value)
            )

    @property
    def user_parented_color(self) -> primitives.ColorX | None:
        """The color a UI should have when parented under the user."""
        member = self.get_member("UserParentedColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @user_parented_color.setter
    def user_parented_color(self, value: primitives.ColorX) -> None:
        """Set the UserParentedColor field value."""
        member = self.get_member("UserParentedColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UserParentedColor", fields.FieldColorX(value=value)
            )

    @property
    def private_color(self) -> primitives.ColorX | None:
        """The color a UI should have when it's in userspace."""
        member = self.get_member("PrivateColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @private_color.setter
    def private_color(self, value: primitives.ColorX) -> None:
        """Set the PrivateColor field value."""
        member = self.get_member("PrivateColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PrivateColor", fields.FieldColorX(value=value)
            )

