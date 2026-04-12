"""Generated component: InteractiveCameraPhotoSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class InteractiveCameraPhotoSettings(GeneratedComponent, ICustomInspector):
    """See Camera.

    See Camera.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraPhotoSettings"

    def __init__(self, spawn_photo_in_world: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            spawn_photo_in_world: Initial value for SpawnPhotoInWorld.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if spawn_photo_in_world is not None:
            self.spawn_photo_in_world = spawn_photo_in_world

    @property
    def spawn_photo_in_world(self) -> primitives.Bool | None:
        """This will spawn the photo in to the world after a picture is taken. If this is off, it will only be saved on your device."""
        member = self.get_member("SpawnPhotoInWorld")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spawn_photo_in_world.setter
    def spawn_photo_in_world(self, value: primitives.Bool) -> None:
        """Set the SpawnPhotoInWorld field value."""
        member = self.get_member("SpawnPhotoInWorld")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpawnPhotoInWorld", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

