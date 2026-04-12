"""Generated component: ParticleSpray."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.interaction_handler import InteractionHandler
from pyresonitelink.generated._types.particle_style import ParticleStyle
from pyresonitelink.generated._types.speed_range_initializer import SpeedRangeInitializer
from pyresonitelink.generated._types.particle_emitter import ParticleEmitter
from pyresonitelink.generated._types.itool import ITool
from pyresonitelink.generated._types.imaterial_apply_policy import IMaterialApplyPolicy
from pyresonitelink.generated._types.itouchable import ITouchable
from pyresonitelink.generated._types.iitem_metadata_source import IItemMetadataSource
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParticleSpray(GeneratedComponent, ITool, IMaterialApplyPolicy, ITouchable, IItemMetadataSource, IWorldEventReceiver):
    """The ParticleSpray component is a tool that shoots particles when the trigger is pulled.

    Category: Tools
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ParticleSpray"

    def __init__(self, tip_reference: str | Slot | None = None, block_grip_equip: primitives.Bool | None = None, block_remote_equip: primitives.Bool | None = None, equip_name: primitives.String | None = None, override_active_tool: str | InteractionHandler | None = None, grip_poses_generated: primitives.Bool | None = None, rate: primitives.Float | None = None, rate_exp: primitives.Float | None = None, min_speed: primitives.Float | None = None, max_speed: primitives.Float | None = None, part_style: str | ParticleStyle | None = None, part_speed: str | SpeedRangeInitializer | None = None, part_emitter: str | ParticleEmitter | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            tip_reference: Initial value for TipReference.
            block_grip_equip: Initial value for BlockGripEquip.
            block_remote_equip: Initial value for BlockRemoteEquip.
            equip_name: Initial value for EquipName.
            override_active_tool: Initial value for _overrideActiveTool.
            grip_poses_generated: Initial value for _gripPosesGenerated.
            rate: Initial value for Rate.
            rate_exp: Initial value for RateExp.
            min_speed: Initial value for MinSpeed.
            max_speed: Initial value for MaxSpeed.
            part_style: Initial value for partStyle.
            part_speed: Initial value for partSpeed.
            part_emitter: Initial value for partEmitter.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if tip_reference is not None:
            self.tip_reference = tip_reference
        if block_grip_equip is not None:
            self.block_grip_equip = block_grip_equip
        if block_remote_equip is not None:
            self.block_remote_equip = block_remote_equip
        if equip_name is not None:
            self.equip_name = equip_name
        if override_active_tool is not None:
            self.override_active_tool = override_active_tool
        if grip_poses_generated is not None:
            self.grip_poses_generated = grip_poses_generated
        if rate is not None:
            self.rate = rate
        if rate_exp is not None:
            self.rate_exp = rate_exp
        if min_speed is not None:
            self.min_speed = min_speed
        if max_speed is not None:
            self.max_speed = max_speed
        if part_style is not None:
            self.part_style = part_style
        if part_speed is not None:
            self.part_speed = part_speed
        if part_emitter is not None:
            self.part_emitter = part_emitter

    @property
    def equip_link(self) -> members.EmptyElement | None:
        """The _equipLink member."""
        member = self.get_member("_equipLink")
        if isinstance(member, members.EmptyElement):
            return member
        return None

    @equip_link.setter
    def equip_link(self, value: members.EmptyElement) -> None:
        """Set the _equipLink member."""
        self.set_member("_equipLink", value)

    @property
    def tip_reference(self) -> str | None:
        """Target ID of the TipReference reference (targets Slot)."""
        member = self.get_member("TipReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tip_reference.setter
    def tip_reference(self, target: str | Slot | None) -> None:
        """Set the TipReference reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("TipReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TipReference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def block_grip_equip(self) -> primitives.Bool | None:
        """The BlockGripEquip field value."""
        member = self.get_member("BlockGripEquip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @block_grip_equip.setter
    def block_grip_equip(self, value: primitives.Bool) -> None:
        """Set the BlockGripEquip field value."""
        member = self.get_member("BlockGripEquip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlockGripEquip", fields.FieldBool(value=value)
            )

    @property
    def block_remote_equip(self) -> primitives.Bool | None:
        """The BlockRemoteEquip field value."""
        member = self.get_member("BlockRemoteEquip")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @block_remote_equip.setter
    def block_remote_equip(self, value: primitives.Bool) -> None:
        """Set the BlockRemoteEquip field value."""
        member = self.get_member("BlockRemoteEquip")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlockRemoteEquip", fields.FieldBool(value=value)
            )

    @property
    def equip_name(self) -> primitives.String | None:
        """The EquipName field value."""
        member = self.get_member("EquipName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @equip_name.setter
    def equip_name(self, value: primitives.String) -> None:
        """Set the EquipName field value."""
        member = self.get_member("EquipName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "EquipName", fields.FieldString(value=value)
            )

    @property
    def override_active_tool(self) -> str | None:
        """Target ID of the _overrideActiveTool reference (targets InteractionHandler)."""
        member = self.get_member("_overrideActiveTool")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @override_active_tool.setter
    def override_active_tool(self, target: str | InteractionHandler | None) -> None:
        """Set the _overrideActiveTool reference by target ID or InteractionHandler instance."""
        target_id: str | None = target.id if isinstance(target, InteractionHandler) else target  # type: ignore[assignment]
        member = self.get_member("_overrideActiveTool")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_overrideActiveTool",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.InteractionHandler'),
            )

    @property
    def grip_poses_generated(self) -> primitives.Bool | None:
        """The _gripPosesGenerated field value."""
        member = self.get_member("_gripPosesGenerated")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grip_poses_generated.setter
    def grip_poses_generated(self, value: primitives.Bool) -> None:
        """Set the _gripPosesGenerated field value."""
        member = self.get_member("_gripPosesGenerated")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_gripPosesGenerated", fields.FieldBool(value=value)
            )

    @property
    def rate(self) -> primitives.Float | None:
        """Ths rate at which the spray tip sprays at max (primary strength is raised to ``RateExp`` first before multiplying with this)"""
        member = self.get_member("Rate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rate.setter
    def rate(self, value: primitives.Float) -> None:
        """Set the Rate field value."""
        member = self.get_member("Rate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Rate", fields.FieldFloat(value=value)
            )

    @property
    def rate_exp(self) -> primitives.Float | None:
        """primary strength of the tool is raised to this number."""
        member = self.get_member("RateExp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rate_exp.setter
    def rate_exp(self, value: primitives.Float) -> None:
        """Set the RateExp field value."""
        member = self.get_member("RateExp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RateExp", fields.FieldFloat(value=value)
            )

    @property
    def min_speed(self) -> primitives.Float | None:
        """The min speed the particles travel at."""
        member = self.get_member("MinSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @min_speed.setter
    def min_speed(self, value: primitives.Float) -> None:
        """Set the MinSpeed field value."""
        member = self.get_member("MinSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinSpeed", fields.FieldFloat(value=value)
            )

    @property
    def max_speed(self) -> primitives.Float | None:
        """The max speed the particles travel at."""
        member = self.get_member("MaxSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_speed.setter
    def max_speed(self, value: primitives.Float) -> None:
        """Set the MaxSpeed field value."""
        member = self.get_member("MaxSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSpeed", fields.FieldFloat(value=value)
            )

    @property
    def part_style(self) -> str | None:
        """The style of the particles."""
        member = self.get_member("partStyle")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @part_style.setter
    def part_style(self, target: str | ParticleStyle | None) -> None:
        """Set the partStyle reference by target ID or ParticleStyle instance."""
        target_id: str | None = target.id if isinstance(target, ParticleStyle) else target  # type: ignore[assignment]
        member = self.get_member("partStyle")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "partStyle",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PhotonDust.ParticleStyle'),
            )

    @property
    def part_speed(self) -> str | None:
        """The min/max speed the particles travel at, is synced with ``MinSpeed`` and ``MaxSpeed``"""
        member = self.get_member("partSpeed")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @part_speed.setter
    def part_speed(self, target: str | SpeedRangeInitializer | None) -> None:
        """Set the partSpeed reference by target ID or SpeedRangeInitializer instance."""
        target_id: str | None = target.id if isinstance(target, SpeedRangeInitializer) else target  # type: ignore[assignment]
        member = self.get_member("partSpeed")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "partSpeed",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PhotonDust.SpeedRangeInitializer'),
            )

    @property
    def part_emitter(self) -> str | None:
        """the Particle emitter this particle spray is controlling."""
        member = self.get_member("partEmitter")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @part_emitter.setter
    def part_emitter(self, target: str | ParticleEmitter | None) -> None:
        """Set the partEmitter reference by target ID or ParticleEmitter instance."""
        target_id: str | None = target.id if isinstance(target, ParticleEmitter) else target  # type: ignore[assignment]
        member = self.get_member("partEmitter")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "partEmitter",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PhotonDust.ParticleEmitter'),
            )

