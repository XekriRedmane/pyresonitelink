"""Generated component: RenderTransformOverride."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RenderTransformOverride(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.RenderTransformOverride.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RenderTransformOverride"

    def __init__(self, position_override: primitives.Float3 | None = None, rotation_override: primitives.FloatQ | None = None, scale_override: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            position_override: Initial value for PositionOverride.
            rotation_override: Initial value for RotationOverride.
            scale_override: Initial value for ScaleOverride.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if position_override is not None:
            self.position_override = position_override
        if rotation_override is not None:
            self.rotation_override = rotation_override
        if scale_override is not None:
            self.scale_override = scale_override

    @property
    def context(self) -> members.FieldEnum | None:
        """The Context member."""
        member = self.get_member("Context")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @context.setter
    def context(self, value: members.FieldEnum) -> None:
        """Set the Context member."""
        self.set_member("Context", value)

    @property
    def position_override(self) -> primitives.Float3 | None:
        """The PositionOverride field value."""
        member = self.get_member("PositionOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position_override.setter
    def position_override(self, value: primitives.Float3) -> None:
        """Set the PositionOverride field value."""
        member = self.get_member("PositionOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PositionOverride", fields.FieldNullableFloat3(value=value)
            )

    @property
    def rotation_override(self) -> primitives.FloatQ | None:
        """The RotationOverride field value."""
        member = self.get_member("RotationOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rotation_override.setter
    def rotation_override(self, value: primitives.FloatQ) -> None:
        """Set the RotationOverride field value."""
        member = self.get_member("RotationOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RotationOverride", fields.FieldNullableFloatQ(value=value)
            )

    @property
    def scale_override(self) -> primitives.Float3 | None:
        """The ScaleOverride field value."""
        member = self.get_member("ScaleOverride")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale_override.setter
    def scale_override(self, value: primitives.Float3) -> None:
        """Set the ScaleOverride field value."""
        member = self.get_member("ScaleOverride")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScaleOverride", fields.FieldNullableFloat3(value=value)
            )

    @property
    def skinned_mesh_renderers(self) -> members.SyncList | None:
        """The SkinnedMeshRenderers member."""
        member = self.get_member("SkinnedMeshRenderers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @skinned_mesh_renderers.setter
    def skinned_mesh_renderers(self, value: members.SyncList) -> None:
        """Set the SkinnedMeshRenderers member."""
        self.set_member("SkinnedMeshRenderers", value)

