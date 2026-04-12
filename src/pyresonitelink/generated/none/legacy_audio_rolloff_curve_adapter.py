"""Generated component: LegacyAudioRolloffCurveAdapter."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.nullable import Nullable
from pyresonitelink.generated._types.audio_rolloff_curve import AudioRolloffCurve
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyAudioRolloffCurveAdapter(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The Legacy Audio Rolloff Curve Adapter component is used to convert driven values from the old audio system to Awwdio.

    used in legacy content only.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyAudioRolloffCurveAdapter"

    def __init__(self, target: str | IField[Nullable[AudioRolloffCurve]] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target

    @property
    def target(self) -> str | None:
        """The field to drive with the value converted."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[Nullable[AudioRolloffCurve]] | None) -> None:
        """Set the Target reference by target ID or IField[Nullable[AudioRolloffCurve]] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<Nullable<[Awwdio]Awwdio.AudioRolloffCurve>>'),
            )

    @property
    def value(self) -> members.FieldEnum | None:
        """The field being driven by a system using the legacy audio curve settings from before Awwdio."""
        member = self.get_member("Value")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @value.setter
    def value(self, value: members.FieldEnum) -> None:
        """Set Value. The field being driven by a system using the legacy audio curve settings from before Awwdio."""
        self.set_member("Value", value)

