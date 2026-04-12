"""Generated component: WorldPermissions."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.save_permission import SavePermission
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworker_permissions import IWorkerPermissions
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldPermissions(GeneratedComponent, IWorkerPermissions, ICustomInspector, IWorldEventReceiver):
    """The WorldPermissions component controls various actions the selected roles can do in the world.

    Category: Permissions
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldPermissions"

    def __init__(self, allow_saving_items: primitives.Bool | None = None, allow_transfering_objects_out: primitives.Bool | None = None, allow_spawning_objects: primitives.Bool | None = None, allow_swapping_avatars: primitives.Bool | None = None, save_copy_permission: SavePermission | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            allow_saving_items: Initial value for AllowSavingItems.
            allow_transfering_objects_out: Initial value for AllowTransferingObjectsOut.
            allow_spawning_objects: Initial value for AllowSpawningObjects.
            allow_swapping_avatars: Initial value for AllowSwappingAvatars.
            save_copy_permission: Initial value for SaveCopyPermission.
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
        if save_copy_permission is not None:
            self.save_copy_permission = save_copy_permission

    @property
    def allow_saving_items(self) -> primitives.Bool | None:
        """Whether the selected roles can save items."""
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
        """Whether the selected roles can smuggle items out."""
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
        """Whether the selected roles can spawn objects."""
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
        """Whether the selected roles can swap into a different avatar."""
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
    def save_copy_permission(self) -> SavePermission | None:
        """When can the selected roles save the world?"""
        member = self.get_member("SaveCopyPermission")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SavePermission(member.value)
        return None

    @save_copy_permission.setter
    def save_copy_permission(self, value: SavePermission | str) -> None:
        """Set SaveCopyPermission. When can the selected roles save the world?"""
        member = self.get_member("SaveCopyPermission")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "SaveCopyPermission",
                members.FieldEnum(value=str(value)),
            )

