"""Generated component: RenderToTextureAsset."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.camera import Camera
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RenderToTextureAsset(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.RenderToTextureAsset.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Rendering
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.RenderToTextureAsset"

    def __init__(self, camera: str | INodeObjectOutput[Camera] | None = None, resolution: str | INodeValueOutput[primitives.Int2] | None = None, format_: str | INodeObjectOutput[str] | None = None, quality: str | INodeValueOutput[np.int32] | None = None, on_render_started: str | INodeOperation | None = None, on_rendered: str | INodeOperation | None = None, on_failed: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            camera: Initial value for Camera.
            resolution: Initial value for Resolution.
            format_: Initial value for Format.
            quality: Initial value for Quality.
            on_render_started: Initial value for OnRenderStarted.
            on_rendered: Initial value for OnRendered.
            on_failed: Initial value for OnFailed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if camera is not None:
            self.camera = camera
        if resolution is not None:
            self.resolution = resolution
        if format_ is not None:
            self.format_ = format_
        if quality is not None:
            self.quality = quality
        if on_render_started is not None:
            self.on_render_started = on_render_started
        if on_rendered is not None:
            self.on_rendered = on_rendered
        if on_failed is not None:
            self.on_failed = on_failed

    @property
    def camera(self) -> str | None:
        """Target ID of the Camera reference (targets INodeObjectOutput[Camera])."""
        member = self.get_member("Camera")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @camera.setter
    def camera(self, target: str | INodeObjectOutput[Camera] | None) -> None:
        """Set the Camera reference by target ID or INodeObjectOutput[Camera] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Camera")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Camera",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Camera>'),
            )

    @property
    def resolution(self) -> str | None:
        """Target ID of the Resolution reference (targets INodeValueOutput[primitives.Int2])."""
        member = self.get_member("Resolution")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @resolution.setter
    def resolution(self, target: str | INodeValueOutput[primitives.Int2] | None) -> None:
        """Set the Resolution reference by target ID or INodeValueOutput[primitives.Int2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Resolution")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Resolution",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int2>'),
            )

    @property
    def format_(self) -> str | None:
        """Target ID of the Format reference (targets INodeObjectOutput[str])."""
        member = self.get_member("Format")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @format_.setter
    def format_(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the Format reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Format")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Format",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def quality(self) -> str | None:
        """Target ID of the Quality reference (targets INodeValueOutput[np.int32])."""
        member = self.get_member("Quality")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @quality.setter
    def quality(self, target: str | INodeValueOutput[np.int32] | None) -> None:
        """Set the Quality reference by target ID or INodeValueOutput[np.int32] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Quality")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Quality",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<int>'),
            )

    @property
    def on_render_started(self) -> str | None:
        """Target ID of the OnRenderStarted reference (targets INodeOperation)."""
        member = self.get_member("OnRenderStarted")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_render_started.setter
    def on_render_started(self, target: str | INodeOperation | None) -> None:
        """Set the OnRenderStarted reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnRenderStarted")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnRenderStarted",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_rendered(self) -> str | None:
        """Target ID of the OnRendered reference (targets INodeOperation)."""
        member = self.get_member("OnRendered")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_rendered.setter
    def on_rendered(self, target: str | INodeOperation | None) -> None:
        """Set the OnRendered reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnRendered")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnRendered",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_failed(self) -> str | None:
        """Target ID of the OnFailed reference (targets INodeOperation)."""
        member = self.get_member("OnFailed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_failed.setter
    def on_failed(self, target: str | INodeOperation | None) -> None:
        """Set the OnFailed reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnFailed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnFailed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def rendered_asset_url(self) -> members.EmptyElement | None:
        """The RenderedAssetURL member."""
        member = self.get_member("RenderedAssetURL")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @rendered_asset_url.setter
    def rendered_asset_url(self, value: members.EmptyElement) -> None:
        """Set the RenderedAssetURL member."""
        self.set_member("RenderedAssetURL", value)

