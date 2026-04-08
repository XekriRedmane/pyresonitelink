"""Generated component: ScreenController."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.pointer_interaction_controller import PointerInteractionController
from pyresonitelink.generated._types.iview_targetting_controller import IViewTargettingController
from pyresonitelink.generated._types.head_simulator import HeadSimulator
from pyresonitelink.generated._types.hand_simulator import HandSimulator
from pyresonitelink.generated._types.first_person_targetting_controller import FirstPersonTargettingController
from pyresonitelink.generated._types.third_person_targetting_controller import ThirdPersonTargettingController
from pyresonitelink.generated._types.ui_targetting_controller import UI_TargettingController
from pyresonitelink.generated._types.freeform_targetting_controller import FreeformTargettingController
from pyresonitelink.generated._types.iinput_update_receiver import IInputUpdateReceiver
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScreenController(GeneratedComponent, IInputUpdateReceiver, IComponent, IWorldEventReceiver):
    """The ScreenController component is used mainly in desktop and is found on user roots. It is used to control the screen controls like third person in the game.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ScreenController"

    def __init__(self, transition_speed: primitives.Float | None = None, pointer_controller: str | PointerInteractionController | None = None, active_targetting: str | IViewTargettingController | None = None, head: str | HeadSimulator | None = None, left_hand: str | HandSimulator | None = None, right_hand: str | HandSimulator | None = None, previous_targetting: str | IViewTargettingController | None = None, first_person: str | FirstPersonTargettingController | None = None, third_person: str | ThirdPersonTargettingController | None = None, ui_camera: str | UI_TargettingController | None = None, freeform_camera: str | FreeformTargettingController | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            transition_speed: Initial value for TransitionSpeed.
            pointer_controller: Initial value for PointerController.
            active_targetting: Initial value for ActiveTargetting.
            head: Initial value for Head.
            left_hand: Initial value for LeftHand.
            right_hand: Initial value for RightHand.
            previous_targetting: Initial value for _previousTargetting.
            first_person: Initial value for _firstPerson.
            third_person: Initial value for _thirdPerson.
            ui_camera: Initial value for _uiCamera.
            freeform_camera: Initial value for _freeformCamera.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if transition_speed is not None:
            self.transition_speed = transition_speed
        if pointer_controller is not None:
            self.pointer_controller = pointer_controller
        if active_targetting is not None:
            self.active_targetting = active_targetting
        if head is not None:
            self.head = head
        if left_hand is not None:
            self.left_hand = left_hand
        if right_hand is not None:
            self.right_hand = right_hand
        if previous_targetting is not None:
            self.previous_targetting = previous_targetting
        if first_person is not None:
            self.first_person = first_person
        if third_person is not None:
            self.third_person = third_person
        if ui_camera is not None:
            self.ui_camera = ui_camera
        if freeform_camera is not None:
            self.freeform_camera = freeform_camera

    @property
    def transition_speed(self) -> primitives.Float | None:
        """How fast to transition the camera between different modes."""
        member = self.get_member("TransitionSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @transition_speed.setter
    def transition_speed(self, value: primitives.Float) -> None:
        """Set the TransitionSpeed field value."""
        member = self.get_member("TransitionSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TransitionSpeed", fields.FieldFloat(value=value)
            )

    @property
    def pointer_controller(self) -> str | None:
        """The pointer component handling inspector interactions."""
        member = self.get_member("PointerController")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pointer_controller.setter
    def pointer_controller(self, target: str | PointerInteractionController | None) -> None:
        """Set the PointerController reference by target ID or PointerInteractionController instance."""
        target_id: str | None = target.id if isinstance(target, PointerInteractionController) else target  # type: ignore[assignment]
        member = self.get_member("PointerController")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "PointerController",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PointerInteractionController'),
            )

    @property
    def active_targetting(self) -> str | None:
        """The view controller targeting mechanism for stuff like UIX targeting."""
        member = self.get_member("ActiveTargetting")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @active_targetting.setter
    def active_targetting(self, target: str | IViewTargettingController | None) -> None:
        """Set the ActiveTargetting reference by target ID or IViewTargettingController instance."""
        target_id: str | None = target.id if isinstance(target, IViewTargettingController) else target  # type: ignore[assignment]
        member = self.get_member("ActiveTargetting")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "ActiveTargetting",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IViewTargettingController'),
            )

    @property
    def head(self) -> str | None:
        """The component handling head control."""
        member = self.get_member("Head")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @head.setter
    def head(self, target: str | HeadSimulator | None) -> None:
        """Set the Head reference by target ID or HeadSimulator instance."""
        target_id: str | None = target.id if isinstance(target, HeadSimulator) else target  # type: ignore[assignment]
        member = self.get_member("Head")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Head",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.HeadSimulator'),
            )

    @property
    def left_hand(self) -> str | None:
        """The component handing the left hand control."""
        member = self.get_member("LeftHand")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @left_hand.setter
    def left_hand(self, target: str | HandSimulator | None) -> None:
        """Set the LeftHand reference by target ID or HandSimulator instance."""
        target_id: str | None = target.id if isinstance(target, HandSimulator) else target  # type: ignore[assignment]
        member = self.get_member("LeftHand")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LeftHand",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.HandSimulator'),
            )

    @property
    def right_hand(self) -> str | None:
        """The component handling the right hand control."""
        member = self.get_member("RightHand")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @right_hand.setter
    def right_hand(self, target: str | HandSimulator | None) -> None:
        """Set the RightHand reference by target ID or HandSimulator instance."""
        target_id: str | None = target.id if isinstance(target, HandSimulator) else target  # type: ignore[assignment]
        member = self.get_member("RightHand")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "RightHand",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.HandSimulator'),
            )

    @property
    def previous_targetting(self) -> str | None:
        """The previously used targeting controller."""
        member = self.get_member("_previousTargetting")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @previous_targetting.setter
    def previous_targetting(self, target: str | IViewTargettingController | None) -> None:
        """Set the _previousTargetting reference by target ID or IViewTargettingController instance."""
        target_id: str | None = target.id if isinstance(target, IViewTargettingController) else target  # type: ignore[assignment]
        member = self.get_member("_previousTargetting")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_previousTargetting",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IViewTargettingController'),
            )

    @property
    def first_person(self) -> str | None:
        """The component to handle first person object targeting."""
        member = self.get_member("_firstPerson")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @first_person.setter
    def first_person(self, target: str | FirstPersonTargettingController | None) -> None:
        """Set the _firstPerson reference by target ID or FirstPersonTargettingController instance."""
        target_id: str | None = target.id if isinstance(target, FirstPersonTargettingController) else target  # type: ignore[assignment]
        member = self.get_member("_firstPerson")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_firstPerson",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FirstPersonTargettingController'),
            )

    @property
    def third_person(self) -> str | None:
        """The component to handle third person object targeting."""
        member = self.get_member("_thirdPerson")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @third_person.setter
    def third_person(self, target: str | ThirdPersonTargettingController | None) -> None:
        """Set the _thirdPerson reference by target ID or ThirdPersonTargettingController instance."""
        target_id: str | None = target.id if isinstance(target, ThirdPersonTargettingController) else target  # type: ignore[assignment]
        member = self.get_member("_thirdPerson")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_thirdPerson",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ThirdPersonTargettingController'),
            )

    @property
    def ui_camera(self) -> str | None:
        """The targetting controller used for UIX targeting."""
        member = self.get_member("_uiCamera")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @ui_camera.setter
    def ui_camera(self, target: str | UI_TargettingController | None) -> None:
        """Set the _uiCamera reference by target ID or UI_TargettingController instance."""
        target_id: str | None = target.id if isinstance(target, UI_TargettingController) else target  # type: ignore[assignment]
        member = self.get_member("_uiCamera")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_uiCamera",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UI_TargettingController'),
            )

    @property
    def freeform_camera(self) -> str | None:
        """The targetting controller used for third person targetting like freeform camera mode in desktop."""
        member = self.get_member("_freeformCamera")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @freeform_camera.setter
    def freeform_camera(self, target: str | FreeformTargettingController | None) -> None:
        """Set the _freeformCamera reference by target ID or FreeformTargettingController instance."""
        target_id: str | None = target.id if isinstance(target, FreeformTargettingController) else target  # type: ignore[assignment]
        member = self.get_member("_freeformCamera")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_freeformCamera",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.FreeformTargettingController'),
            )

