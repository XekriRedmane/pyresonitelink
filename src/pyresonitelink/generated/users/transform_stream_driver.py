"""Generated component: TransformStreamDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.value_stream import ValueStream
from pyresonitelink.generated._types.reference_stream import ReferenceStream
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TransformStreamDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TransformStreamDriver.

    Category: Users
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TransformStreamDriver"

    def __init__(self, position_stream: str | ValueStream[primitives.Float3] | None = None, rotation_stream: str | ValueStream[primitives.FloatQ] | None = None, scale_stream: str | ValueStream[primitives.Float3] | None = None, root_space_stream: str | ReferenceStream[Slot] | None = None, position: str | IField[primitives.Float3] | None = None, rotation: str | IField[primitives.FloatQ] | None = None, scale: str | IField[primitives.Float3] | None = None, allow_offsets: bool | None = None, reset_streams_on_destroy: bool | None = None, position_offset: primitives.Float3 | None = None, rotation_offset: primitives.FloatQ | None = None, scale_offset: primitives.Float3 | None = None, run_before_physics: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            position_stream: Initial value for PositionStream.
            rotation_stream: Initial value for RotationStream.
            scale_stream: Initial value for ScaleStream.
            root_space_stream: Initial value for RootSpaceStream.
            position: Initial value for Position.
            rotation: Initial value for Rotation.
            scale: Initial value for Scale.
            allow_offsets: Initial value for AllowOffsets.
            reset_streams_on_destroy: Initial value for ResetStreamsOnDestroy.
            position_offset: Initial value for PositionOffset.
            rotation_offset: Initial value for RotationOffset.
            scale_offset: Initial value for ScaleOffset.
            run_before_physics: Initial value for RunBeforePhysics.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if position_stream is not None:
            self.position_stream = position_stream
        if rotation_stream is not None:
            self.rotation_stream = rotation_stream
        if scale_stream is not None:
            self.scale_stream = scale_stream
        if root_space_stream is not None:
            self.root_space_stream = root_space_stream
        if position is not None:
            self.position = position
        if rotation is not None:
            self.rotation = rotation
        if scale is not None:
            self.scale = scale
        if allow_offsets is not None:
            self.allow_offsets = allow_offsets
        if reset_streams_on_destroy is not None:
            self.reset_streams_on_destroy = reset_streams_on_destroy
        if position_offset is not None:
            self.position_offset = position_offset
        if rotation_offset is not None:
            self.rotation_offset = rotation_offset
        if scale_offset is not None:
            self.scale_offset = scale_offset
        if run_before_physics is not None:
            self.run_before_physics = run_before_physics

    @property
    def position_stream(self) -> str | None:
        """Target ID of the PositionStream reference (targets ValueStream[primitives.Float3])."""
        member = self.get_member("PositionStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position_stream.setter
    def position_stream(self, target: str | ValueStream[primitives.Float3] | None) -> None:
        """Set the PositionStream reference by target ID or ValueStream[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("PositionStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PositionStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float3>'),
            )

    @property
    def rotation_stream(self) -> str | None:
        """Target ID of the RotationStream reference (targets ValueStream[primitives.FloatQ])."""
        member = self.get_member("RotationStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation_stream.setter
    def rotation_stream(self, target: str | ValueStream[primitives.FloatQ] | None) -> None:
        """Set the RotationStream reference by target ID or ValueStream[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("RotationStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RotationStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<floatQ>'),
            )

    @property
    def scale_stream(self) -> str | None:
        """Target ID of the ScaleStream reference (targets ValueStream[primitives.Float3])."""
        member = self.get_member("ScaleStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale_stream.setter
    def scale_stream(self, target: str | ValueStream[primitives.Float3] | None) -> None:
        """Set the ScaleStream reference by target ID or ValueStream[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("ScaleStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ScaleStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float3>'),
            )

    @property
    def root_space_stream(self) -> str | None:
        """Target ID of the RootSpaceStream reference (targets ReferenceStream[Slot])."""
        member = self.get_member("RootSpaceStream")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root_space_stream.setter
    def root_space_stream(self, target: str | ReferenceStream[Slot] | None) -> None:
        """Set the RootSpaceStream reference by target ID or ReferenceStream[Slot] instance."""
        target_id: str | None = target.id if isinstance(target, ReferenceStream) else target  # type: ignore[assignment]
        member = self.get_member("RootSpaceStream")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RootSpaceStream",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ReferenceStream<[FrooxEngine]FrooxEngine.Slot>'),
            )

    @property
    def position(self) -> str | None:
        """Target ID of the Position reference (targets IField[primitives.Float3])."""
        member = self.get_member("Position")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @position.setter
    def position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the Position reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Position")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Position",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def rotation(self) -> str | None:
        """Target ID of the Rotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("Rotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @rotation.setter
    def rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the Rotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Rotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Rotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def scale(self) -> str | None:
        """Target ID of the Scale reference (targets IField[primitives.Float3])."""
        member = self.get_member("Scale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @scale.setter
    def scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the Scale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Scale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Scale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def allow_offsets(self) -> bool | None:
        """The AllowOffsets field value."""
        member = self.get_member("AllowOffsets")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_offsets.setter
    def allow_offsets(self, value: bool) -> None:
        """Set the AllowOffsets field value."""
        member = self.get_member("AllowOffsets")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowOffsets", fields.FieldBool(value=value)
            )

    @property
    def reset_streams_on_destroy(self) -> bool | None:
        """The ResetStreamsOnDestroy field value."""
        member = self.get_member("ResetStreamsOnDestroy")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reset_streams_on_destroy.setter
    def reset_streams_on_destroy(self, value: bool) -> None:
        """Set the ResetStreamsOnDestroy field value."""
        member = self.get_member("ResetStreamsOnDestroy")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ResetStreamsOnDestroy", fields.FieldBool(value=value)
            )

    @property
    def position_offset(self) -> primitives.Float3 | None:
        """The PositionOffset field value."""
        member = self.get_member("PositionOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_offset.setter
    def position_offset(self, value: primitives.Float3) -> None:
        """Set the PositionOffset field value."""
        member = self.get_member("PositionOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionOffset", fields.FieldNullableFloat3(value=value)
            )

    @property
    def rotation_offset(self) -> primitives.FloatQ | None:
        """The RotationOffset field value."""
        member = self.get_member("RotationOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotation_offset.setter
    def rotation_offset(self, value: primitives.FloatQ) -> None:
        """Set the RotationOffset field value."""
        member = self.get_member("RotationOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RotationOffset", fields.FieldNullableFloatQ(value=value)
            )

    @property
    def scale_offset(self) -> primitives.Float3 | None:
        """The ScaleOffset field value."""
        member = self.get_member("ScaleOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale_offset.setter
    def scale_offset(self, value: primitives.Float3) -> None:
        """Set the ScaleOffset field value."""
        member = self.get_member("ScaleOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScaleOffset", fields.FieldNullableFloat3(value=value)
            )

    @property
    def run_before_physics(self) -> bool | None:
        """The RunBeforePhysics field value."""
        member = self.get_member("RunBeforePhysics")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @run_before_physics.setter
    def run_before_physics(self, value: bool) -> None:
        """Set the RunBeforePhysics field value."""
        member = self.get_member("RunBeforePhysics")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RunBeforePhysics", fields.FieldBool(value=value)
            )

