"""Generated component: RadiantDash."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.radiant_dash_screen import RadiantDashScreen
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.camera import Camera
from pyresonitelink.generated._types.render_texture_provider import RenderTextureProvider
from pyresonitelink.generated._types.curved_plane_mesh import CurvedPlaneMesh
from pyresonitelink.generated._types.unlit_material import UnlitMaterial
from pyresonitelink.generated._types.ui_unlit_material import UI_UnlitMaterial
from pyresonitelink.generated._types.uv_rect_material import UV_RectMaterial
from pyresonitelink.generated._types.canvas import Canvas
from pyresonitelink.generated._types.particle_style import ParticleStyle
from pyresonitelink.generated._types.color_range_initializer import ColorRangeInitializer
from pyresonitelink.generated._types.mesh_emitter import MeshEmitter
from pyresonitelink.generated._types.mesh_collider import MeshCollider
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RadiantDash(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RadiantDash.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RadiantDash"

    def __init__(self, current_screen: str | RadiantDashScreen | None = None, open: bool | None = None, animation_speed: np.float32 | None = None, screen_projection: bool | None = None, curvature: np.float32 | None = None, screen_switching_enabled: bool | None = None, screens_container: str | Slot | None = None, camera: str | Camera | None = None, render_texture: str | RenderTextureProvider | None = None, top_container: str | Slot | None = None, top_mesh: str | CurvedPlaneMesh | None = None, screen_mesh: str | CurvedPlaneMesh | None = None, buttons_mesh: str | CurvedPlaneMesh | None = None, top_material: str | UnlitMaterial | None = None, screen_material: str | UnlitMaterial | None = None, buttons_material: str | UnlitMaterial | None = None, overlay_effect_material: str | UI_UnlitMaterial | None = None, top_border_material: str | UV_RectMaterial | None = None, screen_border_material: str | UV_RectMaterial | None = None, buttons_border_material: str | UV_RectMaterial | None = None, render_root: str | Slot | None = None, top_root: str | Slot | None = None, screen_root: str | Slot | None = None, buttons_root: str | Slot | None = None, visuals_root: str | Slot | None = None, effect_root: str | Slot | None = None, top_canvas: str | Canvas | None = None, buttons_uiroot: str | Slot | None = None, buttons_canvas: str | Canvas | None = None, style: str | ParticleStyle | None = None, particle_colors: str | ColorRangeInitializer | None = None, emitter: str | MeshEmitter | None = None, top_collider: str | MeshCollider | None = None, screen_collider: str | MeshCollider | None = None, buttons_collider: str | MeshCollider | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            current_screen: Initial value for CurrentScreen.
            open: Initial value for Open.
            animation_speed: Initial value for AnimationSpeed.
            screen_projection: Initial value for ScreenProjection.
            curvature: Initial value for Curvature.
            screen_switching_enabled: Initial value for ScreenSwitchingEnabled.
            screens_container: Initial value for _screensContainer.
            camera: Initial value for _camera.
            render_texture: Initial value for _renderTexture.
            top_container: Initial value for _topContainer.
            top_mesh: Initial value for _topMesh.
            screen_mesh: Initial value for _screenMesh.
            buttons_mesh: Initial value for _buttonsMesh.
            top_material: Initial value for _topMaterial.
            screen_material: Initial value for _screenMaterial.
            buttons_material: Initial value for _buttonsMaterial.
            overlay_effect_material: Initial value for _overlayEffectMaterial.
            top_border_material: Initial value for _topBorderMaterial.
            screen_border_material: Initial value for _screenBorderMaterial.
            buttons_border_material: Initial value for _buttonsBorderMaterial.
            render_root: Initial value for _renderRoot.
            top_root: Initial value for _topRoot.
            screen_root: Initial value for _screenRoot.
            buttons_root: Initial value for _buttonsRoot.
            visuals_root: Initial value for _visualsRoot.
            effect_root: Initial value for _effectRoot.
            top_canvas: Initial value for _topCanvas.
            buttons_uiroot: Initial value for _buttonsUIroot.
            buttons_canvas: Initial value for _buttonsCanvas.
            style: Initial value for _style.
            particle_colors: Initial value for _particleColors.
            emitter: Initial value for _emitter.
            top_collider: Initial value for _topCollider.
            screen_collider: Initial value for _screenCollider.
            buttons_collider: Initial value for _buttonsCollider.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if current_screen is not None:
            self.current_screen = current_screen
        if open is not None:
            self.open = open
        if animation_speed is not None:
            self.animation_speed = animation_speed
        if screen_projection is not None:
            self.screen_projection = screen_projection
        if curvature is not None:
            self.curvature = curvature
        if screen_switching_enabled is not None:
            self.screen_switching_enabled = screen_switching_enabled
        if screens_container is not None:
            self.screens_container = screens_container
        if camera is not None:
            self.camera = camera
        if render_texture is not None:
            self.render_texture = render_texture
        if top_container is not None:
            self.top_container = top_container
        if top_mesh is not None:
            self.top_mesh = top_mesh
        if screen_mesh is not None:
            self.screen_mesh = screen_mesh
        if buttons_mesh is not None:
            self.buttons_mesh = buttons_mesh
        if top_material is not None:
            self.top_material = top_material
        if screen_material is not None:
            self.screen_material = screen_material
        if buttons_material is not None:
            self.buttons_material = buttons_material
        if overlay_effect_material is not None:
            self.overlay_effect_material = overlay_effect_material
        if top_border_material is not None:
            self.top_border_material = top_border_material
        if screen_border_material is not None:
            self.screen_border_material = screen_border_material
        if buttons_border_material is not None:
            self.buttons_border_material = buttons_border_material
        if render_root is not None:
            self.render_root = render_root
        if top_root is not None:
            self.top_root = top_root
        if screen_root is not None:
            self.screen_root = screen_root
        if buttons_root is not None:
            self.buttons_root = buttons_root
        if visuals_root is not None:
            self.visuals_root = visuals_root
        if effect_root is not None:
            self.effect_root = effect_root
        if top_canvas is not None:
            self.top_canvas = top_canvas
        if buttons_uiroot is not None:
            self.buttons_uiroot = buttons_uiroot
        if buttons_canvas is not None:
            self.buttons_canvas = buttons_canvas
        if style is not None:
            self.style = style
        if particle_colors is not None:
            self.particle_colors = particle_colors
        if emitter is not None:
            self.emitter = emitter
        if top_collider is not None:
            self.top_collider = top_collider
        if screen_collider is not None:
            self.screen_collider = screen_collider
        if buttons_collider is not None:
            self.buttons_collider = buttons_collider

    @property
    def current_screen(self) -> str | None:
        """Target ID of the CurrentScreen reference (targets RadiantDashScreen)."""
        member = self.get_member("CurrentScreen")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_screen.setter
    def current_screen(self, target: str | RadiantDashScreen | None) -> None:
        """Set the CurrentScreen reference by target ID or RadiantDashScreen instance."""
        target_id: str | None = target.id if isinstance(target, RadiantDashScreen) else target  # type: ignore[assignment]
        member = self.get_member("CurrentScreen")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CurrentScreen",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RadiantDashScreen'),
            )

    @property
    def open(self) -> bool | None:
        """The Open field value."""
        member = self.get_member("Open")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @open.setter
    def open(self, value: bool) -> None:
        """Set the Open field value."""
        member = self.get_member("Open")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Open", fields.FieldBool(value=value)
            )

    @property
    def animation_speed(self) -> np.float32 | None:
        """The AnimationSpeed field value."""
        member = self.get_member("AnimationSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @animation_speed.setter
    def animation_speed(self, value: np.float32) -> None:
        """Set the AnimationSpeed field value."""
        member = self.get_member("AnimationSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnimationSpeed", fields.FieldFloat(value=value)
            )

    @property
    def screen_projection(self) -> bool | None:
        """The ScreenProjection field value."""
        member = self.get_member("ScreenProjection")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @screen_projection.setter
    def screen_projection(self, value: bool) -> None:
        """Set the ScreenProjection field value."""
        member = self.get_member("ScreenProjection")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScreenProjection", fields.FieldBool(value=value)
            )

    @property
    def curvature(self) -> np.float32 | None:
        """The Curvature field value."""
        member = self.get_member("Curvature")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @curvature.setter
    def curvature(self, value: np.float32) -> None:
        """Set the Curvature field value."""
        member = self.get_member("Curvature")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Curvature", fields.FieldFloat(value=value)
            )

    @property
    def aspect_ratio_compensation(self) -> members.FieldEnum | None:
        """The AspectRatioCompensation member."""
        member = self.get_member("AspectRatioCompensation")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @aspect_ratio_compensation.setter
    def aspect_ratio_compensation(self, value: members.FieldEnum) -> None:
        """Set the AspectRatioCompensation member."""
        self.set_member("AspectRatioCompensation", value)

    @property
    def screen_switching_enabled(self) -> bool | None:
        """The ScreenSwitchingEnabled field value."""
        member = self.get_member("ScreenSwitchingEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @screen_switching_enabled.setter
    def screen_switching_enabled(self, value: bool) -> None:
        """Set the ScreenSwitchingEnabled field value."""
        member = self.get_member("ScreenSwitchingEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScreenSwitchingEnabled", fields.FieldBool(value=value)
            )

    @property
    def screens_container(self) -> str | None:
        """Target ID of the _screensContainer reference (targets Slot)."""
        member = self.get_member("_screensContainer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @screens_container.setter
    def screens_container(self, target: str | Slot | None) -> None:
        """Set the _screensContainer reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_screensContainer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_screensContainer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def camera(self) -> str | None:
        """Target ID of the _camera reference (targets Camera)."""
        member = self.get_member("_camera")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @camera.setter
    def camera(self, target: str | Camera | None) -> None:
        """Set the _camera reference by target ID or Camera instance."""
        target_id: str | None = target.id if isinstance(target, Camera) else target  # type: ignore[assignment]
        member = self.get_member("_camera")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_camera",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Camera'),
            )

    @property
    def render_texture(self) -> str | None:
        """Target ID of the _renderTexture reference (targets RenderTextureProvider)."""
        member = self.get_member("_renderTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @render_texture.setter
    def render_texture(self, target: str | RenderTextureProvider | None) -> None:
        """Set the _renderTexture reference by target ID or RenderTextureProvider instance."""
        target_id: str | None = target.id if isinstance(target, RenderTextureProvider) else target  # type: ignore[assignment]
        member = self.get_member("_renderTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_renderTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RenderTextureProvider'),
            )

    @property
    def top_container(self) -> str | None:
        """Target ID of the _topContainer reference (targets Slot)."""
        member = self.get_member("_topContainer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @top_container.setter
    def top_container(self, target: str | Slot | None) -> None:
        """Set the _topContainer reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_topContainer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_topContainer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def top_mesh(self) -> str | None:
        """Target ID of the _topMesh reference (targets CurvedPlaneMesh)."""
        member = self.get_member("_topMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @top_mesh.setter
    def top_mesh(self, target: str | CurvedPlaneMesh | None) -> None:
        """Set the _topMesh reference by target ID or CurvedPlaneMesh instance."""
        target_id: str | None = target.id if isinstance(target, CurvedPlaneMesh) else target  # type: ignore[assignment]
        member = self.get_member("_topMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_topMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CurvedPlaneMesh'),
            )

    @property
    def screen_mesh(self) -> str | None:
        """Target ID of the _screenMesh reference (targets CurvedPlaneMesh)."""
        member = self.get_member("_screenMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @screen_mesh.setter
    def screen_mesh(self, target: str | CurvedPlaneMesh | None) -> None:
        """Set the _screenMesh reference by target ID or CurvedPlaneMesh instance."""
        target_id: str | None = target.id if isinstance(target, CurvedPlaneMesh) else target  # type: ignore[assignment]
        member = self.get_member("_screenMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_screenMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CurvedPlaneMesh'),
            )

    @property
    def buttons_mesh(self) -> str | None:
        """Target ID of the _buttonsMesh reference (targets CurvedPlaneMesh)."""
        member = self.get_member("_buttonsMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @buttons_mesh.setter
    def buttons_mesh(self, target: str | CurvedPlaneMesh | None) -> None:
        """Set the _buttonsMesh reference by target ID or CurvedPlaneMesh instance."""
        target_id: str | None = target.id if isinstance(target, CurvedPlaneMesh) else target  # type: ignore[assignment]
        member = self.get_member("_buttonsMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_buttonsMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CurvedPlaneMesh'),
            )

    @property
    def top_material(self) -> str | None:
        """Target ID of the _topMaterial reference (targets UnlitMaterial)."""
        member = self.get_member("_topMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @top_material.setter
    def top_material(self, target: str | UnlitMaterial | None) -> None:
        """Set the _topMaterial reference by target ID or UnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_topMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_topMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UnlitMaterial'),
            )

    @property
    def screen_material(self) -> str | None:
        """Target ID of the _screenMaterial reference (targets UnlitMaterial)."""
        member = self.get_member("_screenMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @screen_material.setter
    def screen_material(self, target: str | UnlitMaterial | None) -> None:
        """Set the _screenMaterial reference by target ID or UnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_screenMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_screenMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UnlitMaterial'),
            )

    @property
    def buttons_material(self) -> str | None:
        """Target ID of the _buttonsMaterial reference (targets UnlitMaterial)."""
        member = self.get_member("_buttonsMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @buttons_material.setter
    def buttons_material(self, target: str | UnlitMaterial | None) -> None:
        """Set the _buttonsMaterial reference by target ID or UnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_buttonsMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_buttonsMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UnlitMaterial'),
            )

    @property
    def overlay_effect_material(self) -> str | None:
        """Target ID of the _overlayEffectMaterial reference (targets UI_UnlitMaterial)."""
        member = self.get_member("_overlayEffectMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @overlay_effect_material.setter
    def overlay_effect_material(self, target: str | UI_UnlitMaterial | None) -> None:
        """Set the _overlayEffectMaterial reference by target ID or UI_UnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UI_UnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_overlayEffectMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_overlayEffectMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UI_UnlitMaterial'),
            )

    @property
    def top_border_material(self) -> str | None:
        """Target ID of the _topBorderMaterial reference (targets UV_RectMaterial)."""
        member = self.get_member("_topBorderMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @top_border_material.setter
    def top_border_material(self, target: str | UV_RectMaterial | None) -> None:
        """Set the _topBorderMaterial reference by target ID or UV_RectMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UV_RectMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_topBorderMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_topBorderMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UV_RectMaterial'),
            )

    @property
    def screen_border_material(self) -> str | None:
        """Target ID of the _screenBorderMaterial reference (targets UV_RectMaterial)."""
        member = self.get_member("_screenBorderMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @screen_border_material.setter
    def screen_border_material(self, target: str | UV_RectMaterial | None) -> None:
        """Set the _screenBorderMaterial reference by target ID or UV_RectMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UV_RectMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_screenBorderMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_screenBorderMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UV_RectMaterial'),
            )

    @property
    def buttons_border_material(self) -> str | None:
        """Target ID of the _buttonsBorderMaterial reference (targets UV_RectMaterial)."""
        member = self.get_member("_buttonsBorderMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @buttons_border_material.setter
    def buttons_border_material(self, target: str | UV_RectMaterial | None) -> None:
        """Set the _buttonsBorderMaterial reference by target ID or UV_RectMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UV_RectMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_buttonsBorderMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_buttonsBorderMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UV_RectMaterial'),
            )

    @property
    def render_root(self) -> str | None:
        """Target ID of the _renderRoot reference (targets Slot)."""
        member = self.get_member("_renderRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @render_root.setter
    def render_root(self, target: str | Slot | None) -> None:
        """Set the _renderRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_renderRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_renderRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def top_root(self) -> str | None:
        """Target ID of the _topRoot reference (targets Slot)."""
        member = self.get_member("_topRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @top_root.setter
    def top_root(self, target: str | Slot | None) -> None:
        """Set the _topRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_topRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_topRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def screen_root(self) -> str | None:
        """Target ID of the _screenRoot reference (targets Slot)."""
        member = self.get_member("_screenRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @screen_root.setter
    def screen_root(self, target: str | Slot | None) -> None:
        """Set the _screenRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_screenRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_screenRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def buttons_root(self) -> str | None:
        """Target ID of the _buttonsRoot reference (targets Slot)."""
        member = self.get_member("_buttonsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @buttons_root.setter
    def buttons_root(self, target: str | Slot | None) -> None:
        """Set the _buttonsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_buttonsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_buttonsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def visuals_root(self) -> str | None:
        """Target ID of the _visualsRoot reference (targets Slot)."""
        member = self.get_member("_visualsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visuals_root.setter
    def visuals_root(self, target: str | Slot | None) -> None:
        """Set the _visualsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_visualsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visualsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def effect_root(self) -> str | None:
        """Target ID of the _effectRoot reference (targets Slot)."""
        member = self.get_member("_effectRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @effect_root.setter
    def effect_root(self, target: str | Slot | None) -> None:
        """Set the _effectRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_effectRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_effectRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def top_canvas(self) -> str | None:
        """Target ID of the _topCanvas reference (targets Canvas)."""
        member = self.get_member("_topCanvas")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @top_canvas.setter
    def top_canvas(self, target: str | Canvas | None) -> None:
        """Set the _topCanvas reference by target ID or Canvas instance."""
        target_id: str | None = target.id if isinstance(target, Canvas) else target  # type: ignore[assignment]
        member = self.get_member("_topCanvas")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_topCanvas",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Canvas'),
            )

    @property
    def buttons_uiroot(self) -> str | None:
        """Target ID of the _buttonsUIroot reference (targets Slot)."""
        member = self.get_member("_buttonsUIroot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @buttons_uiroot.setter
    def buttons_uiroot(self, target: str | Slot | None) -> None:
        """Set the _buttonsUIroot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_buttonsUIroot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_buttonsUIroot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def buttons_canvas(self) -> str | None:
        """Target ID of the _buttonsCanvas reference (targets Canvas)."""
        member = self.get_member("_buttonsCanvas")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @buttons_canvas.setter
    def buttons_canvas(self, target: str | Canvas | None) -> None:
        """Set the _buttonsCanvas reference by target ID or Canvas instance."""
        target_id: str | None = target.id if isinstance(target, Canvas) else target  # type: ignore[assignment]
        member = self.get_member("_buttonsCanvas")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_buttonsCanvas",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Canvas'),
            )

    @property
    def style(self) -> str | None:
        """Target ID of the _style reference (targets ParticleStyle)."""
        member = self.get_member("_style")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @style.setter
    def style(self, target: str | ParticleStyle | None) -> None:
        """Set the _style reference by target ID or ParticleStyle instance."""
        target_id: str | None = target.id if isinstance(target, ParticleStyle) else target  # type: ignore[assignment]
        member = self.get_member("_style")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_style",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PhotonDust.ParticleStyle'),
            )

    @property
    def particle_colors(self) -> str | None:
        """Target ID of the _particleColors reference (targets ColorRangeInitializer)."""
        member = self.get_member("_particleColors")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @particle_colors.setter
    def particle_colors(self, target: str | ColorRangeInitializer | None) -> None:
        """Set the _particleColors reference by target ID or ColorRangeInitializer instance."""
        target_id: str | None = target.id if isinstance(target, ColorRangeInitializer) else target  # type: ignore[assignment]
        member = self.get_member("_particleColors")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_particleColors",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PhotonDust.ColorRangeInitializer'),
            )

    @property
    def emitter(self) -> str | None:
        """Target ID of the _emitter reference (targets MeshEmitter)."""
        member = self.get_member("_emitter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @emitter.setter
    def emitter(self, target: str | MeshEmitter | None) -> None:
        """Set the _emitter reference by target ID or MeshEmitter instance."""
        target_id: str | None = target.id if isinstance(target, MeshEmitter) else target  # type: ignore[assignment]
        member = self.get_member("_emitter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_emitter",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PhotonDust.MeshEmitter'),
            )

    @property
    def top_collider(self) -> str | None:
        """Target ID of the _topCollider reference (targets MeshCollider)."""
        member = self.get_member("_topCollider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @top_collider.setter
    def top_collider(self, target: str | MeshCollider | None) -> None:
        """Set the _topCollider reference by target ID or MeshCollider instance."""
        target_id: str | None = target.id if isinstance(target, MeshCollider) else target  # type: ignore[assignment]
        member = self.get_member("_topCollider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_topCollider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MeshCollider'),
            )

    @property
    def screen_collider(self) -> str | None:
        """Target ID of the _screenCollider reference (targets MeshCollider)."""
        member = self.get_member("_screenCollider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @screen_collider.setter
    def screen_collider(self, target: str | MeshCollider | None) -> None:
        """Set the _screenCollider reference by target ID or MeshCollider instance."""
        target_id: str | None = target.id if isinstance(target, MeshCollider) else target  # type: ignore[assignment]
        member = self.get_member("_screenCollider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_screenCollider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MeshCollider'),
            )

    @property
    def buttons_collider(self) -> str | None:
        """Target ID of the _buttonsCollider reference (targets MeshCollider)."""
        member = self.get_member("_buttonsCollider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @buttons_collider.setter
    def buttons_collider(self, target: str | MeshCollider | None) -> None:
        """Set the _buttonsCollider reference by target ID or MeshCollider instance."""
        target_id: str | None = target.id if isinstance(target, MeshCollider) else target  # type: ignore[assignment]
        member = self.get_member("_buttonsCollider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_buttonsCollider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MeshCollider'),
            )

