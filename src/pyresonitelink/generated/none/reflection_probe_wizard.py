"""Generated component: ReflectionProbeWizard."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.float_text_editor_parser import FloatTextEditorParser
from pyresonitelink.generated._types.ideveloper_interface import IDeveloperInterface
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReflectionProbeWizard(GeneratedComponent, IDeveloperInterface, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ReflectionProbeWizard.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReflectionProbeWizard"

    def __init__(self, root: str | Slot | None = None, process_disabled: bool | None = None, teleport_user_to_probe: bool | None = None, tag: str | TextField | None = None, delay_between_probes: str | FloatTextEditorParser | None = None, bake_count: np.int32 | None = None, bake_index: np.int32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            root: Initial value for Root.
            process_disabled: Initial value for ProcessDisabled.
            teleport_user_to_probe: Initial value for TeleportUserToProbe.
            tag: Initial value for _tag.
            delay_between_probes: Initial value for _delayBetweenProbes.
            bake_count: Initial value for _bakeCount.
            bake_index: Initial value for _bakeIndex.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if root is not None:
            self.root = root
        if process_disabled is not None:
            self.process_disabled = process_disabled
        if teleport_user_to_probe is not None:
            self.teleport_user_to_probe = teleport_user_to_probe
        if tag is not None:
            self.tag = tag
        if delay_between_probes is not None:
            self.delay_between_probes = delay_between_probes
        if bake_count is not None:
            self.bake_count = bake_count
        if bake_index is not None:
            self.bake_index = bake_index

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
    def process_disabled(self) -> bool | None:
        """The ProcessDisabled field value."""
        member = self.get_member("ProcessDisabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @process_disabled.setter
    def process_disabled(self, value: bool) -> None:
        """Set the ProcessDisabled field value."""
        member = self.get_member("ProcessDisabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProcessDisabled", fields.FieldBool(value=value)
            )

    @property
    def teleport_user_to_probe(self) -> bool | None:
        """The TeleportUserToProbe field value."""
        member = self.get_member("TeleportUserToProbe")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @teleport_user_to_probe.setter
    def teleport_user_to_probe(self, value: bool) -> None:
        """Set the TeleportUserToProbe field value."""
        member = self.get_member("TeleportUserToProbe")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TeleportUserToProbe", fields.FieldBool(value=value)
            )

    @property
    def tag(self) -> str | None:
        """Target ID of the _tag reference (targets TextField)."""
        member = self.get_member("_tag")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tag.setter
    def tag(self, target: str | TextField | None) -> None:
        """Set the _tag reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_tag")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_tag",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def delay_between_probes(self) -> str | None:
        """Target ID of the _delayBetweenProbes reference (targets FloatTextEditorParser)."""
        member = self.get_member("_delayBetweenProbes")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @delay_between_probes.setter
    def delay_between_probes(self, target: str | FloatTextEditorParser | None) -> None:
        """Set the _delayBetweenProbes reference by target ID or FloatTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, FloatTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("_delayBetweenProbes")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_delayBetweenProbes",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FloatTextEditorParser'),
            )

    @property
    def bake_count(self) -> np.int32 | None:
        """The _bakeCount field value."""
        member = self.get_member("_bakeCount")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bake_count.setter
    def bake_count(self, value: np.int32) -> None:
        """Set the _bakeCount field value."""
        member = self.get_member("_bakeCount")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_bakeCount", fields.FieldInt(value=value)
            )

    @property
    def bake_index(self) -> np.int32 | None:
        """The _bakeIndex field value."""
        member = self.get_member("_bakeIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bake_index.setter
    def bake_index(self, value: np.int32) -> None:
        """Set the _bakeIndex field value."""
        member = self.get_member("_bakeIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_bakeIndex", fields.FieldInt(value=value)
            )

