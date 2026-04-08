"""Generated component: AssetLoadStatus."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AssetLoadStatus(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AssetLoadStatus.

    Category: World/Loading
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AssetLoadStatus"

    def __init__(self, is_loaded: primitives.Bool | None = None, load_progress: primitives.Float | None = None, progress_weight: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            is_loaded: Initial value for IsLoaded.
            load_progress: Initial value for LoadProgress.
            progress_weight: Initial value for ProgressWeight.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if is_loaded is not None:
            self.is_loaded = is_loaded
        if load_progress is not None:
            self.load_progress = load_progress
        if progress_weight is not None:
            self.progress_weight = progress_weight

    @property
    def assets(self) -> members.SyncList | None:
        """The Assets member."""
        member = self.get_member("Assets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @assets.setter
    def assets(self, value: members.SyncList) -> None:
        """Set the Assets member."""
        self.set_member("Assets", value)

    @property
    def is_loaded(self) -> primitives.Bool | None:
        """The IsLoaded field value."""
        member = self.get_member("IsLoaded")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_loaded.setter
    def is_loaded(self, value: primitives.Bool) -> None:
        """Set the IsLoaded field value."""
        member = self.get_member("IsLoaded")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsLoaded", fields.FieldBool(value=value)
            )

    @property
    def load_progress(self) -> primitives.Float | None:
        """The LoadProgress field value."""
        member = self.get_member("LoadProgress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @load_progress.setter
    def load_progress(self, value: primitives.Float) -> None:
        """Set the LoadProgress field value."""
        member = self.get_member("LoadProgress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LoadProgress", fields.FieldFloat(value=value)
            )

    @property
    def progress_weight(self) -> primitives.Float | None:
        """The ProgressWeight field value."""
        member = self.get_member("ProgressWeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @progress_weight.setter
    def progress_weight(self, value: primitives.Float) -> None:
        """Set the ProgressWeight field value."""
        member = self.get_member("ProgressWeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProgressWeight", fields.FieldFloat(value=value)
            )

