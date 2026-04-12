"""Generated component: Camera."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.camera_projection import CameraProjection
from pyresonitelink.generated._enums.camera_clear_mode import CameraClearMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.render_texture import RenderTexture
from pyresonitelink.generated._types.iuvto_ray_converter import IUVToRayConverter
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Camera(GeneratedComponent, IUVToRayConverter, ICustomInspector, IWorldEventReceiver):
    """The Camera component represents a Unity Camera which is centered on the slot and facing in the forward direction.

    Category: Rendering

    Put the component onto a slot, and position the slot. The produced image
    can either be accessed through a RenderTextureProvider component or by
    creating a Texture2D asset using the Render To Texture Asset Protoflux
    node.

    **See also**: * CameraPortal, which is often used as a mirror.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Camera"

    def __init__(self, double_buffered: primitives.Bool | None = None, forward_only: primitives.Bool | None = None, projection: CameraProjection | str | None = None, orthographic_size: primitives.Float | None = None, field_of_view: primitives.Float | None = None, near_clipping: primitives.Float | None = None, far_clipping: primitives.Float | None = None, use_transform_scale: primitives.Bool | None = None, clear: CameraClearMode | str | None = None, clear_color: primitives.ColorX | None = None, viewport: primitives.Rect | None = None, depth: primitives.Float | None = None, render_texture: str | IAssetProvider[RenderTexture] | None = None, postprocessing: primitives.Bool | None = None, screen_space_reflections: primitives.Bool | None = None, motion_blur: primitives.Bool | None = None, render_shadows: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            double_buffered: Initial value for DoubleBuffered.
            forward_only: Initial value for ForwardOnly.
            projection: Initial value for Projection.
            orthographic_size: Initial value for OrthographicSize.
            field_of_view: Initial value for FieldOfView.
            near_clipping: Initial value for NearClipping.
            far_clipping: Initial value for FarClipping.
            use_transform_scale: Initial value for UseTransformScale.
            clear: Initial value for Clear.
            clear_color: Initial value for ClearColor.
            viewport: Initial value for Viewport.
            depth: Initial value for Depth.
            render_texture: Initial value for RenderTexture.
            postprocessing: Initial value for Postprocessing.
            screen_space_reflections: Initial value for ScreenSpaceReflections.
            motion_blur: Initial value for MotionBlur.
            render_shadows: Initial value for RenderShadows.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if double_buffered is not None:
            self.double_buffered = double_buffered
        if forward_only is not None:
            self.forward_only = forward_only
        if projection is not None:
            self.projection = projection
        if orthographic_size is not None:
            self.orthographic_size = orthographic_size
        if field_of_view is not None:
            self.field_of_view = field_of_view
        if near_clipping is not None:
            self.near_clipping = near_clipping
        if far_clipping is not None:
            self.far_clipping = far_clipping
        if use_transform_scale is not None:
            self.use_transform_scale = use_transform_scale
        if clear is not None:
            self.clear = clear
        if clear_color is not None:
            self.clear_color = clear_color
        if viewport is not None:
            self.viewport = viewport
        if depth is not None:
            self.depth = depth
        if render_texture is not None:
            self.render_texture = render_texture
        if postprocessing is not None:
            self.postprocessing = postprocessing
        if screen_space_reflections is not None:
            self.screen_space_reflections = screen_space_reflections
        if motion_blur is not None:
            self.motion_blur = motion_blur
        if render_shadows is not None:
            self.render_shadows = render_shadows

    @property
    def double_buffered(self) -> primitives.Bool | None:
        """Determines if DoubleBuffering is applied or not."""
        member = self.get_member("DoubleBuffered")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @double_buffered.setter
    def double_buffered(self, value: primitives.Bool) -> None:
        """Set the DoubleBuffered field value."""
        member = self.get_member("DoubleBuffered")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DoubleBuffered", fields.FieldBool(value=value)
            )

    @property
    def forward_only(self) -> primitives.Bool | None:
        """Determine whether the render technique is only forward. This can badly effect performance."""
        member = self.get_member("ForwardOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @forward_only.setter
    def forward_only(self, value: primitives.Bool) -> None:
        """Set the ForwardOnly field value."""
        member = self.get_member("ForwardOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForwardOnly", fields.FieldBool(value=value)
            )

    @property
    def projection(self) -> CameraProjection | None:
        """Determines whether it's perspective or orthographic"""
        member = self.get_member("Projection")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CameraProjection(member.value)
        return None

    @projection.setter
    def projection(self, value: CameraProjection | str) -> None:
        """Set Projection. Determines whether it's perspective or orthographic"""
        member = self.get_member("Projection")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Projection",
                members.FieldEnum(value=str(value)),
            )

    @property
    def orthographic_size(self) -> primitives.Float | None:
        """The size of the render-output in orthographic view. (Only active when ``Projection`` is set to ``Orthographic``"""
        member = self.get_member("OrthographicSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @orthographic_size.setter
    def orthographic_size(self, value: primitives.Float) -> None:
        """Set the OrthographicSize field value."""
        member = self.get_member("OrthographicSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OrthographicSize", fields.FieldFloat(value=value)
            )

    @property
    def field_of_view(self) -> primitives.Float | None:
        """The vertical field of view of the camera. (Only active when ``Projection`` is set to ``Perspective``"""
        member = self.get_member("FieldOfView")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @field_of_view.setter
    def field_of_view(self, value: primitives.Float) -> None:
        """Set the FieldOfView field value."""
        member = self.get_member("FieldOfView")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FieldOfView", fields.FieldFloat(value=value)
            )

    @property
    def near_clipping(self) -> primitives.Float | None:
        """The point in meters where the camera ignores near objects."""
        member = self.get_member("NearClipping")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_clipping.setter
    def near_clipping(self, value: primitives.Float) -> None:
        """Set the NearClipping field value."""
        member = self.get_member("NearClipping")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearClipping", fields.FieldFloat(value=value)
            )

    @property
    def far_clipping(self) -> primitives.Float | None:
        """The point in meters where the camera ignores far objects."""
        member = self.get_member("FarClipping")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_clipping.setter
    def far_clipping(self, value: primitives.Float) -> None:
        """Set the FarClipping field value."""
        member = self.get_member("FarClipping")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarClipping", fields.FieldFloat(value=value)
            )

    @property
    def use_transform_scale(self) -> primitives.Bool | None:
        """Determines if the scale of the camera should be taken into account."""
        member = self.get_member("UseTransformScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_transform_scale.setter
    def use_transform_scale(self, value: primitives.Bool) -> None:
        """Set the UseTransformScale field value."""
        member = self.get_member("UseTransformScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseTransformScale", fields.FieldBool(value=value)
            )

    @property
    def clear(self) -> CameraClearMode | None:
        """See Camera Clear Mode for what this does."""
        member = self.get_member("Clear")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return CameraClearMode(member.value)
        return None

    @clear.setter
    def clear(self, value: CameraClearMode | str) -> None:
        """Set Clear. See Camera Clear Mode for what this does."""
        member = self.get_member("Clear")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Clear",
                members.FieldEnum(value=str(value)),
            )

    @property
    def clear_color(self) -> primitives.ColorX | None:
        """If ``CameraClearMode`` is set to ``Color``."""
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
    def viewport(self) -> primitives.Rect | None:
        """2D rectangular where the camera is allowed to render"""
        member = self.get_member("Viewport")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @viewport.setter
    def viewport(self, value: primitives.Rect) -> None:
        """Set the Viewport field value."""
        member = self.get_member("Viewport")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Viewport", fields.FieldRect(value=value)
            )

    @property
    def depth(self) -> primitives.Float | None:
        """Whether this camera should be rendered before or after other cameras render."""
        member = self.get_member("Depth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @depth.setter
    def depth(self, value: primitives.Float) -> None:
        """Set the Depth field value."""
        member = self.get_member("Depth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Depth", fields.FieldFloat(value=value)
            )

    @property
    def render_texture(self) -> str | None:
        """The RenderTextureProvider input in order to get a ITexture2D"""
        member = self.get_member("RenderTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @render_texture.setter
    def render_texture(self, target: str | IAssetProvider[RenderTexture] | None) -> None:
        """Set the RenderTexture reference by target ID or IAssetProvider[RenderTexture] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("RenderTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RenderTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.RenderTexture>'),
            )

    @property
    def postprocessing(self) -> primitives.Bool | None:
        """Determines if post processing is allowed."""
        member = self.get_member("Postprocessing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @postprocessing.setter
    def postprocessing(self, value: primitives.Bool) -> None:
        """Set the Postprocessing field value."""
        member = self.get_member("Postprocessing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Postprocessing", fields.FieldBool(value=value)
            )

    @property
    def screen_space_reflections(self) -> primitives.Bool | None:
        """Determines if ScreenSpaceReflections are rendered."""
        member = self.get_member("ScreenSpaceReflections")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @screen_space_reflections.setter
    def screen_space_reflections(self, value: primitives.Bool) -> None:
        """Set the ScreenSpaceReflections field value."""
        member = self.get_member("ScreenSpaceReflections")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScreenSpaceReflections", fields.FieldBool(value=value)
            )

    @property
    def motion_blur(self) -> primitives.Bool | None:
        """Determines if MotionBlur is rendered or not."""
        member = self.get_member("MotionBlur")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @motion_blur.setter
    def motion_blur(self, value: primitives.Bool) -> None:
        """Set the MotionBlur field value."""
        member = self.get_member("MotionBlur")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MotionBlur", fields.FieldBool(value=value)
            )

    @property
    def render_shadows(self) -> primitives.Bool | None:
        """Determines if shadows are rendered or not."""
        member = self.get_member("RenderShadows")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_shadows.setter
    def render_shadows(self, value: primitives.Bool) -> None:
        """Set the RenderShadows field value."""
        member = self.get_member("RenderShadows")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RenderShadows", fields.FieldBool(value=value)
            )

    @property
    def selective_render(self) -> members.SyncList | None:
        """A list of SyncReferences to slots the camera is allowed to render."""
        member = self.get_member("SelectiveRender")
        if isinstance(member, members.SyncList):
            return member
        return None

    @selective_render.setter
    def selective_render(self, value: members.SyncList) -> None:
        """Set SelectiveRender. A list of SyncReferences to slots the camera is allowed to render."""
        self.set_member("SelectiveRender", value)

    @property
    def exclude_render(self) -> members.SyncList | None:
        """A list of SyncReferences to slots the camera is NOT allowed to render."""
        member = self.get_member("ExcludeRender")
        if isinstance(member, members.SyncList):
            return member
        return None

    @exclude_render.setter
    def exclude_render(self, value: members.SyncList) -> None:
        """Set ExcludeRender. A list of SyncReferences to slots the camera is NOT allowed to render."""
        self.set_member("ExcludeRender", value)

