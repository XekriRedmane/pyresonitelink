"""Generated component: MediaPrivacySettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class MediaPrivacySettings(GeneratedComponent, ICustomInspector):
    """See Settings.

    See Settings.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MediaPrivacySettings"

    def __init__(self, media_metadata_opt_out: primitives.Bool | None = None, hide_in_screenshots: primitives.Bool | None = None, strip_image_file_metadata: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            media_metadata_opt_out: Initial value for MediaMetadataOptOut.
            hide_in_screenshots: Initial value for HideInScreenshots.
            strip_image_file_metadata: Initial value for StripImageFileMetadata.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if media_metadata_opt_out is not None:
            self.media_metadata_opt_out = media_metadata_opt_out
        if hide_in_screenshots is not None:
            self.hide_in_screenshots = hide_in_screenshots
        if strip_image_file_metadata is not None:
            self.strip_image_file_metadata = strip_image_file_metadata

    @property
    def media_metadata_opt_out(self) -> primitives.Bool | None:
        """Requests for the user to opt out of being in media metadata like photos or microphone recordings when they are captured in world."""
        member = self.get_member("MediaMetadataOptOut")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @media_metadata_opt_out.setter
    def media_metadata_opt_out(self, value: primitives.Bool) -> None:
        """Set the MediaMetadataOptOut field value."""
        member = self.get_member("MediaMetadataOptOut")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MediaMetadataOptOut", fields.FieldBool(value=value)
            )

    @property
    def hide_in_screenshots(self) -> primitives.Bool | None:
        """Requests the user be not rendered in photos when they are taken in world, including world preview thumbnails."""
        member = self.get_member("HideInScreenshots")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hide_in_screenshots.setter
    def hide_in_screenshots(self, value: primitives.Bool) -> None:
        """Set the HideInScreenshots field value."""
        member = self.get_member("HideInScreenshots")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HideInScreenshots", fields.FieldBool(value=value)
            )

    @property
    def strip_image_file_metadata(self) -> primitives.Bool | None:
        """Strips the metadata from images that the user themselves brings into a scene."""
        member = self.get_member("StripImageFileMetadata")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @strip_image_file_metadata.setter
    def strip_image_file_metadata(self, value: primitives.Bool) -> None:
        """Set the StripImageFileMetadata field value."""
        member = self.get_member("StripImageFileMetadata")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StripImageFileMetadata", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

