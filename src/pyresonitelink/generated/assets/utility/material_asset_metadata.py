"""Generated component: MaterialAssetMetadata."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
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

    def __init__(self, material: str | IAssetProvider[Material] | None = None, variant_index: primitives.UInt | None = None, raw_variant_index: primitives.UInt | None = None, variant_id: primitives.String | None = None, raw_variant_id: primitives.String | None = None, waiting_for_apply: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            material: Initial value for Material.
            variant_index: Initial value for VariantIndex.
            raw_variant_index: Initial value for RawVariantIndex.
            variant_id: Initial value for VariantID.
            raw_variant_id: Initial value for RawVariantID.
            waiting_for_apply: Initial value for WaitingForApply.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if material is not None:
            self.material = material
        if variant_index is not None:
            self.variant_index = variant_index
        if raw_variant_index is not None:
            self.raw_variant_index = raw_variant_index
        if variant_id is not None:
            self.variant_id = variant_id
        if raw_variant_id is not None:
            self.raw_variant_id = raw_variant_id
        if waiting_for_apply is not None:
            self.waiting_for_apply = waiting_for_apply

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
    def variant_index(self) -> primitives.UInt | None:
        """The VariantIndex field value."""
        member = self.get_member("VariantIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @variant_index.setter
    def variant_index(self, value: primitives.UInt) -> None:
        """Set the VariantIndex field value."""
        member = self.get_member("VariantIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VariantIndex", fields.FieldNullableUint(value=value)
            )

    @property
    def raw_variant_index(self) -> primitives.UInt | None:
        """The RawVariantIndex field value."""
        member = self.get_member("RawVariantIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @raw_variant_index.setter
    def raw_variant_index(self, value: primitives.UInt) -> None:
        """Set the RawVariantIndex field value."""
        member = self.get_member("RawVariantIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RawVariantIndex", fields.FieldNullableUint(value=value)
            )

    @property
    def variant_id(self) -> primitives.String | None:
        """The VariantID field value."""
        member = self.get_member("VariantID")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @variant_id.setter
    def variant_id(self, value: primitives.String) -> None:
        """Set the VariantID field value."""
        member = self.get_member("VariantID")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VariantID", fields.FieldString(value=value)
            )

    @property
    def raw_variant_id(self) -> primitives.String | None:
        """The RawVariantID field value."""
        member = self.get_member("RawVariantID")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @raw_variant_id.setter
    def raw_variant_id(self, value: primitives.String) -> None:
        """Set the RawVariantID field value."""
        member = self.get_member("RawVariantID")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RawVariantID", fields.FieldString(value=value)
            )

    @property
    def waiting_for_apply(self) -> primitives.Bool | None:
        """The WaitingForApply field value."""
        member = self.get_member("WaitingForApply")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @waiting_for_apply.setter
    def waiting_for_apply(self, value: primitives.Bool) -> None:
        """Set the WaitingForApply field value."""
        member = self.get_member("WaitingForApply")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WaitingForApply", fields.FieldBool(value=value)
            )

