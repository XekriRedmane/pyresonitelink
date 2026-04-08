"""Generated component: BakeReflectionProbes."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BakeReflectionProbes(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Bake Reflection Probes node takes in the root slot holding all your reflection probes, whether or not to bake the inactive reflection probes, the matching tag to bake only those reflection probes, and a delay before starting the baking process. This node will then attempt to bake them all, then returns the focused reflection probe, the index of that reflection probe, and the count of all reflection probes.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Rendering
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Rendering.BakeReflectionProbes"

    def __init__(self, root: str | INodeObjectOutput[Slot] | None = None, bake_inactive: str | INodeValueOutput[primitives.Bool] | None = None, filter_with_tag: str | INodeObjectOutput[primitives.String] | None = None, delay_before_bake: str | INodeValueOutput[primitives.Float] | None = None, on_bake_batch_start: str | INodeOperation | None = None, on_before_probe_bake: str | INodeOperation | None = None, on_probe_baked: str | INodeOperation | None = None, on_bake_batch_finished: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            root: Initial value for Root.
            bake_inactive: Initial value for BakeInactive.
            filter_with_tag: Initial value for FilterWithTag.
            delay_before_bake: Initial value for DelayBeforeBake.
            on_bake_batch_start: Initial value for OnBakeBatchStart.
            on_before_probe_bake: Initial value for OnBeforeProbeBake.
            on_probe_baked: Initial value for OnProbeBaked.
            on_bake_batch_finished: Initial value for OnBakeBatchFinished.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if root is not None:
            self.root = root
        if bake_inactive is not None:
            self.bake_inactive = bake_inactive
        if filter_with_tag is not None:
            self.filter_with_tag = filter_with_tag
        if delay_before_bake is not None:
            self.delay_before_bake = delay_before_bake
        if on_bake_batch_start is not None:
            self.on_bake_batch_start = on_bake_batch_start
        if on_before_probe_bake is not None:
            self.on_before_probe_bake = on_before_probe_bake
        if on_probe_baked is not None:
            self.on_probe_baked = on_probe_baked
        if on_bake_batch_finished is not None:
            self.on_bake_batch_finished = on_bake_batch_finished

    @property
    def root(self) -> str | None:
        """Target ID of the Root reference (targets INodeObjectOutput[Slot])."""
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root.setter
    def root(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Root reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Root",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def bake_inactive(self) -> str | None:
        """Target ID of the BakeInactive reference (targets INodeValueOutput[primitives.Bool])."""
        member = self.get_member("BakeInactive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bake_inactive.setter
    def bake_inactive(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the BakeInactive reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("BakeInactive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BakeInactive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def filter_with_tag(self) -> str | None:
        """Target ID of the FilterWithTag reference (targets INodeObjectOutput[primitives.String])."""
        member = self.get_member("FilterWithTag")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @filter_with_tag.setter
    def filter_with_tag(self, target: str | INodeObjectOutput[primitives.String] | None) -> None:
        """Set the FilterWithTag reference by target ID or INodeObjectOutput[primitives.String] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("FilterWithTag")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FilterWithTag",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<string>'),
            )

    @property
    def delay_before_bake(self) -> str | None:
        """Target ID of the DelayBeforeBake reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("DelayBeforeBake")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @delay_before_bake.setter
    def delay_before_bake(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the DelayBeforeBake reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("DelayBeforeBake")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DelayBeforeBake",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def probe(self) -> members.EmptyElement | None:
        """The Probe member."""
        member = self.get_member("Probe")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @probe.setter
    def probe(self, value: members.EmptyElement) -> None:
        """Set the Probe member."""
        self.set_member("Probe", value)

    @property
    def probe_index(self) -> members.EmptyElement | None:
        """The ProbeIndex member."""
        member = self.get_member("ProbeIndex")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @probe_index.setter
    def probe_index(self, value: members.EmptyElement) -> None:
        """Set the ProbeIndex member."""
        self.set_member("ProbeIndex", value)

    @property
    def probe_count(self) -> members.EmptyElement | None:
        """The ProbeCount member."""
        member = self.get_member("ProbeCount")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @probe_count.setter
    def probe_count(self, value: members.EmptyElement) -> None:
        """Set the ProbeCount member."""
        self.set_member("ProbeCount", value)

    @property
    def on_bake_batch_start(self) -> str | None:
        """Target ID of the OnBakeBatchStart reference (targets INodeOperation)."""
        member = self.get_member("OnBakeBatchStart")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_bake_batch_start.setter
    def on_bake_batch_start(self, target: str | INodeOperation | None) -> None:
        """Set the OnBakeBatchStart reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnBakeBatchStart")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnBakeBatchStart",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_before_probe_bake(self) -> str | None:
        """Target ID of the OnBeforeProbeBake reference (targets INodeOperation)."""
        member = self.get_member("OnBeforeProbeBake")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_before_probe_bake.setter
    def on_before_probe_bake(self, target: str | INodeOperation | None) -> None:
        """Set the OnBeforeProbeBake reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnBeforeProbeBake")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnBeforeProbeBake",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_probe_baked(self) -> str | None:
        """Target ID of the OnProbeBaked reference (targets INodeOperation)."""
        member = self.get_member("OnProbeBaked")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_probe_baked.setter
    def on_probe_baked(self, target: str | INodeOperation | None) -> None:
        """Set the OnProbeBaked reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnProbeBaked")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnProbeBaked",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_bake_batch_finished(self) -> str | None:
        """Target ID of the OnBakeBatchFinished reference (targets INodeOperation)."""
        member = self.get_member("OnBakeBatchFinished")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_bake_batch_finished.setter
    def on_bake_batch_finished(self, target: str | INodeOperation | None) -> None:
        """Set the OnBakeBatchFinished reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnBakeBatchFinished")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnBakeBatchFinished",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

