"""Generated component: VisemeAnalyzer."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_audio_data_source import IWorldAudioDataSource
from pyresonitelink.generated._types.multi_value_stream import MultiValueStream
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VisemeAnalyzer(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.VisemeAnalyzer.

    Category: Media/Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VisemeAnalyzer"

    def __init__(self, source: str | IWorldAudioDataSource | None = None, remote_source: str | MultiValueStream[np.float32] | None = None, smoothing: np.float32 | None = None, silence: np.float32 | None = None, pp: np.float32 | None = None, ff: np.float32 | None = None, th: np.float32 | None = None, dd: np.float32 | None = None, kk: np.float32 | None = None, ch: np.float32 | None = None, ss: np.float32 | None = None, nn: np.float32 | None = None, rr: np.float32 | None = None, aa: np.float32 | None = None, e: np.float32 | None = None, ih: np.float32 | None = None, oh: np.float32 | None = None, ou: np.float32 | None = None, laughter_probability: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source: Initial value for Source.
            remote_source: Initial value for RemoteSource.
            smoothing: Initial value for Smoothing.
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
            laughter_probability: Initial value for LaughterProbability.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source is not None:
            self.source = source
        if remote_source is not None:
            self.remote_source = remote_source
        if smoothing is not None:
            self.smoothing = smoothing
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
        if laughter_probability is not None:
            self.laughter_probability = laughter_probability

    @property
    def source(self) -> str | None:
        """Target ID of the Source reference (targets IWorldAudioDataSource)."""
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source.setter
    def source(self, target: str | IWorldAudioDataSource | None) -> None:
        """Set the Source reference by target ID or IWorldAudioDataSource instance."""
        target_id: str | None = target.id if isinstance(target, IWorldAudioDataSource) else target  # type: ignore[assignment]
        member = self.get_member("Source")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Source",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IWorldAudioDataSource'),
            )

    @property
    def remote_source(self) -> str | None:
        """Target ID of the RemoteSource reference (targets MultiValueStream[np.float32])."""
        member = self.get_member("RemoteSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @remote_source.setter
    def remote_source(self, target: str | MultiValueStream[np.float32] | None) -> None:
        """Set the RemoteSource reference by target ID or MultiValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, MultiValueStream) else target  # type: ignore[assignment]
        member = self.get_member("RemoteSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RemoteSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MultiValueStream<float>'),
            )

    @property
    def preferred_analyzer(self) -> members.FieldEnum | None:
        """The PreferredAnalyzer member."""
        member = self.get_member("PreferredAnalyzer")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @preferred_analyzer.setter
    def preferred_analyzer(self, value: members.FieldEnum) -> None:
        """Set the PreferredAnalyzer member."""
        self.set_member("PreferredAnalyzer", value)

    @property
    def smoothing(self) -> np.float32 | None:
        """The Smoothing field value."""
        member = self.get_member("Smoothing")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smoothing.setter
    def smoothing(self, value: np.float32) -> None:
        """Set the Smoothing field value."""
        member = self.get_member("Smoothing")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Smoothing", fields.FieldFloat(value=value)
            )

    @property
    def silence(self) -> np.float32 | None:
        """The Silence field value."""
        member = self.get_member("Silence")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @silence.setter
    def silence(self, value: np.float32) -> None:
        """Set the Silence field value."""
        member = self.get_member("Silence")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Silence", fields.FieldFloat(value=value)
            )

    @property
    def pp(self) -> np.float32 | None:
        """The PP field value."""
        member = self.get_member("PP")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pp.setter
    def pp(self, value: np.float32) -> None:
        """Set the PP field value."""
        member = self.get_member("PP")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PP", fields.FieldFloat(value=value)
            )

    @property
    def ff(self) -> np.float32 | None:
        """The FF field value."""
        member = self.get_member("FF")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ff.setter
    def ff(self, value: np.float32) -> None:
        """Set the FF field value."""
        member = self.get_member("FF")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FF", fields.FieldFloat(value=value)
            )

    @property
    def th(self) -> np.float32 | None:
        """The TH field value."""
        member = self.get_member("TH")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @th.setter
    def th(self, value: np.float32) -> None:
        """Set the TH field value."""
        member = self.get_member("TH")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TH", fields.FieldFloat(value=value)
            )

    @property
    def dd(self) -> np.float32 | None:
        """The DD field value."""
        member = self.get_member("DD")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dd.setter
    def dd(self, value: np.float32) -> None:
        """Set the DD field value."""
        member = self.get_member("DD")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DD", fields.FieldFloat(value=value)
            )

    @property
    def kk(self) -> np.float32 | None:
        """The kk field value."""
        member = self.get_member("kk")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @kk.setter
    def kk(self, value: np.float32) -> None:
        """Set the kk field value."""
        member = self.get_member("kk")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "kk", fields.FieldFloat(value=value)
            )

    @property
    def ch(self) -> np.float32 | None:
        """The CH field value."""
        member = self.get_member("CH")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ch.setter
    def ch(self, value: np.float32) -> None:
        """Set the CH field value."""
        member = self.get_member("CH")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CH", fields.FieldFloat(value=value)
            )

    @property
    def ss(self) -> np.float32 | None:
        """The SS field value."""
        member = self.get_member("SS")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ss.setter
    def ss(self, value: np.float32) -> None:
        """Set the SS field value."""
        member = self.get_member("SS")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SS", fields.FieldFloat(value=value)
            )

    @property
    def nn(self) -> np.float32 | None:
        """The nn field value."""
        member = self.get_member("nn")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @nn.setter
    def nn(self, value: np.float32) -> None:
        """Set the nn field value."""
        member = self.get_member("nn")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "nn", fields.FieldFloat(value=value)
            )

    @property
    def rr(self) -> np.float32 | None:
        """The RR field value."""
        member = self.get_member("RR")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rr.setter
    def rr(self, value: np.float32) -> None:
        """Set the RR field value."""
        member = self.get_member("RR")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RR", fields.FieldFloat(value=value)
            )

    @property
    def aa(self) -> np.float32 | None:
        """The aa field value."""
        member = self.get_member("aa")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @aa.setter
    def aa(self, value: np.float32) -> None:
        """Set the aa field value."""
        member = self.get_member("aa")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "aa", fields.FieldFloat(value=value)
            )

    @property
    def e(self) -> np.float32 | None:
        """The E field value."""
        member = self.get_member("E")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @e.setter
    def e(self, value: np.float32) -> None:
        """Set the E field value."""
        member = self.get_member("E")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "E", fields.FieldFloat(value=value)
            )

    @property
    def ih(self) -> np.float32 | None:
        """The ih field value."""
        member = self.get_member("ih")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ih.setter
    def ih(self, value: np.float32) -> None:
        """Set the ih field value."""
        member = self.get_member("ih")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ih", fields.FieldFloat(value=value)
            )

    @property
    def oh(self) -> np.float32 | None:
        """The oh field value."""
        member = self.get_member("oh")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @oh.setter
    def oh(self, value: np.float32) -> None:
        """Set the oh field value."""
        member = self.get_member("oh")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "oh", fields.FieldFloat(value=value)
            )

    @property
    def ou(self) -> np.float32 | None:
        """The ou field value."""
        member = self.get_member("ou")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ou.setter
    def ou(self, value: np.float32) -> None:
        """Set the ou field value."""
        member = self.get_member("ou")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ou", fields.FieldFloat(value=value)
            )

    @property
    def laughter_probability(self) -> np.float32 | None:
        """The LaughterProbability field value."""
        member = self.get_member("LaughterProbability")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @laughter_probability.setter
    def laughter_probability(self, value: np.float32) -> None:
        """Set the LaughterProbability field value."""
        member = self.get_member("LaughterProbability")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LaughterProbability", fields.FieldFloat(value=value)
            )

