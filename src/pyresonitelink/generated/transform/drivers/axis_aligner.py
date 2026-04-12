"""Generated component: AxisAligner."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.axis_dir import AxisDir
from pyresonitelink.generated._enums.align import Align
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class AxisAligner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The AxisAligner component is used to Align elements along a single line axis in local space under a slot based on their Bounding boxes. It also allows for excluding bounded elements from calculations, and for aligning elements themselves so that they can be centered like varied sized beads on a string or like boxes into the corner edge between a wall and floor. These calculations are heavy, and this component is best used lightly. Remove this component after using it to Align world elements, as it will be constantly active and will behave violently if used to Align shelves for example in a world and left unremoved.

    Category: Transform/Drivers

    **Align**: Note: changing the alignment does not change the order of elements. Just how the bounding box for the elements is positioned relative to 0. Basically this acts as a translation alignment, rather than a reordering of elements.

    **Disadvantages and Alternatives**: As the Axis Aligner works off of Bounds Calculations, and runs its calculations under a wide range of criteria, it can quickly become heavy with a doezen slots or so. Its Bounds-based nature alao makes it unsuited for evenly spacing objects with different bounds.

To mitigate these kinds of issues, one can make their own version of this in Protoflux, by having OnChange or other triggers fire a ForLoop, which iterates through all Slot Children, and gives them an offset based on the Iteration multiplied by a Float3 for the position. To further implement the bounds functionality, one can use a value that increases by the bounds calculation every iteration, instead of a number based on the Iteration itself.

A simple example was used to align the Avatars in Avatar Station, and is available in Nuki's Public Folder.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.AxisAligner"

    def __init__(self, auto_add_children: primitives.Bool | None = None, direction: AxisDir | str | None = None, global_axis_xalign: Align | str | None = None, global_axis_yalign: Align | str | None = None, global_axis_zalign: Align | str | None = None, element_axis_xalign: Align | str | None = None, element_axis_yalign: Align | str | None = None, element_axis_zalign: Align | str | None = None, separation: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            auto_add_children: Initial value for AutoAddChildren.
            direction: Initial value for Direction.
            global_axis_xalign: Initial value for GlobalAxisXAlign.
            global_axis_yalign: Initial value for GlobalAxisYAlign.
            global_axis_zalign: Initial value for GlobalAxisZAlign.
            element_axis_xalign: Initial value for ElementAxisXAlign.
            element_axis_yalign: Initial value for ElementAxisYAlign.
            element_axis_zalign: Initial value for ElementAxisZAlign.
            separation: Initial value for Separation.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if auto_add_children is not None:
            self.auto_add_children = auto_add_children
        if direction is not None:
            self.direction = direction
        if global_axis_xalign is not None:
            self.global_axis_xalign = global_axis_xalign
        if global_axis_yalign is not None:
            self.global_axis_yalign = global_axis_yalign
        if global_axis_zalign is not None:
            self.global_axis_zalign = global_axis_zalign
        if element_axis_xalign is not None:
            self.element_axis_xalign = element_axis_xalign
        if element_axis_yalign is not None:
            self.element_axis_yalign = element_axis_yalign
        if element_axis_zalign is not None:
            self.element_axis_zalign = element_axis_zalign
        if separation is not None:
            self.separation = separation

    @property
    def auto_add_children(self) -> primitives.Bool | None:
        """Controls whether slots below this component's slot in the hierarchy are automatically added to ``_targets``"""
        member = self.get_member("AutoAddChildren")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_add_children.setter
    def auto_add_children(self, value: primitives.Bool) -> None:
        """Set the AutoAddChildren field value."""
        member = self.get_member("AutoAddChildren")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AutoAddChildren", fields.FieldBool(value=value)
            )

    @property
    def auto_add_ignore_tags(self) -> members.SyncList | None:
        """if ``AutoAddChildren`` is enabled. A slot will not be added to ``_targets`` if it's tag is in this list."""
        member = self.get_member("AutoAddIgnoreTags")
        if isinstance(member, members.SyncList):
            return member
        return None

    @auto_add_ignore_tags.setter
    def auto_add_ignore_tags(self, value: members.SyncList) -> None:
        """Set AutoAddIgnoreTags. if ``AutoAddChildren`` is enabled. A slot will not be added to ``_targets`` if it's tag is in this list."""
        self.set_member("AutoAddIgnoreTags", value)

    @property
    def direction(self) -> AxisDir | None:
        """The axis and direction the items will be aligned on"""
        member = self.get_member("Direction")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return AxisDir(member.value)
        return None

    @direction.setter
    def direction(self, value: AxisDir | str) -> None:
        """Set Direction. The axis and direction the items will be aligned on"""
        member = self.get_member("Direction")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Direction",
                members.FieldEnum(value=str(value)),
            )

    @property
    def global_axis_xalign(self) -> Align | None:
        """Controls how items will be aligned globally, with each other in the X Axis"""
        member = self.get_member("GlobalAxisXAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Align(member.value)
        return None

    @global_axis_xalign.setter
    def global_axis_xalign(self, value: Align | str) -> None:
        """Set GlobalAxisXAlign. Controls how items will be aligned globally, with each other in the X Axis"""
        member = self.get_member("GlobalAxisXAlign")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "GlobalAxisXAlign",
                members.FieldEnum(value=str(value)),
            )

    @property
    def global_axis_yalign(self) -> Align | None:
        """Controls how items will be aligned globally, with each other in the Y Axis"""
        member = self.get_member("GlobalAxisYAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Align(member.value)
        return None

    @global_axis_yalign.setter
    def global_axis_yalign(self, value: Align | str) -> None:
        """Set GlobalAxisYAlign. Controls how items will be aligned globally, with each other in the Y Axis"""
        member = self.get_member("GlobalAxisYAlign")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "GlobalAxisYAlign",
                members.FieldEnum(value=str(value)),
            )

    @property
    def global_axis_zalign(self) -> Align | None:
        """Controls how items will be aligned globally, with each other in the Z Axis"""
        member = self.get_member("GlobalAxisZAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Align(member.value)
        return None

    @global_axis_zalign.setter
    def global_axis_zalign(self, value: Align | str) -> None:
        """Set GlobalAxisZAlign. Controls how items will be aligned globally, with each other in the Z Axis"""
        member = self.get_member("GlobalAxisZAlign")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "GlobalAxisZAlign",
                members.FieldEnum(value=str(value)),
            )

    @property
    def element_axis_xalign(self) -> Align | None:
        """Controls how each item aligns itself, within the align, in the X Axis"""
        member = self.get_member("ElementAxisXAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Align(member.value)
        return None

    @element_axis_xalign.setter
    def element_axis_xalign(self, value: Align | str) -> None:
        """Set ElementAxisXAlign. Controls how each item aligns itself, within the align, in the X Axis"""
        member = self.get_member("ElementAxisXAlign")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ElementAxisXAlign",
                members.FieldEnum(value=str(value)),
            )

    @property
    def element_axis_yalign(self) -> Align | None:
        """Controls how each item aligns itself, within the align, in the Y Axis"""
        member = self.get_member("ElementAxisYAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Align(member.value)
        return None

    @element_axis_yalign.setter
    def element_axis_yalign(self, value: Align | str) -> None:
        """Set ElementAxisYAlign. Controls how each item aligns itself, within the align, in the Y Axis"""
        member = self.get_member("ElementAxisYAlign")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ElementAxisYAlign",
                members.FieldEnum(value=str(value)),
            )

    @property
    def element_axis_zalign(self) -> Align | None:
        """Controls how each item aligns itself, within the align, in the Z Axis"""
        member = self.get_member("ElementAxisZAlign")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Align(member.value)
        return None

    @element_axis_zalign.setter
    def element_axis_zalign(self, value: Align | str) -> None:
        """Set ElementAxisZAlign. Controls how each item aligns itself, within the align, in the Z Axis"""
        member = self.get_member("ElementAxisZAlign")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "ElementAxisZAlign",
                members.FieldEnum(value=str(value)),
            )

    @property
    def separation(self) -> primitives.Float | None:
        """The spacing between each item in ``_targets`` along the specified axis"""
        member = self.get_member("Separation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @separation.setter
    def separation(self, value: primitives.Float) -> None:
        """Set the Separation field value."""
        member = self.get_member("Separation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Separation", fields.FieldFloat(value=value)
            )

    @property
    def exclude_list(self) -> members.SyncList | None:
        """A list of Bounded elements under target slots which are excluded from the aligners bounds calculations"""
        member = self.get_member("ExcludeList")
        if isinstance(member, members.SyncList):
            return member
        return None

    @exclude_list.setter
    def exclude_list(self, value: members.SyncList) -> None:
        """Set ExcludeList. A list of Bounded elements under target slots which are excluded from the aligners bounds calculations"""
        self.set_member("ExcludeList", value)

    @property
    def targets(self) -> members.SyncList | None:
        """A list of slots which will be aligned. This will be automatically generated if ``AutoAddChildren`` is enabled."""
        member = self.get_member("_targets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @targets.setter
    def targets(self, value: members.SyncList) -> None:
        """Set _targets. A list of slots which will be aligned. This will be automatically generated if ``AutoAddChildren`` is enabled."""
        self.set_member("_targets", value)

