"""Generated component: ColorToColorX."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.color_profile import ColorProfile
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ColorToColorX(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ColorToColorX.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ColorToColorX"

    def __init__(self, source_color: str | IField[primitives.Color] | None = None, source_profile: str | IField[ColorProfile] | None = None, target: str | IField[primitives.ColorX] | None = None, write_back: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            source_color: Initial value for SourceColor.
            source_profile: Initial value for SourceProfile.
            target: Initial value for Target.
            write_back: Initial value for WriteBack.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if source_color is not None:
            self.source_color = source_color
        if source_profile is not None:
            self.source_profile = source_profile
        if target is not None:
            self.target = target
        if write_back is not None:
            self.write_back = write_back

    @property
    def source_color(self) -> str | None:
        """Target ID of the SourceColor reference (targets IField[primitives.Color])."""
        member = self.get_member("SourceColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source_color.setter
    def source_color(self, target: str | IField[primitives.Color] | None) -> None:
        """Set the SourceColor reference by target ID or IField[primitives.Color] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SourceColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SourceColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<color>'),
            )

    @property
    def source_profile(self) -> str | None:
        """Target ID of the SourceProfile reference (targets IField[ColorProfile])."""
        member = self.get_member("SourceProfile")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @source_profile.setter
    def source_profile(self, target: str | IField[ColorProfile] | None) -> None:
        """Set the SourceProfile reference by target ID or IField[ColorProfile] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("SourceProfile")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "SourceProfile",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<[Renderite.Shared]Renderite.Shared.ColorProfile>'),
            )

    @property
    def default_profile(self) -> members.FieldEnum | None:
        """The DefaultProfile member."""
        member = self.get_member("DefaultProfile")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @default_profile.setter
    def default_profile(self, value: members.FieldEnum) -> None:
        """Set the DefaultProfile member."""
        self.set_member("DefaultProfile", value)

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[primitives.ColorX])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the Target reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def write_back(self) -> bool | None:
        """The WriteBack field value."""
        member = self.get_member("WriteBack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @write_back.setter
    def write_back(self, value: bool) -> None:
        """Set the WriteBack field value."""
        member = self.get_member("WriteBack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WriteBack", fields.FieldBool(value=value)
            )

