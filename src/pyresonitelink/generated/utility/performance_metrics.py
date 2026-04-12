"""Generated component: PerformanceMetrics."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class PerformanceMetrics(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The PerformanceMetrics component is used to show performance for a particular ``User`` at the present moment.

    Category: Utility

    Attach to a slot and provide a user for ``User`` for it to start giving
    performance metrics.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.PerformanceMetrics"

    def __init__(self, fps: primitives.Float | None = None, immediate_fps: primitives.Float | None = None, render_time: primitives.Float | None = None, total_engine_update_time: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            fps: Initial value for FPS.
            immediate_fps: Initial value for ImmediateFPS.
            render_time: Initial value for RenderTime.
            total_engine_update_time: Initial value for TotalEngineUpdateTime.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if fps is not None:
            self.fps = fps
        if immediate_fps is not None:
            self.immediate_fps = immediate_fps
        if render_time is not None:
            self.render_time = render_time
        if total_engine_update_time is not None:
            self.total_engine_update_time = total_engine_update_time

    @property
    def user(self) -> members.SyncObject | None:
        """The user we are measuring performance for."""
        member = self.get_member("User")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @user.setter
    def user(self, value: members.SyncObject) -> None:
        """Set User. The user we are measuring performance for."""
        self.set_member("User", value)

    @property
    def fps(self) -> primitives.Float | None:
        """``User``'s Frames Per second."""
        member = self.get_member("FPS")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @fps.setter
    def fps(self, value: primitives.Float) -> None:
        """Set the FPS field value."""
        member = self.get_member("FPS")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FPS", fields.FieldFloat(value=value)
            )

    @property
    def immediate_fps(self) -> primitives.Float | None:
        """``User``'s immediate Frames Per Second."""
        member = self.get_member("ImmediateFPS")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @immediate_fps.setter
    def immediate_fps(self, value: primitives.Float) -> None:
        """Set the ImmediateFPS field value."""
        member = self.get_member("ImmediateFPS")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ImmediateFPS", fields.FieldFloat(value=value)
            )

    @property
    def render_time(self) -> primitives.Float | None:
        """``User``'s time it takes to render the scene in seconds."""
        member = self.get_member("RenderTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_time.setter
    def render_time(self, value: primitives.Float) -> None:
        """Set the RenderTime field value."""
        member = self.get_member("RenderTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RenderTime", fields.FieldFloat(value=value)
            )

    @property
    def total_engine_update_time(self) -> primitives.Float | None:
        """``User``'s time it takes to update the engine in seconds."""
        member = self.get_member("TotalEngineUpdateTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_engine_update_time.setter
    def total_engine_update_time(self, value: primitives.Float) -> None:
        """Set the TotalEngineUpdateTime field value."""
        member = self.get_member("TotalEngineUpdateTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalEngineUpdateTime", fields.FieldFloat(value=value)
            )

