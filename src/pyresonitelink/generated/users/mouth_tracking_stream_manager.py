"""Generated component: MouthTrackingStreamManager."""

import numpy as np

from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.value_stream import ValueStream
from pyresonitelink.generated._types.imouth_tracking_source_component import IMouthTrackingSourceComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MouthTrackingStreamManager(GeneratedComponent, IMouthTrackingSourceComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.MouthTrackingStreamManager.

    Category: Users
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MouthTrackingStreamManager"

    def __init__(self, user: str | User | None = None, is_tracking: str | ValueStream[bool] | None = None, jaw: str | ValueStream[primitives.Float3] | None = None, jaw_open: str | ValueStream[np.float32] | None = None, tongue: str | ValueStream[primitives.Float3] | None = None, tongue_roll: str | ValueStream[np.float32] | None = None, lip_upper_left_raise: str | ValueStream[np.float32] | None = None, lip_upper_right_raise: str | ValueStream[np.float32] | None = None, lip_lower_leftaise: str | ValueStream[np.float32] | None = None, lip_lower_right_raise: str | ValueStream[np.float32] | None = None, lip_upper_horizontal: str | ValueStream[np.float32] | None = None, lip_lower_horizontal: str | ValueStream[np.float32] | None = None, mouth_left_smile_frown: str | ValueStream[np.float32] | None = None, mouth_right_smile_frown: str | ValueStream[np.float32] | None = None, mouth_left_dimple: str | ValueStream[np.float32] | None = None, mouth_right_dimple: str | ValueStream[np.float32] | None = None, mouth_pout_left: str | ValueStream[np.float32] | None = None, mouth_pout_right: str | ValueStream[np.float32] | None = None, lip_top_left_overturn: str | ValueStream[np.float32] | None = None, lip_top_right_overturn: str | ValueStream[np.float32] | None = None, lip_bottom_left_overturn: str | ValueStream[np.float32] | None = None, lip_bottom_right_overturn: str | ValueStream[np.float32] | None = None, lip_top_left_over_under: str | ValueStream[np.float32] | None = None, lip_top_right_over_under: str | ValueStream[np.float32] | None = None, lip_bottom_left_over_under: str | ValueStream[np.float32] | None = None, lip_bottom_right_over_under: str | ValueStream[np.float32] | None = None, lip_left_stretch_tighten: str | ValueStream[np.float32] | None = None, lip_right_stretch_tighten: str | ValueStream[np.float32] | None = None, lips_left_press: str | ValueStream[np.float32] | None = None, lips_right_press: str | ValueStream[np.float32] | None = None, cheek_left_puff_suck: str | ValueStream[np.float32] | None = None, cheek_right_puff_suck: str | ValueStream[np.float32] | None = None, cheek_left_raise: str | ValueStream[np.float32] | None = None, cheek_right_raise: str | ValueStream[np.float32] | None = None, nose_wrinkle_left: str | ValueStream[np.float32] | None = None, nose_wrinkle_right: str | ValueStream[np.float32] | None = None, chin_raise_bottom: str | ValueStream[np.float32] | None = None, chin_raise_top: str | ValueStream[np.float32] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            user: Initial value for User.
            is_tracking: Initial value for IsTracking.
            jaw: Initial value for Jaw.
            jaw_open: Initial value for JawOpen.
            tongue: Initial value for Tongue.
            tongue_roll: Initial value for TongueRoll.
            lip_upper_left_raise: Initial value for LipUpperLeftRaise.
            lip_upper_right_raise: Initial value for LipUpperRightRaise.
            lip_lower_leftaise: Initial value for LipLowerLeftaise.
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
        if user is not None:
            self.user = user
        if is_tracking is not None:
            self.is_tracking = is_tracking
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
        if lip_lower_leftaise is not None:
            self.lip_lower_leftaise = lip_lower_leftaise
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
    def user(self) -> str | None:
        """Target ID of the User reference (targets User)."""
        member = self.get_member("User")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @user.setter
    def user(self, target: str | User | None) -> None:
        """Set the User reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("User")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "User",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def is_tracking(self) -> str | None:
        """Target ID of the IsTracking reference (targets ValueStream[bool])."""
        member = self.get_member("IsTracking")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @is_tracking.setter
    def is_tracking(self, target: str | ValueStream[bool] | None) -> None:
        """Set the IsTracking reference by target ID or ValueStream[bool] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("IsTracking")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "IsTracking",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<bool>'),
            )

    @property
    def jaw(self) -> str | None:
        """Target ID of the Jaw reference (targets ValueStream[primitives.Float3])."""
        member = self.get_member("Jaw")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @jaw.setter
    def jaw(self, target: str | ValueStream[primitives.Float3] | None) -> None:
        """Set the Jaw reference by target ID or ValueStream[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("Jaw")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Jaw",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float3>'),
            )

    @property
    def jaw_open(self) -> str | None:
        """Target ID of the JawOpen reference (targets ValueStream[np.float32])."""
        member = self.get_member("JawOpen")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @jaw_open.setter
    def jaw_open(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the JawOpen reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("JawOpen")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "JawOpen",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def tongue(self) -> str | None:
        """Target ID of the Tongue reference (targets ValueStream[primitives.Float3])."""
        member = self.get_member("Tongue")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tongue.setter
    def tongue(self, target: str | ValueStream[primitives.Float3] | None) -> None:
        """Set the Tongue reference by target ID or ValueStream[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("Tongue")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Tongue",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float3>'),
            )

    @property
    def tongue_roll(self) -> str | None:
        """Target ID of the TongueRoll reference (targets ValueStream[np.float32])."""
        member = self.get_member("TongueRoll")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tongue_roll.setter
    def tongue_roll(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the TongueRoll reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("TongueRoll")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "TongueRoll",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lip_upper_left_raise(self) -> str | None:
        """Target ID of the LipUpperLeftRaise reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipUpperLeftRaise")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lip_upper_left_raise.setter
    def lip_upper_left_raise(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipUpperLeftRaise reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipUpperLeftRaise")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipUpperLeftRaise",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lip_upper_right_raise(self) -> str | None:
        """Target ID of the LipUpperRightRaise reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipUpperRightRaise")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lip_upper_right_raise.setter
    def lip_upper_right_raise(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipUpperRightRaise reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipUpperRightRaise")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipUpperRightRaise",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lip_lower_leftaise(self) -> str | None:
        """Target ID of the LipLowerLeftaise reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipLowerLeftaise")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lip_lower_leftaise.setter
    def lip_lower_leftaise(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipLowerLeftaise reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipLowerLeftaise")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipLowerLeftaise",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lip_lower_right_raise(self) -> str | None:
        """Target ID of the LipLowerRightRaise reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipLowerRightRaise")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lip_lower_right_raise.setter
    def lip_lower_right_raise(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipLowerRightRaise reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipLowerRightRaise")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipLowerRightRaise",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lip_upper_horizontal(self) -> str | None:
        """Target ID of the LipUpperHorizontal reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipUpperHorizontal")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lip_upper_horizontal.setter
    def lip_upper_horizontal(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipUpperHorizontal reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipUpperHorizontal")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipUpperHorizontal",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lip_lower_horizontal(self) -> str | None:
        """Target ID of the LipLowerHorizontal reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipLowerHorizontal")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lip_lower_horizontal.setter
    def lip_lower_horizontal(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipLowerHorizontal reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipLowerHorizontal")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipLowerHorizontal",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def mouth_left_smile_frown(self) -> str | None:
        """Target ID of the MouthLeftSmileFrown reference (targets ValueStream[np.float32])."""
        member = self.get_member("MouthLeftSmileFrown")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mouth_left_smile_frown.setter
    def mouth_left_smile_frown(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the MouthLeftSmileFrown reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("MouthLeftSmileFrown")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MouthLeftSmileFrown",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def mouth_right_smile_frown(self) -> str | None:
        """Target ID of the MouthRightSmileFrown reference (targets ValueStream[np.float32])."""
        member = self.get_member("MouthRightSmileFrown")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mouth_right_smile_frown.setter
    def mouth_right_smile_frown(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the MouthRightSmileFrown reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("MouthRightSmileFrown")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MouthRightSmileFrown",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def mouth_left_dimple(self) -> str | None:
        """Target ID of the MouthLeftDimple reference (targets ValueStream[np.float32])."""
        member = self.get_member("MouthLeftDimple")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mouth_left_dimple.setter
    def mouth_left_dimple(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the MouthLeftDimple reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("MouthLeftDimple")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MouthLeftDimple",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def mouth_right_dimple(self) -> str | None:
        """Target ID of the MouthRightDimple reference (targets ValueStream[np.float32])."""
        member = self.get_member("MouthRightDimple")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mouth_right_dimple.setter
    def mouth_right_dimple(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the MouthRightDimple reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("MouthRightDimple")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MouthRightDimple",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def mouth_pout_left(self) -> str | None:
        """Target ID of the MouthPoutLeft reference (targets ValueStream[np.float32])."""
        member = self.get_member("MouthPoutLeft")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mouth_pout_left.setter
    def mouth_pout_left(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the MouthPoutLeft reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("MouthPoutLeft")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MouthPoutLeft",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def mouth_pout_right(self) -> str | None:
        """Target ID of the MouthPoutRight reference (targets ValueStream[np.float32])."""
        member = self.get_member("MouthPoutRight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @mouth_pout_right.setter
    def mouth_pout_right(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the MouthPoutRight reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("MouthPoutRight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MouthPoutRight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lip_top_left_overturn(self) -> str | None:
        """Target ID of the LipTopLeftOverturn reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipTopLeftOverturn")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lip_top_left_overturn.setter
    def lip_top_left_overturn(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipTopLeftOverturn reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipTopLeftOverturn")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipTopLeftOverturn",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lip_top_right_overturn(self) -> str | None:
        """Target ID of the LipTopRightOverturn reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipTopRightOverturn")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lip_top_right_overturn.setter
    def lip_top_right_overturn(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipTopRightOverturn reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipTopRightOverturn")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipTopRightOverturn",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lip_bottom_left_overturn(self) -> str | None:
        """Target ID of the LipBottomLeftOverturn reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipBottomLeftOverturn")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lip_bottom_left_overturn.setter
    def lip_bottom_left_overturn(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipBottomLeftOverturn reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipBottomLeftOverturn")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipBottomLeftOverturn",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lip_bottom_right_overturn(self) -> str | None:
        """Target ID of the LipBottomRightOverturn reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipBottomRightOverturn")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lip_bottom_right_overturn.setter
    def lip_bottom_right_overturn(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipBottomRightOverturn reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipBottomRightOverturn")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipBottomRightOverturn",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lip_top_left_over_under(self) -> str | None:
        """Target ID of the LipTopLeftOverUnder reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipTopLeftOverUnder")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lip_top_left_over_under.setter
    def lip_top_left_over_under(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipTopLeftOverUnder reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipTopLeftOverUnder")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipTopLeftOverUnder",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lip_top_right_over_under(self) -> str | None:
        """Target ID of the LipTopRightOverUnder reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipTopRightOverUnder")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lip_top_right_over_under.setter
    def lip_top_right_over_under(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipTopRightOverUnder reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipTopRightOverUnder")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipTopRightOverUnder",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lip_bottom_left_over_under(self) -> str | None:
        """Target ID of the LipBottomLeftOverUnder reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipBottomLeftOverUnder")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lip_bottom_left_over_under.setter
    def lip_bottom_left_over_under(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipBottomLeftOverUnder reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipBottomLeftOverUnder")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipBottomLeftOverUnder",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lip_bottom_right_over_under(self) -> str | None:
        """Target ID of the LipBottomRightOverUnder reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipBottomRightOverUnder")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lip_bottom_right_over_under.setter
    def lip_bottom_right_over_under(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipBottomRightOverUnder reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipBottomRightOverUnder")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipBottomRightOverUnder",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lip_left_stretch_tighten(self) -> str | None:
        """Target ID of the LipLeftStretchTighten reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipLeftStretchTighten")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lip_left_stretch_tighten.setter
    def lip_left_stretch_tighten(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipLeftStretchTighten reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipLeftStretchTighten")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipLeftStretchTighten",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lip_right_stretch_tighten(self) -> str | None:
        """Target ID of the LipRightStretchTighten reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipRightStretchTighten")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lip_right_stretch_tighten.setter
    def lip_right_stretch_tighten(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipRightStretchTighten reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipRightStretchTighten")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipRightStretchTighten",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lips_left_press(self) -> str | None:
        """Target ID of the LipsLeftPress reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipsLeftPress")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lips_left_press.setter
    def lips_left_press(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipsLeftPress reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipsLeftPress")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipsLeftPress",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def lips_right_press(self) -> str | None:
        """Target ID of the LipsRightPress reference (targets ValueStream[np.float32])."""
        member = self.get_member("LipsRightPress")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @lips_right_press.setter
    def lips_right_press(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the LipsRightPress reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("LipsRightPress")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LipsRightPress",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def cheek_left_puff_suck(self) -> str | None:
        """Target ID of the CheekLeftPuffSuck reference (targets ValueStream[np.float32])."""
        member = self.get_member("CheekLeftPuffSuck")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cheek_left_puff_suck.setter
    def cheek_left_puff_suck(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the CheekLeftPuffSuck reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("CheekLeftPuffSuck")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CheekLeftPuffSuck",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def cheek_right_puff_suck(self) -> str | None:
        """Target ID of the CheekRightPuffSuck reference (targets ValueStream[np.float32])."""
        member = self.get_member("CheekRightPuffSuck")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cheek_right_puff_suck.setter
    def cheek_right_puff_suck(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the CheekRightPuffSuck reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("CheekRightPuffSuck")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CheekRightPuffSuck",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def cheek_left_raise(self) -> str | None:
        """Target ID of the CheekLeftRaise reference (targets ValueStream[np.float32])."""
        member = self.get_member("CheekLeftRaise")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cheek_left_raise.setter
    def cheek_left_raise(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the CheekLeftRaise reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("CheekLeftRaise")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CheekLeftRaise",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def cheek_right_raise(self) -> str | None:
        """Target ID of the CheekRightRaise reference (targets ValueStream[np.float32])."""
        member = self.get_member("CheekRightRaise")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cheek_right_raise.setter
    def cheek_right_raise(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the CheekRightRaise reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("CheekRightRaise")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "CheekRightRaise",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def nose_wrinkle_left(self) -> str | None:
        """Target ID of the NoseWrinkleLeft reference (targets ValueStream[np.float32])."""
        member = self.get_member("NoseWrinkleLeft")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @nose_wrinkle_left.setter
    def nose_wrinkle_left(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the NoseWrinkleLeft reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("NoseWrinkleLeft")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NoseWrinkleLeft",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def nose_wrinkle_right(self) -> str | None:
        """Target ID of the NoseWrinkleRight reference (targets ValueStream[np.float32])."""
        member = self.get_member("NoseWrinkleRight")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @nose_wrinkle_right.setter
    def nose_wrinkle_right(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the NoseWrinkleRight reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("NoseWrinkleRight")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "NoseWrinkleRight",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def chin_raise_bottom(self) -> str | None:
        """Target ID of the ChinRaiseBottom reference (targets ValueStream[np.float32])."""
        member = self.get_member("ChinRaiseBottom")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @chin_raise_bottom.setter
    def chin_raise_bottom(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the ChinRaiseBottom reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("ChinRaiseBottom")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ChinRaiseBottom",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

    @property
    def chin_raise_top(self) -> str | None:
        """Target ID of the ChinRaiseTop reference (targets ValueStream[np.float32])."""
        member = self.get_member("ChinRaiseTop")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @chin_raise_top.setter
    def chin_raise_top(self, target: str | ValueStream[np.float32] | None) -> None:
        """Set the ChinRaiseTop reference by target ID or ValueStream[np.float32] instance."""
        target_id: str | None = target.id if isinstance(target, ValueStream) else target  # type: ignore[assignment]
        member = self.get_member("ChinRaiseTop")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ChinRaiseTop",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ValueStream<float>'),
            )

