"""Generated component: AttachMesh."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AttachMesh(GeneratedComponent, ISyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The Attach Mesh node allows one to attach a provided Uri as a new StaticMesh component and return the StaticMesh raw IAsset`1 itself.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Assets
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Assets.AttachMesh"

    def __init__(self, next: str | INodeOperation | None = None, url: str | INodeObjectOutput[str] | None = None, target: str | INodeObjectOutput[Slot] | None = None, get_existing: str | INodeValueOutput[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            next: Initial value for Next.
            url: Initial value for URL.
            target: Initial value for Target.
            get_existing: Initial value for GetExisting.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if next is not None:
            self.next = next
        if url is not None:
            self.url = url
        if target is not None:
            self.target = target
        if get_existing is not None:
            self.get_existing = get_existing

    @property
    def next(self) -> str | None:
        """Fires after * (Call) is called and the asset was successfully attached."""
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @next.setter
    def next(self, target: str | INodeOperation | None) -> None:
        """Set the Next reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Next")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Next",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def url(self) -> str | None:
        """The URI of the asset you want to attach. Can be a resdb or a local or a website hosted asset."""
        member = self.get_member("URL")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @url.setter
    def url(self, target: str | INodeObjectOutput[str] | None) -> None:
        """Set the URL reference by target ID or INodeObjectOutput[str] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("URL")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "URL",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<Uri>'),
            )

    @property
    def target(self) -> str | None:
        """The slot to attach the asset to."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | INodeObjectOutput[Slot] | None) -> None:
        """Set the Target reference by target ID or INodeObjectOutput[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def get_existing(self) -> str | None:
        """Get an existing asset on Target (Slot) of the same URL (uri) or attach a new one."""
        member = self.get_member("GetExisting")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @get_existing.setter
    def get_existing(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the GetExisting reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("GetExisting")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "GetExisting",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def attached_provider(self) -> members.EmptyElement | None:
        """The attached provider or an existing one on Target (Slot) if GetExisting (bool) is true."""
        member = self.get_member("AttachedProvider")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @attached_provider.setter
    def attached_provider(self, value: members.EmptyElement) -> None:
        """Set AttachedProvider. The attached provider or an existing one on Target (Slot) if GetExisting (bool) is true."""
        self.set_member("AttachedProvider", value)

