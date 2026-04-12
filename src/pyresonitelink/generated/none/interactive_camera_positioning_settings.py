"""Generated component: InteractiveCameraPositioningSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class InteractiveCameraPositioningSettings(GeneratedComponent, ICustomInspector):
    """See Camera.

    See Camera.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraPositioningSettings"

    def __init__(self, avoid_occlusion: primitives.Bool | None = None, keep_in_world_space: primitives.Bool | None = None, movement_wobble: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            avoid_occlusion: Initial value for AvoidOcclusion.
            keep_in_world_space: Initial value for KeepInWorldSpace.
            movement_wobble: Initial value for MovementWobble.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if avoid_occlusion is not None:
            self.avoid_occlusion = avoid_occlusion
        if keep_in_world_space is not None:
            self.keep_in_world_space = keep_in_world_space
        if movement_wobble is not None:
            self.movement_wobble = movement_wobble

    @property
    def avoid_occlusion(self) -> primitives.Bool | None:
        """When the camera is behind a wall or anything that is collidable, it will zoom the view in front of it to focus on the subject. This will not work in manual mode."""
        member = self.get_member("AvoidOcclusion")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @avoid_occlusion.setter
    def avoid_occlusion(self, value: primitives.Bool) -> None:
        """Set the AvoidOcclusion field value."""
        member = self.get_member("AvoidOcclusion")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AvoidOcclusion", fields.FieldBool(value=value)
            )

    @property
    def keep_in_world_space(self) -> primitives.Bool | None:
        """This keeps the camera in world space."""
        member = self.get_member("KeepInWorldSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @keep_in_world_space.setter
    def keep_in_world_space(self, value: primitives.Bool) -> None:
        """Set the KeepInWorldSpace field value."""
        member = self.get_member("KeepInWorldSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "KeepInWorldSpace", fields.FieldBool(value=value)
            )

    @property
    def movement_wobble(self) -> primitives.Bool | None:
        """This makes the camera have gradual movement in different positions around the subject. This only works with Third Person or Group modes."""
        member = self.get_member("MovementWobble")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @movement_wobble.setter
    def movement_wobble(self, value: primitives.Bool) -> None:
        """Set the MovementWobble field value."""
        member = self.get_member("MovementWobble")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MovementWobble", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

