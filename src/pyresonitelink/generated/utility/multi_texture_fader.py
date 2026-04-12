"""Generated component: MultiTextureFader."""

from typing import Any

A = Any
from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.asset_ref import AssetRef
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MultiTextureFader(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The MultiTextureFader component can be used with the PBSLerpMetallic or PBSLerpSpecular to lerp multiple textures rather than just one.

    Category: Utility

    Can be attached to a slot and given a list of materials. Using a
    PBSLerpMetallic or PBSLerpSpecular with this component can lerp the list
    of ``Textures`` using ``Position``. The lerp of the material can be
    driven via the ``Lerp`` on this component.

    Parameterize with a value type::

        MultiTextureFader[primitives.Float]
        MultiTextureFader[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MultiTextureFader<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.MultiTextureFader<>"

    def __init__(self, first_texture: str | AssetRef[A] | None = None, second_texture: str | AssetRef[A] | None = None, lerp: str | IField[primitives.Float] | None = None, position: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
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
        """Usually set to the Texture set 0 of a lerping material."""
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
        """Usually set to the Texture set 1 of a lerping material. The type of texture set like albedo or emission this one is driving should be the same as ``FirstTexture``."""
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
        """The lerp field of the material. Can be left blank if using multiple of this component on the same material."""
        member = self.get_member("Lerp")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lerp.setter
    def lerp(self, target: str | IField[primitives.Float] | None) -> None:
        """Set the Lerp reference by target ID or IField[primitives.Float] instance."""
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
    def position(self) -> primitives.Float | None:
        """The position in the list of ``Textures`` to fade between. If this is a decimal, the ``FirstTexture`` and ``SecondTexture`` will be set to textures in ``Textures`` that are at the positon of floor and ceiling of this value."""
        member = self.get_member("Position")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @position.setter
    def position(self, value: primitives.Float) -> None:
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
        """A list of textures to lerp between and set ``FirstTexture`` and ``SecondTexture`` to using ``Position`` to determine the texture from this list."""
        member = self.get_member("Textures")
        if isinstance(member, members.SyncList):
            return member
        return None

    @textures.setter
    def textures(self, value: members.SyncList) -> None:
        """Set Textures. A list of textures to lerp between and set ``FirstTexture`` and ``SecondTexture`` to using ``Position`` to determine the texture from this list."""
        self.set_member("Textures", value)

