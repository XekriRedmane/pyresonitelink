"""Generated component: AvatarRenderSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.irender_settings_source import IRenderSettingsSource
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarRenderSettings(GeneratedComponent, IRenderSettingsSource, IAvatarObjectComponent, IWorldEventReceiver):
    """Avatar Render Settings is a component that can be placed anywhere on an avatar for it to work. This component changes the internal camera settings for the first person view for a user wearing an avatar with this component under it by optionally changing the far and/or near clip values of the POV camera.

    Category: Users/Common Avatar System

    **Behavior**: This component does not start working on an avatar when added, until the avatar is re-equipped. After this, changing values on the component change what the user sees live. This component can be used to extend the distance a user can see, which by default is 4096 meters multipled by user global scale.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarRenderSettings"

    def __init__(self, near_clip: primitives.Float | None = None, far_clip: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            near_clip: Initial value for NearClip.
            far_clip: Initial value for FarClip.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if near_clip is not None:
            self.near_clip = near_clip
        if far_clip is not None:
            self.far_clip = far_clip

    @property
    def near_clip(self) -> primitives.Float | None:
        """If not null, changes the NearClip of the user's POV camera when this component is under the user's avatar hierarchy."""
        member = self.get_member("NearClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_clip.setter
    def near_clip(self, value: primitives.Float) -> None:
        """Set the NearClip field value."""
        member = self.get_member("NearClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearClip", fields.FieldNullableFloat(value=value)
            )

    @property
    def far_clip(self) -> primitives.Float | None:
        """If not null, changes the FarClip of the user's POV camera when this component is under the user's avatar hierarchy."""
        member = self.get_member("FarClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_clip.setter
    def far_clip(self, value: primitives.Float) -> None:
        """Set the FarClip field value."""
        member = self.get_member("FarClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarClip", fields.FieldNullableFloat(value=value)
            )

