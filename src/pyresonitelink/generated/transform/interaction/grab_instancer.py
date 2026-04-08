"""Generated component: GrabInstancer."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.igrabbable import IGrabbable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabInstancer(GeneratedComponent, IGrabbable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GrabInstancer.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabInstancer"

    def __init__(self, template: str | Slot | None = None, container_template: str | Slot | None = None, container_template_instance_root: str | Slot | None = None, activate_root: bool | None = None, enable_grabbable: bool | None = None, set_instance_persistent: bool | None = None, physical: bool | None = None, grab_priority: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            template: Initial value for Template.
            container_template: Initial value for ContainerTemplate.
            container_template_instance_root: Initial value for ContainerTemplateInstanceRoot.
            activate_root: Initial value for ActivateRoot.
            enable_grabbable: Initial value for EnableGrabbable.
            set_instance_persistent: Initial value for SetInstancePersistent.
            physical: Initial value for Physical.
            grab_priority: Initial value for GrabPriority.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if template is not None:
            self.template = template
        if container_template is not None:
            self.container_template = container_template
        if container_template_instance_root is not None:
            self.container_template_instance_root = container_template_instance_root
        if activate_root is not None:
            self.activate_root = activate_root
        if enable_grabbable is not None:
            self.enable_grabbable = enable_grabbable
        if set_instance_persistent is not None:
            self.set_instance_persistent = set_instance_persistent
        if physical is not None:
            self.physical = physical
        if grab_priority is not None:
            self.grab_priority = grab_priority

    @property
    def template(self) -> str | None:
        """Target ID of the Template reference (targets Slot)."""
        member = self.get_member("Template")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @template.setter
    def template(self, target: str | Slot | None) -> None:
        """Set the Template reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Template")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Template",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def container_template(self) -> str | None:
        """Target ID of the ContainerTemplate reference (targets Slot)."""
        member = self.get_member("ContainerTemplate")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @container_template.setter
    def container_template(self, target: str | Slot | None) -> None:
        """Set the ContainerTemplate reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ContainerTemplate")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ContainerTemplate",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def container_template_instance_root(self) -> str | None:
        """Target ID of the ContainerTemplateInstanceRoot reference (targets Slot)."""
        member = self.get_member("ContainerTemplateInstanceRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @container_template_instance_root.setter
    def container_template_instance_root(self, target: str | Slot | None) -> None:
        """Set the ContainerTemplateInstanceRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("ContainerTemplateInstanceRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ContainerTemplateInstanceRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def activate_root(self) -> bool | None:
        """The ActivateRoot field value."""
        member = self.get_member("ActivateRoot")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @activate_root.setter
    def activate_root(self, value: bool) -> None:
        """Set the ActivateRoot field value."""
        member = self.get_member("ActivateRoot")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActivateRoot", fields.FieldBool(value=value)
            )

    @property
    def enable_grabbable(self) -> bool | None:
        """The EnableGrabbable field value."""
        member = self.get_member("EnableGrabbable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @enable_grabbable.setter
    def enable_grabbable(self, value: bool) -> None:
        """Set the EnableGrabbable field value."""
        member = self.get_member("EnableGrabbable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EnableGrabbable", fields.FieldBool(value=value)
            )

    @property
    def set_instance_persistent(self) -> bool | None:
        """The SetInstancePersistent field value."""
        member = self.get_member("SetInstancePersistent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @set_instance_persistent.setter
    def set_instance_persistent(self, value: bool) -> None:
        """Set the SetInstancePersistent field value."""
        member = self.get_member("SetInstancePersistent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SetInstancePersistent", fields.FieldNullableBool(value=value)
            )

    @property
    def excluded_parts(self) -> members.SyncList | None:
        """The ExcludedParts member."""
        member = self.get_member("ExcludedParts")
        if isinstance(member, members.SyncList):
            return member
        return None

    @excluded_parts.setter
    def excluded_parts(self, value: members.SyncList) -> None:
        """Set the ExcludedParts member."""
        self.set_member("ExcludedParts", value)

    @property
    def physical(self) -> bool | None:
        """The Physical field value."""
        member = self.get_member("Physical")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @physical.setter
    def physical(self, value: bool) -> None:
        """Set the Physical field value."""
        member = self.get_member("Physical")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Physical", fields.FieldBool(value=value)
            )

    @property
    def grab_priority(self) -> np.int32 | None:
        """The GrabPriority field value."""
        member = self.get_member("GrabPriority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grab_priority.setter
    def grab_priority(self, value: np.int32) -> None:
        """Set the GrabPriority field value."""
        member = self.get_member("GrabPriority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "GrabPriority", fields.FieldInt(value=value)
            )

