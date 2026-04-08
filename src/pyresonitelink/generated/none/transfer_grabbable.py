"""Generated component: TransferGrabbable."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.fresnel_material import FresnelMaterial
from pyresonitelink.generated._types.igrabbable import IGrabbable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TransferGrabbable(GeneratedComponent, IGrabbable, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.TransferGrabbable.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TransferGrabbable"

    def __init__(self, paste_on_grab: bool | None = None, indicator_material: str | FresnelMaterial | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            paste_on_grab: Initial value for PasteOnGrab.
            indicator_material: Initial value for _indicatorMaterial.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if paste_on_grab is not None:
            self.paste_on_grab = paste_on_grab
        if indicator_material is not None:
            self.indicator_material = indicator_material

    @property
    def paste_on_grab(self) -> bool | None:
        """The PasteOnGrab field value."""
        member = self.get_member("PasteOnGrab")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @paste_on_grab.setter
    def paste_on_grab(self, value: bool) -> None:
        """Set the PasteOnGrab field value."""
        member = self.get_member("PasteOnGrab")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PasteOnGrab", fields.FieldBool(value=value)
            )

    @property
    def indicator_material(self) -> str | None:
        """Target ID of the _indicatorMaterial reference (targets FresnelMaterial)."""
        member = self.get_member("_indicatorMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @indicator_material.setter
    def indicator_material(self, target: str | FresnelMaterial | None) -> None:
        """Set the _indicatorMaterial reference by target ID or FresnelMaterial instance."""
        target_id: str | None = target.id if isinstance(target, FresnelMaterial) else target  # type: ignore[assignment]
        member = self.get_member("_indicatorMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_indicatorMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FresnelMaterial'),
            )

