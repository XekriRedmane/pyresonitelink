"""Generated component: DebugVector."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugVector(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DebugVector.

    Category: Debug
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugVector"

    def __init__(self, position_offset: primitives.Float3 | None = None, rotation_offset: primitives.FloatQ | None = None, vector: primitives.Float3 | None = None, color: primitives.ColorX | None = None, use_global_space: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            position_offset: Initial value for PositionOffset.
            rotation_offset: Initial value for RotationOffset.
            vector: Initial value for Vector.
            color: Initial value for Color.
            use_global_space: Initial value for UseGlobalSpace.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if position_offset is not None:
            self.position_offset = position_offset
        if rotation_offset is not None:
            self.rotation_offset = rotation_offset
        if vector is not None:
            self.vector = vector
        if color is not None:
            self.color = color
        if use_global_space is not None:
            self.use_global_space = use_global_space

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
                "PositionOffset", fields.FieldFloat3(value=value)
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
                "RotationOffset", fields.FieldFloatQ(value=value)
            )

    @property
    def vector(self) -> primitives.Float3 | None:
        """The Vector field value."""
        member = self.get_member("Vector")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vector.setter
    def vector(self, value: primitives.Float3) -> None:
        """Set the Vector field value."""
        member = self.get_member("Vector")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Vector", fields.FieldFloat3(value=value)
            )

    @property
    def color(self) -> primitives.ColorX | None:
        """The Color field value."""
        member = self.get_member("Color")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color.setter
    def color(self, value: primitives.ColorX) -> None:
        """Set the Color field value."""
        member = self.get_member("Color")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Color", fields.FieldColorX(value=value)
            )

    @property
    def use_global_space(self) -> primitives.Bool | None:
        """The UseGlobalSpace field value."""
        member = self.get_member("UseGlobalSpace")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_global_space.setter
    def use_global_space(self, value: primitives.Bool) -> None:
        """Set the UseGlobalSpace field value."""
        member = self.get_member("UseGlobalSpace")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseGlobalSpace", fields.FieldBool(value=value)
            )

