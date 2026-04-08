"""Generated component: FootstepSoundSplatmapSplitter."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_2d import Texture2D
from pyresonitelink.generated._types.ifootstep_sound_material import IFootstepSoundMaterial
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FootstepSoundSplatmapSplitter(GeneratedComponent, IFootstepSoundMaterial, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FootstepSoundSplatmapSplitter.

    Category: Locomotion/Footsteps
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FootstepSoundSplatmapSplitter"

    def __init__(self, splat_map: str | IAssetProvider[Texture2D] | None = None, r_sound_material: str | IFootstepSoundMaterial | None = None, g_sound_material: str | IFootstepSoundMaterial | None = None, b_sound_material: str | IFootstepSoundMaterial | None = None, a_sound_material: str | IFootstepSoundMaterial | None = None, blend_sounds: primitives.Bool | None = None, minimum_threshold: primitives.Float | None = None, r_weight: primitives.Float | None = None, g_weight: primitives.Float | None = None, b_weight: primitives.Float | None = None, a_weight: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            splat_map: Initial value for SplatMap.
            r_sound_material: Initial value for R_SoundMaterial.
            g_sound_material: Initial value for G_SoundMaterial.
            b_sound_material: Initial value for B_SoundMaterial.
            a_sound_material: Initial value for A_SoundMaterial.
            blend_sounds: Initial value for BlendSounds.
            minimum_threshold: Initial value for MinimumThreshold.
            r_weight: Initial value for R_Weight.
            g_weight: Initial value for G_Weight.
            b_weight: Initial value for B_Weight.
            a_weight: Initial value for A_Weight.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if splat_map is not None:
            self.splat_map = splat_map
        if r_sound_material is not None:
            self.r_sound_material = r_sound_material
        if g_sound_material is not None:
            self.g_sound_material = g_sound_material
        if b_sound_material is not None:
            self.b_sound_material = b_sound_material
        if a_sound_material is not None:
            self.a_sound_material = a_sound_material
        if blend_sounds is not None:
            self.blend_sounds = blend_sounds
        if minimum_threshold is not None:
            self.minimum_threshold = minimum_threshold
        if r_weight is not None:
            self.r_weight = r_weight
        if g_weight is not None:
            self.g_weight = g_weight
        if b_weight is not None:
            self.b_weight = b_weight
        if a_weight is not None:
            self.a_weight = a_weight

    @property
    def splat_map(self) -> str | None:
        """Target ID of the SplatMap reference (targets IAssetProvider[Texture2D])."""
        member = self.get_member("SplatMap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @splat_map.setter
    def splat_map(self, target: str | IAssetProvider[Texture2D] | None) -> None:
        """Set the SplatMap reference by target ID or IAssetProvider[Texture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("SplatMap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SplatMap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture2D>'),
            )

    @property
    def r_sound_material(self) -> str | None:
        """Target ID of the R_SoundMaterial reference (targets IFootstepSoundMaterial)."""
        member = self.get_member("R_SoundMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @r_sound_material.setter
    def r_sound_material(self, target: str | IFootstepSoundMaterial | None) -> None:
        """Set the R_SoundMaterial reference by target ID or IFootstepSoundMaterial instance."""
        target_id: str | None = target.id if isinstance(target, IFootstepSoundMaterial) else target  # type: ignore[assignment]
        member = self.get_member("R_SoundMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "R_SoundMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IFootstepSoundMaterial'),
            )

    @property
    def g_sound_material(self) -> str | None:
        """Target ID of the G_SoundMaterial reference (targets IFootstepSoundMaterial)."""
        member = self.get_member("G_SoundMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @g_sound_material.setter
    def g_sound_material(self, target: str | IFootstepSoundMaterial | None) -> None:
        """Set the G_SoundMaterial reference by target ID or IFootstepSoundMaterial instance."""
        target_id: str | None = target.id if isinstance(target, IFootstepSoundMaterial) else target  # type: ignore[assignment]
        member = self.get_member("G_SoundMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "G_SoundMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IFootstepSoundMaterial'),
            )

    @property
    def b_sound_material(self) -> str | None:
        """Target ID of the B_SoundMaterial reference (targets IFootstepSoundMaterial)."""
        member = self.get_member("B_SoundMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @b_sound_material.setter
    def b_sound_material(self, target: str | IFootstepSoundMaterial | None) -> None:
        """Set the B_SoundMaterial reference by target ID or IFootstepSoundMaterial instance."""
        target_id: str | None = target.id if isinstance(target, IFootstepSoundMaterial) else target  # type: ignore[assignment]
        member = self.get_member("B_SoundMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "B_SoundMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IFootstepSoundMaterial'),
            )

    @property
    def a_sound_material(self) -> str | None:
        """Target ID of the A_SoundMaterial reference (targets IFootstepSoundMaterial)."""
        member = self.get_member("A_SoundMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @a_sound_material.setter
    def a_sound_material(self, target: str | IFootstepSoundMaterial | None) -> None:
        """Set the A_SoundMaterial reference by target ID or IFootstepSoundMaterial instance."""
        target_id: str | None = target.id if isinstance(target, IFootstepSoundMaterial) else target  # type: ignore[assignment]
        member = self.get_member("A_SoundMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "A_SoundMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IFootstepSoundMaterial'),
            )

    @property
    def blend_sounds(self) -> primitives.Bool | None:
        """The BlendSounds field value."""
        member = self.get_member("BlendSounds")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @blend_sounds.setter
    def blend_sounds(self, value: primitives.Bool) -> None:
        """Set the BlendSounds field value."""
        member = self.get_member("BlendSounds")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlendSounds", fields.FieldBool(value=value)
            )

    @property
    def minimum_threshold(self) -> primitives.Float | None:
        """The MinimumThreshold field value."""
        member = self.get_member("MinimumThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @minimum_threshold.setter
    def minimum_threshold(self, value: primitives.Float) -> None:
        """Set the MinimumThreshold field value."""
        member = self.get_member("MinimumThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinimumThreshold", fields.FieldFloat(value=value)
            )

    @property
    def r_weight(self) -> primitives.Float | None:
        """The R_Weight field value."""
        member = self.get_member("R_Weight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @r_weight.setter
    def r_weight(self, value: primitives.Float) -> None:
        """Set the R_Weight field value."""
        member = self.get_member("R_Weight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "R_Weight", fields.FieldFloat(value=value)
            )

    @property
    def g_weight(self) -> primitives.Float | None:
        """The G_Weight field value."""
        member = self.get_member("G_Weight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @g_weight.setter
    def g_weight(self, value: primitives.Float) -> None:
        """Set the G_Weight field value."""
        member = self.get_member("G_Weight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "G_Weight", fields.FieldFloat(value=value)
            )

    @property
    def b_weight(self) -> primitives.Float | None:
        """The B_Weight field value."""
        member = self.get_member("B_Weight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @b_weight.setter
    def b_weight(self, value: primitives.Float) -> None:
        """Set the B_Weight field value."""
        member = self.get_member("B_Weight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "B_Weight", fields.FieldFloat(value=value)
            )

    @property
    def a_weight(self) -> primitives.Float | None:
        """The A_Weight field value."""
        member = self.get_member("A_Weight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @a_weight.setter
    def a_weight(self, value: primitives.Float) -> None:
        """Set the A_Weight field value."""
        member = self.get_member("A_Weight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "A_Weight", fields.FieldFloat(value=value)
            )

