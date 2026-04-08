"""Generated component: FileVisual."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.file_metadata import FileMetadata
from pyresonitelink.generated._types.text_renderer import TextRenderer
from pyresonitelink.generated._types.pbs_dual_sided_metallic import PBS_DualSidedMetallic
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FileVisual(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FileVisual.

    Category: Utility
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FileVisual"

    def __init__(self, metadata_source: str | FileMetadata | None = None, type_label: str | TextRenderer | None = None, name_label: str | TextRenderer | None = None, fill_material: str | PBS_DualSidedMetallic | None = None, outline_material: str | PBS_DualSidedMetallic | None = None, type_material: str | PBS_DualSidedMetallic | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            metadata_source: Initial value for MetadataSource.
            type_label: Initial value for TypeLabel.
            name_label: Initial value for NameLabel.
            fill_material: Initial value for FillMaterial.
            outline_material: Initial value for OutlineMaterial.
            type_material: Initial value for TypeMaterial.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if metadata_source is not None:
            self.metadata_source = metadata_source
        if type_label is not None:
            self.type_label = type_label
        if name_label is not None:
            self.name_label = name_label
        if fill_material is not None:
            self.fill_material = fill_material
        if outline_material is not None:
            self.outline_material = outline_material
        if type_material is not None:
            self.type_material = type_material

    @property
    def metadata_source(self) -> str | None:
        """Target ID of the MetadataSource reference (targets FileMetadata)."""
        member = self.get_member("MetadataSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @metadata_source.setter
    def metadata_source(self, target: str | FileMetadata | None) -> None:
        """Set the MetadataSource reference by target ID or FileMetadata instance."""
        target_id: str | None = target.id if isinstance(target, FileMetadata) else target  # type: ignore[assignment]
        member = self.get_member("MetadataSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MetadataSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FileMetadata'),
            )

    @property
    def type_label(self) -> str | None:
        """Target ID of the TypeLabel reference (targets TextRenderer)."""
        member = self.get_member("TypeLabel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @type_label.setter
    def type_label(self, target: str | TextRenderer | None) -> None:
        """Set the TypeLabel reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("TypeLabel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TypeLabel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def name_label(self) -> str | None:
        """Target ID of the NameLabel reference (targets TextRenderer)."""
        member = self.get_member("NameLabel")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @name_label.setter
    def name_label(self, target: str | TextRenderer | None) -> None:
        """Set the NameLabel reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("NameLabel")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NameLabel",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def fill_material(self) -> str | None:
        """Target ID of the FillMaterial reference (targets PBS_DualSidedMetallic)."""
        member = self.get_member("FillMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @fill_material.setter
    def fill_material(self, target: str | PBS_DualSidedMetallic | None) -> None:
        """Set the FillMaterial reference by target ID or PBS_DualSidedMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_DualSidedMetallic) else target  # type: ignore[assignment]
        member = self.get_member("FillMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "FillMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_DualSidedMetallic'),
            )

    @property
    def outline_material(self) -> str | None:
        """Target ID of the OutlineMaterial reference (targets PBS_DualSidedMetallic)."""
        member = self.get_member("OutlineMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @outline_material.setter
    def outline_material(self, target: str | PBS_DualSidedMetallic | None) -> None:
        """Set the OutlineMaterial reference by target ID or PBS_DualSidedMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_DualSidedMetallic) else target  # type: ignore[assignment]
        member = self.get_member("OutlineMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "OutlineMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_DualSidedMetallic'),
            )

    @property
    def type_material(self) -> str | None:
        """Target ID of the TypeMaterial reference (targets PBS_DualSidedMetallic)."""
        member = self.get_member("TypeMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @type_material.setter
    def type_material(self, target: str | PBS_DualSidedMetallic | None) -> None:
        """Set the TypeMaterial reference by target ID or PBS_DualSidedMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_DualSidedMetallic) else target  # type: ignore[assignment]
        member = self.get_member("TypeMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TypeMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_DualSidedMetallic'),
            )

