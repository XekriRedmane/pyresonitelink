"""Generated component: SimpleAwayIndicator."""

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.mesh_renderer import MeshRenderer
from pyresonitelink.generated._types.imesh_bake_event_receiver import IMeshBakeEventReceiver
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class SimpleAwayIndicator(GeneratedComponent, IMeshBakeEventReceiver, ICustomInspector, IWorldEventReceiver):
    """The SimpleAwayIndicator indicates when a user doesn't have the session focused by temporarily replacing the materials of a MeshRenderer with the specified Away Material.

Usually found on the body slot of an avatar (but can be put anywhere in the world), this just needs a reference to the MeshRenderer or SkinnedMeshRenderer components to work.

}}

    Category: Users

    This is used to make a customized or fancier way of stating that you are
    focused away into another world.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.SimpleAwayIndicator"

    def __init__(self, user: str | User | None = None, away_material: str | IAssetProvider[Material] | None = None, renderer: str | MeshRenderer | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user: Initial value for User.
            away_material: Initial value for AwayMaterial.
            renderer: Initial value for Renderer.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if user is not None:
            self.user = user
        if away_material is not None:
            self.away_material = away_material
        if renderer is not None:
            self.renderer = renderer

    @property
    def user(self) -> str | None:
        """User whose away state will be watched. On avatars, may be set by an AvatarUserReferenceAssigner component."""
        member = self.get_member("User")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user.setter
    def user(self, target: str | User | None) -> None:
        """Set the User reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("User")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "User",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def away_material(self) -> str | None:
        """Material to display when the user is away."""
        member = self.get_member("AwayMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @away_material.setter
    def away_material(self, target: str | IAssetProvider[Material] | None) -> None:
        """Set the AwayMaterial reference by target ID or IAssetProvider[Material] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("AwayMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "AwayMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>'),
            )

    @property
    def renderer(self) -> str | None:
        """Mesh renderer component whose materials should be replaced"""
        member = self.get_member("Renderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @renderer.setter
    def renderer(self, target: str | MeshRenderer | None) -> None:
        """Set the Renderer reference by target ID or MeshRenderer instance."""
        target_id: str | None = target.id if isinstance(target, MeshRenderer) else target  # type: ignore[assignment]
        member = self.get_member("Renderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Renderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MeshRenderer'),
            )

    @property
    def old_materials(self) -> members.SyncList | None:
        """Backup of the renderer's original material list. Written automatically when "Away" state is triggered."""
        member = self.get_member("_oldMaterials")
        if isinstance(member, members.SyncList):
            return member
        return None

    @old_materials.setter
    def old_materials(self, value: members.SyncList) -> None:
        """Set _oldMaterials. Backup of the renderer's original material list. Written automatically when "Away" state is triggered."""
        self.set_member("_oldMaterials", value)

    async def set_away(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Stores the renderer's material list in ``_oldMaterials`` and replaces them with the ``AwayMaterial``.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetAway", {}, debug,
        )

    async def restore(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Restores the renderer's materials from ``_oldMaterials``.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Restore", {}, debug,
        )

