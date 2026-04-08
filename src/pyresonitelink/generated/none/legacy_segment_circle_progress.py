"""Generated component: LegacySegmentCircleProgress."""

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.text_renderer import TextRenderer
from pyresonitelink.generated._types.unlit_material import UnlitMaterial
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacySegmentCircleProgress(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacySegmentCircleProgress.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacySegmentCircleProgress"

    def __init__(self, progress_text: str | TextRenderer | None = None, detail_text: str | TextRenderer | None = None, material: str | UnlitMaterial | None = None, tint: str | IField[primitives.ColorX] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            progress_text: Initial value for _progressText.
            detail_text: Initial value for _detailText.
            material: Initial value for _material.
            tint: Initial value for _tint.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if progress_text is not None:
            self.progress_text = progress_text
        if detail_text is not None:
            self.detail_text = detail_text
        if material is not None:
            self.material = material
        if tint is not None:
            self.tint = tint

    @property
    def stage(self) -> members.FieldEnum | None:
        """The Stage member."""
        member = self.get_member("Stage")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @stage.setter
    def stage(self, value: members.FieldEnum) -> None:
        """Set the Stage member."""
        self.set_member("Stage", value)

    @property
    def progress_text(self) -> str | None:
        """Target ID of the _progressText reference (targets TextRenderer)."""
        member = self.get_member("_progressText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @progress_text.setter
    def progress_text(self, target: str | TextRenderer | None) -> None:
        """Set the _progressText reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_progressText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_progressText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def detail_text(self) -> str | None:
        """Target ID of the _detailText reference (targets TextRenderer)."""
        member = self.get_member("_detailText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @detail_text.setter
    def detail_text(self, target: str | TextRenderer | None) -> None:
        """Set the _detailText reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_detailText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_detailText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def material(self) -> str | None:
        """Target ID of the _material reference (targets UnlitMaterial)."""
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | UnlitMaterial | None) -> None:
        """Set the _material reference by target ID or UnlitMaterial instance."""
        target_id: str | None = target.id if isinstance(target, UnlitMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UnlitMaterial'),
            )

    @property
    def tint(self) -> str | None:
        """Target ID of the _tint reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_tint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tint.setter
    def tint(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _tint reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_tint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_tint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

