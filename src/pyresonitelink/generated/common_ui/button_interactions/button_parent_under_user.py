"""Generated component: ButtonParentUnderUser."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonParentUnderUser(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ButtonParentUnderUser.

    Category: Common UI/Button Interactions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonParentUnderUser"

    def __init__(self, root: str | Slot | None = None, find_object_root: bool | None = None, unparent_when_parented: bool | None = None, preserve_original_space: bool | None = None, original_space: str | Slot | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            root: Initial value for Root.
            find_object_root: Initial value for FindObjectRoot.
            unparent_when_parented: Initial value for UnparentWhenParented.
            preserve_original_space: Initial value for PreserveOriginalSpace.
            original_space: Initial value for _originalSpace.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if root is not None:
            self.root = root
        if find_object_root is not None:
            self.find_object_root = find_object_root
        if unparent_when_parented is not None:
            self.unparent_when_parented = unparent_when_parented
        if preserve_original_space is not None:
            self.preserve_original_space = preserve_original_space
        if original_space is not None:
            self.original_space = original_space

    @property
    def root(self) -> str | None:
        """Target ID of the Root reference (targets Slot)."""
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root.setter
    def root(self, target: str | Slot | None) -> None:
        """Set the Root reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Root",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def find_object_root(self) -> bool | None:
        """The FindObjectRoot field value."""
        member = self.get_member("FindObjectRoot")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @find_object_root.setter
    def find_object_root(self, value: bool) -> None:
        """Set the FindObjectRoot field value."""
        member = self.get_member("FindObjectRoot")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FindObjectRoot", fields.FieldBool(value=value)
            )

    @property
    def unparent_when_parented(self) -> bool | None:
        """The UnparentWhenParented field value."""
        member = self.get_member("UnparentWhenParented")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @unparent_when_parented.setter
    def unparent_when_parented(self, value: bool) -> None:
        """Set the UnparentWhenParented field value."""
        member = self.get_member("UnparentWhenParented")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UnparentWhenParented", fields.FieldBool(value=value)
            )

    @property
    def preserve_original_space(self) -> bool | None:
        """The PreserveOriginalSpace field value."""
        member = self.get_member("PreserveOriginalSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preserve_original_space.setter
    def preserve_original_space(self, value: bool) -> None:
        """Set the PreserveOriginalSpace field value."""
        member = self.get_member("PreserveOriginalSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreserveOriginalSpace", fields.FieldBool(value=value)
            )

    @property
    def original_space(self) -> str | None:
        """Target ID of the _originalSpace reference (targets Slot)."""
        member = self.get_member("_originalSpace")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @original_space.setter
    def original_space(self, target: str | Slot | None) -> None:
        """Set the _originalSpace reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_originalSpace")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_originalSpace",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

