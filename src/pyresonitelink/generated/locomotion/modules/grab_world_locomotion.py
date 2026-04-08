"""Generated component: GrabWorldLocomotion."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.locomotion_controller import LocomotionController
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.cross_mesh import CrossMesh
from pyresonitelink.generated._types.pbs_rim_metallic import PBS_RimMetallic
from pyresonitelink.generated._types.ilocomotion_module import ILocomotionModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabWorldLocomotion(GeneratedComponent, ILocomotionModule, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.GrabWorldLocomotion.

    Category: Locomotion/Modules
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabWorldLocomotion"

    def __init__(self, icon: str | IAssetProvider[ITexture2D] | None = None, color: primitives.ColorX | None = None, current_controller: str | LocomotionController | None = None, last_default_icon: str | None = None, last_default_color: primitives.ColorX | None = None, activation_threshold: primitives.Float | None = None, deactivation_threshold: primitives.Float | None = None, visual: str | Slot | None = None, cross_mesh: str | CrossMesh | None = None, material: str | PBS_RimMetallic | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            icon: Initial value for Icon.
            color: Initial value for Color.
            current_controller: Initial value for _currentController.
            last_default_icon: Initial value for _lastDefaultIcon.
            last_default_color: Initial value for _lastDefaultColor.
            activation_threshold: Initial value for ActivationThreshold.
            deactivation_threshold: Initial value for DeactivationThreshold.
            visual: Initial value for _visual.
            cross_mesh: Initial value for _crossMesh.
            material: Initial value for _material.
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
        if activation_threshold is not None:
            self.activation_threshold = activation_threshold
        if deactivation_threshold is not None:
            self.deactivation_threshold = deactivation_threshold
        if visual is not None:
            self.visual = visual
        if cross_mesh is not None:
            self.cross_mesh = cross_mesh
        if material is not None:
            self.material = material

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
    def activation_threshold(self) -> primitives.Float | None:
        """The ActivationThreshold field value."""
        member = self.get_member("ActivationThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @activation_threshold.setter
    def activation_threshold(self, value: primitives.Float) -> None:
        """Set the ActivationThreshold field value."""
        member = self.get_member("ActivationThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActivationThreshold", fields.FieldFloat(value=value)
            )

    @property
    def deactivation_threshold(self) -> primitives.Float | None:
        """The DeactivationThreshold field value."""
        member = self.get_member("DeactivationThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @deactivation_threshold.setter
    def deactivation_threshold(self, value: primitives.Float) -> None:
        """Set the DeactivationThreshold field value."""
        member = self.get_member("DeactivationThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DeactivationThreshold", fields.FieldFloat(value=value)
            )

    @property
    def visual(self) -> str | None:
        """Target ID of the _visual reference (targets Slot)."""
        member = self.get_member("_visual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual.setter
    def visual(self, target: str | Slot | None) -> None:
        """Set the _visual reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_visual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def cross_mesh(self) -> str | None:
        """Target ID of the _crossMesh reference (targets CrossMesh)."""
        member = self.get_member("_crossMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @cross_mesh.setter
    def cross_mesh(self, target: str | CrossMesh | None) -> None:
        """Set the _crossMesh reference by target ID or CrossMesh instance."""
        target_id: str | None = target.id if isinstance(target, CrossMesh) else target  # type: ignore[assignment]
        member = self.get_member("_crossMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_crossMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CrossMesh'),
            )

    @property
    def material(self) -> str | None:
        """Target ID of the _material reference (targets PBS_RimMetallic)."""
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _material reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

