"""Generated component: GetAsset."""

from typing import Any

A = Any
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GetAsset(GenericComponent[T], INodeObjectOutput[T], IExecutionNode[T], INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<>.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Assets

    Parameterize with a value type::

        GetAsset[primitives.Float]
        GetAsset[primitives.Float3]
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<>"
    _GENERIC_TYPE_TEMPLATE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.GetAsset<>"

    def __init__(self, provider: str | INodeObjectOutput[IAssetProvider[A]] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            provider: Initial value for Provider.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if provider is not None:
            self.provider = provider

    @property
    def provider(self) -> str | None:
        """Target ID of the Provider reference (targets INodeObjectOutput[IAssetProvider[A]])."""
        member = self.get_member("Provider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @provider.setter
    def provider(self, target: str | INodeObjectOutput[IAssetProvider[A]] | None) -> None:
        """Set the Provider reference by target ID or INodeObjectOutput[IAssetProvider[A]] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Provider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Provider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.IAssetProvider<A>>'),
            )

