"""Generated component: ReflectionProbe."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.reflection_probe_type import ReflectionProbeType
from pyresonitelink.generated._enums.reflection_probe_time_slicing_mode import ReflectionProbeTimeSlicingMode
from pyresonitelink.generated._enums.reflection_probe_clear import ReflectionProbeClear
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.cubemap import Cubemap
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReflectionProbe(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """The ReflectionProbe component is used to make points in space that makes reflective surfaces within a box around the point show a different reflection map than the skybox. This is useful for controlling the lighting and look of a scene.

    Category: Rendering

    Attach to a slot to start using this component as a point source for
    reflection map data.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReflectionProbe"

    def __init__(self, probe_type: ReflectionProbeType | str | None = None, importance: primitives.Int | None = None, intensity: primitives.Float | None = None, blend_distance: primitives.Float | None = None, box_size: primitives.Float3 | None = None, box_projection: primitives.Bool | None = None, baked_cubemap: str | IAssetProvider[Cubemap] | None = None, time_slicing: ReflectionProbeTimeSlicingMode | str | None = None, resolution: primitives.Int | None = None, hdr: primitives.Bool | None = None, shadow_distance: primitives.Float | None = None, clear_flags: ReflectionProbeClear | str | None = None, background_color: primitives.ColorX | None = None, near_clip: primitives.Float | None = None, far_clip: primitives.Float | None = None, skybox_only: primitives.Bool | None = None, show_debug_visuals: primitives.Bool | None = None, debug_visual: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            probe_type: Initial value for ProbeType.
            importance: Initial value for Importance.
            intensity: Initial value for Intensity.
            blend_distance: Initial value for BlendDistance.
            box_size: Initial value for BoxSize.
            box_projection: Initial value for BoxProjection.
            baked_cubemap: Initial value for BakedCubemap.
            time_slicing: Initial value for TimeSlicing.
            resolution: Initial value for Resolution.
            hdr: Initial value for HDR.
            shadow_distance: Initial value for ShadowDistance.
            clear_flags: Initial value for ClearFlags.
            background_color: Initial value for BackgroundColor.
            near_clip: Initial value for NearClip.
            far_clip: Initial value for FarClip.
            skybox_only: Initial value for SkyboxOnly.
            show_debug_visuals: Initial value for ShowDebugVisuals.
            debug_visual: Initial value for _debugVisual.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if probe_type is not None:
            self.probe_type = probe_type
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
        if time_slicing is not None:
            self.time_slicing = time_slicing
        if resolution is not None:
            self.resolution = resolution
        if hdr is not None:
            self.hdr = hdr
        if shadow_distance is not None:
            self.shadow_distance = shadow_distance
        if clear_flags is not None:
            self.clear_flags = clear_flags
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
    def probe_type(self) -> ReflectionProbeType | None:
        """What mode this reflection probe uses."""
        member = self.get_member("ProbeType")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ReflectionProbeType(member.value)
        return None

    @probe_type.setter
    def probe_type(self, value: ReflectionProbeType | str) -> None:
        """Set ProbeType. What mode this reflection probe uses."""
        member = self.get_member("ProbeType")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ProbeType",
                members.FieldEnum(value=str(value)),
            )

    @property
    def importance(self) -> primitives.Int | None:
        """How much priority this probe takes over another probe when two probes overlap"""
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
        """how strong or bright the reflection is"""
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
        """how far the probe will slowly take over the reflection map of objects as an object goes towards the center of influence"""
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
        """the area that this reflection probe will affect the reflection maps of objects"""
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
        """project the reflection map in a box shape from the reflection probe rather than a sphere."""
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
        """The cube map to replace the refection maps of reflective objects with in the influence area of this reflection probe"""
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
        """A list of elements that will prompt this reflection probe to render a new map whenever they change."""
        member = self.get_member("ChangesSources")
        if isinstance(member, members.SyncList):
            return member
        return None

    @changes_sources.setter
    def changes_sources(self, value: members.SyncList) -> None:
        """Set ChangesSources. A list of elements that will prompt this reflection probe to render a new map whenever they change."""
        self.set_member("ChangesSources", value)

    @property
    def time_slicing(self) -> ReflectionProbeTimeSlicingMode | None:
        """How updates to this reflection probe should happen in updates if this probe is a realtime probe."""
        member = self.get_member("TimeSlicing")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ReflectionProbeTimeSlicingMode(member.value)
        return None

    @time_slicing.setter
    def time_slicing(self, value: ReflectionProbeTimeSlicingMode | str) -> None:
        """Set TimeSlicing. How updates to this reflection probe should happen in updates if this probe is a realtime probe."""
        member = self.get_member("TimeSlicing")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "TimeSlicing",
                members.FieldEnum(value=str(value)),
            )

    @property
    def resolution(self) -> primitives.Int | None:
        """the forced resolution of the reflection map from this reflection probe shown in the reflections of shiny objects."""
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
        """Whether the color encoding should be in HDR."""
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
        """how far to render shadows from the reflection probe"""
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
    def clear_flags(self) -> ReflectionProbeClear | None:
        """Whether to use the skybox or color when backing transparent pixels"""
        member = self.get_member("ClearFlags")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ReflectionProbeClear(member.value)
        return None

    @clear_flags.setter
    def clear_flags(self, value: ReflectionProbeClear | str) -> None:
        """Set ClearFlags. Whether to use the skybox or color when backing transparent pixels"""
        member = self.get_member("ClearFlags")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ClearFlags",
                members.FieldEnum(value=str(value)),
            )

    @property
    def background_color(self) -> primitives.ColorX | None:
        """The color to clear with when ``ClearFlags`` is set to "Color\""""
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
        """The closest distance to render from the reflection probe center when using "Realtime" on ``ProbeType``"""
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
        """The furthest distance to render from the reflection probe center when using "Realtime" on ``ProbeType``"""
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
        """Whether to render only the skybox or not."""
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
        """Shows the box influence area and the center point of this reflection probe"""
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
        """The current debug visual that this reflection probe is showing, if applicable."""
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
        """Creates a static cubemap and inserts it into ``BakedCubemap`` instead of having ``ProbeType`` be set to realtime.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Bake", {}, debug,
        )

