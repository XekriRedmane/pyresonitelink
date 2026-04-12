"""Generated component: CubemapCreator."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.rotation import Rotation
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.ideveloper_interface import IDeveloperInterface
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CubemapCreator(GeneratedComponent, ICustomInspector, IDeveloperInterface, IWorldEventReceiver):
    """See Cubemap Creator.

    Category: Wizards
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CubemapCreator"

    def __init__(self, top_bottom_rotation: Rotation | str | None = None, pos_x: str | IAssetProvider[Texture2D] | None = None, neg_x: str | IAssetProvider[Texture2D] | None = None, pos_y: str | IAssetProvider[Texture2D] | None = None, neg_y: str | IAssetProvider[Texture2D] | None = None, pos_z: str | IAssetProvider[Texture2D] | None = None, neg_z: str | IAssetProvider[Texture2D] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            top_bottom_rotation: Initial value for TopBottomRotation.
            pos_x: Initial value for PosX.
            neg_x: Initial value for NegX.
            pos_y: Initial value for PosY.
            neg_y: Initial value for NegY.
            pos_z: Initial value for PosZ.
            neg_z: Initial value for NegZ.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if top_bottom_rotation is not None:
            self.top_bottom_rotation = top_bottom_rotation
        if pos_x is not None:
            self.pos_x = pos_x
        if neg_x is not None:
            self.neg_x = neg_x
        if pos_y is not None:
            self.pos_y = pos_y
        if neg_y is not None:
            self.neg_y = neg_y
        if pos_z is not None:
            self.pos_z = pos_z
        if neg_z is not None:
            self.neg_z = neg_z

    @property
    def top_bottom_rotation(self) -> Rotation | None:
        """How to Rotate the top and bottom images to fit."""
        member = self.get_member("TopBottomRotation")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Rotation(member.value)
        return None

    @top_bottom_rotation.setter
    def top_bottom_rotation(self, value: Rotation | str) -> None:
        """Set TopBottomRotation. How to Rotate the top and bottom images to fit."""
        member = self.get_member("TopBottomRotation")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "TopBottomRotation",
                members.FieldEnum(value=str(value)),
            )

    @property
    def pos_x(self) -> str | None:
        """What to use for the positive X side."""
        member = self.get_member("PosX")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pos_x.setter
    def pos_x(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the PosX reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("PosX")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PosX",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

    @property
    def neg_x(self) -> str | None:
        """What to use for the negative X side."""
        member = self.get_member("NegX")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @neg_x.setter
    def neg_x(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the NegX reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("NegX")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NegX",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

    @property
    def pos_y(self) -> str | None:
        """What to use for the positive Y side."""
        member = self.get_member("PosY")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pos_y.setter
    def pos_y(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the PosY reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("PosY")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PosY",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

    @property
    def neg_y(self) -> str | None:
        """What to use for the negative Y side."""
        member = self.get_member("NegY")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @neg_y.setter
    def neg_y(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the NegY reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("NegY")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NegY",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

    @property
    def pos_z(self) -> str | None:
        """What to use for the top side."""
        member = self.get_member("PosZ")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pos_z.setter
    def pos_z(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the PosZ reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("PosZ")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PosZ",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

    @property
    def neg_z(self) -> str | None:
        """What to use for the bottom side."""
        member = self.get_member("NegZ")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @neg_z.setter
    def neg_z(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the NegZ reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("NegZ")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NegZ",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

