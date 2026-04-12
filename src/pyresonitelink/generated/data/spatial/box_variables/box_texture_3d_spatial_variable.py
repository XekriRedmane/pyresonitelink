"""Generated component: BoxTexture3D_SpatialVariable."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.spatial_variable_blend_distance_mode import SpatialVariableBlendDistanceMode
from pyresonitelink.generated._enums.wrap_mode import WrapMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.texture_3d import Texture3D
from pyresonitelink.generated._types.ispatial_variable import ISpatialVariable
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BoxTexture3D_SpatialVariable(GeneratedComponent, ISpatialVariable, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BoxTexture3D_SpatialVariable.

    Category: Data/Spatial/Box Variables
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BoxTexture3D_SpatialVariable"

    def __init__(self, variable_name: primitives.String | None = None, priority: primitives.Int | None = None, size: primitives.Float3 | None = None, blend_distance: primitives.Float | None = None, blend_distance_mode: SpatialVariableBlendDistanceMode | str | None = None, texture: str | IAssetProvider[Texture3D] | None = None, use_normalized_coordinates: primitives.Bool | None = None, scale: primitives.Float3 | None = None, offset: primitives.Float3 | None = None, wrap_u: WrapMode | str | None = None, wrap_v: WrapMode | str | None = None, wrap_w: WrapMode | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            variable_name: Initial value for VariableName.
            priority: Initial value for Priority.
            size: Initial value for Size.
            blend_distance: Initial value for BlendDistance.
            blend_distance_mode: Initial value for BlendDistanceMode.
            texture: Initial value for Texture.
            use_normalized_coordinates: Initial value for UseNormalizedCoordinates.
            scale: Initial value for Scale.
            offset: Initial value for Offset.
            wrap_u: Initial value for WrapU.
            wrap_v: Initial value for WrapV.
            wrap_w: Initial value for WrapW.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if variable_name is not None:
            self.variable_name = variable_name
        if priority is not None:
            self.priority = priority
        if size is not None:
            self.size = size
        if blend_distance is not None:
            self.blend_distance = blend_distance
        if blend_distance_mode is not None:
            self.blend_distance_mode = blend_distance_mode
        if texture is not None:
            self.texture = texture
        if use_normalized_coordinates is not None:
            self.use_normalized_coordinates = use_normalized_coordinates
        if scale is not None:
            self.scale = scale
        if offset is not None:
            self.offset = offset
        if wrap_u is not None:
            self.wrap_u = wrap_u
        if wrap_v is not None:
            self.wrap_v = wrap_v
        if wrap_w is not None:
            self.wrap_w = wrap_w

    @property
    def variable_name(self) -> primitives.String | None:
        """The VariableName field value."""
        member = self.get_member("VariableName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @variable_name.setter
    def variable_name(self, value: primitives.String) -> None:
        """Set the VariableName field value."""
        member = self.get_member("VariableName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VariableName", fields.FieldString(value=value)
            )

    @property
    def priority(self) -> primitives.Int | None:
        """The Priority field value."""
        member = self.get_member("Priority")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @priority.setter
    def priority(self, value: primitives.Int) -> None:
        """Set the Priority field value."""
        member = self.get_member("Priority")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Priority", fields.FieldInt(value=value)
            )

    @property
    def size(self) -> primitives.Float3 | None:
        """The Size field value."""
        member = self.get_member("Size")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @size.setter
    def size(self, value: primitives.Float3) -> None:
        """Set the Size field value."""
        member = self.get_member("Size")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Size", fields.FieldFloat3(value=value)
            )

    @property
    def blend_distance(self) -> primitives.Float | None:
        """The BlendDistance field value."""
        member = self.get_member("BlendDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @blend_distance.setter
    def blend_distance(self, value: primitives.Float) -> None:
        """Set the BlendDistance field value."""
        member = self.get_member("BlendDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BlendDistance", fields.FieldFloat(value=value)
            )

    @property
    def blend_distance_mode(self) -> SpatialVariableBlendDistanceMode | None:
        """The BlendDistanceMode enum value."""
        member = self.get_member("BlendDistanceMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return SpatialVariableBlendDistanceMode(member.value)
        return None

    @blend_distance_mode.setter
    def blend_distance_mode(self, value: SpatialVariableBlendDistanceMode | str) -> None:
        """Set the BlendDistanceMode enum value."""
        member = self.get_member("BlendDistanceMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "BlendDistanceMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def texture(self) -> str | None:
        """Target ID of the Texture reference (targets IAssetProvider[Texture3D])."""
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @texture.setter
    def texture(self, target: str | IAssetProvider[Texture3D] | None) -> None:
        """Set the Texture reference by target ID or IAssetProvider[Texture3D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Texture")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Texture",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture3D>'),
            )

    @property
    def use_normalized_coordinates(self) -> primitives.Bool | None:
        """The UseNormalizedCoordinates field value."""
        member = self.get_member("UseNormalizedCoordinates")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_normalized_coordinates.setter
    def use_normalized_coordinates(self, value: primitives.Bool) -> None:
        """Set the UseNormalizedCoordinates field value."""
        member = self.get_member("UseNormalizedCoordinates")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseNormalizedCoordinates", fields.FieldBool(value=value)
            )

    @property
    def scale(self) -> primitives.Float3 | None:
        """The Scale field value."""
        member = self.get_member("Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale.setter
    def scale(self, value: primitives.Float3) -> None:
        """Set the Scale field value."""
        member = self.get_member("Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Scale", fields.FieldFloat3(value=value)
            )

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
    def wrap_u(self) -> WrapMode | None:
        """The WrapU enum value."""
        member = self.get_member("WrapU")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return WrapMode(member.value)
        return None

    @wrap_u.setter
    def wrap_u(self, value: WrapMode | str) -> None:
        """Set the WrapU enum value."""
        member = self.get_member("WrapU")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "WrapU",
                members.FieldEnum(value=str(value)),
            )

    @property
    def wrap_v(self) -> WrapMode | None:
        """The WrapV enum value."""
        member = self.get_member("WrapV")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return WrapMode(member.value)
        return None

    @wrap_v.setter
    def wrap_v(self, value: WrapMode | str) -> None:
        """Set the WrapV enum value."""
        member = self.get_member("WrapV")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "WrapV",
                members.FieldEnum(value=str(value)),
            )

    @property
    def wrap_w(self) -> WrapMode | None:
        """The WrapW enum value."""
        member = self.get_member("WrapW")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return WrapMode(member.value)
        return None

    @wrap_w.setter
    def wrap_w(self, value: WrapMode | str) -> None:
        """Set the WrapW enum value."""
        member = self.get_member("WrapW")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "WrapW",
                members.FieldEnum(value=str(value)),
            )

