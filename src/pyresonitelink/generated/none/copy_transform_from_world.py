"""Generated component: CopyTransformFromWorld."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class CopyTransformFromWorld(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.CopyTransformFromWorld.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CopyTransformFromWorld"

    def __init__(self, copy_position: primitives.Bool | None = None, copy_rotation: primitives.Bool | None = None, copy_scale: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            copy_position: Initial value for CopyPosition.
            copy_rotation: Initial value for CopyRotation.
            copy_scale: Initial value for CopyScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if copy_position is not None:
            self.copy_position = copy_position
        if copy_rotation is not None:
            self.copy_rotation = copy_rotation
        if copy_scale is not None:
            self.copy_scale = copy_scale

    @property
    def copy_position(self) -> primitives.Bool | None:
        """The CopyPosition field value."""
        member = self.get_member("CopyPosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @copy_position.setter
    def copy_position(self, value: primitives.Bool) -> None:
        """Set the CopyPosition field value."""
        member = self.get_member("CopyPosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CopyPosition", fields.FieldBool(value=value)
            )

    @property
    def copy_rotation(self) -> primitives.Bool | None:
        """The CopyRotation field value."""
        member = self.get_member("CopyRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @copy_rotation.setter
    def copy_rotation(self, value: primitives.Bool) -> None:
        """Set the CopyRotation field value."""
        member = self.get_member("CopyRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CopyRotation", fields.FieldBool(value=value)
            )

    @property
    def copy_scale(self) -> primitives.Bool | None:
        """The CopyScale field value."""
        member = self.get_member("CopyScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @copy_scale.setter
    def copy_scale(self, value: primitives.Bool) -> None:
        """Set the CopyScale field value."""
        member = self.get_member("CopyScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CopyScale", fields.FieldBool(value=value)
            )

