"""Generated component: Snapper."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.igrab_event_receiver import IGrabEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Snapper(GeneratedComponent, IGrabEventReceiver, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.Snapper.

    Category: Transform/Interaction
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Snapper"

    def __init__(self, use_bounding_box_center: bool | None = None, snap_check_radius: np.float32 | None = None, check_static_colliders: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            use_bounding_box_center: Initial value for UseBoundingBoxCenter.
            snap_check_radius: Initial value for SnapCheckRadius.
            check_static_colliders: Initial value for CheckStaticColliders.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if use_bounding_box_center is not None:
            self.use_bounding_box_center = use_bounding_box_center
        if snap_check_radius is not None:
            self.snap_check_radius = snap_check_radius
        if check_static_colliders is not None:
            self.check_static_colliders = check_static_colliders

    @property
    def use_bounding_box_center(self) -> bool | None:
        """The UseBoundingBoxCenter field value."""
        member = self.get_member("UseBoundingBoxCenter")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_bounding_box_center.setter
    def use_bounding_box_center(self, value: bool) -> None:
        """Set the UseBoundingBoxCenter field value."""
        member = self.get_member("UseBoundingBoxCenter")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseBoundingBoxCenter", fields.FieldBool(value=value)
            )

    @property
    def snap_check_radius(self) -> np.float32 | None:
        """The SnapCheckRadius field value."""
        member = self.get_member("SnapCheckRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snap_check_radius.setter
    def snap_check_radius(self, value: np.float32) -> None:
        """Set the SnapCheckRadius field value."""
        member = self.get_member("SnapCheckRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SnapCheckRadius", fields.FieldFloat(value=value)
            )

    @property
    def check_static_colliders(self) -> bool | None:
        """The CheckStaticColliders field value."""
        member = self.get_member("CheckStaticColliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @check_static_colliders.setter
    def check_static_colliders(self, value: bool) -> None:
        """Set the CheckStaticColliders field value."""
        member = self.get_member("CheckStaticColliders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CheckStaticColliders", fields.FieldBool(value=value)
            )

    @property
    def snap_target_whitelist(self) -> members.SyncList | None:
        """The SnapTargetWhitelist member."""
        member = self.get_member("SnapTargetWhitelist")
        if isinstance(member, members.SyncList):
            return member
        return None

    @snap_target_whitelist.setter
    def snap_target_whitelist(self, value: members.SyncList) -> None:
        """Set the SnapTargetWhitelist member."""
        self.set_member("SnapTargetWhitelist", value)

    @property
    def keywords(self) -> members.SyncList | None:
        """The Keywords member."""
        member = self.get_member("Keywords")
        if isinstance(member, members.SyncList):
            return member
        return None

    @keywords.setter
    def keywords(self, value: members.SyncList) -> None:
        """Set the Keywords member."""
        self.set_member("Keywords", value)

