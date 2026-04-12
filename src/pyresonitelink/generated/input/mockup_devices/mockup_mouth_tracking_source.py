"""Generated component: MockupMouthTrackingSource."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.imouth_tracking_source_component import IMouthTrackingSourceComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MockupMouthTrackingSource(GeneratedComponent, IMouthTrackingSourceComponent, IWorldEventReceiver):
    """The MockupMouthTrackingSource component can be used to simulate the tracking data of a tracking device and be applied to any field that takes a IMouthTrackingSourceComponent.

    Category: Input/Mockup Devices

    Attach to a slot and insert the component into another Component on an
    avatar like an AvatarExpressionDriver to test its value influences.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MockupMouthTrackingSource"

    def __init__(self, jaw: primitives.Float3 | None = None, jaw_open: primitives.Float | None = None, tongue: primitives.Float3 | None = None, tongue_roll: primitives.Float | None = None, lip_upper_left_raise: primitives.Float | None = None, lip_upper_right_raise: primitives.Float | None = None, lip_lower_left_raise: primitives.Float | None = None, lip_lower_right_raise: primitives.Float | None = None, lip_upper_horizontal: primitives.Float | None = None, lip_lower_horizontal: primitives.Float | None = None, mouth_left_smile_frown: primitives.Float | None = None, mouth_right_smile_frown: primitives.Float | None = None, mouth_left_dimple: primitives.Float | None = None, mouth_right_dimple: primitives.Float | None = None, mouth_pout_left: primitives.Float | None = None, mouth_pout_right: primitives.Float | None = None, lip_top_left_overturn: primitives.Float | None = None, lip_top_right_overturn: primitives.Float | None = None, lip_bottom_left_overturn: primitives.Float | None = None, lip_bottom_right_overturn: primitives.Float | None = None, lip_top_left_over_under: primitives.Float | None = None, lip_top_right_over_under: primitives.Float | None = None, lip_bottom_left_over_under: primitives.Float | None = None, lip_bottom_right_over_under: primitives.Float | None = None, lip_left_stretch_tighten: primitives.Float | None = None, lip_right_stretch_tighten: primitives.Float | None = None, lips_left_press: primitives.Float | None = None, lips_right_press: primitives.Float | None = None, cheek_left_puff_suck: primitives.Float | None = None, cheek_right_puff_suck: primitives.Float | None = None, cheek_left_raise: primitives.Float | None = None, cheek_right_raise: primitives.Float | None = None, nose_wrinkle_left: primitives.Float | None = None, nose_wrinkle_right: primitives.Float | None = None, chin_raise_bottom: primitives.Float | None = None, chin_raise_top: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            jaw: Initial value for Jaw.
            jaw_open: Initial value for JawOpen.
            tongue: Initial value for Tongue.
            tongue_roll: Initial value for TongueRoll.
            lip_upper_left_raise: Initial value for LipUpperLeftRaise.
            lip_upper_right_raise: Initial value for LipUpperRightRaise.
            lip_lower_left_raise: Initial value for LipLowerLeftRaise.
            lip_lower_right_raise: Initial value for LipLowerRightRaise.
            lip_upper_horizontal: Initial value for LipUpperHorizontal.
            lip_lower_horizontal: Initial value for LipLowerHorizontal.
            mouth_left_smile_frown: Initial value for MouthLeftSmileFrown.
            mouth_right_smile_frown: Initial value for MouthRightSmileFrown.
            mouth_left_dimple: Initial value for MouthLeftDimple.
            mouth_right_dimple: Initial value for MouthRightDimple.
            mouth_pout_left: Initial value for MouthPoutLeft.
            mouth_pout_right: Initial value for MouthPoutRight.
            lip_top_left_overturn: Initial value for LipTopLeftOverturn.
            lip_top_right_overturn: Initial value for LipTopRightOverturn.
            lip_bottom_left_overturn: Initial value for LipBottomLeftOverturn.
            lip_bottom_right_overturn: Initial value for LipBottomRightOverturn.
            lip_top_left_over_under: Initial value for LipTopLeftOverUnder.
            lip_top_right_over_under: Initial value for LipTopRightOverUnder.
            lip_bottom_left_over_under: Initial value for LipBottomLeftOverUnder.
            lip_bottom_right_over_under: Initial value for LipBottomRightOverUnder.
            lip_left_stretch_tighten: Initial value for LipLeftStretchTighten.
            lip_right_stretch_tighten: Initial value for LipRightStretchTighten.
            lips_left_press: Initial value for LipsLeftPress.
            lips_right_press: Initial value for LipsRightPress.
            cheek_left_puff_suck: Initial value for CheekLeftPuffSuck.
            cheek_right_puff_suck: Initial value for CheekRightPuffSuck.
            cheek_left_raise: Initial value for CheekLeftRaise.
            cheek_right_raise: Initial value for CheekRightRaise.
            nose_wrinkle_left: Initial value for NoseWrinkleLeft.
            nose_wrinkle_right: Initial value for NoseWrinkleRight.
            chin_raise_bottom: Initial value for ChinRaiseBottom.
            chin_raise_top: Initial value for ChinRaiseTop.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if jaw is not None:
            self.jaw = jaw
        if jaw_open is not None:
            self.jaw_open = jaw_open
        if tongue is not None:
            self.tongue = tongue
        if tongue_roll is not None:
            self.tongue_roll = tongue_roll
        if lip_upper_left_raise is not None:
            self.lip_upper_left_raise = lip_upper_left_raise
        if lip_upper_right_raise is not None:
            self.lip_upper_right_raise = lip_upper_right_raise
        if lip_lower_left_raise is not None:
            self.lip_lower_left_raise = lip_lower_left_raise
        if lip_lower_right_raise is not None:
            self.lip_lower_right_raise = lip_lower_right_raise
        if lip_upper_horizontal is not None:
            self.lip_upper_horizontal = lip_upper_horizontal
        if lip_lower_horizontal is not None:
            self.lip_lower_horizontal = lip_lower_horizontal
        if mouth_left_smile_frown is not None:
            self.mouth_left_smile_frown = mouth_left_smile_frown
        if mouth_right_smile_frown is not None:
            self.mouth_right_smile_frown = mouth_right_smile_frown
        if mouth_left_dimple is not None:
            self.mouth_left_dimple = mouth_left_dimple
        if mouth_right_dimple is not None:
            self.mouth_right_dimple = mouth_right_dimple
        if mouth_pout_left is not None:
            self.mouth_pout_left = mouth_pout_left
        if mouth_pout_right is not None:
            self.mouth_pout_right = mouth_pout_right
        if lip_top_left_overturn is not None:
            self.lip_top_left_overturn = lip_top_left_overturn
        if lip_top_right_overturn is not None:
            self.lip_top_right_overturn = lip_top_right_overturn
        if lip_bottom_left_overturn is not None:
            self.lip_bottom_left_overturn = lip_bottom_left_overturn
        if lip_bottom_right_overturn is not None:
            self.lip_bottom_right_overturn = lip_bottom_right_overturn
        if lip_top_left_over_under is not None:
            self.lip_top_left_over_under = lip_top_left_over_under
        if lip_top_right_over_under is not None:
            self.lip_top_right_over_under = lip_top_right_over_under
        if lip_bottom_left_over_under is not None:
            self.lip_bottom_left_over_under = lip_bottom_left_over_under
        if lip_bottom_right_over_under is not None:
            self.lip_bottom_right_over_under = lip_bottom_right_over_under
        if lip_left_stretch_tighten is not None:
            self.lip_left_stretch_tighten = lip_left_stretch_tighten
        if lip_right_stretch_tighten is not None:
            self.lip_right_stretch_tighten = lip_right_stretch_tighten
        if lips_left_press is not None:
            self.lips_left_press = lips_left_press
        if lips_right_press is not None:
            self.lips_right_press = lips_right_press
        if cheek_left_puff_suck is not None:
            self.cheek_left_puff_suck = cheek_left_puff_suck
        if cheek_right_puff_suck is not None:
            self.cheek_right_puff_suck = cheek_right_puff_suck
        if cheek_left_raise is not None:
            self.cheek_left_raise = cheek_left_raise
        if cheek_right_raise is not None:
            self.cheek_right_raise = cheek_right_raise
        if nose_wrinkle_left is not None:
            self.nose_wrinkle_left = nose_wrinkle_left
        if nose_wrinkle_right is not None:
            self.nose_wrinkle_right = nose_wrinkle_right
        if chin_raise_bottom is not None:
            self.chin_raise_bottom = chin_raise_bottom
        if chin_raise_top is not None:
            self.chin_raise_top = chin_raise_top

    @property
    def jaw(self) -> primitives.Float3 | None:
        """The jaw position from rest."""
        member = self.get_member("Jaw")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @jaw.setter
    def jaw(self, value: primitives.Float3) -> None:
        """Set the Jaw field value."""
        member = self.get_member("Jaw")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Jaw", fields.FieldFloat3(value=value)
            )

    @property
    def jaw_open(self) -> primitives.Float | None:
        """The jaw openess."""
        member = self.get_member("JawOpen")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @jaw_open.setter
    def jaw_open(self, value: primitives.Float) -> None:
        """Set the JawOpen field value."""
        member = self.get_member("JawOpen")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "JawOpen", fields.FieldFloat(value=value)
            )

    @property
    def tongue(self) -> primitives.Float3 | None:
        """The tongue position."""
        member = self.get_member("Tongue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tongue.setter
    def tongue(self, value: primitives.Float3) -> None:
        """Set the Tongue field value."""
        member = self.get_member("Tongue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Tongue", fields.FieldFloat3(value=value)
            )

    @property
    def tongue_roll(self) -> primitives.Float | None:
        """The tongue roll into a burrito shape."""
        member = self.get_member("TongueRoll")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @tongue_roll.setter
    def tongue_roll(self, value: primitives.Float) -> None:
        """Set the TongueRoll field value."""
        member = self.get_member("TongueRoll")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TongueRoll", fields.FieldFloat(value=value)
            )

    @property
    def lip_upper_left_raise(self) -> primitives.Float | None:
        """The upper left lip raise amount."""
        member = self.get_member("LipUpperLeftRaise")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lip_upper_left_raise.setter
    def lip_upper_left_raise(self, value: primitives.Float) -> None:
        """Set the LipUpperLeftRaise field value."""
        member = self.get_member("LipUpperLeftRaise")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipUpperLeftRaise", fields.FieldFloat(value=value)
            )

    @property
    def lip_upper_right_raise(self) -> primitives.Float | None:
        """The upper right lip raise amount."""
        member = self.get_member("LipUpperRightRaise")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lip_upper_right_raise.setter
    def lip_upper_right_raise(self, value: primitives.Float) -> None:
        """Set the LipUpperRightRaise field value."""
        member = self.get_member("LipUpperRightRaise")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipUpperRightRaise", fields.FieldFloat(value=value)
            )

    @property
    def lip_lower_left_raise(self) -> primitives.Float | None:
        """The lower left lip raise amount."""
        member = self.get_member("LipLowerLeftRaise")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lip_lower_left_raise.setter
    def lip_lower_left_raise(self, value: primitives.Float) -> None:
        """Set the LipLowerLeftRaise field value."""
        member = self.get_member("LipLowerLeftRaise")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipLowerLeftRaise", fields.FieldFloat(value=value)
            )

    @property
    def lip_lower_right_raise(self) -> primitives.Float | None:
        """The lower right lip raise amount."""
        member = self.get_member("LipLowerRightRaise")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lip_lower_right_raise.setter
    def lip_lower_right_raise(self, value: primitives.Float) -> None:
        """Set the LipLowerRightRaise field value."""
        member = self.get_member("LipLowerRightRaise")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipLowerRightRaise", fields.FieldFloat(value=value)
            )

    @property
    def lip_upper_horizontal(self) -> primitives.Float | None:
        """The shift side to side of the upper lip."""
        member = self.get_member("LipUpperHorizontal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lip_upper_horizontal.setter
    def lip_upper_horizontal(self, value: primitives.Float) -> None:
        """Set the LipUpperHorizontal field value."""
        member = self.get_member("LipUpperHorizontal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipUpperHorizontal", fields.FieldFloat(value=value)
            )

    @property
    def lip_lower_horizontal(self) -> primitives.Float | None:
        """The shift side to side of the lower lip. (negative to positive 1)"""
        member = self.get_member("LipLowerHorizontal")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lip_lower_horizontal.setter
    def lip_lower_horizontal(self, value: primitives.Float) -> None:
        """Set the LipLowerHorizontal field value."""
        member = self.get_member("LipLowerHorizontal")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipLowerHorizontal", fields.FieldFloat(value=value)
            )

    @property
    def mouth_left_smile_frown(self) -> primitives.Float | None:
        """The left frown/smile amount. (negative to positive 1)"""
        member = self.get_member("MouthLeftSmileFrown")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mouth_left_smile_frown.setter
    def mouth_left_smile_frown(self, value: primitives.Float) -> None:
        """Set the MouthLeftSmileFrown field value."""
        member = self.get_member("MouthLeftSmileFrown")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MouthLeftSmileFrown", fields.FieldFloat(value=value)
            )

    @property
    def mouth_right_smile_frown(self) -> primitives.Float | None:
        """The right frown/smile amount. (negative to positive 1)"""
        member = self.get_member("MouthRightSmileFrown")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mouth_right_smile_frown.setter
    def mouth_right_smile_frown(self, value: primitives.Float) -> None:
        """Set the MouthRightSmileFrown field value."""
        member = self.get_member("MouthRightSmileFrown")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MouthRightSmileFrown", fields.FieldFloat(value=value)
            )

    @property
    def mouth_left_dimple(self) -> primitives.Float | None:
        """push the area closest to the corners of the lips inwards on the left."""
        member = self.get_member("MouthLeftDimple")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mouth_left_dimple.setter
    def mouth_left_dimple(self, value: primitives.Float) -> None:
        """Set the MouthLeftDimple field value."""
        member = self.get_member("MouthLeftDimple")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MouthLeftDimple", fields.FieldFloat(value=value)
            )

    @property
    def mouth_right_dimple(self) -> primitives.Float | None:
        """push the area closest to the corners of the lips inwards on the right."""
        member = self.get_member("MouthRightDimple")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mouth_right_dimple.setter
    def mouth_right_dimple(self, value: primitives.Float) -> None:
        """Set the MouthRightDimple field value."""
        member = self.get_member("MouthRightDimple")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MouthRightDimple", fields.FieldFloat(value=value)
            )

    @property
    def mouth_pout_left(self) -> primitives.Float | None:
        """The mouth kissy amount on the left."""
        member = self.get_member("MouthPoutLeft")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mouth_pout_left.setter
    def mouth_pout_left(self, value: primitives.Float) -> None:
        """Set the MouthPoutLeft field value."""
        member = self.get_member("MouthPoutLeft")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MouthPoutLeft", fields.FieldFloat(value=value)
            )

    @property
    def mouth_pout_right(self) -> primitives.Float | None:
        """The mouth kissy amount on the right."""
        member = self.get_member("MouthPoutRight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @mouth_pout_right.setter
    def mouth_pout_right(self, value: primitives.Float) -> None:
        """Set the MouthPoutRight field value."""
        member = self.get_member("MouthPoutRight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MouthPoutRight", fields.FieldFloat(value=value)
            )

    @property
    def lip_top_left_overturn(self) -> primitives.Float | None:
        """The amount The top lip is flipping upwards on the left."""
        member = self.get_member("LipTopLeftOverturn")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lip_top_left_overturn.setter
    def lip_top_left_overturn(self, value: primitives.Float) -> None:
        """Set the LipTopLeftOverturn field value."""
        member = self.get_member("LipTopLeftOverturn")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipTopLeftOverturn", fields.FieldFloat(value=value)
            )

    @property
    def lip_top_right_overturn(self) -> primitives.Float | None:
        """The amount The top lip is flipping upwards on the right."""
        member = self.get_member("LipTopRightOverturn")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lip_top_right_overturn.setter
    def lip_top_right_overturn(self, value: primitives.Float) -> None:
        """Set the LipTopRightOverturn field value."""
        member = self.get_member("LipTopRightOverturn")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipTopRightOverturn", fields.FieldFloat(value=value)
            )

    @property
    def lip_bottom_left_overturn(self) -> primitives.Float | None:
        """The amount The top lip is flipping upwards"""
        member = self.get_member("LipBottomLeftOverturn")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lip_bottom_left_overturn.setter
    def lip_bottom_left_overturn(self, value: primitives.Float) -> None:
        """Set the LipBottomLeftOverturn field value."""
        member = self.get_member("LipBottomLeftOverturn")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipBottomLeftOverturn", fields.FieldFloat(value=value)
            )

    @property
    def lip_bottom_right_overturn(self) -> primitives.Float | None:
        """how much the bottom right side of the lips is pushing outwards like duck lips."""
        member = self.get_member("LipBottomRightOverturn")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lip_bottom_right_overturn.setter
    def lip_bottom_right_overturn(self, value: primitives.Float) -> None:
        """Set the LipBottomRightOverturn field value."""
        member = self.get_member("LipBottomRightOverturn")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipBottomRightOverturn", fields.FieldFloat(value=value)
            )

    @property
    def lip_top_left_over_under(self) -> primitives.Float | None:
        """The amount the top lip is going down to cover the bottom lip."""
        member = self.get_member("LipTopLeftOverUnder")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lip_top_left_over_under.setter
    def lip_top_left_over_under(self, value: primitives.Float) -> None:
        """Set the LipTopLeftOverUnder field value."""
        member = self.get_member("LipTopLeftOverUnder")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipTopLeftOverUnder", fields.FieldFloat(value=value)
            )

    @property
    def lip_top_right_over_under(self) -> primitives.Float | None:
        """How much the bottom right part of the lips is going behind the top right lip."""
        member = self.get_member("LipTopRightOverUnder")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lip_top_right_over_under.setter
    def lip_top_right_over_under(self, value: primitives.Float) -> None:
        """Set the LipTopRightOverUnder field value."""
        member = self.get_member("LipTopRightOverUnder")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipTopRightOverUnder", fields.FieldFloat(value=value)
            )

    @property
    def lip_bottom_left_over_under(self) -> primitives.Float | None:
        """The amount the bottom lip is going up to cover the top lip left."""
        member = self.get_member("LipBottomLeftOverUnder")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lip_bottom_left_over_under.setter
    def lip_bottom_left_over_under(self, value: primitives.Float) -> None:
        """Set the LipBottomLeftOverUnder field value."""
        member = self.get_member("LipBottomLeftOverUnder")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipBottomLeftOverUnder", fields.FieldFloat(value=value)
            )

    @property
    def lip_bottom_right_over_under(self) -> primitives.Float | None:
        """The amount the bottom lip is going up to cover the top lip right."""
        member = self.get_member("LipBottomRightOverUnder")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lip_bottom_right_over_under.setter
    def lip_bottom_right_over_under(self, value: primitives.Float) -> None:
        """Set the LipBottomRightOverUnder field value."""
        member = self.get_member("LipBottomRightOverUnder")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipBottomRightOverUnder", fields.FieldFloat(value=value)
            )

    @property
    def lip_left_stretch_tighten(self) -> primitives.Float | None:
        """The amount the left side of the lips are pulling towards the outside."""
        member = self.get_member("LipLeftStretchTighten")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lip_left_stretch_tighten.setter
    def lip_left_stretch_tighten(self, value: primitives.Float) -> None:
        """Set the LipLeftStretchTighten field value."""
        member = self.get_member("LipLeftStretchTighten")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipLeftStretchTighten", fields.FieldFloat(value=value)
            )

    @property
    def lip_right_stretch_tighten(self) -> primitives.Float | None:
        """The amount the right side of the lips are pulling towards the outside."""
        member = self.get_member("LipRightStretchTighten")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lip_right_stretch_tighten.setter
    def lip_right_stretch_tighten(self, value: primitives.Float) -> None:
        """Set the LipRightStretchTighten field value."""
        member = self.get_member("LipRightStretchTighten")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipRightStretchTighten", fields.FieldFloat(value=value)
            )

    @property
    def lips_left_press(self) -> primitives.Float | None:
        """The amount the left side of the lips are pulling towards the inside."""
        member = self.get_member("LipsLeftPress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lips_left_press.setter
    def lips_left_press(self, value: primitives.Float) -> None:
        """Set the LipsLeftPress field value."""
        member = self.get_member("LipsLeftPress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipsLeftPress", fields.FieldFloat(value=value)
            )

    @property
    def lips_right_press(self) -> primitives.Float | None:
        """The amount the right side of the lips are pulling towards the inside."""
        member = self.get_member("LipsRightPress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @lips_right_press.setter
    def lips_right_press(self, value: primitives.Float) -> None:
        """Set the LipsRightPress field value."""
        member = self.get_member("LipsRightPress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LipsRightPress", fields.FieldFloat(value=value)
            )

    @property
    def cheek_left_puff_suck(self) -> primitives.Float | None:
        """The amount the left cheek is sucking inwards or being puffed out. (negative to positive 1)"""
        member = self.get_member("CheekLeftPuffSuck")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cheek_left_puff_suck.setter
    def cheek_left_puff_suck(self, value: primitives.Float) -> None:
        """Set the CheekLeftPuffSuck field value."""
        member = self.get_member("CheekLeftPuffSuck")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CheekLeftPuffSuck", fields.FieldFloat(value=value)
            )

    @property
    def cheek_right_puff_suck(self) -> primitives.Float | None:
        """The amount the right cheek is sucking inwards or being puffed out. (negative to positive 1)"""
        member = self.get_member("CheekRightPuffSuck")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cheek_right_puff_suck.setter
    def cheek_right_puff_suck(self, value: primitives.Float) -> None:
        """Set the CheekRightPuffSuck field value."""
        member = self.get_member("CheekRightPuffSuck")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CheekRightPuffSuck", fields.FieldFloat(value=value)
            )

    @property
    def cheek_left_raise(self) -> primitives.Float | None:
        """How much the cheek area of the left side of the face is being pushed upwards (Usually caused by smile) (negative to positive one)"""
        member = self.get_member("CheekLeftRaise")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cheek_left_raise.setter
    def cheek_left_raise(self, value: primitives.Float) -> None:
        """Set the CheekLeftRaise field value."""
        member = self.get_member("CheekLeftRaise")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CheekLeftRaise", fields.FieldFloat(value=value)
            )

    @property
    def cheek_right_raise(self) -> primitives.Float | None:
        """How much the cheek area of the right side of the face is being pushed upwards (Usually caused by smile) (negative to positive one)"""
        member = self.get_member("CheekRightRaise")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @cheek_right_raise.setter
    def cheek_right_raise(self, value: primitives.Float) -> None:
        """Set the CheekRightRaise field value."""
        member = self.get_member("CheekRightRaise")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "CheekRightRaise", fields.FieldFloat(value=value)
            )

    @property
    def nose_wrinkle_left(self) -> primitives.Float | None:
        """How much the left side of the nose is being pushed up."""
        member = self.get_member("NoseWrinkleLeft")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @nose_wrinkle_left.setter
    def nose_wrinkle_left(self, value: primitives.Float) -> None:
        """Set the NoseWrinkleLeft field value."""
        member = self.get_member("NoseWrinkleLeft")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoseWrinkleLeft", fields.FieldFloat(value=value)
            )

    @property
    def nose_wrinkle_right(self) -> primitives.Float | None:
        """How much the right side of the nose is being pushed up."""
        member = self.get_member("NoseWrinkleRight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @nose_wrinkle_right.setter
    def nose_wrinkle_right(self, value: primitives.Float) -> None:
        """Set the NoseWrinkleRight field value."""
        member = self.get_member("NoseWrinkleRight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NoseWrinkleRight", fields.FieldFloat(value=value)
            )

    @property
    def chin_raise_bottom(self) -> primitives.Float | None:
        """How much the bottom chin is being pulled up."""
        member = self.get_member("ChinRaiseBottom")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @chin_raise_bottom.setter
    def chin_raise_bottom(self, value: primitives.Float) -> None:
        """Set the ChinRaiseBottom field value."""
        member = self.get_member("ChinRaiseBottom")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ChinRaiseBottom", fields.FieldFloat(value=value)
            )

    @property
    def chin_raise_top(self) -> primitives.Float | None:
        """How much the top chin is being pulled up."""
        member = self.get_member("ChinRaiseTop")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @chin_raise_top.setter
    def chin_raise_top(self, value: primitives.Float) -> None:
        """Set the ChinRaiseTop field value."""
        member = self.get_member("ChinRaiseTop")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ChinRaiseTop", fields.FieldFloat(value=value)
            )

