"""Generated component: ScaleGroup."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.scale_element import ScaleElement
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScaleGroup(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ScaleGroup.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ScaleGroup"

    def __init__(self, selected_element: str | ScaleElement | None = None, idle_scale: primitives.Float3 | None = None, background_scale: primitives.Float3 | None = None, selected_scale: primitives.Float3 | None = None, smooth_speed: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            selected_element: Initial value for SelectedElement.
            idle_scale: Initial value for IdleScale.
            background_scale: Initial value for BackgroundScale.
            selected_scale: Initial value for SelectedScale.
            smooth_speed: Initial value for SmoothSpeed.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if selected_element is not None:
            self.selected_element = selected_element
        if idle_scale is not None:
            self.idle_scale = idle_scale
        if background_scale is not None:
            self.background_scale = background_scale
        if selected_scale is not None:
            self.selected_scale = selected_scale
        if smooth_speed is not None:
            self.smooth_speed = smooth_speed

    @property
    def selected_element(self) -> str | None:
        """Target ID of the SelectedElement reference (targets ScaleElement)."""
        member = self.get_member("SelectedElement")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @selected_element.setter
    def selected_element(self, target: str | ScaleElement | None) -> None:
        """Set the SelectedElement reference by target ID or ScaleElement instance."""
        target_id: str | None = target.id if isinstance(target, ScaleElement) else target  # type: ignore[assignment]
        member = self.get_member("SelectedElement")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SelectedElement",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ScaleElement'),
            )

    @property
    def idle_scale(self) -> primitives.Float3 | None:
        """The IdleScale field value."""
        member = self.get_member("IdleScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @idle_scale.setter
    def idle_scale(self, value: primitives.Float3) -> None:
        """Set the IdleScale field value."""
        member = self.get_member("IdleScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IdleScale", fields.FieldFloat3(value=value)
            )

    @property
    def background_scale(self) -> primitives.Float3 | None:
        """The BackgroundScale field value."""
        member = self.get_member("BackgroundScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @background_scale.setter
    def background_scale(self, value: primitives.Float3) -> None:
        """Set the BackgroundScale field value."""
        member = self.get_member("BackgroundScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BackgroundScale", fields.FieldFloat3(value=value)
            )

    @property
    def selected_scale(self) -> primitives.Float3 | None:
        """The SelectedScale field value."""
        member = self.get_member("SelectedScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @selected_scale.setter
    def selected_scale(self, value: primitives.Float3) -> None:
        """Set the SelectedScale field value."""
        member = self.get_member("SelectedScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SelectedScale", fields.FieldFloat3(value=value)
            )

    @property
    def smooth_speed(self) -> primitives.Float | None:
        """The SmoothSpeed field value."""
        member = self.get_member("SmoothSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @smooth_speed.setter
    def smooth_speed(self, value: primitives.Float) -> None:
        """Set the SmoothSpeed field value."""
        member = self.get_member("SmoothSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SmoothSpeed", fields.FieldFloat(value=value)
            )

