"""Generated component: WorldGrabMover."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.user import User
from pyresonitelink.generated._types.cross_mesh import CrossMesh
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.pbs_rim_metallic import PBS_RimMetallic
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldGrabMover(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The WorldGrabMover component is used as a visual for the grab world locomotion.

    Not used directly by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldGrabMover"

    def __init__(self, show_lerp: primitives.Float | None = None, activating_user: str | User | None = None, cross_mesh: str | CrossMesh | None = None, visual_visible: str | IField[primitives.Bool] | None = None, visual_rotation: str | IField[primitives.FloatQ] | None = None, material: str | PBS_RimMetallic | None = None, reference_position: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            show_lerp: Initial value for ShowLerp.
            activating_user: Initial value for _activatingUser.
            cross_mesh: Initial value for _crossMesh.
            visual_visible: Initial value for _visualVisible.
            visual_rotation: Initial value for _visualRotation.
            material: Initial value for _material.
            reference_position: Initial value for _referencePosition.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if show_lerp is not None:
            self.show_lerp = show_lerp
        if activating_user is not None:
            self.activating_user = activating_user
        if cross_mesh is not None:
            self.cross_mesh = cross_mesh
        if visual_visible is not None:
            self.visual_visible = visual_visible
        if visual_rotation is not None:
            self.visual_rotation = visual_rotation
        if material is not None:
            self.material = material
        if reference_position is not None:
            self.reference_position = reference_position

    @property
    def show_lerp(self) -> primitives.Float | None:
        """The lerp value for showing the visual."""
        member = self.get_member("ShowLerp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_lerp.setter
    def show_lerp(self, value: primitives.Float) -> None:
        """Set the ShowLerp field value."""
        member = self.get_member("ShowLerp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowLerp", fields.FieldFloat(value=value)
            )

    @property
    def activating_user(self) -> str | None:
        """The user making this visual for grabbing onto the world."""
        member = self.get_member("_activatingUser")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @activating_user.setter
    def activating_user(self, target: str | User | None) -> None:
        """Set the _activatingUser reference by target ID or User instance."""
        target_id: str | None = target.id if isinstance(target, User) else target  # type: ignore[assignment]
        member = self.get_member("_activatingUser")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_activatingUser",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.User'),
            )

    @property
    def cross_mesh(self) -> str | None:
        """The cross mesh being used for the anchor visual."""
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
    def visual_visible(self) -> str | None:
        """Whether the visual should be visible."""
        member = self.get_member("_visualVisible")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual_visible.setter
    def visual_visible(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _visualVisible reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_visualVisible")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visualVisible",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def visual_rotation(self) -> str | None:
        """The field to drive with the rotation for the visual."""
        member = self.get_member("_visualRotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @visual_rotation.setter
    def visual_rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _visualRotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_visualRotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_visualRotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def material(self) -> str | None:
        """The material that the visual is using."""
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

    @property
    def reference_position(self) -> primitives.Float3 | None:
        """the position this visual is trying to stay and anchor at."""
        member = self.get_member("_referencePosition")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @reference_position.setter
    def reference_position(self, value: primitives.Float3) -> None:
        """Set the _referencePosition field value."""
        member = self.get_member("_referencePosition")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_referencePosition", fields.FieldFloat3(value=value)
            )

