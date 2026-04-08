"""Generated component: UsersAssetLoadProgress."""

from typing import Any

A = Any
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UsersAssetLoadProgress(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UsersAssetLoadProgress<>.

    Category: Assets/Loading

    Parameterize with a value type::

        UsersAssetLoadProgress[primitives.Float]
        UsersAssetLoadProgress[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UsersAssetLoadProgress<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.UsersAssetLoadProgress<>"

    def __init__(self, asset: str | IAssetProvider[A] | None = None, total_users: primitives.Int | None = None, users_not_loaded: primitives.Int | None = None, users_loading: primitives.Int | None = None, users_partially_loaded: primitives.Int | None = None, users_fully_loaded: primitives.Int | None = None, users_failed_to_load: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            asset: Initial value for Asset.
            total_users: Initial value for TotalUsers.
            users_not_loaded: Initial value for UsersNotLoaded.
            users_loading: Initial value for UsersLoading.
            users_partially_loaded: Initial value for UsersPartiallyLoaded.
            users_fully_loaded: Initial value for UsersFullyLoaded.
            users_failed_to_load: Initial value for UsersFailedToLoad.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if asset is not None:
            self.asset = asset
        if total_users is not None:
            self.total_users = total_users
        if users_not_loaded is not None:
            self.users_not_loaded = users_not_loaded
        if users_loading is not None:
            self.users_loading = users_loading
        if users_partially_loaded is not None:
            self.users_partially_loaded = users_partially_loaded
        if users_fully_loaded is not None:
            self.users_fully_loaded = users_fully_loaded
        if users_failed_to_load is not None:
            self.users_failed_to_load = users_failed_to_load

    @property
    def asset(self) -> str | None:
        """Target ID of the Asset reference (targets IAssetProvider[A])."""
        member = self.get_member("Asset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @asset.setter
    def asset(self, target: str | IAssetProvider[A] | None) -> None:
        """Set the Asset reference by target ID or IAssetProvider[A] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Asset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Asset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<A>'),
            )

    @property
    def progress_info(self) -> members.SyncList | None:
        """The ProgressInfo member."""
        member = self.get_member("ProgressInfo")
        if isinstance(member, members.SyncList):
            return member
        return None

    @progress_info.setter
    def progress_info(self, value: members.SyncList) -> None:
        """Set the ProgressInfo member."""
        self.set_member("ProgressInfo", value)

    @property
    def total_users(self) -> primitives.Int | None:
        """The TotalUsers field value."""
        member = self.get_member("TotalUsers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @total_users.setter
    def total_users(self, value: primitives.Int) -> None:
        """Set the TotalUsers field value."""
        member = self.get_member("TotalUsers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TotalUsers", fields.FieldInt(value=value)
            )

    @property
    def users_not_loaded(self) -> primitives.Int | None:
        """The UsersNotLoaded field value."""
        member = self.get_member("UsersNotLoaded")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_not_loaded.setter
    def users_not_loaded(self, value: primitives.Int) -> None:
        """Set the UsersNotLoaded field value."""
        member = self.get_member("UsersNotLoaded")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersNotLoaded", fields.FieldInt(value=value)
            )

    @property
    def users_loading(self) -> primitives.Int | None:
        """The UsersLoading field value."""
        member = self.get_member("UsersLoading")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_loading.setter
    def users_loading(self, value: primitives.Int) -> None:
        """Set the UsersLoading field value."""
        member = self.get_member("UsersLoading")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersLoading", fields.FieldInt(value=value)
            )

    @property
    def users_partially_loaded(self) -> primitives.Int | None:
        """The UsersPartiallyLoaded field value."""
        member = self.get_member("UsersPartiallyLoaded")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_partially_loaded.setter
    def users_partially_loaded(self, value: primitives.Int) -> None:
        """Set the UsersPartiallyLoaded field value."""
        member = self.get_member("UsersPartiallyLoaded")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersPartiallyLoaded", fields.FieldInt(value=value)
            )

    @property
    def users_fully_loaded(self) -> primitives.Int | None:
        """The UsersFullyLoaded field value."""
        member = self.get_member("UsersFullyLoaded")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_fully_loaded.setter
    def users_fully_loaded(self, value: primitives.Int) -> None:
        """Set the UsersFullyLoaded field value."""
        member = self.get_member("UsersFullyLoaded")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersFullyLoaded", fields.FieldInt(value=value)
            )

    @property
    def users_failed_to_load(self) -> primitives.Int | None:
        """The UsersFailedToLoad field value."""
        member = self.get_member("UsersFailedToLoad")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @users_failed_to_load.setter
    def users_failed_to_load(self, value: primitives.Int) -> None:
        """Set the UsersFailedToLoad field value."""
        member = self.get_member("UsersFailedToLoad")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UsersFailedToLoad", fields.FieldInt(value=value)
            )

