"""Generated component: Camera."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.render_texture import RenderTexture
from pyresonitelink.generated._types.iuvto_ray_converter import IUVToRayConverter
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Camera(GeneratedComponent, IUVToRayConverter, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Camera.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Camera"

    def __init__(self, render_texture: str | IAssetProvider[RenderTexture] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            render_texture: Initial value for RenderTexture.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if render_texture is not None:
            self.render_texture = render_texture

    @property
    def double_buffered(self) -> bool | None:
        """The DoubleBuffered field value."""
        member = self.get_member("DoubleBuffered")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @double_buffered.setter
    def double_buffered(self, value: bool) -> None:
        """Set the DoubleBuffered field value."""
        member = self.get_member("DoubleBuffered")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DoubleBuffered", fields.FieldBool(value=value)
            )

    @property
    def forward_only(self) -> bool | None:
        """The ForwardOnly field value."""
        member = self.get_member("ForwardOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @forward_only.setter
    def forward_only(self, value: bool) -> None:
        """Set the ForwardOnly field value."""
        member = self.get_member("ForwardOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForwardOnly", fields.FieldBool(value=value)
            )

    @property
    def projection(self) -> members.FieldEnum | None:
        """The Projection member."""
        member = self.get_member("Projection")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @projection.setter
    def projection(self, value: members.FieldEnum) -> None:
        """Set the Projection member."""
        self.set_member("Projection", value)

    @property
    def orthographic_size(self) -> np.float32 | None:
        """The OrthographicSize field value."""
        member = self.get_member("OrthographicSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @orthographic_size.setter
    def orthographic_size(self, value: np.float32) -> None:
        """Set the OrthographicSize field value."""
        member = self.get_member("OrthographicSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OrthographicSize", fields.FieldFloat(value=value)
            )

    @property
    def field_of_view(self) -> np.float32 | None:
        """The FieldOfView field value."""
        member = self.get_member("FieldOfView")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @field_of_view.setter
    def field_of_view(self, value: np.float32) -> None:
        """Set the FieldOfView field value."""
        member = self.get_member("FieldOfView")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FieldOfView", fields.FieldFloat(value=value)
            )

    @property
    def near_clipping(self) -> np.float32 | None:
        """The NearClipping field value."""
        member = self.get_member("NearClipping")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @near_clipping.setter
    def near_clipping(self, value: np.float32) -> None:
        """Set the NearClipping field value."""
        member = self.get_member("NearClipping")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NearClipping", fields.FieldFloat(value=value)
            )

    @property
    def far_clipping(self) -> np.float32 | None:
        """The FarClipping field value."""
        member = self.get_member("FarClipping")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @far_clipping.setter
    def far_clipping(self, value: np.float32) -> None:
        """Set the FarClipping field value."""
        member = self.get_member("FarClipping")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FarClipping", fields.FieldFloat(value=value)
            )

    @property
    def use_transform_scale(self) -> bool | None:
        """The UseTransformScale field value."""
        member = self.get_member("UseTransformScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_transform_scale.setter
    def use_transform_scale(self, value: bool) -> None:
        """Set the UseTransformScale field value."""
        member = self.get_member("UseTransformScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseTransformScale", fields.FieldBool(value=value)
            )

    @property
    def clear(self) -> members.FieldEnum | None:
        """The Clear member."""
        member = self.get_member("Clear")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @clear.setter
    def clear(self, value: members.FieldEnum) -> None:
        """Set the Clear member."""
        self.set_member("Clear", value)

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
    def viewport(self) -> primitives.Rect | None:
        """The Viewport field value."""
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
    def depth(self) -> np.float32 | None:
        """The Depth field value."""
        member = self.get_member("Depth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @depth.setter
    def depth(self, value: np.float32) -> None:
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
        """Target ID of the RenderTexture reference (targets IAssetProvider[RenderTexture])."""
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
    def postprocessing(self) -> bool | None:
        """The Postprocessing field value."""
        member = self.get_member("Postprocessing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @postprocessing.setter
    def postprocessing(self, value: bool) -> None:
        """Set the Postprocessing field value."""
        member = self.get_member("Postprocessing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Postprocessing", fields.FieldBool(value=value)
            )

    @property
    def screen_space_reflections(self) -> bool | None:
        """The ScreenSpaceReflections field value."""
        member = self.get_member("ScreenSpaceReflections")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @screen_space_reflections.setter
    def screen_space_reflections(self, value: bool) -> None:
        """Set the ScreenSpaceReflections field value."""
        member = self.get_member("ScreenSpaceReflections")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScreenSpaceReflections", fields.FieldBool(value=value)
            )

    @property
    def motion_blur(self) -> bool | None:
        """The MotionBlur field value."""
        member = self.get_member("MotionBlur")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @motion_blur.setter
    def motion_blur(self, value: bool) -> None:
        """Set the MotionBlur field value."""
        member = self.get_member("MotionBlur")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MotionBlur", fields.FieldBool(value=value)
            )

    @property
    def render_shadows(self) -> bool | None:
        """The RenderShadows field value."""
        member = self.get_member("RenderShadows")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_shadows.setter
    def render_shadows(self, value: bool) -> None:
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
        """The SelectiveRender member."""
        member = self.get_member("SelectiveRender")
        if isinstance(member, members.SyncList):
            return member
        return None

    @selective_render.setter
    def selective_render(self, value: members.SyncList) -> None:
        """Set the SelectiveRender member."""
        self.set_member("SelectiveRender", value)

    @property
    def exclude_render(self) -> members.SyncList | None:
        """The ExcludeRender member."""
        member = self.get_member("ExcludeRender")
        if isinstance(member, members.SyncList):
            return member
        return None

    @exclude_render.setter
    def exclude_render(self, value: members.SyncList) -> None:
        """Set the ExcludeRender member."""
        self.set_member("ExcludeRender", value)

