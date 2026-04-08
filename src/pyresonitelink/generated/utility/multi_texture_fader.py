"""Generated component: MultiTextureFader."""

from typing import Any
import numpy as np

A = Any
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.asset_ref import AssetRef
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MultiTextureFader(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MultiTextureFader<>.

    Category: Utility

    Parameterize with a value type::

        MultiTextureFader[np.float32]
        MultiTextureFader[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MultiTextureFader<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.MultiTextureFader<>"

    def __init__(self, first_texture: str | AssetRef[A] | None = None, second_texture: str | AssetRef[A] | None = None, lerp: str | IField[np.float32] | None = None, position: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            first_texture: Initial value for FirstTexture.
            second_texture: Initial value for SecondTexture.
            lerp: Initial value for Lerp.
            position: Initial value for Position.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if first_texture is not None:
            self.first_texture = first_texture
        if second_texture is not None:
            self.second_texture = second_texture
        if lerp is not None:
            self.lerp = lerp
        if position is not None:
            self.position = position

    @property
    def first_texture(self) -> str | None:
        """Target ID of the FirstTexture reference (targets AssetRef[A])."""
        member = self.get_member("FirstTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @first_texture.setter
    def first_texture(self, target: str | AssetRef[A] | None) -> None:
        """Set the FirstTexture reference by target ID or AssetRef[A] instance."""
        target_id: str | None = target.id if isinstance(target, AssetRef) else target  # type: ignore[assignment]
        member = self.get_member("FirstTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FirstTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetRef<A>'),
            )

    @property
    def second_texture(self) -> str | None:
        """Target ID of the SecondTexture reference (targets AssetRef[A])."""
        member = self.get_member("SecondTexture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @second_texture.setter
    def second_texture(self, target: str | AssetRef[A] | None) -> None:
        """Set the SecondTexture reference by target ID or AssetRef[A] instance."""
        target_id: str | None = target.id if isinstance(target, AssetRef) else target  # type: ignore[assignment]
        member = self.get_member("SecondTexture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SecondTexture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.AssetRef<A>'),
            )

    @property
    def lerp(self) -> str | None:
        """Target ID of the Lerp reference (targets IField[np.float32])."""
        member = self.get_member("Lerp")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lerp.setter
    def lerp(self, target: str | IField[np.float32] | None) -> None:
        """Set the Lerp reference by target ID or IField[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Lerp")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Lerp",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float>'),
            )

    @property
    def position(self) -> np.float32 | None:
        """The Position field value."""
        member = self.get_member("Position")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position.setter
    def position(self, value: np.float32) -> None:
        """Set the Position field value."""
        member = self.get_member("Position")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Position", fields.FieldFloat(value=value)
            )

    @property
    def textures(self) -> members.SyncList | None:
        """The Textures member."""
        member = self.get_member("Textures")
        if isinstance(member, members.SyncList):
            return member
        return None

    @textures.setter
    def textures(self, value: members.SyncList) -> None:
        """Set the Textures member."""
        self.set_member("Textures", value)

