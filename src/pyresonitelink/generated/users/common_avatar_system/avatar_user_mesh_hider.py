"""Generated component: AvatarUserMeshHider."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.hide_method import HideMethod
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iavatar_object_component import IAvatarObjectComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AvatarUserMeshHider(GeneratedComponent, IAvatarObjectComponent, IWorldEventReceiver):
    """The AvatarUserMeshHider component makes non Skinned meshes invisible or only cast shadows according to the active user's perspective. It does this by making value User overrides for all MeshRenderers except for those in ``Exclude``. It restores the fields back to normal after dequipping.

    Category: Users/Common Avatar System
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.CommonAvatar.AvatarUserMeshHider"

    def __init__(self, method: HideMethod | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            method: Initial value for Method.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if method is not None:
            self.method = method

    @property
    def method(self) -> HideMethod | None:
        """How to hide the meshes for the active user under the avatar."""
        member = self.get_member("Method")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return HideMethod(member.value)
        return None

    @method.setter
    def method(self, value: HideMethod | str) -> None:
        """Set Method. How to hide the meshes for the active user under the avatar."""
        member = self.get_member("Method")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Method",
                members.FieldEnum(value=str(value)),
            )

    @property
    def exclude(self) -> members.SyncList | None:
        """Which meshes to not hide for the active user."""
        member = self.get_member("Exclude")
        if isinstance(member, members.SyncList):
            return member
        return None

    @exclude.setter
    def exclude(self, value: members.SyncList) -> None:
        """Set Exclude. Which meshes to not hide for the active user."""
        self.set_member("Exclude", value)

