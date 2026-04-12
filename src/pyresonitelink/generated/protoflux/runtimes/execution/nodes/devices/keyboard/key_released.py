"""Generated component: KeyReleased."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.key import Key
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class KeyReleased(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Key Released`` node returns the local user's keyboard key being released. This will change within that frame, so combining it with Fire On True is recommended.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Devices/Keyboard
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Input.Keyboard.KeyReleased"

    def __init__(self, key: str | INodeValueOutput[Key] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            key: Initial value for Key.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if key is not None:
            self.key = key

    @property
    def key(self) -> str | None:
        """The key to check."""
        member = self.get_member("Key")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @key.setter
    def key(self, target: str | INodeValueOutput[Key] | None) -> None:
        """Set the Key reference by target ID or INodeValueOutput[Key] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Key")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Key",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[Renderite.Shared]Renderite.Shared.Key>'),
            )

