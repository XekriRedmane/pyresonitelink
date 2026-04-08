"""Generated component: GaussianSplatRenderer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.gaussian_splat import GaussianSplat
from pyresonitelink.generated._types.ibounded import IBounded
from pyresonitelink.generated._types.irenderable import IRenderable
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GaussianSplatRenderer(GeneratedComponent, IBounded, IRenderable, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GaussianSplatRenderer.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GaussianSplatRenderer"

    def __init__(self, gaussian_splat: str | IAssetProvider[GaussianSplat] | None = None, size_scale: primitives.Float | None = None, opacity_scale: primitives.Float | None = None, max_sh_order: primitives.Int | None = None, spherical_harmonics_only: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            gaussian_splat: Initial value for GaussianSplat.
            size_scale: Initial value for SizeScale.
            opacity_scale: Initial value for OpacityScale.
            max_sh_order: Initial value for MaxSHOrder.
            spherical_harmonics_only: Initial value for SphericalHarmonicsOnly.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if gaussian_splat is not None:
            self.gaussian_splat = gaussian_splat
        if size_scale is not None:
            self.size_scale = size_scale
        if opacity_scale is not None:
            self.opacity_scale = opacity_scale
        if max_sh_order is not None:
            self.max_sh_order = max_sh_order
        if spherical_harmonics_only is not None:
            self.spherical_harmonics_only = spherical_harmonics_only

    @property
    def gaussian_splat(self) -> str | None:
        """Target ID of the GaussianSplat reference (targets IAssetProvider[GaussianSplat])."""
        member = self.get_member("GaussianSplat")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @gaussian_splat.setter
    def gaussian_splat(self, target: str | IAssetProvider[GaussianSplat] | None) -> None:
        """Set the GaussianSplat reference by target ID or IAssetProvider[GaussianSplat] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("GaussianSplat")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "GaussianSplat",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.GaussianSplat>'),
            )

    @property
    def size_scale(self) -> primitives.Float | None:
        """The SizeScale field value."""
        member = self.get_member("SizeScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size_scale.setter
    def size_scale(self, value: primitives.Float) -> None:
        """Set the SizeScale field value."""
        member = self.get_member("SizeScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SizeScale", fields.FieldFloat(value=value)
            )

    @property
    def opacity_scale(self) -> primitives.Float | None:
        """The OpacityScale field value."""
        member = self.get_member("OpacityScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @opacity_scale.setter
    def opacity_scale(self, value: primitives.Float) -> None:
        """Set the OpacityScale field value."""
        member = self.get_member("OpacityScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OpacityScale", fields.FieldFloat(value=value)
            )

    @property
    def max_sh_order(self) -> primitives.Int | None:
        """The MaxSHOrder field value."""
        member = self.get_member("MaxSHOrder")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_sh_order.setter
    def max_sh_order(self, value: primitives.Int) -> None:
        """Set the MaxSHOrder field value."""
        member = self.get_member("MaxSHOrder")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSHOrder", fields.FieldNullableInt(value=value)
            )

    @property
    def spherical_harmonics_only(self) -> primitives.Bool | None:
        """The SphericalHarmonicsOnly field value."""
        member = self.get_member("SphericalHarmonicsOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spherical_harmonics_only.setter
    def spherical_harmonics_only(self, value: primitives.Bool) -> None:
        """Set the SphericalHarmonicsOnly field value."""
        member = self.get_member("SphericalHarmonicsOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SphericalHarmonicsOnly", fields.FieldBool(value=value)
            )

