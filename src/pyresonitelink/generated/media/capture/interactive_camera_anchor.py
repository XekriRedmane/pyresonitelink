"""Generated component: InteractiveCameraAnchor."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class InteractiveCameraAnchor(GeneratedComponent, ITouchable, IWorldEventReceiver):
    """The InteractiveCameraAnchor component acts as a spot to drop or auto transition a streaming or other type of camera or to.

See Camera Anchors.

    Category: Media/Capture

    Attaching this component to a slot creates the visual as well as the
    default values. Simply dropping a stream camera into the visual will
    snap the camera to it.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.InteractiveCameraAnchor"

    def __init__(self, override_root: str | Slot | None = None, field_of_view: primitives.Float | None = None, highlighted: primitives.Bool | None = None, in_use: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
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
        """The place other than under this component's slot to parent the cameta."""
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
    def field_of_view(self) -> primitives.Float | None:
        """What the FOV of a camera anchored to this anchor should be set to."""
        member = self.get_member("FieldOfView")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @field_of_view.setter
    def field_of_view(self, value: primitives.Float) -> None:
        """Set the FieldOfView field value."""
        member = self.get_member("FieldOfView")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FieldOfView", fields.FieldFloat(value=value)
            )

    @property
    def highlighted(self) -> primitives.Bool | None:
        """Whether this anchor is being highlighted as part of specifying a camera anchor set/route."""
        member = self.get_member("Highlighted")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @highlighted.setter
    def highlighted(self, value: primitives.Bool) -> None:
        """Set the Highlighted field value."""
        member = self.get_member("Highlighted")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Highlighted", fields.FieldBool(value=value)
            )

    @property
    def in_use(self) -> primitives.Bool | None:
        """Whether or not the anchor has a camera in it."""
        member = self.get_member("InUse")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @in_use.setter
    def in_use(self, value: primitives.Bool) -> None:
        """Set the InUse field value."""
        member = self.get_member("InUse")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InUse", fields.FieldBool(value=value)
            )

