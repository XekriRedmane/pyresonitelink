"""Generated component: AnchorLocomotionData."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iglobal_value_proxy import IGlobalValueProxy
from pyresonitelink.generated._types.avatar_anchor import AvatarAnchor
from pyresonitelink.generated._types.isync_node_operation import ISyncNodeOperation
from pyresonitelink.generated._types.imappable_node import IMappableNode
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AnchorLocomotionData(GeneratedComponent, IMappableNode, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.Anchors.AnchorLocomotionData.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Avatars/Anchors
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Avatar.Anchors.AnchorLocomotionData"

    def __init__(self, anchor: str | IGlobalValueProxy[AvatarAnchor] | None = None, on_locomotion_update: str | ISyncNodeOperation | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            anchor: Initial value for Anchor.
            on_locomotion_update: Initial value for OnLocomotionUpdate.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if anchor is not None:
            self.anchor = anchor
        if on_locomotion_update is not None:
            self.on_locomotion_update = on_locomotion_update

    @property
    def anchor(self) -> str | None:
        """Target ID of the Anchor reference (targets IGlobalValueProxy[AvatarAnchor])."""
        member = self.get_member("Anchor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @anchor.setter
    def anchor(self, target: str | IGlobalValueProxy[AvatarAnchor] | None) -> None:
        """Set the Anchor reference by target ID or IGlobalValueProxy[AvatarAnchor] instance."""
        target_id: str | None = target.id if isinstance(target, IGlobalValueProxy) else target  # type: ignore[assignment]
        member = self.get_member("Anchor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Anchor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.IGlobalValueProxy<[FrooxEngine]FrooxEngine.CommonAvatar.AvatarAnchor>'),
            )

    @property
    def on_locomotion_update(self) -> str | None:
        """Target ID of the OnLocomotionUpdate reference (targets ISyncNodeOperation)."""
        member = self.get_member("OnLocomotionUpdate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @on_locomotion_update.setter
    def on_locomotion_update(self, target: str | ISyncNodeOperation | None) -> None:
        """Set the OnLocomotionUpdate reference by target ID or ISyncNodeOperation instance."""
        target_id: str | None = target.id if isinstance(target, ISyncNodeOperation) else target  # type: ignore[assignment]
        member = self.get_member("OnLocomotionUpdate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OnLocomotionUpdate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ISyncNodeOperation'),
            )

    @property
    def has_primary(self) -> members.EmptyElement | None:
        """The HasPrimary member."""
        member = self.get_member("HasPrimary")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @has_primary.setter
    def has_primary(self, value: members.EmptyElement) -> None:
        """Set the HasPrimary member."""
        self.set_member("HasPrimary", value)

    @property
    def has_secondary(self) -> members.EmptyElement | None:
        """The HasSecondary member."""
        member = self.get_member("HasSecondary")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @has_secondary.setter
    def has_secondary(self, value: members.EmptyElement) -> None:
        """Set the HasSecondary member."""
        self.set_member("HasSecondary", value)

    @property
    def primary_axis(self) -> members.EmptyElement | None:
        """The PrimaryAxis member."""
        member = self.get_member("PrimaryAxis")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @primary_axis.setter
    def primary_axis(self, value: members.EmptyElement) -> None:
        """Set the PrimaryAxis member."""
        self.set_member("PrimaryAxis", value)

    @property
    def secondary_axis(self) -> members.EmptyElement | None:
        """The SecondaryAxis member."""
        member = self.get_member("SecondaryAxis")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @secondary_axis.setter
    def secondary_axis(self, value: members.EmptyElement) -> None:
        """Set the SecondaryAxis member."""
        self.set_member("SecondaryAxis", value)

    @property
    def primary_action(self) -> members.EmptyElement | None:
        """The PrimaryAction member."""
        member = self.get_member("PrimaryAction")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @primary_action.setter
    def primary_action(self, value: members.EmptyElement) -> None:
        """Set the PrimaryAction member."""
        self.set_member("PrimaryAction", value)

    @property
    def secondary_action(self) -> members.EmptyElement | None:
        """The SecondaryAction member."""
        member = self.get_member("SecondaryAction")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @secondary_action.setter
    def secondary_action(self, value: members.EmptyElement) -> None:
        """Set the SecondaryAction member."""
        self.set_member("SecondaryAction", value)

