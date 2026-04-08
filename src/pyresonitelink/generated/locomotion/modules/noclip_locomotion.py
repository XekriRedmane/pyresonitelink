"""Generated component: NoclipLocomotion."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.locomotion_controller import LocomotionController
from pyresonitelink.generated._types.iinput_update_receiver import IInputUpdateReceiver
from pyresonitelink.generated._types.ilocomotion_module import ILocomotionModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NoclipLocomotion(GeneratedComponent, IInputUpdateReceiver, ILocomotionModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.NoclipLocomotion.

    Category: Locomotion/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NoclipLocomotion"

    def __init__(self, icon: str | IAssetProvider[ITexture2D] | None = None, color: primitives.ColorX | None = None, current_controller: str | LocomotionController | None = None, last_default_icon: str | None = None, last_default_color: primitives.ColorX | None = None, max_speed: primitives.Float | None = None, minimum_fly_speed_ratio: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            icon: Initial value for Icon.
            color: Initial value for Color.
            current_controller: Initial value for _currentController.
            last_default_icon: Initial value for _lastDefaultIcon.
            last_default_color: Initial value for _lastDefaultColor.
            max_speed: Initial value for MaxSpeed.
            minimum_fly_speed_ratio: Initial value for MinimumFlySpeedRatio.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if icon is not None:
            self.icon = icon
        if color is not None:
            self.color = color
        if current_controller is not None:
            self.current_controller = current_controller
        if last_default_icon is not None:
            self.last_default_icon = last_default_icon
        if last_default_color is not None:
            self.last_default_color = last_default_color
        if max_speed is not None:
            self.max_speed = max_speed
        if minimum_fly_speed_ratio is not None:
            self.minimum_fly_speed_ratio = minimum_fly_speed_ratio

    @property
    def icon(self) -> str | None:
        """Target ID of the Icon reference (targets IAssetProvider[ITexture2D])."""
        member = self.get_member("Icon")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @icon.setter
    def icon(self, target: str | IAssetProvider[ITexture2D] | None) -> None:
        """Set the Icon reference by target ID or IAssetProvider[ITexture2D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Icon")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Icon",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.ITexture2D>'),
            )

    @property
    def color(self) -> primitives.ColorX | None:
        """The Color field value."""
        member = self.get_member("Color")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color.setter
    def color(self, value: primitives.ColorX) -> None:
        """Set the Color field value."""
        member = self.get_member("Color")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Color", fields.FieldColorX(value=value)
            )

    @property
    def current_controller(self) -> str | None:
        """Target ID of the _currentController reference (targets LocomotionController)."""
        member = self.get_member("_currentController")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_controller.setter
    def current_controller(self, target: str | LocomotionController | None) -> None:
        """Set the _currentController reference by target ID or LocomotionController instance."""
        target_id: str | None = target.id if isinstance(target, LocomotionController) else target  # type: ignore[assignment]
        member = self.get_member("_currentController")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentController",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LocomotionController'),
            )

    @property
    def last_default_icon(self) -> str | None:
        """The _lastDefaultIcon field value."""
        member = self.get_member("_lastDefaultIcon")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_default_icon.setter
    def last_default_icon(self, value: str) -> None:
        """Set the _lastDefaultIcon field value."""
        member = self.get_member("_lastDefaultIcon")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lastDefaultIcon", fields.FieldUri(value=value)
            )

    @property
    def last_default_color(self) -> primitives.ColorX | None:
        """The _lastDefaultColor field value."""
        member = self.get_member("_lastDefaultColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @last_default_color.setter
    def last_default_color(self, value: primitives.ColorX) -> None:
        """Set the _lastDefaultColor field value."""
        member = self.get_member("_lastDefaultColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_lastDefaultColor", fields.FieldNullableColorX(value=value)
            )

    @property
    def turn(self) -> members.SyncObject | None:
        """The Turn member."""
        member = self.get_member("Turn")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @turn.setter
    def turn(self, value: members.SyncObject) -> None:
        """Set the Turn member."""
        self.set_member("Turn", value)

    @property
    def max_speed(self) -> primitives.Float | None:
        """The MaxSpeed field value."""
        member = self.get_member("MaxSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_speed.setter
    def max_speed(self, value: primitives.Float) -> None:
        """Set the MaxSpeed field value."""
        member = self.get_member("MaxSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSpeed", fields.FieldFloat(value=value)
            )

    @property
    def minimum_fly_speed_ratio(self) -> primitives.Float | None:
        """The MinimumFlySpeedRatio field value."""
        member = self.get_member("MinimumFlySpeedRatio")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @minimum_fly_speed_ratio.setter
    def minimum_fly_speed_ratio(self, value: primitives.Float) -> None:
        """Set the MinimumFlySpeedRatio field value."""
        member = self.get_member("MinimumFlySpeedRatio")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MinimumFlySpeedRatio", fields.FieldFloat(value=value)
            )

