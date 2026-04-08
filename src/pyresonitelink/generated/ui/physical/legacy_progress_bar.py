"""Generated component: LegacyProgressBar."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.legacy_ui_style import LegacyUIStyle
from pyresonitelink.generated._types.bevel_stripe_mesh import BevelStripeMesh
from pyresonitelink.generated._types.pbs_rim_metallic import PBS_RimMetallic
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyProgressBar(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacyProgressBar.

    Category: UI/Physical
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyProgressBar"

    def __init__(self, style: str | LegacyUIStyle | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, is_enabled_field: primitives.Bool | None = None, progress: primitives.Float | None = None, bar_color_field: primitives.ColorX | None = None, container_color_field: primitives.ColorX | None = None, width_field: primitives.Float | None = None, height_field: primitives.Float | None = None, thickness_field: primitives.Float | None = None, slant_field: primitives.Float | None = None, bar_mesh: str | BevelStripeMesh | None = None, container_mesh: str | BevelStripeMesh | None = None, bar_material: str | PBS_RimMetallic | None = None, container_material: str | PBS_RimMetallic | None = None, bar_position: str | IField[primitives.Float3] | None = None, collider_size: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            style: Initial value for Style.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            is_enabled_field: Initial value for IsEnabledField.
            progress: Initial value for Progress.
            bar_color_field: Initial value for BarColorField.
            container_color_field: Initial value for ContainerColorField.
            width_field: Initial value for WidthField.
            height_field: Initial value for HeightField.
            thickness_field: Initial value for ThicknessField.
            slant_field: Initial value for SlantField.
            bar_mesh: Initial value for _barMesh.
            container_mesh: Initial value for _containerMesh.
            bar_material: Initial value for _barMaterial.
            container_material: Initial value for _containerMaterial.
            bar_position: Initial value for _barPosition.
            collider_size: Initial value for _colliderSize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if style is not None:
            self.style = style
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if is_enabled_field is not None:
            self.is_enabled_field = is_enabled_field
        if progress is not None:
            self.progress = progress
        if bar_color_field is not None:
            self.bar_color_field = bar_color_field
        if container_color_field is not None:
            self.container_color_field = container_color_field
        if width_field is not None:
            self.width_field = width_field
        if height_field is not None:
            self.height_field = height_field
        if thickness_field is not None:
            self.thickness_field = thickness_field
        if slant_field is not None:
            self.slant_field = slant_field
        if bar_mesh is not None:
            self.bar_mesh = bar_mesh
        if container_mesh is not None:
            self.container_mesh = container_mesh
        if bar_material is not None:
            self.bar_material = bar_material
        if container_material is not None:
            self.container_material = container_material
        if bar_position is not None:
            self.bar_position = bar_position
        if collider_size is not None:
            self.collider_size = collider_size

    @property
    def style(self) -> str | None:
        """Target ID of the Style reference (targets LegacyUIStyle)."""
        member = self.get_member("Style")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @style.setter
    def style(self, target: str | LegacyUIStyle | None) -> None:
        """Set the Style reference by target ID or LegacyUIStyle instance."""
        target_id: str | None = target.id if isinstance(target, LegacyUIStyle) else target  # type: ignore[assignment]
        member = self.get_member("Style")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Style",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyUIStyle'),
            )

    @property
    def accept_physical_touch(self) -> primitives.Bool | None:
        """The AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_physical_touch.setter
    def accept_physical_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptPhysicalTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_remote_touch(self) -> primitives.Bool | None:
        """The AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_remote_touch.setter
    def accept_remote_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptRemoteTouch", fields.FieldBool(value=value)
            )

    @property
    def is_enabled_field(self) -> primitives.Bool | None:
        """The IsEnabledField field value."""
        member = self.get_member("IsEnabledField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_enabled_field.setter
    def is_enabled_field(self, value: primitives.Bool) -> None:
        """Set the IsEnabledField field value."""
        member = self.get_member("IsEnabledField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsEnabledField", fields.FieldBool(value=value)
            )

    @property
    def progress(self) -> primitives.Float | None:
        """The Progress field value."""
        member = self.get_member("Progress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @progress.setter
    def progress(self, value: primitives.Float) -> None:
        """Set the Progress field value."""
        member = self.get_member("Progress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Progress", fields.FieldFloat(value=value)
            )

    @property
    def bar_color_field(self) -> primitives.ColorX | None:
        """The BarColorField field value."""
        member = self.get_member("BarColorField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @bar_color_field.setter
    def bar_color_field(self, value: primitives.ColorX) -> None:
        """Set the BarColorField field value."""
        member = self.get_member("BarColorField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BarColorField", fields.FieldColorX(value=value)
            )

    @property
    def container_color_field(self) -> primitives.ColorX | None:
        """The ContainerColorField field value."""
        member = self.get_member("ContainerColorField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @container_color_field.setter
    def container_color_field(self, value: primitives.ColorX) -> None:
        """Set the ContainerColorField field value."""
        member = self.get_member("ContainerColorField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ContainerColorField", fields.FieldColorX(value=value)
            )

    @property
    def width_field(self) -> primitives.Float | None:
        """The WidthField field value."""
        member = self.get_member("WidthField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @width_field.setter
    def width_field(self, value: primitives.Float) -> None:
        """Set the WidthField field value."""
        member = self.get_member("WidthField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WidthField", fields.FieldFloat(value=value)
            )

    @property
    def height_field(self) -> primitives.Float | None:
        """The HeightField field value."""
        member = self.get_member("HeightField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height_field.setter
    def height_field(self, value: primitives.Float) -> None:
        """Set the HeightField field value."""
        member = self.get_member("HeightField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeightField", fields.FieldFloat(value=value)
            )

    @property
    def thickness_field(self) -> primitives.Float | None:
        """The ThicknessField field value."""
        member = self.get_member("ThicknessField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @thickness_field.setter
    def thickness_field(self, value: primitives.Float) -> None:
        """Set the ThicknessField field value."""
        member = self.get_member("ThicknessField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ThicknessField", fields.FieldFloat(value=value)
            )

    @property
    def slant_field(self) -> primitives.Float | None:
        """The SlantField field value."""
        member = self.get_member("SlantField")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @slant_field.setter
    def slant_field(self, value: primitives.Float) -> None:
        """Set the SlantField field value."""
        member = self.get_member("SlantField")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SlantField", fields.FieldFloat(value=value)
            )

    @property
    def bar_mesh(self) -> str | None:
        """Target ID of the _barMesh reference (targets BevelStripeMesh)."""
        member = self.get_member("_barMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bar_mesh.setter
    def bar_mesh(self, target: str | BevelStripeMesh | None) -> None:
        """Set the _barMesh reference by target ID or BevelStripeMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelStripeMesh) else target  # type: ignore[assignment]
        member = self.get_member("_barMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_barMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelStripeMesh'),
            )

    @property
    def container_mesh(self) -> str | None:
        """Target ID of the _containerMesh reference (targets BevelStripeMesh)."""
        member = self.get_member("_containerMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @container_mesh.setter
    def container_mesh(self, target: str | BevelStripeMesh | None) -> None:
        """Set the _containerMesh reference by target ID or BevelStripeMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelStripeMesh) else target  # type: ignore[assignment]
        member = self.get_member("_containerMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_containerMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelStripeMesh'),
            )

    @property
    def bar_material(self) -> str | None:
        """Target ID of the _barMaterial reference (targets PBS_RimMetallic)."""
        member = self.get_member("_barMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bar_material.setter
    def bar_material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _barMaterial reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_barMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_barMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

    @property
    def container_material(self) -> str | None:
        """Target ID of the _containerMaterial reference (targets PBS_RimMetallic)."""
        member = self.get_member("_containerMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @container_material.setter
    def container_material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _containerMaterial reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_containerMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_containerMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

    @property
    def bar_position(self) -> str | None:
        """Target ID of the _barPosition reference (targets IField[primitives.Float3])."""
        member = self.get_member("_barPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bar_position.setter
    def bar_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _barPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_barPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_barPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def collider_size(self) -> str | None:
        """Target ID of the _colliderSize reference (targets IField[primitives.Float3])."""
        member = self.get_member("_colliderSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @collider_size.setter
    def collider_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _colliderSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_colliderSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_colliderSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

