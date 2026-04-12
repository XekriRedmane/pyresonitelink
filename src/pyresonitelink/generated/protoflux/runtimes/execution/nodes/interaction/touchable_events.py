"""Generated component: TouchableEvents."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.touch_event_relay import TouchEventRelay
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TouchableEvents(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """The ``Touchable Events`` node takes in a global Event Source reference and will listen for events from that global reference. When it detects something happening, it will fire events depending on what happens, along with other data.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Interaction

    **See also**: ButtonEvents
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.TouchableEvents"

    def __init__(self, event_source: str | IGlobalValueProxy[TouchEventRelay] | None = None, on_event: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            event_source: Initial value for EventSource.
            on_event: Initial value for OnEvent.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if event_source is not None:
            self.event_source = event_source
        if on_event is not None:
            self.on_event = on_event

    @property
    def event_source(self) -> str | None:
        """Target ID of the EventSource reference (targets IGlobalValueProxy[TouchEventRelay])."""
        member = self.get_member("EventSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @event_source.setter
    def event_source(self, target: str | IGlobalValueProxy[TouchEventRelay] | None) -> None:
        """Set the EventSource reference by target ID or IGlobalValueProxy[TouchEventRelay] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("EventSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EventSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.TouchEventRelay>'),
            )

    @property
    def on_event(self) -> str | None:
        """Target ID of the OnEvent reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnEvent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_event.setter
    def on_event(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnEvent reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnEvent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnEvent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def hover(self) -> members.EmptyElement | None:
        """The Hover member."""
        member = self.get_member("Hover")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @hover.setter
    def hover(self, value: members.EmptyElement) -> None:
        """Set the Hover member."""
        self.set_member("Hover", value)

    @property
    def touch(self) -> members.EmptyElement | None:
        """The Touch member."""
        member = self.get_member("Touch")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @touch.setter
    def touch(self, value: members.EmptyElement) -> None:
        """Set the Touch member."""
        self.set_member("Touch", value)

    @property
    def point(self) -> members.EmptyElement | None:
        """The Point member."""
        member = self.get_member("Point")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @point.setter
    def point(self, value: members.EmptyElement) -> None:
        """Set the Point member."""
        self.set_member("Point", value)

    @property
    def tip(self) -> members.EmptyElement | None:
        """The Tip member."""
        member = self.get_member("Tip")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @tip.setter
    def tip(self, value: members.EmptyElement) -> None:
        """Set the Tip member."""
        self.set_member("Tip", value)

    @property
    def type_(self) -> members.EmptyElement | None:
        """The Type member."""
        member = self.get_member("Type")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @type_.setter
    def type_(self, value: members.EmptyElement) -> None:
        """Set the Type member."""
        self.set_member("Type", value)

    @property
    def source(self) -> members.EmptyElement | None:
        """The Source member."""
        member = self.get_member("Source")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @source.setter
    def source(self, value: members.EmptyElement) -> None:
        """Set the Source member."""
        self.set_member("Source", value)

