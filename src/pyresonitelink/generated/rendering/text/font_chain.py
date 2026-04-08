"""Generated component: FontChain."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.font import Font
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FontChain(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.FontChain.

    Category: Rendering/Text
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FontChain"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, main_font: str | IAssetProvider[Font] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            main_font: Initial value for MainFont.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if main_font is not None:
            self.main_font = main_font

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
    def main_font(self) -> str | None:
        """Target ID of the MainFont reference (targets IAssetProvider[Font])."""
        member = self.get_member("MainFont")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @main_font.setter
    def main_font(self, target: str | IAssetProvider[Font] | None) -> None:
        """Set the MainFont reference by target ID or IAssetProvider[Font] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("MainFont")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MainFont",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Font>'),
            )

    @property
    def fallback_fonts(self) -> members.SyncList | None:
        """The FallbackFonts member."""
        member = self.get_member("FallbackFonts")
        if isinstance(member, members.SyncList):
            return member
        return None

    @fallback_fonts.setter
    def fallback_fonts(self, value: members.SyncList) -> None:
        """Set the FallbackFonts member."""
        self.set_member("FallbackFonts", value)

