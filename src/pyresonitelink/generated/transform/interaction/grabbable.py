"""Generated component: Grabbable."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.active_user_handling import ActiveUserHandling
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.grabber import Grabber
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.igrabbable import IGrabbable
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Grabbable(GeneratedComponent, IGrabbable, IObjectRoot, IWorldEventReceiver):
    """The Grabbable component allows you to grab any slot it is attached to, provided it has some type of Collider.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Grabbable"

    def __init__(self, reparent_on_release: primitives.Bool | None = None, preserve_user_space: primitives.Bool | None = None, destroy_on_release: primitives.Bool | None = None, grab_priority: primitives.Int | None = None, grab_priority_when_grabbed: primitives.Int | None = None, edit_mode_only: primitives.Bool | None = None, allow_steal: primitives.Bool | None = None, drop_on_disable: primitives.Bool | None = None, active_user_filter: ActiveUserHandling | str | None = None, scalable: primitives.Bool | None = None, receivable: primitives.Bool | None = None, allow_only_physical_grab: primitives.Bool | None = None, grabber: str | Grabber | None = None, last_parent: str | Slot | None = None, last_parent_is_user_space: primitives.Bool | None = None, legacy_active_user_root_only: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reparent_on_release: Initial value for ReparentOnRelease.
            preserve_user_space: Initial value for PreserveUserSpace.
            destroy_on_release: Initial value for DestroyOnRelease.
            grab_priority: Initial value for GrabPriority.
            grab_priority_when_grabbed: Initial value for GrabPriorityWhenGrabbed.
            edit_mode_only: Initial value for EditModeOnly.
            allow_steal: Initial value for AllowSteal.
            drop_on_disable: Initial value for DropOnDisable.
            active_user_filter: Initial value for ActiveUserFilter.
            scalable: Initial value for Scalable.
            receivable: Initial value for Receivable.
            allow_only_physical_grab: Initial value for AllowOnlyPhysicalGrab.
            grabber: Initial value for _grabber.
            last_parent: Initial value for _lastParent.
            last_parent_is_user_space: Initial value for _lastParentIsUserSpace.
            legacy_active_user_root_only: Initial value for __legacyActiveUserRootOnly.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reparent_on_release is not None:
            self.reparent_on_release = reparent_on_release
        if preserve_user_space is not None:
            self.preserve_user_space = preserve_user_space
        if destroy_on_release is not None:
            self.destroy_on_release = destroy_on_release
        if grab_priority is not None:
            self.grab_priority = grab_priority
        if grab_priority_when_grabbed is not None:
            self.grab_priority_when_grabbed = grab_priority_when_grabbed
        if edit_mode_only is not None:
            self.edit_mode_only = edit_mode_only
        if allow_steal is not None:
            self.allow_steal = allow_steal
        if drop_on_disable is not None:
            self.drop_on_disable = drop_on_disable
        if active_user_filter is not None:
            self.active_user_filter = active_user_filter
        if scalable is not None:
            self.scalable = scalable
        if receivable is not None:
            self.receivable = receivable
        if allow_only_physical_grab is not None:
            self.allow_only_physical_grab = allow_only_physical_grab
        if grabber is not None:
            self.grabber = grabber
        if last_parent is not None:
            self.last_parent = last_parent
        if last_parent_is_user_space is not None:
            self.last_parent_is_user_space = last_parent_is_user_space
        if legacy_active_user_root_only is not None:
            self.legacy_active_user_root_only = legacy_active_user_root_only

    @property
    def reparent_on_release(self) -> primitives.Bool | None:
        """The slot is reparented to the value of ``_lastParent``, instead of root when dropped __TPL__"""
        member = self.get_member("ReparentOnRelease")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reparent_on_release.setter
    def reparent_on_release(self, value: primitives.Bool) -> None:
        """Set the ReparentOnRelease field value."""
        member = self.get_member("ReparentOnRelease")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ReparentOnRelease", fields.FieldBool(value=value)
            )

    @property
    def preserve_user_space(self) -> primitives.Bool | None:
        """The slot is reparented to Local User Space __TPL__"""
        member = self.get_member("PreserveUserSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @preserve_user_space.setter
    def preserve_user_space(self, value: primitives.Bool) -> None:
        """Set the PreserveUserSpace field value."""
        member = self.get_member("PreserveUserSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreserveUserSpace", fields.FieldBool(value=value)
            )

    @property
    def destroy_on_release(self) -> primitives.Bool | None:
        """The slot this component is attached to is destroyed upon release"""
        member = self.get_member("DestroyOnRelease")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @destroy_on_release.setter
    def destroy_on_release(self, value: primitives.Bool) -> None:
        """Set the DestroyOnRelease field value."""
        member = self.get_member("DestroyOnRelease")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DestroyOnRelease", fields.FieldBool(value=value)
            )

    @property
    def grab_priority(self) -> primitives.Int | None:
        """The GrabPriority field value."""
        member = self.get_member("GrabPriority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_priority.setter
    def grab_priority(self, value: primitives.Int) -> None:
        """Set the GrabPriority field value."""
        member = self.get_member("GrabPriority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabPriority", fields.FieldInt(value=value)
            )

    @property
    def grab_priority_when_grabbed(self) -> primitives.Int | None:
        """Optionally changes the grab priority of the object when it is already being grabbed. Useful for different behavior when it can be grab stolen by another player."""
        member = self.get_member("GrabPriorityWhenGrabbed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_priority_when_grabbed.setter
    def grab_priority_when_grabbed(self, value: primitives.Int) -> None:
        """Set the GrabPriorityWhenGrabbed field value."""
        member = self.get_member("GrabPriorityWhenGrabbed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabPriorityWhenGrabbed", fields.FieldNullableInt(value=value)
            )

    @property
    def edit_mode_only(self) -> primitives.Bool | None:
        """Determines if this grabbable is effective only in Edit Mode"""
        member = self.get_member("EditModeOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @edit_mode_only.setter
    def edit_mode_only(self, value: primitives.Bool) -> None:
        """Set the EditModeOnly field value."""
        member = self.get_member("EditModeOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EditModeOnly", fields.FieldBool(value=value)
            )

    @property
    def allow_steal(self) -> primitives.Bool | None:
        """Other users can grab the slot this component is attached to. Like a flag in capture the flag."""
        member = self.get_member("AllowSteal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_steal.setter
    def allow_steal(self, value: primitives.Bool) -> None:
        """Set the AllowSteal field value."""
        member = self.get_member("AllowSteal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowSteal", fields.FieldBool(value=value)
            )

    @property
    def drop_on_disable(self) -> primitives.Bool | None:
        """The parent slot will be dropped when this component is disabled."""
        member = self.get_member("DropOnDisable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @drop_on_disable.setter
    def drop_on_disable(self, value: primitives.Bool) -> None:
        """Set the DropOnDisable field value."""
        member = self.get_member("DropOnDisable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DropOnDisable", fields.FieldBool(value=value)
            )

    @property
    def active_user_filter(self) -> ActiveUserHandling | None:
        """Changes if this component can be grabbed based on who is the active user if any."""
        member = self.get_member("ActiveUserFilter")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ActiveUserHandling(member.value)
        return None

    @active_user_filter.setter
    def active_user_filter(self, value: ActiveUserHandling | str) -> None:
        """Set ActiveUserFilter. Changes if this component can be grabbed based on who is the active user if any."""
        member = self.get_member("ActiveUserFilter")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ActiveUserFilter",
                members.FieldEnum(value=str(value)),
            )

    @property
    def only_users(self) -> members.SyncList | None:
        """A list of users that are allowed to grab this slot."""
        member = self.get_member("OnlyUsers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @only_users.setter
    def only_users(self, value: members.SyncList) -> None:
        """Set OnlyUsers. A list of users that are allowed to grab this slot."""
        self.set_member("OnlyUsers", value)

    @property
    def scalable(self) -> primitives.Bool | None:
        """The Scalable field value."""
        member = self.get_member("Scalable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scalable.setter
    def scalable(self, value: primitives.Bool) -> None:
        """Set the Scalable field value."""
        member = self.get_member("Scalable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Scalable", fields.FieldBool(value=value)
            )

    @property
    def receivable(self) -> primitives.Bool | None:
        """The Receivable field value."""
        member = self.get_member("Receivable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @receivable.setter
    def receivable(self, value: primitives.Bool) -> None:
        """Set the Receivable field value."""
        member = self.get_member("Receivable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Receivable", fields.FieldBool(value=value)
            )

    @property
    def allow_only_physical_grab(self) -> primitives.Bool | None:
        """Only allow grab an object with a physical interaction - remote grabs are not allowed"""
        member = self.get_member("AllowOnlyPhysicalGrab")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_only_physical_grab.setter
    def allow_only_physical_grab(self, value: primitives.Bool) -> None:
        """Set the AllowOnlyPhysicalGrab field value."""
        member = self.get_member("AllowOnlyPhysicalGrab")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowOnlyPhysicalGrab", fields.FieldBool(value=value)
            )

    @property
    def grabber(self) -> str | None:
        """Automatically Assigned, the grabber that is grabbing this component."""
        member = self.get_member("_grabber")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @grabber.setter
    def grabber(self, target: str | Grabber | None) -> None:
        """Set the _grabber reference by target ID or Grabber instance."""
        target_id: str | None = target.id if isinstance(target, Grabber) else target  # type: ignore[assignment]
        member = self.get_member("_grabber")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_grabber",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Grabber'),
            )

    @property
    def last_parent(self) -> str | None:
        """Automatically Assigned, the last parent this slot had. Is used to parent the slot back (if allowed) when let go of."""
        member = self.get_member("_lastParent")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @last_parent.setter
    def last_parent(self, target: str | Slot | None) -> None:
        """Set the _lastParent reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_lastParent")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_lastParent",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def last_parent_is_user_space(self) -> primitives.Bool | None:
        """Automatically Assigned Whether the last parent slot is the user space slot of the user grabbing this."""
        member = self.get_member("_lastParentIsUserSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_parent_is_user_space.setter
    def last_parent_is_user_space(self, value: primitives.Bool) -> None:
        """Set the _lastParentIsUserSpace field value."""
        member = self.get_member("_lastParentIsUserSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lastParentIsUserSpace", fields.FieldBool(value=value)
            )

    @property
    def legacy_active_user_root_only(self) -> primitives.Bool | None:
        """Automatically Assigned Legacy do not use. Used to handle whether only the active user can grab. Use ``ActiveUserFilter`` instead!"""
        member = self.get_member("__legacyActiveUserRootOnly")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @legacy_active_user_root_only.setter
    def legacy_active_user_root_only(self, value: primitives.Bool) -> None:
        """Set the __legacyActiveUserRootOnly field value."""
        member = self.get_member("__legacyActiveUserRootOnly")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "__legacyActiveUserRootOnly", fields.FieldBool(value=value)
            )

    async def user_root_grab_check(self, resolink: protocols.ResoniteLinkClient, grabbable: str, grabber: str, debug: bool = False) -> dict:
        """Call the UserRootGrabCheck sync method.

        Args:
            resolink: Connected ResoniteLink client.
            grabbable: The grabbable parameter.
            grabber: The grabber parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "UserRootGrabCheck", {"grabbable": grabbable, "grabber": grabber}, debug,
        )

