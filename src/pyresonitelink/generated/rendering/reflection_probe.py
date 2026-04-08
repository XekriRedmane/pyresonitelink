"""Generated component: ReflectionProbe."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.cubemap import Cubemap
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReflectionProbe(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ReflectionProbe.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReflectionProbe"

    def __init__(self, importance: primitives.Int | None = None, intensity: primitives.Float | None = None, blend_distance: primitives.Float | None = None, box_size: primitives.Float3 | None = None, box_projection: primitives.Bool | None = None, baked_cubemap: str | IAssetProvider[Cubemap] | None = None, resolution: primitives.Int | None = None, hdr: primitives.Bool | None = None, shadow_distance: primitives.Float | None = None, background_color: primitives.ColorX | None = None, near_clip: primitives.Float | None = None, far_clip: primitives.Float | None = None, skybox_only: primitives.Bool | None = None, show_debug_visuals: primitives.Bool | None = None, debug_visual: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            importance: Initial value for Importance.
            intensity: Initial value for Intensity.
            blend_distance: Initial value for BlendDistance.
            box_size: Initial value for BoxSize.
            box_projection: Initial value for BoxProjection.
            baked_cubemap: Initial value for BakedCubemap.
            resolution: Initial value for Resolution.
            hdr: Initial value for HDR.
            shadow_distance: Initial value for ShadowDistance.
            background_color: Initial value for BackgroundColor.
            near_clip: Initial value for NearClip.
            far_clip: Initial value for FarClip.
            skybox_only: Initial value for SkyboxOnly.
            show_debug_visuals: Initial value for ShowDebugVisuals.
            debug_visual: Initial value for _debugVisual.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if importance is not None:
            self.importance = importance
        if intensity is not None:
            self.intensity = intensity
        if blend_distance is not None:
            self.blend_distance = blend_distance
        if box_size is not None:
            self.box_size = box_size
        if box_projection is not None:
            self.box_projection = box_projection
        if baked_cubemap is not None:
            self.baked_cubemap = baked_cubemap
        if resolution is not None:
            self.resolution = resolution
        if hdr is not None:
            self.hdr = hdr
        if shadow_distance is not None:
            self.shadow_distance = shadow_distance
        if background_color is not None:
            self.background_color = background_color
        if near_clip is not None:
            self.near_clip = near_clip
        if far_clip is not None:
            self.far_clip = far_clip
        if skybox_only is not None:
            self.skybox_only = skybox_only
        if show_debug_visuals is not None:
            self.show_debug_visuals = show_debug_visuals
        if debug_visual is not None:
            self.debug_visual = debug_visual

    @property
    def probe_type(self) -> members.FieldEnum | None:
        """The ProbeType member."""
        member = self.get_member("ProbeType")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @probe_type.setter
    def probe_type(self, value: members.FieldEnum) -> None:
        """Set the ProbeType member."""
        self.set_member("ProbeType", value)

    @property
    def importance(self) -> primitives.Int | None:
        """The Importance field value."""
        member = self.get_member("Importance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @importance.setter
    def importance(self, value: primitives.Int) -> None:
        """Set the Importance field value."""
        member = self.get_member("Importance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Importance", fields.FieldInt(value=value)
            )

    @property
    def intensity(self) -> primitives.Float | None:
        """The Intensity field value."""
        member = self.get_member("Intensity")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @intensity.setter
    def intensity(self, value: primitives.Float) -> None:
        """Set the Intensity field value."""
        member = self.get_member("Intensity")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Intensity", fields.FieldFloat(value=value)
            )

    @property
    def blend_distance(self) -> primitives.Float | None:
        """The BlendDistance field value."""
        member = self.get_member("BlendDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @blend_distance.setter
    def blend_distance(self, value: primitives.Float) -> None:
        """Set the BlendDistance field value."""
        member = self.get_member("BlendDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlendDistance", fields.FieldFloat(value=value)
            )

    @property
    def box_size(self) -> primitives.Float3 | None:
        """The BoxSize field value."""
        member = self.get_member("BoxSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @box_size.setter
    def box_size(self, value: primitives.Float3) -> None:
        """Set the BoxSize field value."""
        member = self.get_member("BoxSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BoxSize", fields.FieldFloat3(value=value)
            )

    @property
    def box_projection(self) -> primitives.Bool | None:
        """The BoxProjection field value."""
        member = self.get_member("BoxProjection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @box_projection.setter
    def box_projection(self, value: primitives.Bool) -> None:
        """Set the BoxProjection field value."""
        member = self.get_member("BoxProjection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BoxProjection", fields.FieldBool(value=value)
            )

    @property
    def baked_cubemap(self) -> str | None:
        """Target ID of the BakedCubemap reference (targets IAssetProvider[Cubemap])."""
        member = self.get_member("BakedCubemap")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @baked_cubemap.setter
    def baked_cubemap(self, target: str | IAssetProvider[Cubemap] | None) -> None:
        """Set the BakedCubemap reference by target ID or IAssetProvider[Cubemap] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("BakedCubemap")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BakedCubemap",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Cubemap>'),
            )

    @property
    def changes_sources(self) -> members.SyncList | None:
        """The ChangesSources member."""
        member = self.get_member("ChangesSources")
        if isinstance(member, members.SyncList):
            return member
        return None

    @changes_sources.setter
    def changes_sources(self, value: members.SyncList) -> None:
        """Set the ChangesSources member."""
        self.set_member("ChangesSources", value)

    @property
    def time_slicing(self) -> members.FieldEnum | None:
        """The TimeSlicing member."""
        member = self.get_member("TimeSlicing")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @time_slicing.setter
    def time_slicing(self, value: members.FieldEnum) -> None:
        """Set the TimeSlicing member."""
        self.set_member("TimeSlicing", value)

    @property
    def resolution(self) -> primitives.Int | None:
        """The Resolution field value."""
        member = self.get_member("Resolution")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @resolution.setter
    def resolution(self, value: primitives.Int) -> None:
        """Set the Resolution field value."""
        member = self.get_member("Resolution")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Resolution", fields.FieldInt(value=value)
            )

    @property
    def hdr(self) -> primitives.Bool | None:
        """The HDR field value."""
        member = self.get_member("HDR")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hdr.setter
    def hdr(self, value: primitives.Bool) -> None:
        """Set the HDR field value."""
        member = self.get_member("HDR")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HDR", fields.FieldBool(value=value)
            )

    @property
    def shadow_distance(self) -> primitives.Float | None:
        """The ShadowDistance field value."""
        member = self.get_member("ShadowDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @shadow_distance.setter
    def shadow_distance(self, value: primitives.Float) -> None:
        """Set the ShadowDistance field value."""
        member = self.get_member("ShadowDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShadowDistance", fields.FieldFloat(value=value)
            )

    @property
    def clear_flags(self) -> members.FieldEnum | None:
        """The ClearFlags member."""
        member = self.get_member("ClearFlags")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @clear_flags.setter
    def clear_flags(self, value: members.FieldEnum) -> None:
        """Set the ClearFlags member."""
        self.set_member("ClearFlags", value)

    @property
    def background_color(self) -> primitives.ColorX | None:
        """The BackgroundColor field value."""
        member = self.get_member("BackgroundColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @background_color.setter
    def background_color(self, value: primitives.ColorX) -> None:
        """Set the BackgroundColor field value."""
        member = self.get_member("BackgroundColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BackgroundColor", fields.FieldColorX(value=value)
            )

    @property
    def near_clip(self) -> primitives.Float | None:
        """The NearClip field value."""
        member = self.get_member("NearClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_clip.setter
    def near_clip(self, value: primitives.Float) -> None:
        """Set the NearClip field value."""
        member = self.get_member("NearClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearClip", fields.FieldFloat(value=value)
            )

    @property
    def far_clip(self) -> primitives.Float | None:
        """The FarClip field value."""
        member = self.get_member("FarClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_clip.setter
    def far_clip(self, value: primitives.Float) -> None:
        """Set the FarClip field value."""
        member = self.get_member("FarClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarClip", fields.FieldFloat(value=value)
            )

    @property
    def skybox_only(self) -> primitives.Bool | None:
        """The SkyboxOnly field value."""
        member = self.get_member("SkyboxOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @skybox_only.setter
    def skybox_only(self, value: primitives.Bool) -> None:
        """Set the SkyboxOnly field value."""
        member = self.get_member("SkyboxOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SkyboxOnly", fields.FieldBool(value=value)
            )

    @property
    def show_debug_visuals(self) -> primitives.Bool | None:
        """The ShowDebugVisuals field value."""
        member = self.get_member("ShowDebugVisuals")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_debug_visuals.setter
    def show_debug_visuals(self, value: primitives.Bool) -> None:
        """Set the ShowDebugVisuals field value."""
        member = self.get_member("ShowDebugVisuals")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowDebugVisuals", fields.FieldBool(value=value)
            )

    @property
    def debug_visual(self) -> str | None:
        """Target ID of the _debugVisual reference (targets Slot)."""
        member = self.get_member("_debugVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @debug_visual.setter
    def debug_visual(self, target: str | Slot | None) -> None:
        """Set the _debugVisual reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_debugVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_debugVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    async def bake(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the Bake sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Bake", {}, debug,
        )

