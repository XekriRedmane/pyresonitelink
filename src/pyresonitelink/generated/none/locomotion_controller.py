"""Generated component: LocomotionController."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icollider import ICollider
from pyresonitelink.generated._types.character_controller import CharacterController
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LocomotionController(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LocomotionController.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LocomotionController"

    def __init__(self, scaling_enabled: primitives.Bool | None = None, active_module_index: primitives.Int | None = None, find_user_preferred_module: primitives.Bool | None = None, current_ground_collider: str | ICollider | None = None, last_ground_collider: str | ICollider | None = None, dummy_character_controller: str | CharacterController | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            scaling_enabled: Initial value for ScalingEnabled.
            active_module_index: Initial value for ActiveModuleIndex.
            find_user_preferred_module: Initial value for FindUserPreferredModule.
            current_ground_collider: Initial value for _currentGroundCollider.
            last_ground_collider: Initial value for _lastGroundCollider.
            dummy_character_controller: Initial value for _dummyCharacterController.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if scaling_enabled is not None:
            self.scaling_enabled = scaling_enabled
        if active_module_index is not None:
            self.active_module_index = active_module_index
        if find_user_preferred_module is not None:
            self.find_user_preferred_module = find_user_preferred_module
        if current_ground_collider is not None:
            self.current_ground_collider = current_ground_collider
        if last_ground_collider is not None:
            self.last_ground_collider = last_ground_collider
        if dummy_character_controller is not None:
            self.dummy_character_controller = dummy_character_controller

    @property
    def scaling_enabled(self) -> primitives.Bool | None:
        """The ScalingEnabled field value."""
        member = self.get_member("ScalingEnabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scaling_enabled.setter
    def scaling_enabled(self, value: primitives.Bool) -> None:
        """Set the ScalingEnabled field value."""
        member = self.get_member("ScalingEnabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScalingEnabled", fields.FieldBool(value=value)
            )

    @property
    def supress_sources(self) -> members.SyncList | None:
        """The SupressSources member."""
        member = self.get_member("SupressSources")
        if isinstance(member, members.SyncList):
            return member
        return None

    @supress_sources.setter
    def supress_sources(self, value: members.SyncList) -> None:
        """Set the SupressSources member."""
        self.set_member("SupressSources", value)

    @property
    def input_supress_sources(self) -> members.SyncList | None:
        """The InputSupressSources member."""
        member = self.get_member("InputSupressSources")
        if isinstance(member, members.SyncList):
            return member
        return None

    @input_supress_sources.setter
    def input_supress_sources(self, value: members.SyncList) -> None:
        """Set the InputSupressSources member."""
        self.set_member("InputSupressSources", value)

    @property
    def locomotion_modules(self) -> members.SyncList | None:
        """The LocomotionModules member."""
        member = self.get_member("LocomotionModules")
        if isinstance(member, members.SyncList):
            return member
        return None

    @locomotion_modules.setter
    def locomotion_modules(self, value: members.SyncList) -> None:
        """Set the LocomotionModules member."""
        self.set_member("LocomotionModules", value)

    @property
    def active_module_index(self) -> primitives.Int | None:
        """The ActiveModuleIndex field value."""
        member = self.get_member("ActiveModuleIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @active_module_index.setter
    def active_module_index(self, value: primitives.Int) -> None:
        """Set the ActiveModuleIndex field value."""
        member = self.get_member("ActiveModuleIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActiveModuleIndex", fields.FieldInt(value=value)
            )

    @property
    def find_user_preferred_module(self) -> primitives.Bool | None:
        """The FindUserPreferredModule field value."""
        member = self.get_member("FindUserPreferredModule")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @find_user_preferred_module.setter
    def find_user_preferred_module(self, value: primitives.Bool) -> None:
        """Set the FindUserPreferredModule field value."""
        member = self.get_member("FindUserPreferredModule")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "FindUserPreferredModule", fields.FieldBool(value=value)
            )

    @property
    def current_ground_collider(self) -> str | None:
        """Target ID of the _currentGroundCollider reference (targets ICollider)."""
        member = self.get_member("_currentGroundCollider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @current_ground_collider.setter
    def current_ground_collider(self, target: str | ICollider | None) -> None:
        """Set the _currentGroundCollider reference by target ID or ICollider instance."""
        target_id: str | None = target.id if isinstance(target, ICollider) else target  # type: ignore[assignment]
        member = self.get_member("_currentGroundCollider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_currentGroundCollider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ICollider'),
            )

    @property
    def last_ground_collider(self) -> str | None:
        """Target ID of the _lastGroundCollider reference (targets ICollider)."""
        member = self.get_member("_lastGroundCollider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @last_ground_collider.setter
    def last_ground_collider(self, target: str | ICollider | None) -> None:
        """Set the _lastGroundCollider reference by target ID or ICollider instance."""
        target_id: str | None = target.id if isinstance(target, ICollider) else target  # type: ignore[assignment]
        member = self.get_member("_lastGroundCollider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_lastGroundCollider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ICollider'),
            )

    @property
    def parent_hierarchy(self) -> members.SyncList | None:
        """The _parentHierarchy member."""
        member = self.get_member("_parentHierarchy")
        if isinstance(member, members.SyncList):
            return member
        return None

    @parent_hierarchy.setter
    def parent_hierarchy(self, value: members.SyncList) -> None:
        """Set the _parentHierarchy member."""
        self.set_member("_parentHierarchy", value)

    @property
    def dummy_character_controller(self) -> str | None:
        """Target ID of the _dummyCharacterController reference (targets CharacterController)."""
        member = self.get_member("_dummyCharacterController")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dummy_character_controller.setter
    def dummy_character_controller(self, target: str | CharacterController | None) -> None:
        """Set the _dummyCharacterController reference by target ID or CharacterController instance."""
        target_id: str | None = target.id if isinstance(target, CharacterController) else target  # type: ignore[assignment]
        member = self.get_member("_dummyCharacterController")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_dummyCharacterController",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.CharacterController'),
            )

