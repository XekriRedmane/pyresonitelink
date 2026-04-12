"""Generated component: RenderTransformOverride."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.rendering_context import RenderingContext
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RenderTransformOverride(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """The RenderTransformOverride component is used to transform, rotate or scale a Slot following a specific rendering context. 

It can be used, for instance, to scale a player's head to zero locally to effectively hide it from the user's view while it still being visible in mirrors, cameras and by other players.

This component is automatically added to all Avatars on the Head BodyNode by the AvatarUserViewHeadOverride component. It will also setup drives for Enabled, PositionOverride, and RotationOverride.

    Category: Rendering

    **Bugs**: * This component has a very small chance to increase the frequency of crashes.https://github.com/Yellow-Dog-Man/Resonite-Issues/issues/269 
* This component might not function correctly if there are any Null fields in the SkinnedMeshRenderers list.https://github.com/Yellow-Dog-Man/Resonite-Issues/issues/2474 
* This component currently has an imprecise understanding of the UserView context and will be active while an item is grabbed or when saving a thumbnail to the inventory.https://github.com/Yellow-Dog-Man/Resonite-Issues/issues/3732 
* This component will cause motion blur to be very visible on object when looking through a cameras or in a mirror.https://github.com/Yellow-Dog-Man/Resonite-Issues/issues/1654
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RenderTransformOverride"

    def __init__(self, context: RenderingContext | str | None = None, position_override: primitives.Float3 | None = None, rotation_override: primitives.FloatQ | None = None, scale_override: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            context: Initial value for Context.
            position_override: Initial value for PositionOverride.
            rotation_override: Initial value for RotationOverride.
            scale_override: Initial value for ScaleOverride.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if context is not None:
            self.context = context
        if position_override is not None:
            self.position_override = position_override
        if rotation_override is not None:
            self.rotation_override = rotation_override
        if scale_override is not None:
            self.scale_override = scale_override

    @property
    def context(self) -> RenderingContext | None:
        """The Context when rendering from to apply this override."""
        member = self.get_member("Context")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return RenderingContext(member.value)
        return None

    @context.setter
    def context(self, value: RenderingContext | str) -> None:
        """Set Context. The Context when rendering from to apply this override."""
        member = self.get_member("Context")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Context",
                members.FieldEnum(value=str(value)),
            )

    @property
    def position_override(self) -> primitives.Float3 | None:
        """If not null, will override the position of the slot this component is on."""
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
        """If not null, will override the rotation of the slot this component is on."""
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
        """If not null, will override the scale of the slot this component is on."""
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
        """List of SkinnedMeshRenderers that need to be recalculated and overridden."""
        member = self.get_member("SkinnedMeshRenderers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @skinned_mesh_renderers.setter
    def skinned_mesh_renderers(self, value: members.SyncList) -> None:
        """Set SkinnedMeshRenderers. List of SkinnedMeshRenderers that need to be recalculated and overridden."""
        self.set_member("SkinnedMeshRenderers", value)

