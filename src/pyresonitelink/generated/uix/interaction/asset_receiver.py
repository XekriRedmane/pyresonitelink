"""Generated component: AssetReceiver."""

from typing import Any

A = Any
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.asset_ref import AssetRef
from pyresonitelink.generated._types.iui_grab_receiver import IUIGrabReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AssetReceiver(GenericComponent[T], IUIGrabReceiver, IWorldEventReceiver):
    """Asset Receiver is a useful component for getting asset data from a user through a UIX. When this item is placed on a UIX that allows receiving (like a Button) and it's ``Reference`` field is filled, it will be active. When an item is pushed through the canvas where the button is so the interaction laser is hitting it and the item is let go; the value within the field inside of ``Reference`` is set to the first available IAsset which is exposed by an Asset Proxy.

    Category: UIX/Interaction

    Parameterize with a value type::

        AssetReceiver[primitives.Float]
        AssetReceiver[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.AssetReceiver<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.UIX.AssetReceiver<>"

    def __init__(self, reference: str | AssetRef[A] | None = None, undoable: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reference: Initial value for Reference.
            undoable: Initial value for Undoable.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reference is not None:
            self.reference = reference
        if undoable is not None:
            self.undoable = undoable

    @property
    def reference(self) -> str | None:
        """The field to fill with a value when a grabbed item with an Asset Proxy is dropped onto the canvas region with this component."""
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference.setter
    def reference(self, target: str | AssetRef[A] | None) -> None:
        """Set the Reference reference by target ID or AssetRef[A] instance."""
        target_id: str | None = target.id if isinstance(target, AssetRef) else target  # type: ignore[assignment]
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Reference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetRef<A>'),
            )

    @property
    def undoable(self) -> primitives.Bool | None:
        """Whether to add changes to this value via grab receiving to the undo stack of the user that changed it."""
        member = self.get_member("Undoable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @undoable.setter
    def undoable(self, value: primitives.Bool) -> None:
        """Set the Undoable field value."""
        member = self.get_member("Undoable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Undoable", fields.FieldBool(value=value)
            )

