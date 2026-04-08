"""Generated component: WorldPermissions."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldPermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.WorldPermissions.

    Category: Permissions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldPermissions"

    def __init__(self, allow_saving_items: primitives.Bool | None = None, allow_transfering_objects_out: primitives.Bool | None = None, allow_spawning_objects: primitives.Bool | None = None, allow_swapping_avatars: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            allow_saving_items: Initial value for AllowSavingItems.
            allow_transfering_objects_out: Initial value for AllowTransferingObjectsOut.
            allow_spawning_objects: Initial value for AllowSpawningObjects.
            allow_swapping_avatars: Initial value for AllowSwappingAvatars.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if allow_saving_items is not None:
            self.allow_saving_items = allow_saving_items
        if allow_transfering_objects_out is not None:
            self.allow_transfering_objects_out = allow_transfering_objects_out
        if allow_spawning_objects is not None:
            self.allow_spawning_objects = allow_spawning_objects
        if allow_swapping_avatars is not None:
            self.allow_swapping_avatars = allow_swapping_avatars

    @property
    def allow_saving_items(self) -> primitives.Bool | None:
        """The AllowSavingItems field value."""
        member = self.get_member("AllowSavingItems")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_saving_items.setter
    def allow_saving_items(self, value: primitives.Bool) -> None:
        """Set the AllowSavingItems field value."""
        member = self.get_member("AllowSavingItems")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowSavingItems", fields.FieldBool(value=value)
            )

    @property
    def allow_transfering_objects_out(self) -> primitives.Bool | None:
        """The AllowTransferingObjectsOut field value."""
        member = self.get_member("AllowTransferingObjectsOut")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_transfering_objects_out.setter
    def allow_transfering_objects_out(self, value: primitives.Bool) -> None:
        """Set the AllowTransferingObjectsOut field value."""
        member = self.get_member("AllowTransferingObjectsOut")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowTransferingObjectsOut", fields.FieldBool(value=value)
            )

    @property
    def allow_spawning_objects(self) -> primitives.Bool | None:
        """The AllowSpawningObjects field value."""
        member = self.get_member("AllowSpawningObjects")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_spawning_objects.setter
    def allow_spawning_objects(self, value: primitives.Bool) -> None:
        """Set the AllowSpawningObjects field value."""
        member = self.get_member("AllowSpawningObjects")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowSpawningObjects", fields.FieldBool(value=value)
            )

    @property
    def allow_swapping_avatars(self) -> primitives.Bool | None:
        """The AllowSwappingAvatars field value."""
        member = self.get_member("AllowSwappingAvatars")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_swapping_avatars.setter
    def allow_swapping_avatars(self, value: primitives.Bool) -> None:
        """Set the AllowSwappingAvatars field value."""
        member = self.get_member("AllowSwappingAvatars")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowSwappingAvatars", fields.FieldBool(value=value)
            )

    @property
    def save_copy_permission(self) -> members.FieldEnum | None:
        """The SaveCopyPermission member."""
        member = self.get_member("SaveCopyPermission")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @save_copy_permission.setter
    def save_copy_permission(self, value: members.FieldEnum) -> None:
        """Set the SaveCopyPermission member."""
        self.set_member("SaveCopyPermission", value)

