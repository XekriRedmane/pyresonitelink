"""Generated component: OpenWorld."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_object_output import INodeObjectOutput
from pyresonitelink.generated._types.iworld_link import IWorldLink
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.world_relation import WorldRelation
from pyresonitelink.generated._types.inode_operation import INodeOperation
from pyresonitelink.generated._types.iasync_node_operation import IAsyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class OpenWorld(GeneratedComponent, IAsyncNodeOperation, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Open World`` node is used to open a world when called, given a valid Url and a set of optional parameters the user can give it to open a world in a certain way. You can chain this node with the Focus World node by using this node's SessionURL connected to the focus world node.

You can easily make a custom loading indicator using this node just by turning off the loading indicator and utilizing the OnOpenStart Async Continuation, however there is no way to make a custom loading bar to have an "accurate" percentage, thus is a tradeoff.

This node is also useful when making Exit Strategies, as you can set it up to where if the world is valid to open and using the AutoFocus option, you can jump to the new focused world, and have the node continue from here to play a particle effect, a sound, and much more. Combining it further with the focus world node to close the old world is also an option.

    Category: ProtoFlux/Runtimes/Execution/Nodes/World
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Worlds.OpenWorld"

    def __init__(self, url: str | INodeObjectOutput[str] | None = None, world_link: str | INodeObjectOutput[IWorldLink] | None = None, relation: str | INodeValueOutput[WorldRelation] | None = None, get_existing: str | INodeValueOutput[primitives.Bool] | None = None, loading_indicator: str | INodeValueOutput[primitives.Bool] | None = None, auto_focus: str | INodeValueOutput[primitives.Bool] | None = None, make_private: str | INodeValueOutput[primitives.Bool] | None = None, on_open_start: str | INodeOperation | None = None, on_open_done: str | INodeOperation | None = None, on_world_ready: str | INodeOperation | None = None, on_open_fail: str | INodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            world_link: Initial value for WorldLink.
            relation: Initial value for Relation.
            get_existing: Initial value for GetExisting.
            loading_indicator: Initial value for LoadingIndicator.
            auto_focus: Initial value for AutoFocus.
            make_private: Initial value for MakePrivate.
            on_open_start: Initial value for OnOpenStart.
            on_open_done: Initial value for OnOpenDone.
            on_world_ready: Initial value for OnWorldReady.
            on_open_fail: Initial value for OnOpenFail.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if url is not None:
            self.url = url
        if world_link is not None:
            self.world_link = world_link
        if relation is not None:
            self.relation = relation
        if get_existing is not None:
            self.get_existing = get_existing
        if loading_indicator is not None:
            self.loading_indicator = loading_indicator
        if auto_focus is not None:
            self.auto_focus = auto_focus
        if make_private is not None:
            self.make_private = make_private
        if on_open_start is not None:
            self.on_open_start = on_open_start
        if on_open_done is not None:
            self.on_open_done = on_open_done
        if on_world_ready is not None:
            self.on_world_ready = on_world_ready
        if on_open_fail is not None:
            self.on_open_fail = on_open_fail

    @property
    def url(self) -> str | None:
        """The World URL needed to open a world."""
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
    def world_link(self) -> str | None:
        """The link to a world (using the WorldLink component). This can be an alternative way of opening a world."""
        member = self.get_member("WorldLink")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @world_link.setter
    def world_link(self, target: str | INodeObjectOutput[IWorldLink] | None) -> None:
        """Set the WorldLink reference by target ID or INodeObjectOutput[IWorldLink] instance."""
        target_id: str | None = target.id if isinstance(target, INodeObjectOutput) else target  # type: ignore[assignment]
        member = self.get_member("WorldLink")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "WorldLink",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeObjectOutput<[FrooxEngine]FrooxEngine.IWorldLink>'),
            )

    @property
    def relation(self) -> str | None:
        """The relation to a world (Not necessary for opening a world). See the Relation Type for more info."""
        member = self.get_member("Relation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @relation.setter
    def relation(self, target: str | INodeValueOutput[WorldRelation] | None) -> None:
        """Set the Relation reference by target ID or INodeValueOutput[WorldRelation] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Relation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Relation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<[FrooxEngine]FrooxEngine.Userspace+WorldRelation>'),
            )

    @property
    def get_existing(self) -> str | None:
        """Should this try to get an already opened world first."""
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
    def loading_indicator(self) -> str | None:
        """Should this show a loading indicator to the user that is opening the world."""
        member = self.get_member("LoadingIndicator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @loading_indicator.setter
    def loading_indicator(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the LoadingIndicator reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("LoadingIndicator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LoadingIndicator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def auto_focus(self) -> str | None:
        """Should this automatically focus the user to the opened world as soon as it opens."""
        member = self.get_member("AutoFocus")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @auto_focus.setter
    def auto_focus(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the AutoFocus reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("AutoFocus")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AutoFocus",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def make_private(self) -> str | None:
        """Should this make the opening world private when opening it."""
        member = self.get_member("MakePrivate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @make_private.setter
    def make_private(self, target: str | INodeValueOutput[primitives.Bool] | None) -> None:
        """Set the MakePrivate reference by target ID or INodeValueOutput[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("MakePrivate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MakePrivate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<bool>'),
            )

    @property
    def session_id(self) -> members.EmptyElement | None:
        """The session ID for the opened world and user connection to it."""
        member = self.get_member("SessionID")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @session_id.setter
    def session_id(self, value: members.EmptyElement) -> None:
        """Set SessionID. The session ID for the opened world and user connection to it."""
        self.set_member("SessionID", value)

    @property
    def session_url(self) -> members.EmptyElement | None:
        """The world URL for the opened session."""
        member = self.get_member("SessionURL")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @session_url.setter
    def session_url(self, value: members.EmptyElement) -> None:
        """Set SessionURL. The world URL for the opened session."""
        self.set_member("SessionURL", value)

    @property
    def on_open_start(self) -> str | None:
        """Fires when the world has started to open."""
        member = self.get_member("OnOpenStart")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_open_start.setter
    def on_open_start(self, target: str | INodeOperation | None) -> None:
        """Set the OnOpenStart reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnOpenStart")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnOpenStart",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_open_done(self) -> str | None:
        """Fires when the world has finished opening."""
        member = self.get_member("OnOpenDone")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_open_done.setter
    def on_open_done(self, target: str | INodeOperation | None) -> None:
        """Set the OnOpenDone reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnOpenDone")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnOpenDone",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_world_ready(self) -> str | None:
        """Fires when the world has finished opening and is ready to hold users."""
        member = self.get_member("OnWorldReady")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_world_ready.setter
    def on_world_ready(self, target: str | INodeOperation | None) -> None:
        """Set the OnWorldReady reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnWorldReady")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnWorldReady",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

    @property
    def on_open_fail(self) -> str | None:
        """Fires when the world could not be opened or the world URL is not valid."""
        member = self.get_member("OnOpenFail")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_open_fail.setter
    def on_open_fail(self, target: str | INodeOperation | None) -> None:
        """Set the OnOpenFail reference by target ID or INodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, INodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnOpenFail")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnOpenFail",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeOperation'),
            )

