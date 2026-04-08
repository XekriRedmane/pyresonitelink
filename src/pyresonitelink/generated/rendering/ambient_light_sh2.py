"""Generated component: AmbientLightSH2."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AmbientLightSH2(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.AmbientLightSH2.

    Category: Rendering
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AmbientLightSH2"

    def __init__(self, is_active: bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            is_active: Initial value for IsActive.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if is_active is not None:
            self.is_active = is_active

    @property
    def ambient_light(self) -> members.FieldEnum | None:
        """The AmbientLight member."""
        member = self.get_member("AmbientLight")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @ambient_light.setter
    def ambient_light(self, value: members.FieldEnum) -> None:
        """Set the AmbientLight member."""
        self.set_member("AmbientLight", value)

    @property
    def is_active(self) -> bool | None:
        """The IsActive field value."""
        member = self.get_member("IsActive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_active.setter
    def is_active(self, value: bool) -> None:
        """Set the IsActive field value."""
        member = self.get_member("IsActive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsActive", fields.FieldBool(value=value)
            )

    async def set_active(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the SetActive sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "SetActive", {}, debug,
        )

