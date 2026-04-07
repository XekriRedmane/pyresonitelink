"""Generated component: BakeReflectionProbe."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.reflection_probe import ReflectionProbe
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BakeReflectionProbe(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.BakeReflectionProbe.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Rendering
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.BakeReflectionProbe"

    def __init__(self, probe: str | INodeObjectOutput[ReflectionProbe] | None = None, on_bake_start: str | INodeOperation | None = None, on_bake_fail: str | INodeOperation | None = None, on_bake_complete: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            probe: Initial value for Probe.
            on_bake_start: Initial value for OnBakeStart.
            on_bake_fail: Initial value for OnBakeFail.
            on_bake_complete: Initial value for OnBakeComplete.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if probe is not None:
            self.probe = probe
        if on_bake_start is not None:
            self.on_bake_start = on_bake_start
        if on_bake_fail is not None:
            self.on_bake_fail = on_bake_fail
        if on_bake_complete is not None:
            self.on_bake_complete = on_bake_complete

    @property
    def probe(self) -> str | None:
        """Target ID of the Probe reference (targets INodeObjectOutput[ReflectionProbe])."""
        member = self.get_member("Probe")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @probe.setter
    def probe(self, target: str | INodeObjectOutput[ReflectionProbe] | None) -> None:
        """Set the Probe reference by target ID or INodeObjectOutput[ReflectionProbe] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Probe")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Probe",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.ReflectionProbe>'),
            )

    @property
    def on_bake_start(self) -> str | None:
        """Target ID of the OnBakeStart reference (targets INodeOperation)."""
        member = self.get_member("OnBakeStart")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_bake_start.setter
    def on_bake_start(self, target: str | INodeOperation | None) -> None:
        """Set the OnBakeStart reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnBakeStart")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnBakeStart",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_bake_fail(self) -> str | None:
        """Target ID of the OnBakeFail reference (targets INodeOperation)."""
        member = self.get_member("OnBakeFail")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_bake_fail.setter
    def on_bake_fail(self, target: str | INodeOperation | None) -> None:
        """Set the OnBakeFail reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnBakeFail")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnBakeFail",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_bake_complete(self) -> str | None:
        """Target ID of the OnBakeComplete reference (targets INodeOperation)."""
        member = self.get_member("OnBakeComplete")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_bake_complete.setter
    def on_bake_complete(self, target: str | INodeOperation | None) -> None:
        """Set the OnBakeComplete reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnBakeComplete")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnBakeComplete",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def baked_cubemap_url(self) -> members.EmptyElement | None:
        """The BakedCubemapURL member."""
        member = self.get_member("BakedCubemapURL")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @baked_cubemap_url.setter
    def baked_cubemap_url(self, value: members.EmptyElement) -> None:
        """Set the BakedCubemapURL member."""
        self.set_member("BakedCubemapURL", value)

