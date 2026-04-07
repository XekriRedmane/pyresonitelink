"""Generated component: ButtonEvents."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.ibutton import IButton
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonEvents(GeneratedComponent, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.ButtonEvents.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Interaction
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Interaction.ButtonEvents"

    def __init__(self, button: str | IGlobalValueProxy[IButton] | None = None, pressed: str | ISyncNodeOperation | None = None, pressing: str | ISyncNodeOperation | None = None, released: str | ISyncNodeOperation | None = None, hover_enter: str | ISyncNodeOperation | None = None, hover_stay: str | ISyncNodeOperation | None = None, hover_leave: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            button: Initial value for Button.
            pressed: Initial value for Pressed.
            pressing: Initial value for Pressing.
            released: Initial value for Released.
            hover_enter: Initial value for HoverEnter.
            hover_stay: Initial value for HoverStay.
            hover_leave: Initial value for HoverLeave.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if button is not None:
            self.button = button
        if pressed is not None:
            self.pressed = pressed
        if pressing is not None:
            self.pressing = pressing
        if released is not None:
            self.released = released
        if hover_enter is not None:
            self.hover_enter = hover_enter
        if hover_stay is not None:
            self.hover_stay = hover_stay
        if hover_leave is not None:
            self.hover_leave = hover_leave

    @property
    def button(self) -> str | None:
        """Target ID of the Button reference (targets IGlobalValueProxy[IButton])."""
        member = self.get_member("Button")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @button.setter
    def button(self, target: str | IGlobalValueProxy[IButton] | None) -> None:
        """Set the Button reference by target ID or IGlobalValueProxy[IButton] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Button")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Button",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.IButton>'),
            )

    @property
    def pressed(self) -> str | None:
        """Target ID of the Pressed reference (targets ISyncNodeOperation)."""
        member = self.get_member("Pressed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pressed.setter
    def pressed(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the Pressed reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Pressed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Pressed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def pressing(self) -> str | None:
        """Target ID of the Pressing reference (targets ISyncNodeOperation)."""
        member = self.get_member("Pressing")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pressing.setter
    def pressing(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the Pressing reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Pressing")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Pressing",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def released(self) -> str | None:
        """Target ID of the Released reference (targets ISyncNodeOperation)."""
        member = self.get_member("Released")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @released.setter
    def released(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the Released reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("Released")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Released",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def hover_enter(self) -> str | None:
        """Target ID of the HoverEnter reference (targets ISyncNodeOperation)."""
        member = self.get_member("HoverEnter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hover_enter.setter
    def hover_enter(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the HoverEnter reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("HoverEnter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HoverEnter",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def hover_stay(self) -> str | None:
        """Target ID of the HoverStay reference (targets ISyncNodeOperation)."""
        member = self.get_member("HoverStay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hover_stay.setter
    def hover_stay(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the HoverStay reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("HoverStay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HoverStay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def hover_leave(self) -> str | None:
        """Target ID of the HoverLeave reference (targets ISyncNodeOperation)."""
        member = self.get_member("HoverLeave")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hover_leave.setter
    def hover_leave(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the HoverLeave reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("HoverLeave")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HoverLeave",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

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

    @property
    def global_point(self) -> members.EmptyElement | None:
        """The GlobalPoint member."""
        member = self.get_member("GlobalPoint")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @global_point.setter
    def global_point(self, value: members.EmptyElement) -> None:
        """Set the GlobalPoint member."""
        self.set_member("GlobalPoint", value)

    @property
    def local_point(self) -> members.EmptyElement | None:
        """The LocalPoint member."""
        member = self.get_member("LocalPoint")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @local_point.setter
    def local_point(self, value: members.EmptyElement) -> None:
        """Set the LocalPoint member."""
        self.set_member("LocalPoint", value)

    @property
    def normalized_point(self) -> members.EmptyElement | None:
        """The NormalizedPoint member."""
        member = self.get_member("NormalizedPoint")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @normalized_point.setter
    def normalized_point(self, value: members.EmptyElement) -> None:
        """Set the NormalizedPoint member."""
        self.set_member("NormalizedPoint", value)

