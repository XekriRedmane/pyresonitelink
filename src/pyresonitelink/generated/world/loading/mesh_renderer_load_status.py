"""Generated component: MeshRendererLoadStatus."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MeshRendererLoadStatus(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MeshRendererLoadStatus.

    Category: World/Loading
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MeshRendererLoadStatus"

    def __init__(self, is_loaded: bool | None = None, load_progress: np.float32 | None = None, progress_weight: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
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
    def renderers(self) -> members.SyncList | None:
        """The Renderers member."""
        member = self.get_member("Renderers")
        if isinstance(member, members.SyncList):
            return member
        return None

    @renderers.setter
    def renderers(self, value: members.SyncList) -> None:
        """Set the Renderers member."""
        self.set_member("Renderers", value)

    @property
    def is_loaded(self) -> bool | None:
        """The IsLoaded field value."""
        member = self.get_member("IsLoaded")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_loaded.setter
    def is_loaded(self, value: bool) -> None:
        """Set the IsLoaded field value."""
        member = self.get_member("IsLoaded")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsLoaded", fields.FieldBool(value=value)
            )

    @property
    def load_progress(self) -> np.float32 | None:
        """The LoadProgress field value."""
        member = self.get_member("LoadProgress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @load_progress.setter
    def load_progress(self, value: np.float32) -> None:
        """Set the LoadProgress field value."""
        member = self.get_member("LoadProgress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LoadProgress", fields.FieldFloat(value=value)
            )

    @property
    def progress_weight(self) -> np.float32 | None:
        """The ProgressWeight field value."""
        member = self.get_member("ProgressWeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @progress_weight.setter
    def progress_weight(self, value: np.float32) -> None:
        """Set the ProgressWeight field value."""
        member = self.get_member("ProgressWeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProgressWeight", fields.FieldFloat(value=value)
            )

