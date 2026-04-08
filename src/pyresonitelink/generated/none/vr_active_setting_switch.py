"""Generated component: VR_ActiveSettingSwitch."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent


class VR_ActiveSettingSwitch(GeneratedComponent):
    """Wrapper for [FrooxEngine]FrooxEngine.VR_ActiveSettingSwitch.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VR_ActiveSettingSwitch"

    def __init__(self, vr_active: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            vr_active: Initial value for VR_Active.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if vr_active is not None:
            self.vr_active = vr_active

    @property
    def vr_active(self) -> primitives.Bool | None:
        """The VR_Active field value."""
        member = self.get_member("VR_Active")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @vr_active.setter
    def vr_active(self, value: primitives.Bool) -> None:
        """Set the VR_Active field value."""
        member = self.get_member("VR_Active")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "VR_Active", fields.FieldBool(value=value)
            )

