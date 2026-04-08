"""Generated component: OBSSettings."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector


class OBSSettings(GeneratedComponent, ICustomInspector):
    """Wrapper for [FrooxEngine]FrooxEngine.OBSSettings.

    Category: Misc
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.OBSSettings"

    def __init__(self, auto_mirror: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            auto_mirror: Initial value for AutoMirror.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if auto_mirror is not None:
            self.auto_mirror = auto_mirror

    @property
    def auto_mirror(self) -> primitives.Bool | None:
        """The AutoMirror field value."""
        member = self.get_member("AutoMirror")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_mirror.setter
    def auto_mirror(self, value: primitives.Bool) -> None:
        """Set the AutoMirror field value."""
        member = self.get_member("AutoMirror")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoMirror", fields.FieldBool(value=value)
            )

    async def reset_to_default(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the ResetToDefault sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ResetToDefault", {}, debug,
        )

