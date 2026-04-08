"""Generated component: WorldCaptureThumbnailSource."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.iworld_thumbnail_source import IWorldThumbnailSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldCaptureThumbnailSource(GeneratedComponent, IWorldThumbnailSource, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.WorldCaptureThumbnailSource.

    Category: World
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldCaptureThumbnailSource"

    def __init__(self, overlay: str | IAssetProvider[Texture2D] | None = None, exclude_users_in_capture: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            overlay: Initial value for Overlay.
            exclude_users_in_capture: Initial value for ExcludeUsersInCapture.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if overlay is not None:
            self.overlay = overlay
        if exclude_users_in_capture is not None:
            self.exclude_users_in_capture = exclude_users_in_capture

    @property
    def overlay(self) -> str | None:
        """Target ID of the Overlay reference (targets IAssetProvider[Texture2D])."""
        member = self.get_member("Overlay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @overlay.setter
    def overlay(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the Overlay reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Overlay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Overlay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

    @property
    def exclude_users_in_capture(self) -> primitives.Bool | None:
        """The ExcludeUsersInCapture field value."""
        member = self.get_member("ExcludeUsersInCapture")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exclude_users_in_capture.setter
    def exclude_users_in_capture(self, value: primitives.Bool) -> None:
        """Set the ExcludeUsersInCapture field value."""
        member = self.get_member("ExcludeUsersInCapture")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ExcludeUsersInCapture", fields.FieldBool(value=value)
            )

