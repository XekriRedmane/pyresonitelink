"""Generated component: Projection360PropertyBlock."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class Projection360PropertyBlock(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """See Material Property Block for a vastly detailed explaination.

    Category: Assets/Material Property Blocks

    See Material Property Block for a vastly detailed explaination.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.Projection360PropertyBlock"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, texture: str | IAssetProvider[ITexture2D] | None = None, perspective_field_of_view: primitives.Float2 | None = None, perspective_angle_offset: primitives.Float2 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            texture: Initial value for Texture.
            perspective_field_of_view: Initial value for PerspectiveFieldOfView.
            perspective_angle_offset: Initial value for PerspectiveAngleOffset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if texture is not None:
            self.texture = texture
        if perspective_field_of_view is not None:
            self.perspective_field_of_view = perspective_field_of_view
        if perspective_angle_offset is not None:
            self.perspective_angle_offset = perspective_angle_offset

    @property
    def high_priority_integration(self) -> primitives.Bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: primitives.Bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def texture(self) -> str | None:
        """The texture to override the ``Texture`` field of a Projection360Material for a renderer."""
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the Texture reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def perspective_field_of_view(self) -> primitives.Float2 | None:
        """The value to override the ``PerspectiveFieldOfView`` field of a Projection360Material for a renderer."""
        member = self.get_member("PerspectiveFieldOfView")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @perspective_field_of_view.setter
    def perspective_field_of_view(self, value: primitives.Float2) -> None:
        """Set the PerspectiveFieldOfView field value."""
        member = self.get_member("PerspectiveFieldOfView")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PerspectiveFieldOfView", fields.FieldFloat2(value=value)
            )

    @property
    def perspective_angle_offset(self) -> primitives.Float2 | None:
        """The value to override the ``PerspectiveAngleOffset`` field of a Projection360Material for a renderer."""
        member = self.get_member("PerspectiveAngleOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @perspective_angle_offset.setter
    def perspective_angle_offset(self, value: primitives.Float2) -> None:
        """Set the PerspectiveAngleOffset field value."""
        member = self.get_member("PerspectiveAngleOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PerspectiveAngleOffset", fields.FieldFloat2(value=value)
            )

