"""Generated component: MeshCollider."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.mesh import Mesh
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.imesh_physics_data_requester import IMeshPhysicsDataRequester


class MeshCollider(GeneratedComponent, ICustomInspector, IMeshPhysicsDataRequester):
    """Wrapper for [FrooxEngine]FrooxEngine.MeshCollider.

    Category: Physics/Colliders
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MeshCollider"

    def __init__(self, offset: primitives.Float3 | None = None, mass: np.float32 | None = None, character_collider: bool | None = None, ignore_raycasts: bool | None = None, mesh: str | IAssetProvider[Mesh] | None = None, actual_speculative_margin: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            offset: Initial value for Offset.
            mass: Initial value for Mass.
            character_collider: Initial value for CharacterCollider.
            ignore_raycasts: Initial value for IgnoreRaycasts.
            mesh: Initial value for Mesh.
            actual_speculative_margin: Initial value for ActualSpeculativeMargin.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if offset is not None:
            self.offset = offset
        if mass is not None:
            self.mass = mass
        if character_collider is not None:
            self.character_collider = character_collider
        if ignore_raycasts is not None:
            self.ignore_raycasts = ignore_raycasts
        if mesh is not None:
            self.mesh = mesh
        if actual_speculative_margin is not None:
            self.actual_speculative_margin = actual_speculative_margin

    @property
    def offset(self) -> primitives.Float3 | None:
        """The Offset field value."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float3) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat3(value=value)
            )

    @property
    def type_(self) -> members.FieldEnum | None:
        """The Type member."""
        member = self.get_member("Type")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @type_.setter
    def type_(self, value: members.FieldEnum) -> None:
        """Set the Type member."""
        self.set_member("Type", value)

    @property
    def mass(self) -> np.float32 | None:
        """The Mass field value."""
        member = self.get_member("Mass")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mass.setter
    def mass(self, value: np.float32) -> None:
        """Set the Mass field value."""
        member = self.get_member("Mass")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Mass", fields.FieldFloat(value=value)
            )

    @property
    def character_collider(self) -> bool | None:
        """The CharacterCollider field value."""
        member = self.get_member("CharacterCollider")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @character_collider.setter
    def character_collider(self, value: bool) -> None:
        """Set the CharacterCollider field value."""
        member = self.get_member("CharacterCollider")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CharacterCollider", fields.FieldBool(value=value)
            )

    @property
    def ignore_raycasts(self) -> bool | None:
        """The IgnoreRaycasts field value."""
        member = self.get_member("IgnoreRaycasts")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @ignore_raycasts.setter
    def ignore_raycasts(self, value: bool) -> None:
        """Set the IgnoreRaycasts field value."""
        member = self.get_member("IgnoreRaycasts")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IgnoreRaycasts", fields.FieldBool(value=value)
            )

    @property
    def mesh(self) -> str | None:
        """Target ID of the Mesh reference (targets IAssetProvider[Mesh])."""
        member = self.get_member("Mesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mesh.setter
    def mesh(self, target: str | IAssetProvider[Mesh] | None) -> None:
        """Set the Mesh reference by target ID or IAssetProvider[Mesh] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Mesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Mesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Mesh>'),
            )

    @property
    def sidedness(self) -> members.FieldEnum | None:
        """The Sidedness member."""
        member = self.get_member("Sidedness")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @sidedness.setter
    def sidedness(self, value: members.FieldEnum) -> None:
        """Set the Sidedness member."""
        self.set_member("Sidedness", value)

    @property
    def actual_speculative_margin(self) -> np.float32 | None:
        """The ActualSpeculativeMargin field value."""
        member = self.get_member("ActualSpeculativeMargin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @actual_speculative_margin.setter
    def actual_speculative_margin(self, value: np.float32) -> None:
        """Set the ActualSpeculativeMargin field value."""
        member = self.get_member("ActualSpeculativeMargin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActualSpeculativeMargin", fields.FieldFloat(value=value)
            )

