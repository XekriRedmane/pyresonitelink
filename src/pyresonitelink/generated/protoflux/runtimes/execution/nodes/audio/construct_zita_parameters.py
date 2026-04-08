"""Generated component: ConstructZitaParameters."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.inode_value_output import INodeValueOutput
from pyresonitelink.generated._types.iexecution_node import IExecutionNode
from pyresonitelink.generated._types.inode import INode
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ConstructZitaParameters(GeneratedComponent, INodeValueOutput, IExecutionNode, INode, ICustomInspector, IObjectRoot, IWorldEventReceiver):
    """Wrapper for [ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Audio.ConstructZitaParameters.

    Category: ProtoFlux/Runtimes/Execution/Nodes/Audio
    """

    COMPONENT_TYPE = "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.FrooxEngine.Audio.ConstructZitaParameters"

    def __init__(self, in_delay: str | INodeValueOutput[primitives.Float] | None = None, crossover: str | INodeValueOutput[primitives.Float] | None = None, rt60_low: str | INodeValueOutput[primitives.Float] | None = None, rt60_mid: str | INodeValueOutput[primitives.Float] | None = None, high_frequency_damping: str | INodeValueOutput[primitives.Float] | None = None, eq1_frequency: str | INodeValueOutput[primitives.Float] | None = None, eq1_level: str | INodeValueOutput[primitives.Float] | None = None, eq2_frequency: str | INodeValueOutput[primitives.Float] | None = None, eq2_level: str | INodeValueOutput[primitives.Float] | None = None, mix: str | INodeValueOutput[primitives.Float] | None = None, level: str | INodeValueOutput[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            in_delay: Initial value for InDelay.
            crossover: Initial value for Crossover.
            rt60_low: Initial value for RT60Low.
            rt60_mid: Initial value for RT60Mid.
            high_frequency_damping: Initial value for HighFrequencyDamping.
            eq1_frequency: Initial value for EQ1Frequency.
            eq1_level: Initial value for EQ1Level.
            eq2_frequency: Initial value for EQ2Frequency.
            eq2_level: Initial value for EQ2Level.
            mix: Initial value for Mix.
            level: Initial value for Level.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if in_delay is not None:
            self.in_delay = in_delay
        if crossover is not None:
            self.crossover = crossover
        if rt60_low is not None:
            self.rt60_low = rt60_low
        if rt60_mid is not None:
            self.rt60_mid = rt60_mid
        if high_frequency_damping is not None:
            self.high_frequency_damping = high_frequency_damping
        if eq1_frequency is not None:
            self.eq1_frequency = eq1_frequency
        if eq1_level is not None:
            self.eq1_level = eq1_level
        if eq2_frequency is not None:
            self.eq2_frequency = eq2_frequency
        if eq2_level is not None:
            self.eq2_level = eq2_level
        if mix is not None:
            self.mix = mix
        if level is not None:
            self.level = level

    @property
    def in_delay(self) -> str | None:
        """Target ID of the InDelay reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("InDelay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @in_delay.setter
    def in_delay(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the InDelay reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("InDelay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "InDelay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def crossover(self) -> str | None:
        """Target ID of the Crossover reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Crossover")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @crossover.setter
    def crossover(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Crossover reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Crossover")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Crossover",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def rt60_low(self) -> str | None:
        """Target ID of the RT60Low reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("RT60Low")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rt60_low.setter
    def rt60_low(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the RT60Low reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("RT60Low")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RT60Low",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def rt60_mid(self) -> str | None:
        """Target ID of the RT60Mid reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("RT60Mid")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rt60_mid.setter
    def rt60_mid(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the RT60Mid reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("RT60Mid")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RT60Mid",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def high_frequency_damping(self) -> str | None:
        """Target ID of the HighFrequencyDamping reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("HighFrequencyDamping")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @high_frequency_damping.setter
    def high_frequency_damping(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the HighFrequencyDamping reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("HighFrequencyDamping")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "HighFrequencyDamping",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def eq1_frequency(self) -> str | None:
        """Target ID of the EQ1Frequency reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("EQ1Frequency")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @eq1_frequency.setter
    def eq1_frequency(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the EQ1Frequency reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("EQ1Frequency")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EQ1Frequency",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def eq1_level(self) -> str | None:
        """Target ID of the EQ1Level reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("EQ1Level")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @eq1_level.setter
    def eq1_level(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the EQ1Level reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("EQ1Level")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EQ1Level",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def eq2_frequency(self) -> str | None:
        """Target ID of the EQ2Frequency reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("EQ2Frequency")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @eq2_frequency.setter
    def eq2_frequency(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the EQ2Frequency reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("EQ2Frequency")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EQ2Frequency",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def eq2_level(self) -> str | None:
        """Target ID of the EQ2Level reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("EQ2Level")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @eq2_level.setter
    def eq2_level(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the EQ2Level reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("EQ2Level")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "EQ2Level",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def mix(self) -> str | None:
        """Target ID of the Mix reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Mix")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mix.setter
    def mix(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Mix reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Mix")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Mix",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

    @property
    def level(self) -> str | None:
        """Target ID of the Level reference (targets INodeValueOutput[primitives.Float])."""
        member = self.get_member("Level")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @level.setter
    def level(self, target: str | INodeValueOutput[primitives.Float] | None) -> None:
        """Set the Level reference by target ID or INodeValueOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, INodeValueOutput) else target  # type: ignore[assignment]
        member = self.get_member("Level")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Level",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<float>'),
            )

