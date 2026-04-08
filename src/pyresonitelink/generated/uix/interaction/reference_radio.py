"""Generated component: ReferenceRadio."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceRadio(GenericComponent[T], IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UIX.ReferenceRadio<>.

    Category: UIX/Interaction

    Parameterize with a value type::

        ReferenceRadio[np.float32]
        ReferenceRadio[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UIX.ReferenceRadio<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.UIX.ReferenceRadio<>"

    def __init__(self, check_visual: str | IField[bool] | None = None, option_reference: str | T | None = None, target_reference: str | SyncRef[T] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            check_visual: Initial value for CheckVisual.
            option_reference: Initial value for OptionReference.
            target_reference: Initial value for TargetReference.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if check_visual is not None:
            self.check_visual = check_visual
        if option_reference is not None:
            self.option_reference = option_reference
        if target_reference is not None:
            self.target_reference = target_reference

    @property
    def check_visual(self) -> str | None:
        """Target ID of the CheckVisual reference (targets IField[bool])."""
        member = self.get_member("CheckVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @check_visual.setter
    def check_visual(self, target: str | IField[bool] | None) -> None:
        """Set the CheckVisual reference by target ID or IField[bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("CheckVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CheckVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def option_reference(self) -> str | None:
        """Target ID of the OptionReference reference (targets T)."""
        member = self.get_member("OptionReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @option_reference.setter
    def option_reference(self, target: str | T | None) -> None:
        """Set the OptionReference reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("OptionReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OptionReference",
                members.Reference(targetId=target_id, targetType='T'),
            )

    @property
    def target_reference(self) -> str | None:
        """Target ID of the TargetReference reference (targets SyncRef[T])."""
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_reference.setter
    def target_reference(self, target: str | SyncRef[T] | None) -> None:
        """Set the TargetReference reference by target ID or SyncRef[T] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("TargetReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TargetReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<T>'),
            )

