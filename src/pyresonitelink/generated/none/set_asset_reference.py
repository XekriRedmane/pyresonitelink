"""Generated component: SetAssetReference."""

from typing import Any

A = Any
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.asset_ref import AssetRef
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.iundoable import IUndoable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SetAssetReference(GenericComponent[T], IUndoable, IWorldEventReceiver):
    """The Set Asset Reference component is used to store an undo step for setting a reference field for assets to another asset.

    Not used directly by the user.

    Parameterize with a value type::

        SetAssetReference[primitives.Float]
        SetAssetReference[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Undo.SetAssetReference<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.Undo.SetAssetReference<>"

    def __init__(self, target: str | AssetRef[A] | None = None, target_before: str | IAssetProvider[A] | None = None, target_after: str | IAssetProvider[A] | None = None, performed: primitives.Bool | None = None, description: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            target_before: Initial value for TargetBefore.
            target_after: Initial value for TargetAfter.
            performed: Initial value for _performed.
            description: Initial value for _description.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if target_before is not None:
            self.target_before = target_before
        if target_after is not None:
            self.target_after = target_after
        if performed is not None:
            self.performed = performed
        if description is not None:
            self.description = description

    @property
    def target(self) -> str | None:
        """The field that was changed."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | AssetRef[A] | None) -> None:
        """Set the Target reference by target ID or AssetRef[A] instance."""
        target_id: str | None = target.id if isinstance(target, AssetRef) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetRef<A>'),
            )

    @property
    def target_before(self) -> str | None:
        """The asset value before the change"""
        member = self.get_member("TargetBefore")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_before.setter
    def target_before(self, target: str | IAssetProvider[A] | None) -> None:
        """Set the TargetBefore reference by target ID or IAssetProvider[A] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("TargetBefore")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetBefore",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<A>'),
            )

    @property
    def target_after(self) -> str | None:
        """The asset value after the change."""
        member = self.get_member("TargetAfter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_after.setter
    def target_after(self, target: str | IAssetProvider[A] | None) -> None:
        """Set the TargetAfter reference by target ID or IAssetProvider[A] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("TargetAfter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetAfter",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<A>'),
            )

    @property
    def performed(self) -> primitives.Bool | None:
        """Whether the undo step was done or undone."""
        member = self.get_member("_performed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @performed.setter
    def performed(self, value: primitives.Bool) -> None:
        """Set the _performed field value."""
        member = self.get_member("_performed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_performed", fields.FieldBool(value=value)
            )

    @property
    def description(self) -> primitives.String | None:
        """The description of the change that was made and what to for the context menu label text when undoing/redoing."""
        member = self.get_member("_description")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @description.setter
    def description(self, value: primitives.String) -> None:
        """Set the _description field value."""
        member = self.get_member("_description")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_description", fields.FieldString(value=value)
            )

