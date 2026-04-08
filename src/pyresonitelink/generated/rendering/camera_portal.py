"""Generated component: CameraPortal."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.mesh_renderer import MeshRenderer
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.render_texture import RenderTexture
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CameraPortal(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CameraPortal.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CameraPortal"

    def __init__(self, renderer: str | MeshRenderer | None = None, reflection_texture: str | IAssetProvider[RenderTexture] | None = None, plane_offset: np.float32 | None = None, plane_normal: primitives.Float3 | None = None, portal_target: str | Slot | None = None, clear_color: primitives.ColorX | None = None, disable_per_pixel_lights: bool | None = None, disable_shadows: bool | None = None, override_far_clip: np.float32 | None = None, override_near_clip: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            renderer: Initial value for Renderer.
            reflection_texture: Initial value for ReflectionTexture.
            plane_offset: Initial value for PlaneOffset.
            plane_normal: Initial value for PlaneNormal.
            portal_target: Initial value for PortalTarget.
            clear_color: Initial value for ClearColor.
            disable_per_pixel_lights: Initial value for DisablePerPixelLights.
            disable_shadows: Initial value for DisableShadows.
            override_far_clip: Initial value for OverrideFarClip.
            override_near_clip: Initial value for OverrideNearClip.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if renderer is not None:
            self.renderer = renderer
        if reflection_texture is not None:
            self.reflection_texture = reflection_texture
        if plane_offset is not None:
            self.plane_offset = plane_offset
        if plane_normal is not None:
            self.plane_normal = plane_normal
        if portal_target is not None:
            self.portal_target = portal_target
        if clear_color is not None:
            self.clear_color = clear_color
        if disable_per_pixel_lights is not None:
            self.disable_per_pixel_lights = disable_per_pixel_lights
        if disable_shadows is not None:
            self.disable_shadows = disable_shadows
        if override_far_clip is not None:
            self.override_far_clip = override_far_clip
        if override_near_clip is not None:
            self.override_near_clip = override_near_clip

    @property
    def renderer(self) -> str | None:
        """Target ID of the Renderer reference (targets MeshRenderer)."""
        member = self.get_member("Renderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @renderer.setter
    def renderer(self, target: str | MeshRenderer | None) -> None:
        """Set the Renderer reference by target ID or MeshRenderer instance."""
        target_id: str | None = target.id if isinstance(target, MeshRenderer) else target  # type: ignore[assignment]
        member = self.get_member("Renderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Renderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MeshRenderer'),
            )

    @property
    def reflection_texture(self) -> str | None:
        """Target ID of the ReflectionTexture reference (targets IAssetProvider[RenderTexture])."""
        member = self.get_member("ReflectionTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reflection_texture.setter
    def reflection_texture(self, target: str | IAssetProvider[RenderTexture] | None) -> None:
        """Set the ReflectionTexture reference by target ID or IAssetProvider[RenderTexture] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("ReflectionTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ReflectionTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.RenderTexture>'),
            )

    @property
    def plane_offset(self) -> np.float32 | None:
        """The PlaneOffset field value."""
        member = self.get_member("PlaneOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @plane_offset.setter
    def plane_offset(self, value: np.float32) -> None:
        """Set the PlaneOffset field value."""
        member = self.get_member("PlaneOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PlaneOffset", fields.FieldFloat(value=value)
            )

    @property
    def plane_normal(self) -> primitives.Float3 | None:
        """The PlaneNormal field value."""
        member = self.get_member("PlaneNormal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @plane_normal.setter
    def plane_normal(self, value: primitives.Float3) -> None:
        """Set the PlaneNormal field value."""
        member = self.get_member("PlaneNormal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PlaneNormal", fields.FieldFloat3(value=value)
            )

    @property
    def render_mode(self) -> members.FieldEnum | None:
        """The RenderMode member."""
        member = self.get_member("RenderMode")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @render_mode.setter
    def render_mode(self, value: members.FieldEnum) -> None:
        """Set the RenderMode member."""
        self.set_member("RenderMode", value)

    @property
    def portal_target(self) -> str | None:
        """Target ID of the PortalTarget reference (targets Slot)."""
        member = self.get_member("PortalTarget")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @portal_target.setter
    def portal_target(self, target: str | Slot | None) -> None:
        """Set the PortalTarget reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("PortalTarget")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PortalTarget",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def override_clear(self) -> members.FieldEnum | None:
        """The OverrideClear member."""
        member = self.get_member("OverrideClear")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @override_clear.setter
    def override_clear(self, value: members.FieldEnum) -> None:
        """Set the OverrideClear member."""
        self.set_member("OverrideClear", value)

    @property
    def clear_color(self) -> primitives.ColorX | None:
        """The ClearColor field value."""
        member = self.get_member("ClearColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @clear_color.setter
    def clear_color(self, value: primitives.ColorX) -> None:
        """Set the ClearColor field value."""
        member = self.get_member("ClearColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ClearColor", fields.FieldColorX(value=value)
            )

    @property
    def disable_per_pixel_lights(self) -> bool | None:
        """The DisablePerPixelLights field value."""
        member = self.get_member("DisablePerPixelLights")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disable_per_pixel_lights.setter
    def disable_per_pixel_lights(self, value: bool) -> None:
        """Set the DisablePerPixelLights field value."""
        member = self.get_member("DisablePerPixelLights")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisablePerPixelLights", fields.FieldBool(value=value)
            )

    @property
    def disable_shadows(self) -> bool | None:
        """The DisableShadows field value."""
        member = self.get_member("DisableShadows")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @disable_shadows.setter
    def disable_shadows(self, value: bool) -> None:
        """Set the DisableShadows field value."""
        member = self.get_member("DisableShadows")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DisableShadows", fields.FieldBool(value=value)
            )

    @property
    def override_far_clip(self) -> np.float32 | None:
        """The OverrideFarClip field value."""
        member = self.get_member("OverrideFarClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_far_clip.setter
    def override_far_clip(self, value: np.float32) -> None:
        """Set the OverrideFarClip field value."""
        member = self.get_member("OverrideFarClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideFarClip", fields.FieldNullableFloat(value=value)
            )

    @property
    def override_near_clip(self) -> np.float32 | None:
        """The OverrideNearClip field value."""
        member = self.get_member("OverrideNearClip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_near_clip.setter
    def override_near_clip(self, value: np.float32) -> None:
        """Set the OverrideNearClip field value."""
        member = self.get_member("OverrideNearClip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideNearClip", fields.FieldNullableFloat(value=value)
            )

