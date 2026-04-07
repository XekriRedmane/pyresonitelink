"""Generated component: OrientationOnUVSphere."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OrientationOnUVSphere(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.OrientationOnUVSphere.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Math/Geometry 3D
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.Math.Geometry3D.OrientationOnUVSphere"

    def __init__(self, uv: str | INodeValueOutput[primitives.Float2] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            uv: Initial value for UV.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if uv is not None:
            self.uv = uv

    @property
    def uv(self) -> str | None:
        """Target ID of the UV reference (targets INodeValueOutput[primitives.Float2])."""
        member = self.get_member("UV")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @uv.setter
    def uv(self, target: str | INodeValueOutput[primitives.Float2] | None) -> None:
        """Set the UV reference by target ID or INodeValueOutput[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("UV")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "UV",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float2>'),
            )

