"""Generated component: FullBodyCalibratorDialog."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.page import Page
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.full_body_calibrator import FullBodyCalibrator
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.slider import Slider
from pyresonitelink.generated._types.checkbox import Checkbox
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.quantity_text_editor_parser import QuantityTextEditorParser
from pyresonitelink.generated._types.slide_swap_region import SlideSwapRegion
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FullBodyCalibratorDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """See Full Body Tracking.

    See Full Body Tracking.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FullBodyCalibratorDialog"

    def __init__(self, calibrator: str | FullBodyCalibrator | None = None, current_page: Page | str | None = None, confirm_trackers: str | Button | None = None, reset_trackers: str | Button | None = None, calibrate_avatar: str | Button | None = None, height_compensation: str | Slider[primitives.Float] | None = None, use_symmetry: str | Checkbox | None = None, show_body_overlay: str | Checkbox | None = None, show_avatar_overlay: str | Checkbox | None = None, hips_mapping: str | Text | None = None, feet_mapping: str | Text | None = None, chest_mapping: str | Text | None = None, elbows_mapping: str | Text | None = None, knees_mapping: str | Text | None = None, height_field: str | QuantityTextEditorParser | None = None, height_warning: str | Text | None = None, use_imperial: primitives.Bool | None = None, swap_region: str | SlideSwapRegion | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            calibrator: Initial value for _calibrator.
            current_page: Initial value for _currentPage.
            confirm_trackers: Initial value for _confirmTrackers.
            reset_trackers: Initial value for _resetTrackers.
            calibrate_avatar: Initial value for _calibrateAvatar.
            height_compensation: Initial value for _heightCompensation.
            use_symmetry: Initial value for _useSymmetry.
            show_body_overlay: Initial value for _showBodyOverlay.
            show_avatar_overlay: Initial value for _showAvatarOverlay.
            hips_mapping: Initial value for _hipsMapping.
            feet_mapping: Initial value for _feetMapping.
            chest_mapping: Initial value for _chestMapping.
            elbows_mapping: Initial value for _elbowsMapping.
            knees_mapping: Initial value for _kneesMapping.
            height_field: Initial value for _heightField.
            height_warning: Initial value for _heightWarning.
            use_imperial: Initial value for _useImperial.
            swap_region: Initial value for _swapRegion.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if calibrator is not None:
            self.calibrator = calibrator
        if current_page is not None:
            self.current_page = current_page
        if confirm_trackers is not None:
            self.confirm_trackers = confirm_trackers
        if reset_trackers is not None:
            self.reset_trackers = reset_trackers
        if calibrate_avatar is not None:
            self.calibrate_avatar = calibrate_avatar
        if height_compensation is not None:
            self.height_compensation = height_compensation
        if use_symmetry is not None:
            self.use_symmetry = use_symmetry
        if show_body_overlay is not None:
            self.show_body_overlay = show_body_overlay
        if show_avatar_overlay is not None:
            self.show_avatar_overlay = show_avatar_overlay
        if hips_mapping is not None:
            self.hips_mapping = hips_mapping
        if feet_mapping is not None:
            self.feet_mapping = feet_mapping
        if chest_mapping is not None:
            self.chest_mapping = chest_mapping
        if elbows_mapping is not None:
            self.elbows_mapping = elbows_mapping
        if knees_mapping is not None:
            self.knees_mapping = knees_mapping
        if height_field is not None:
            self.height_field = height_field
        if height_warning is not None:
            self.height_warning = height_warning
        if use_imperial is not None:
            self.use_imperial = use_imperial
        if swap_region is not None:
            self.swap_region = swap_region

    @property
    def calibrator(self) -> str | None:
        """The current calibrator this dialog is linked to."""
        member = self.get_member("_calibrator")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @calibrator.setter
    def calibrator(self, target: str | FullBodyCalibrator | None) -> None:
        """Set the _calibrator reference by target ID or FullBodyCalibrator instance."""
        target_id: str | None = target.id if isinstance(target, FullBodyCalibrator) else target  # type: ignore[assignment]
        member = self.get_member("_calibrator")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_calibrator",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FullBodyCalibrator'),
            )

    @property
    def current_page(self) -> Page | None:
        """The current dialog page this is showing."""
        member = self.get_member("_currentPage")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Page(member.value)
        return None

    @current_page.setter
    def current_page(self, value: Page | str) -> None:
        """Set _currentPage. The current dialog page this is showing."""
        member = self.get_member("_currentPage")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_currentPage",
                members.FieldEnum(value=str(value)),
            )

    @property
    def confirm_trackers(self) -> str | None:
        """The button to confirm trackers."""
        member = self.get_member("_confirmTrackers")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @confirm_trackers.setter
    def confirm_trackers(self, target: str | Button | None) -> None:
        """Set the _confirmTrackers reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_confirmTrackers")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_confirmTrackers",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def reset_trackers(self) -> str | None:
        """The button to reset tracker mappings."""
        member = self.get_member("_resetTrackers")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reset_trackers.setter
    def reset_trackers(self, target: str | Button | None) -> None:
        """Set the _resetTrackers reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_resetTrackers")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_resetTrackers",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def calibrate_avatar(self) -> str | None:
        """The button to start avatar calibration"""
        member = self.get_member("_calibrateAvatar")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @calibrate_avatar.setter
    def calibrate_avatar(self, target: str | Button | None) -> None:
        """Set the _calibrateAvatar reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_calibrateAvatar")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_calibrateAvatar",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def height_compensation(self) -> str | None:
        """How much to scale up the avatar to fit the user."""
        member = self.get_member("_heightCompensation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @height_compensation.setter
    def height_compensation(self, target: str | Slider[primitives.Float] | None) -> None:
        """Set the _heightCompensation reference by target ID or Slider[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, Slider) else target  # type: ignore[assignment]
        member = self.get_member("_heightCompensation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_heightCompensation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Slider<float>'),
            )

    @property
    def use_symmetry(self) -> str | None:
        """Whether changes to sided points (left versus right) mirror onto the other side."""
        member = self.get_member("_useSymmetry")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @use_symmetry.setter
    def use_symmetry(self, target: str | Checkbox | None) -> None:
        """Set the _useSymmetry reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_useSymmetry")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_useSymmetry",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def show_body_overlay(self) -> str | None:
        """Whether to show the invisible person Overlay."""
        member = self.get_member("_showBodyOverlay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @show_body_overlay.setter
    def show_body_overlay(self, target: str | Checkbox | None) -> None:
        """Set the _showBodyOverlay reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_showBodyOverlay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_showBodyOverlay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def show_avatar_overlay(self) -> str | None:
        """Whether to show a copy of the avatar on the pedestal."""
        member = self.get_member("_showAvatarOverlay")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @show_avatar_overlay.setter
    def show_avatar_overlay(self, target: str | Checkbox | None) -> None:
        """Set the _showAvatarOverlay reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_showAvatarOverlay")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_showAvatarOverlay",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def hips_mapping(self) -> str | None:
        """The text to indicate if hips are mapped or not."""
        member = self.get_member("_hipsMapping")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @hips_mapping.setter
    def hips_mapping(self, target: str | Text | None) -> None:
        """Set the _hipsMapping reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_hipsMapping")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_hipsMapping",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def feet_mapping(self) -> str | None:
        """The text to indicate if feet are mapped or not."""
        member = self.get_member("_feetMapping")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @feet_mapping.setter
    def feet_mapping(self, target: str | Text | None) -> None:
        """Set the _feetMapping reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_feetMapping")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_feetMapping",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def chest_mapping(self) -> str | None:
        """The text to indicate if chest is mapped or not."""
        member = self.get_member("_chestMapping")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @chest_mapping.setter
    def chest_mapping(self, target: str | Text | None) -> None:
        """Set the _chestMapping reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_chestMapping")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_chestMapping",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def elbows_mapping(self) -> str | None:
        """The text to indicate if elbows are mapped or not."""
        member = self.get_member("_elbowsMapping")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @elbows_mapping.setter
    def elbows_mapping(self, target: str | Text | None) -> None:
        """Set the _elbowsMapping reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_elbowsMapping")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_elbowsMapping",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def knees_mapping(self) -> str | None:
        """The text to indicate if knees are mapped or not."""
        member = self.get_member("_kneesMapping")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @knees_mapping.setter
    def knees_mapping(self, target: str | Text | None) -> None:
        """Set the _kneesMapping reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_kneesMapping")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_kneesMapping",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def height_field(self) -> str | None:
        """The text field that changes your user height setting on the fly."""
        member = self.get_member("_heightField")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @height_field.setter
    def height_field(self, target: str | QuantityTextEditorParser | None) -> None:
        """Set the _heightField reference by target ID or QuantityTextEditorParser instance."""
        target_id: str | None = target.id if isinstance(target, QuantityTextEditorParser) else target  # type: ignore[assignment]
        member = self.get_member("_heightField")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_heightField",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.QuantityTextEditorParser<,>'),
            )

    @property
    def height_warning(self) -> str | None:
        """The text to warn if the height is improper."""
        member = self.get_member("_heightWarning")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @height_warning.setter
    def height_warning(self, target: str | Text | None) -> None:
        """Set the _heightWarning reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_heightWarning")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_heightWarning",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

    @property
    def use_imperial(self) -> primitives.Bool | None:
        """Whether the height should be interpreted in yee haw (imperal height)."""
        member = self.get_member("_useImperial")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_imperial.setter
    def use_imperial(self, value: primitives.Bool) -> None:
        """Set the _useImperial field value."""
        member = self.get_member("_useImperial")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_useImperial", fields.FieldBool(value=value)
            )

    @property
    def swap_region(self) -> str | None:
        """The component that handles transitions from one page to another on the dialog."""
        member = self.get_member("_swapRegion")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @swap_region.setter
    def swap_region(self, target: str | SlideSwapRegion | None) -> None:
        """Set the _swapRegion reference by target ID or SlideSwapRegion instance."""
        target_id: str | None = target.id if isinstance(target, SlideSwapRegion) else target  # type: ignore[assignment]
        member = self.get_member("_swapRegion")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_swapRegion",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.SlideSwapRegion'),
            )

