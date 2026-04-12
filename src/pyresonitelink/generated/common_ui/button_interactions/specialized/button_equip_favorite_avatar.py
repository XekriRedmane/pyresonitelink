"""Generated component: ButtonEquipFavoriteAvatar."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibutton_press_receiver import IButtonPressReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ButtonEquipFavoriteAvatar(GeneratedComponent, IButtonPressReceiver, IWorldEventReceiver):
    """The ButtonEquipFavoriteAvatar will equip the current users' favorite avatar when an IButton is pressed with this component is on it. This component only functions while in Userspace.

    Category: Common UI/Button Interactions/Specialized

    Attach to a button, when pressed while in Userspace, your current
    favorite avatar will be equipped.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ButtonEquipFavoriteAvatar"

    pass

