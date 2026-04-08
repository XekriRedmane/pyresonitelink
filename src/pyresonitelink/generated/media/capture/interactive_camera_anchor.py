"""Generated component: InteractiveCameraAnchor."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InteractiveCameraAnchor(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.InteractiveCameraAnchor.

    Category: Media/Capture
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraAnchor"

    def __init__(self, override_root: str | Slot | None = None, field_of_view: np.float32 | None = None, highlighted: bool | None = None, in_use: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            override_root: Initial value for OverrideRoot.
            field_of_view: Initial value for FieldOfView.
            highlighted: Initial value for Highlighted.
            in_use: Initial value for InUse.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if override_root is not None:
            self.override_root = override_root
        if field_of_view is not None:
            self.field_of_view = field_of_view
        if highlighted is not None:
            self.highlighted = highlighted
        if in_use is not None:
            self.in_use = in_use

    @property
    def override_root(self) -> str | None:
        """Target ID of the OverrideRoot reference (targets Slot)."""
        member = self.get_member("OverrideRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @override_root.setter
    def override_root(self, target: str | Slot | None) -> None:
        """Set the OverrideRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("OverrideRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OverrideRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def field_of_view(self) -> np.float32 | None:
        """The FieldOfView field value."""
        member = self.get_member("FieldOfView")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @field_of_view.setter
    def field_of_view(self, value: np.float32) -> None:
        """Set the FieldOfView field value."""
        member = self.get_member("FieldOfView")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FieldOfView", fields.FieldFloat(value=value)
            )

    @property
    def highlighted(self) -> bool | None:
        """The Highlighted field value."""
        member = self.get_member("Highlighted")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @highlighted.setter
    def highlighted(self, value: bool) -> None:
        """Set the Highlighted field value."""
        member = self.get_member("Highlighted")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Highlighted", fields.FieldBool(value=value)
            )

    @property
    def in_use(self) -> bool | None:
        """The InUse field value."""
        member = self.get_member("InUse")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @in_use.setter
    def in_use(self, value: bool) -> None:
        """Set the InUse field value."""
        member = self.get_member("InUse")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InUse", fields.FieldBool(value=value)
            )

