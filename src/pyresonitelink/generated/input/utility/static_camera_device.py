"""Generated component: StaticCameraDevice."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StaticCameraDevice(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.StaticCameraDevice.

    Category: Input/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StaticCameraDevice"

    def __init__(self, owner: str | User | None = None, field_of_view: primitives.Float | None = None, aspect_ratio: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            owner: Initial value for Owner.
            field_of_view: Initial value for FieldOfView.
            aspect_ratio: Initial value for AspectRatio.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if owner is not None:
            self.owner = owner
        if field_of_view is not None:
            self.field_of_view = field_of_view
        if aspect_ratio is not None:
            self.aspect_ratio = aspect_ratio

    @property
    def owner(self) -> str | None:
        """Target ID of the Owner reference (targets User)."""
        member = self.get_member("Owner")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @owner.setter
    def owner(self, target: str | User | None) -> None:
        """Set the Owner reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("Owner")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Owner",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def field_of_view(self) -> primitives.Float | None:
        """The FieldOfView field value."""
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
    def aspect_ratio(self) -> primitives.Float | None:
        """The AspectRatio field value."""
        member = self.get_member("AspectRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @aspect_ratio.setter
    def aspect_ratio(self, value: primitives.Float) -> None:
        """Set the AspectRatio field value."""
        member = self.get_member("AspectRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AspectRatio", fields.FieldFloat(value=value)
            )

