"""Generated component: TextureSizeDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.mode import Mode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TextureSizeDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The TextureSizeDriver component drives a field with the size of a texture in pixels.

    Category: Transform/Drivers

    Attach to a slot and provide a ``Texture`` and a ``Target`` to get
    started.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TextureSizeDriver"

    def __init__(self, texture: str | IAssetProvider[ITexture2D] | None = None, target: str | IField[primitives.Float2] | None = None, drive_mode: Mode | str | None = None, premultiply: primitives.Float2 | None = None, ratio: primitives.Float2 | None = None, max_size: primitives.Float2 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            texture: Initial value for Texture.
            target: Initial value for Target.
            drive_mode: Initial value for DriveMode.
            premultiply: Initial value for Premultiply.
            ratio: Initial value for Ratio.
            max_size: Initial value for MaxSize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if texture is not None:
            self.texture = texture
        if target is not None:
            self.target = target
        if drive_mode is not None:
            self.drive_mode = drive_mode
        if premultiply is not None:
            self.premultiply = premultiply
        if ratio is not None:
            self.ratio = ratio
        if max_size is not None:
            self.max_size = max_size

    @property
    def texture(self) -> str | None:
        """The texture to get a size from."""
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the Texture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def target(self) -> str | None:
        """The value field to drive with the final result value."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def drive_mode(self) -> Mode | None:
        """The way of restricting ``Texture`` size values as second step."""
        member = self.get_member("DriveMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Mode(member.value)
        return None

    @drive_mode.setter
    def drive_mode(self, value: Mode | str) -> None:
        """Set DriveMode. The way of restricting ``Texture`` size values as second step."""
        member = self.get_member("DriveMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "DriveMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def premultiply(self) -> primitives.Float2 | None:
        """The value to multiply the ``Texture`` size by as first step."""
        member = self.get_member("Premultiply")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @premultiply.setter
    def premultiply(self, value: primitives.Float2) -> None:
        """Set the Premultiply field value."""
        member = self.get_member("Premultiply")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Premultiply", fields.FieldFloat2(value=value)
            )

    @property
    def ratio(self) -> primitives.Float2 | None:
        """The value to multiply the ``Texture`` size by as the third step."""
        member = self.get_member("Ratio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ratio.setter
    def ratio(self, value: primitives.Float2) -> None:
        """Set the Ratio field value."""
        member = self.get_member("Ratio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Ratio", fields.FieldFloat2(value=value)
            )

    @property
    def max_size(self) -> primitives.Float2 | None:
        """The value to restrict the output value to be less than this as the final step."""
        member = self.get_member("MaxSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_size.setter
    def max_size(self, value: primitives.Float2) -> None:
        """Set the MaxSize field value."""
        member = self.get_member("MaxSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSize", fields.FieldFloat2(value=value)
            )

