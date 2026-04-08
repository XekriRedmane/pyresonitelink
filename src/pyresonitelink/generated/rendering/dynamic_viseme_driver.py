"""Generated component: DynamicVisemeDriver."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.viseme_analyzer import VisemeAnalyzer
from pyresonitelink.generated._types.imouth_tracking_source_component import IMouthTrackingSourceComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicVisemeDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DynamicVisemeDriver.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicVisemeDriver"

    def __init__(self, source: str | VisemeAnalyzer | None = None, mouth_tracking_source: str | IMouthTrackingSourceComponent | None = None, strength_multiplier: np.float32 | None = None, voice_mouth_supress_weight: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            mouth_tracking_source: Initial value for MouthTrackingSource.
            strength_multiplier: Initial value for StrengthMultiplier.
            voice_mouth_supress_weight: Initial value for VoiceMouthSupressWeight.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if mouth_tracking_source is not None:
            self.mouth_tracking_source = mouth_tracking_source
        if strength_multiplier is not None:
            self.strength_multiplier = strength_multiplier
        if voice_mouth_supress_weight is not None:
            self.voice_mouth_supress_weight = voice_mouth_supress_weight

    @property
    def source(self) -> str | None:
        """Target ID of the Source reference (targets VisemeAnalyzer)."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | VisemeAnalyzer | None) -> None:
        """Set the Source reference by target ID or VisemeAnalyzer instance."""
        target_id: str | None = target.id if isinstance(target, VisemeAnalyzer) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.VisemeAnalyzer'),
            )

    @property
    def mouth_tracking_source(self) -> str | None:
        """Target ID of the MouthTrackingSource reference (targets IMouthTrackingSourceComponent)."""
        member = self.get_member("MouthTrackingSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mouth_tracking_source.setter
    def mouth_tracking_source(self, target: str | IMouthTrackingSourceComponent | None) -> None:
        """Set the MouthTrackingSource reference by target ID or IMouthTrackingSourceComponent instance."""
        target_id: str | None = target.id if isinstance(target, IMouthTrackingSourceComponent) else target  # type: ignore[assignment]
        member = self.get_member("MouthTrackingSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MouthTrackingSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IMouthTrackingSourceComponent'),
            )

    @property
    def strength_multiplier(self) -> np.float32 | None:
        """The StrengthMultiplier field value."""
        member = self.get_member("StrengthMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @strength_multiplier.setter
    def strength_multiplier(self, value: np.float32) -> None:
        """Set the StrengthMultiplier field value."""
        member = self.get_member("StrengthMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StrengthMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def voice_mouth_supress_weight(self) -> np.float32 | None:
        """The VoiceMouthSupressWeight field value."""
        member = self.get_member("VoiceMouthSupressWeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @voice_mouth_supress_weight.setter
    def voice_mouth_supress_weight(self, value: np.float32) -> None:
        """Set the VoiceMouthSupressWeight field value."""
        member = self.get_member("VoiceMouthSupressWeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VoiceMouthSupressWeight", fields.FieldFloat(value=value)
            )

    @property
    def drivers(self) -> members.SyncList | None:
        """The Drivers member."""
        member = self.get_member("Drivers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @drivers.setter
    def drivers(self, value: members.SyncList) -> None:
        """Set the Drivers member."""
        self.set_member("Drivers", value)

