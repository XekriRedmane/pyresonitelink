"""Generated component: MaterialAssetMetadata."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MaterialAssetMetadata(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MaterialAssetMetadata.

    Category: Assets/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MaterialAssetMetadata"

    def __init__(self, material: str | IAssetProvider[Material] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material: Initial value for Material.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if material is not None:
            self.material = material

    @property
    def material(self) -> str | None:
        """Target ID of the Material reference (targets IAssetProvider[Material])."""
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | IAssetProvider[Material] | None) -> None:
        """Set the Material reference by target ID or IAssetProvider[Material] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>'),
            )

    @property
    def variant_index(self) -> members.EmptyElement | None:
        """The VariantIndex member."""
        member = self.get_member("VariantIndex")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @variant_index.setter
    def variant_index(self, value: members.EmptyElement) -> None:
        """Set the VariantIndex member."""
        self.set_member("VariantIndex", value)

    @property
    def raw_variant_index(self) -> members.EmptyElement | None:
        """The RawVariantIndex member."""
        member = self.get_member("RawVariantIndex")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @raw_variant_index.setter
    def raw_variant_index(self, value: members.EmptyElement) -> None:
        """Set the RawVariantIndex member."""
        self.set_member("RawVariantIndex", value)

    @property
    def variant_id(self) -> members.EmptyElement | None:
        """The VariantID member."""
        member = self.get_member("VariantID")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @variant_id.setter
    def variant_id(self, value: members.EmptyElement) -> None:
        """Set the VariantID member."""
        self.set_member("VariantID", value)

    @property
    def raw_variant_id(self) -> members.EmptyElement | None:
        """The RawVariantID member."""
        member = self.get_member("RawVariantID")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @raw_variant_id.setter
    def raw_variant_id(self, value: members.EmptyElement) -> None:
        """Set the RawVariantID member."""
        self.set_member("RawVariantID", value)

    @property
    def waiting_for_apply(self) -> members.EmptyElement | None:
        """The WaitingForApply member."""
        member = self.get_member("WaitingForApply")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @waiting_for_apply.setter
    def waiting_for_apply(self, value: members.EmptyElement) -> None:
        """Set the WaitingForApply member."""
        self.set_member("WaitingForApply", value)

