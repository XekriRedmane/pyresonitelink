"""Generated component: PhotoMetadata."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.stereo_layout import StereoLayout
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PhotoMetadata(GeneratedComponent, IItemMetadataSource, IWorldEventReceiver):
    """The PhotoMetadata component is used to contain the information on a photo usually taken within Resonite. It is automatically attached to every screenshot taken using the finger photo gesture. This component can also be attached to a photo imported with the "import as screenshot" option when importing an image.

    Category: Data
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PhotoMetadata"

    def __init__(self, location_name: primitives.String | None = None, location_url: str | None = None, location_hidden_from_listing: primitives.Bool | None = None, time_taken: str | None = None, taken_global_position: primitives.Float3 | None = None, taken_global_rotation: primitives.FloatQ | None = None, taken_global_scale: primitives.Float3 | None = None, app_version: primitives.String | None = None, camera_manufacturer: primitives.String | None = None, camera_model: primitives.String | None = None, camera_fov: primitives.Float | None = None, is360: primitives.Bool | None = None, stereo_layout: StereoLayout | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            location_name: Initial value for LocationName.
            location_url: Initial value for LocationURL.
            location_hidden_from_listing: Initial value for LocationHiddenFromListing.
            time_taken: Initial value for TimeTaken.
            taken_global_position: Initial value for TakenGlobalPosition.
            taken_global_rotation: Initial value for TakenGlobalRotation.
            taken_global_scale: Initial value for TakenGlobalScale.
            app_version: Initial value for AppVersion.
            camera_manufacturer: Initial value for CameraManufacturer.
            camera_model: Initial value for CameraModel.
            camera_fov: Initial value for CameraFOV.
            is360: Initial value for Is360.
            stereo_layout: Initial value for StereoLayout.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if location_name is not None:
            self.location_name = location_name
        if location_url is not None:
            self.location_url = location_url
        if location_hidden_from_listing is not None:
            self.location_hidden_from_listing = location_hidden_from_listing
        if time_taken is not None:
            self.time_taken = time_taken
        if taken_global_position is not None:
            self.taken_global_position = taken_global_position
        if taken_global_rotation is not None:
            self.taken_global_rotation = taken_global_rotation
        if taken_global_scale is not None:
            self.taken_global_scale = taken_global_scale
        if app_version is not None:
            self.app_version = app_version
        if camera_manufacturer is not None:
            self.camera_manufacturer = camera_manufacturer
        if camera_model is not None:
            self.camera_model = camera_model
        if camera_fov is not None:
            self.camera_fov = camera_fov
        if is360 is not None:
            self.is360 = is360
        if stereo_layout is not None:
            self.stereo_layout = stereo_layout

    @property
    def location_name(self) -> primitives.String | None:
        """Name of the session the screenshot was taken in."""
        member = self.get_member("LocationName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @location_name.setter
    def location_name(self, value: primitives.String) -> None:
        """Set the LocationName field value."""
        member = self.get_member("LocationName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocationName", fields.FieldString(value=value)
            )

    @property
    def location_url(self) -> str | None:
        """The URI of the session's world that the photo was taken in. (basically a world link)"""
        member = self.get_member("LocationURL")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @location_url.setter
    def location_url(self, value: str) -> None:
        """Set the LocationURL field value."""
        member = self.get_member("LocationURL")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocationURL", fields.FieldUri(value=value)
            )

    @property
    def location_host(self) -> members.SyncObject | None:
        """Host of the session the screenshot was taken in."""
        member = self.get_member("LocationHost")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @location_host.setter
    def location_host(self, value: members.SyncObject) -> None:
        """Set LocationHost. Host of the session the screenshot was taken in."""
        self.set_member("LocationHost", value)

    @property
    def location_access_level(self) -> members.FieldEnum | None:
        """Access level of the session."""
        member = self.get_member("LocationAccessLevel")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @location_access_level.setter
    def location_access_level(self, value: members.FieldEnum) -> None:
        """Set LocationAccessLevel. Access level of the session."""
        self.set_member("LocationAccessLevel", value)

    @property
    def location_hidden_from_listing(self) -> primitives.Bool | None:
        """Whether the location was marked as hidden."""
        member = self.get_member("LocationHiddenFromListing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @location_hidden_from_listing.setter
    def location_hidden_from_listing(self, value: primitives.Bool) -> None:
        """Set the LocationHiddenFromListing field value."""
        member = self.get_member("LocationHiddenFromListing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LocationHiddenFromListing", fields.FieldNullableBool(value=value)
            )

    @property
    def time_taken(self) -> str | None:
        """Exact timestamp that the screenshot was taken."""
        member = self.get_member("TimeTaken")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @time_taken.setter
    def time_taken(self, value: str) -> None:
        """Set the TimeTaken field value."""
        member = self.get_member("TimeTaken")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TimeTaken", fields.FieldDateTime(value=value)
            )

    @property
    def taken_by(self) -> members.SyncObject | None:
        """User who took the screenshot."""
        member = self.get_member("TakenBy")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @taken_by.setter
    def taken_by(self, value: members.SyncObject) -> None:
        """Set TakenBy. User who took the screenshot."""
        self.set_member("TakenBy", value)

    @property
    def taken_global_position(self) -> primitives.Float3 | None:
        """The position in global space the camera had when the photo was taken."""
        member = self.get_member("TakenGlobalPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @taken_global_position.setter
    def taken_global_position(self, value: primitives.Float3) -> None:
        """Set the TakenGlobalPosition field value."""
        member = self.get_member("TakenGlobalPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TakenGlobalPosition", fields.FieldFloat3(value=value)
            )

    @property
    def taken_global_rotation(self) -> primitives.FloatQ | None:
        """The rotation in global space the camera had when the photo was taken."""
        member = self.get_member("TakenGlobalRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @taken_global_rotation.setter
    def taken_global_rotation(self, value: primitives.FloatQ) -> None:
        """Set the TakenGlobalRotation field value."""
        member = self.get_member("TakenGlobalRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TakenGlobalRotation", fields.FieldFloatQ(value=value)
            )

    @property
    def taken_global_scale(self) -> primitives.Float3 | None:
        """The scale in global space the camera had when the photo was taken."""
        member = self.get_member("TakenGlobalScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @taken_global_scale.setter
    def taken_global_scale(self, value: primitives.Float3) -> None:
        """Set the TakenGlobalScale field value."""
        member = self.get_member("TakenGlobalScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TakenGlobalScale", fields.FieldFloat3(value=value)
            )

    @property
    def app_version(self) -> primitives.String | None:
        """Resonite version number of the photographer."""
        member = self.get_member("AppVersion")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @app_version.setter
    def app_version(self, value: primitives.String) -> None:
        """Set the AppVersion field value."""
        member = self.get_member("AppVersion")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AppVersion", fields.FieldString(value=value)
            )

    @property
    def user_infos(self) -> members.SyncList | None:
        """See UserInfo"""
        member = self.get_member("UserInfos")
        if isinstance(member, members.SyncList):
            return member
        return None

    @user_infos.setter
    def user_infos(self, value: members.SyncList) -> None:
        """Set UserInfos. See UserInfo"""
        self.set_member("UserInfos", value)

    @property
    def legacy_present_users(self) -> members.SyncList | None:
        """Internal. no longer used."""
        member = self.get_member("__legacyPresentUsers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @legacy_present_users.setter
    def legacy_present_users(self, value: members.SyncList) -> None:
        """Set __legacyPresentUsers. Internal. no longer used."""
        self.set_member("__legacyPresentUsers", value)

    @property
    def camera_manufacturer(self) -> primitives.String | None:
        """Manufacturer of the camera."""
        member = self.get_member("CameraManufacturer")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @camera_manufacturer.setter
    def camera_manufacturer(self, value: primitives.String) -> None:
        """Set the CameraManufacturer field value."""
        member = self.get_member("CameraManufacturer")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CameraManufacturer", fields.FieldString(value=value)
            )

    @property
    def camera_model(self) -> primitives.String | None:
        """Model of the camera."""
        member = self.get_member("CameraModel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @camera_model.setter
    def camera_model(self, value: primitives.String) -> None:
        """Set the CameraModel field value."""
        member = self.get_member("CameraModel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CameraModel", fields.FieldString(value=value)
            )

    @property
    def camera_fov(self) -> primitives.Float | None:
        """FOV of the camera at picture time."""
        member = self.get_member("CameraFOV")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @camera_fov.setter
    def camera_fov(self, value: primitives.Float) -> None:
        """Set the CameraFOV field value."""
        member = self.get_member("CameraFOV")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CameraFOV", fields.FieldFloat(value=value)
            )

    @property
    def is360(self) -> primitives.Bool | None:
        """Whether the image is a 360 degree image or not."""
        member = self.get_member("Is360")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is360.setter
    def is360(self, value: primitives.Bool) -> None:
        """Set the Is360 field value."""
        member = self.get_member("Is360")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Is360", fields.FieldBool(value=value)
            )

    @property
    def stereo_layout(self) -> StereoLayout | None:
        """The layout of the image's left and right sections if it is a stereoscopic image, also known as a 3D image."""
        member = self.get_member("StereoLayout")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return StereoLayout(member.value)
        return None

    @stereo_layout.setter
    def stereo_layout(self, value: StereoLayout | str) -> None:
        """Set StereoLayout. The layout of the image's left and right sections if it is a stereoscopic image, also known as a 3D image."""
        member = self.get_member("StereoLayout")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "StereoLayout",
                members.FieldEnum(value=str(value)),
            )

    async def set_from_current_world(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the SetFromCurrentWorld sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetFromCurrentWorld", {}, debug,
        )

