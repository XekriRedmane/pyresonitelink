"""Generated component: TeleportLocomotion."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.itexture_2d import ITexture2D
from pyresonitelink.generated._types.locomotion_controller import LocomotionController
from pyresonitelink.generated._types.ballistic_path_mesh import BallisticPathMesh
from pyresonitelink.generated._types.pbs_rim_metallic import PBS_RimMetallic
from pyresonitelink.generated._types.mesh_renderer import MeshRenderer
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.character_controller import CharacterController
from pyresonitelink.generated._types.ilocomotion_module import ILocomotionModule
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TeleportLocomotion(GeneratedComponent, ILocomotionModule, IWorldEventReceiver):
    """The TeleportLocomotion component is used to allow users to teleport to spots using an arc path as a location selector.

    Category: Locomotion/Modules

    Used for accessibility reasons, and for puzzle games.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TeleportLocomotion"

    def __init__(self, icon: str | IAssetProvider[ITexture2D] | None = None, color: primitives.ColorX | None = None, current_controller: str | LocomotionController | None = None, last_default_icon: str | None = None, last_default_color: primitives.ColorX | None = None, backstep_distance: primitives.Float | None = None, activation_time: primitives.Float | None = None, height_input_max: primitives.Float | None = None, height_input_min: primitives.Float | None = None, initial_force_min: primitives.Float | None = None, initial_force_max: primitives.Float | None = None, range_exp: primitives.Float | None = None, step_unit: primitives.Float | None = None, drag: primitives.Float | None = None, max_small_object_size: primitives.Float | None = None, wall_distance: primitives.Float | None = None, path_mesh: str | BallisticPathMesh | None = None, path_material: str | PBS_RimMetallic | None = None, path_renderer: str | MeshRenderer | None = None, path_visual: str | Slot | None = None, target_point_visual: str | Slot | None = None, character_controller: str | CharacterController | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            icon: Initial value for Icon.
            color: Initial value for Color.
            current_controller: Initial value for _currentController.
            last_default_icon: Initial value for _lastDefaultIcon.
            last_default_color: Initial value for _lastDefaultColor.
            backstep_distance: Initial value for BackstepDistance.
            activation_time: Initial value for ActivationTime.
            height_input_max: Initial value for HeightInputMax.
            height_input_min: Initial value for HeightInputMin.
            initial_force_min: Initial value for InitialForceMin.
            initial_force_max: Initial value for InitialForceMax.
            range_exp: Initial value for RangeExp.
            step_unit: Initial value for StepUnit.
            drag: Initial value for Drag.
            max_small_object_size: Initial value for MaxSmallObjectSize.
            wall_distance: Initial value for WallDistance.
            path_mesh: Initial value for _pathMesh.
            path_material: Initial value for _pathMaterial.
            path_renderer: Initial value for _pathRenderer.
            path_visual: Initial value for _pathVisual.
            target_point_visual: Initial value for _targetPointVisual.
            character_controller: Initial value for _characterController.
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
        if backstep_distance is not None:
            self.backstep_distance = backstep_distance
        if activation_time is not None:
            self.activation_time = activation_time
        if height_input_max is not None:
            self.height_input_max = height_input_max
        if height_input_min is not None:
            self.height_input_min = height_input_min
        if initial_force_min is not None:
            self.initial_force_min = initial_force_min
        if initial_force_max is not None:
            self.initial_force_max = initial_force_max
        if range_exp is not None:
            self.range_exp = range_exp
        if step_unit is not None:
            self.step_unit = step_unit
        if drag is not None:
            self.drag = drag
        if max_small_object_size is not None:
            self.max_small_object_size = max_small_object_size
        if wall_distance is not None:
            self.wall_distance = wall_distance
        if path_mesh is not None:
            self.path_mesh = path_mesh
        if path_material is not None:
            self.path_material = path_material
        if path_renderer is not None:
            self.path_renderer = path_renderer
        if path_visual is not None:
            self.path_visual = path_visual
        if target_point_visual is not None:
            self.target_point_visual = target_point_visual
        if character_controller is not None:
            self.character_controller = character_controller

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
    def backstep_distance(self) -> primitives.Float | None:
        """How far to go backwards when pressing the backwards movement direction."""
        member = self.get_member("BackstepDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @backstep_distance.setter
    def backstep_distance(self, value: primitives.Float) -> None:
        """Set the BackstepDistance field value."""
        member = self.get_member("BackstepDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BackstepDistance", fields.FieldFloat(value=value)
            )

    @property
    def activation_time(self) -> primitives.Float | None:
        """How long it takes for the teleport visual to show and for the locomotion to allow teleport when pressing the forward movement direction."""
        member = self.get_member("ActivationTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @activation_time.setter
    def activation_time(self, value: primitives.Float) -> None:
        """Set the ActivationTime field value."""
        member = self.get_member("ActivationTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActivationTime", fields.FieldFloat(value=value)
            )

    @property
    def height_input_max(self) -> primitives.Float | None:
        """The maximum teleport up distance."""
        member = self.get_member("HeightInputMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height_input_max.setter
    def height_input_max(self, value: primitives.Float) -> None:
        """Set the HeightInputMax field value."""
        member = self.get_member("HeightInputMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeightInputMax", fields.FieldFloat(value=value)
            )

    @property
    def height_input_min(self) -> primitives.Float | None:
        """The minimum teleport height distance."""
        member = self.get_member("HeightInputMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height_input_min.setter
    def height_input_min(self, value: primitives.Float) -> None:
        """Set the HeightInputMin field value."""
        member = self.get_member("HeightInputMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HeightInputMin", fields.FieldFloat(value=value)
            )

    @property
    def initial_force_min(self) -> primitives.Float | None:
        """The minimum inital arc force value for the destination selection arc."""
        member = self.get_member("InitialForceMin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @initial_force_min.setter
    def initial_force_min(self, value: primitives.Float) -> None:
        """Set the InitialForceMin field value."""
        member = self.get_member("InitialForceMin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InitialForceMin", fields.FieldFloat(value=value)
            )

    @property
    def initial_force_max(self) -> primitives.Float | None:
        """The maximum inital arc force value for the destination selection arc."""
        member = self.get_member("InitialForceMax")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @initial_force_max.setter
    def initial_force_max(self, value: primitives.Float) -> None:
        """Set the InitialForceMax field value."""
        member = self.get_member("InitialForceMax")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InitialForceMax", fields.FieldFloat(value=value)
            )

    @property
    def range_exp(self) -> primitives.Float | None:
        """The amount to boost the teleport range."""
        member = self.get_member("RangeExp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @range_exp.setter
    def range_exp(self, value: primitives.Float) -> None:
        """Set the RangeExp field value."""
        member = self.get_member("RangeExp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RangeExp", fields.FieldFloat(value=value)
            )

    @property
    def step_unit(self) -> primitives.Float | None:
        """What to use for the step value in the teleport arc."""
        member = self.get_member("StepUnit")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @step_unit.setter
    def step_unit(self, value: primitives.Float) -> None:
        """Set the StepUnit field value."""
        member = self.get_member("StepUnit")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StepUnit", fields.FieldFloat(value=value)
            )

    @property
    def drag(self) -> primitives.Float | None:
        """What to use for the drag value in the teleport arc."""
        member = self.get_member("Drag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @drag.setter
    def drag(self, value: primitives.Float) -> None:
        """Set the Drag field value."""
        member = self.get_member("Drag")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Drag", fields.FieldFloat(value=value)
            )

    @property
    def max_small_object_size(self) -> primitives.Float | None:
        """The maximum size to allow before a small object is not ignored for teleport destinations."""
        member = self.get_member("MaxSmallObjectSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_small_object_size.setter
    def max_small_object_size(self, value: primitives.Float) -> None:
        """Set the MaxSmallObjectSize field value."""
        member = self.get_member("MaxSmallObjectSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxSmallObjectSize", fields.FieldFloat(value=value)
            )

    @property
    def wall_distance(self) -> primitives.Float | None:
        """The depth a wall has to be compared to the user's size to be considered a wall."""
        member = self.get_member("WallDistance")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @wall_distance.setter
    def wall_distance(self, value: primitives.Float) -> None:
        """Set the WallDistance field value."""
        member = self.get_member("WallDistance")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WallDistance", fields.FieldFloat(value=value)
            )

    @property
    def path_mesh(self) -> str | None:
        """The path mesh being used to display this locomotion's teleport location selector."""
        member = self.get_member("_pathMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @path_mesh.setter
    def path_mesh(self, target: str | BallisticPathMesh | None) -> None:
        """Set the _pathMesh reference by target ID or BallisticPathMesh instance."""
        target_id: str | None = target.id if isinstance(target, BallisticPathMesh) else target  # type: ignore[assignment]
        member = self.get_member("_pathMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pathMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BallisticPathMesh'),
            )

    @property
    def path_material(self) -> str | None:
        """The material to control the look of that is on ``_pathMesh``."""
        member = self.get_member("_pathMaterial")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @path_material.setter
    def path_material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _pathMaterial reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_pathMaterial")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pathMaterial",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

    @property
    def path_renderer(self) -> str | None:
        """The renderer of this teleport locomotion's location selector visual."""
        member = self.get_member("_pathRenderer")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @path_renderer.setter
    def path_renderer(self, target: str | MeshRenderer | None) -> None:
        """Set the _pathRenderer reference by target ID or MeshRenderer instance."""
        target_id: str | None = target.id if isinstance(target, MeshRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_pathRenderer")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pathRenderer",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.MeshRenderer'),
            )

    @property
    def path_visual(self) -> str | None:
        """the root slot of this teleport locomotion's location selector visual"""
        member = self.get_member("_pathVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @path_visual.setter
    def path_visual(self, target: str | Slot | None) -> None:
        """Set the _pathVisual reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_pathVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pathVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def target_point_visual(self) -> str | None:
        """the root of the hit point visual of this teleport locomotion's location selector visual"""
        member = self.get_member("_targetPointVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_point_visual.setter
    def target_point_visual(self, target: str | Slot | None) -> None:
        """Set the _targetPointVisual reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_targetPointVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetPointVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def character_controller(self) -> str | None:
        """The character controller for this teleport locomotion."""
        member = self.get_member("_characterController")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @character_controller.setter
    def character_controller(self, target: str | CharacterController | None) -> None:
        """Set the _characterController reference by target ID or CharacterController instance."""
        target_id: str | None = target.id if isinstance(target, CharacterController) else target  # type: ignore[assignment]
        member = self.get_member("_characterController")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_characterController",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CharacterController'),
            )

