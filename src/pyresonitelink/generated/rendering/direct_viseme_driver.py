"""Generated component: DirectVisemeDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.viseme_analyzer import VisemeAnalyzer
from pyresonitelink.generated._types.imouth_tracking_source_component import IMouthTrackingSourceComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DirectVisemeDriver(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DirectVisemeDriver.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DirectVisemeDriver"

    def __init__(self, source: str | VisemeAnalyzer | None = None, mouth_tracking_source: str | IMouthTrackingSourceComponent | None = None, strength_multiplier: primitives.Float | None = None, voice_mouth_supress_weight: primitives.Float | None = None, laugh_threshold: primitives.Float | None = None, laugh_begin_speed: primitives.Float | None = None, laugh_end_speed: primitives.Float | None = None, silence: str | IField[primitives.Float] | None = None, pp: str | IField[primitives.Float] | None = None, ff: str | IField[primitives.Float] | None = None, th: str | IField[primitives.Float] | None = None, dd: str | IField[primitives.Float] | None = None, kk: str | IField[primitives.Float] | None = None, ch: str | IField[primitives.Float] | None = None, ss: str | IField[primitives.Float] | None = None, nn: str | IField[primitives.Float] | None = None, rr: str | IField[primitives.Float] | None = None, aa: str | IField[primitives.Float] | None = None, e: str | IField[primitives.Float] | None = None, ih: str | IField[primitives.Float] | None = None, oh: str | IField[primitives.Float] | None = None, ou: str | IField[primitives.Float] | None = None, laugh: str | IField[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            mouth_tracking_source: Initial value for MouthTrackingSource.
            strength_multiplier: Initial value for StrengthMultiplier.
            voice_mouth_supress_weight: Initial value for VoiceMouthSupressWeight.
            laugh_threshold: Initial value for LaughThreshold.
            laugh_begin_speed: Initial value for LaughBeginSpeed.
            laugh_end_speed: Initial value for LaughEndSpeed.
            silence: Initial value for Silence.
            pp: Initial value for PP.
            ff: Initial value for FF.
            th: Initial value for TH.
            dd: Initial value for DD.
            kk: Initial value for kk.
            ch: Initial value for CH.
            ss: Initial value for SS.
            nn: Initial value for nn.
            rr: Initial value for RR.
            aa: Initial value for aa.
            e: Initial value for E.
            ih: Initial value for ih.
            oh: Initial value for oh.
            ou: Initial value for ou.
            laugh: Initial value for Laugh.
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
        if laugh_threshold is not None:
            self.laugh_threshold = laugh_threshold
        if laugh_begin_speed is not None:
            self.laugh_begin_speed = laugh_begin_speed
        if laugh_end_speed is not None:
            self.laugh_end_speed = laugh_end_speed
        if silence is not None:
            self.silence = silence
        if pp is not None:
            self.pp = pp
        if ff is not None:
            self.ff = ff
        if th is not None:
            self.th = th
        if dd is not None:
            self.dd = dd
        if kk is not None:
            self.kk = kk
        if ch is not None:
            self.ch = ch
        if ss is not None:
            self.ss = ss
        if nn is not None:
            self.nn = nn
        if rr is not None:
            self.rr = rr
        if aa is not None:
            self.aa = aa
        if e is not None:
            self.e = e
        if ih is not None:
            self.ih = ih
        if oh is not None:
            self.oh = oh
        if ou is not None:
            self.ou = ou
        if laugh is not None:
            self.laugh = laugh

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
    def strength_multiplier(self) -> primitives.Float | None:
        """The StrengthMultiplier field value."""
        member = self.get_member("StrengthMultiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @strength_multiplier.setter
    def strength_multiplier(self, value: primitives.Float) -> None:
        """Set the StrengthMultiplier field value."""
        member = self.get_member("StrengthMultiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StrengthMultiplier", fields.FieldFloat(value=value)
            )

    @property
    def voice_mouth_supress_weight(self) -> primitives.Float | None:
        """The VoiceMouthSupressWeight field value."""
        member = self.get_member("VoiceMouthSupressWeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @voice_mouth_supress_weight.setter
    def voice_mouth_supress_weight(self, value: primitives.Float) -> None:
        """Set the VoiceMouthSupressWeight field value."""
        member = self.get_member("VoiceMouthSupressWeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VoiceMouthSupressWeight", fields.FieldFloat(value=value)
            )

    @property
    def laugh_threshold(self) -> primitives.Float | None:
        """The LaughThreshold field value."""
        member = self.get_member("LaughThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @laugh_threshold.setter
    def laugh_threshold(self, value: primitives.Float) -> None:
        """Set the LaughThreshold field value."""
        member = self.get_member("LaughThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LaughThreshold", fields.FieldFloat(value=value)
            )

    @property
    def laugh_begin_speed(self) -> primitives.Float | None:
        """The LaughBeginSpeed field value."""
        member = self.get_member("LaughBeginSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @laugh_begin_speed.setter
    def laugh_begin_speed(self, value: primitives.Float) -> None:
        """Set the LaughBeginSpeed field value."""
        member = self.get_member("LaughBeginSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LaughBeginSpeed", fields.FieldFloat(value=value)
            )

    @property
    def laugh_end_speed(self) -> primitives.Float | None:
        """The LaughEndSpeed field value."""
        member = self.get_member("LaughEndSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @laugh_end_speed.setter
    def laugh_end_speed(self, value: primitives.Float) -> None:
        """Set the LaughEndSpeed field value."""
        member = self.get_member("LaughEndSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LaughEndSpeed", fields.FieldFloat(value=value)
            )

    @property
    def silence(self) -> str | None:
        """Target ID of the Silence reference (targets IField[primitives.Float])."""
        member = self.get_member("Silence")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @silence.setter
    def silence(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the Silence reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Silence")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Silence",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def pp(self) -> str | None:
        """Target ID of the PP reference (targets IField[primitives.Float])."""
        member = self.get_member("PP")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pp.setter
    def pp(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the PP reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("PP")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PP",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def ff(self) -> str | None:
        """Target ID of the FF reference (targets IField[primitives.Float])."""
        member = self.get_member("FF")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ff.setter
    def ff(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the FF reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("FF")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FF",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def th(self) -> str | None:
        """Target ID of the TH reference (targets IField[primitives.Float])."""
        member = self.get_member("TH")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @th.setter
    def th(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the TH reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("TH")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TH",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def dd(self) -> str | None:
        """Target ID of the DD reference (targets IField[primitives.Float])."""
        member = self.get_member("DD")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dd.setter
    def dd(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the DD reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("DD")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DD",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def kk(self) -> str | None:
        """Target ID of the kk reference (targets IField[primitives.Float])."""
        member = self.get_member("kk")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @kk.setter
    def kk(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the kk reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("kk")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "kk",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def ch(self) -> str | None:
        """Target ID of the CH reference (targets IField[primitives.Float])."""
        member = self.get_member("CH")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ch.setter
    def ch(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the CH reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("CH")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CH",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def ss(self) -> str | None:
        """Target ID of the SS reference (targets IField[primitives.Float])."""
        member = self.get_member("SS")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ss.setter
    def ss(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the SS reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SS")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SS",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def nn(self) -> str | None:
        """Target ID of the nn reference (targets IField[primitives.Float])."""
        member = self.get_member("nn")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @nn.setter
    def nn(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the nn reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("nn")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "nn",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def rr(self) -> str | None:
        """Target ID of the RR reference (targets IField[primitives.Float])."""
        member = self.get_member("RR")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rr.setter
    def rr(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the RR reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("RR")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RR",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def aa(self) -> str | None:
        """Target ID of the aa reference (targets IField[primitives.Float])."""
        member = self.get_member("aa")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @aa.setter
    def aa(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the aa reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("aa")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "aa",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def e(self) -> str | None:
        """Target ID of the E reference (targets IField[primitives.Float])."""
        member = self.get_member("E")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @e.setter
    def e(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the E reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("E")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "E",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def ih(self) -> str | None:
        """Target ID of the ih reference (targets IField[primitives.Float])."""
        member = self.get_member("ih")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ih.setter
    def ih(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the ih reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ih")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ih",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def oh(self) -> str | None:
        """Target ID of the oh reference (targets IField[primitives.Float])."""
        member = self.get_member("oh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @oh.setter
    def oh(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the oh reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("oh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "oh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def ou(self) -> str | None:
        """Target ID of the ou reference (targets IField[primitives.Float])."""
        member = self.get_member("ou")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ou.setter
    def ou(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the ou reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("ou")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ou",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def laugh(self) -> str | None:
        """Target ID of the Laugh reference (targets IField[primitives.Float])."""
        member = self.get_member("Laugh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @laugh.setter
    def laugh(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the Laugh reference by target ID or IField[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Laugh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Laugh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

