"""Generated component: FontCollection."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FontCollection(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The FontCollection component acts as a set of fonts that can be used to make one mega font. When a font in the set does not have a character for a unicode point, another font can take over.

    Category: Rendering/Text

    Used to combine fonts
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FontCollection"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration

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
    def font_sets(self) -> members.SyncList | None:
        """The list of fonts to congregate into one huge font."""
        member = self.get_member("FontSets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @font_sets.setter
    def font_sets(self, value: members.SyncList) -> None:
        """Set FontSets. The list of fonts to congregate into one huge font."""
        self.set_member("FontSets", value)

