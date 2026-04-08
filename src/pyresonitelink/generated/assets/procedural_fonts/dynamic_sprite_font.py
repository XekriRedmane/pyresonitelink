"""Generated component: DynamicSpriteFont."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DynamicSpriteFont(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DynamicSpriteFont.

    Category: Assets/Procedural Fonts
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DynamicSpriteFont"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, max_size: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            max_size: Initial value for MaxSize.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if max_size is not None:
            self.max_size = max_size

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
    def max_size(self) -> primitives.Int | None:
        """The MaxSize field value."""
        member = self.get_member("MaxSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_size.setter
    def max_size(self, value: primitives.Int) -> None:
        """Set the MaxSize field value."""
        member = self.get_member("MaxSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSize", fields.FieldInt(value=value)
            )

    @property
    def glyphs(self) -> members.SyncList | None:
        """The Glyphs member."""
        member = self.get_member("Glyphs")
        if isinstance(member, members.SyncList):
            return member
        return None

    @glyphs.setter
    def glyphs(self, value: members.SyncList) -> None:
        """Set the Glyphs member."""
        self.set_member("Glyphs", value)

