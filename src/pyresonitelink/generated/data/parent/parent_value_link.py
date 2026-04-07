"""Generated component: ParentValueLink."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParentValueLink(GenericComponent[T], IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ParentValueLink<>.

    Category: Data/Parent

    Parameterize with a value type::

        ParentValueLink[np.float32]
        ParentValueLink[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ParentValueLink<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ParentValueLink<>"

    def __init__(self, match_tag: str | None = None, target: str | IField[T] | None = None, write_back: bool | None = None, default_value: T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            match_tag: Initial value for MatchTag.
            target: Initial value for Target.
            write_back: Initial value for WriteBack.
            default_value: Initial value for DefaultValue.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if match_tag is not None:
            self.match_tag = match_tag
        if target is not None:
            self.target = target
        if write_back is not None:
            self.write_back = write_back
        if default_value is not None:
            self.default_value = default_value

    @property
    def match_tag(self) -> str | None:
        """The MatchTag field value."""
        member = self.get_member("MatchTag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @match_tag.setter
    def match_tag(self, value: str) -> None:
        """Set the MatchTag field value."""
        member = self.get_member("MatchTag")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MatchTag", fields.FieldString(value=value)
            )

    @property
    def target(self) -> str | None:
        """Target ID of the Target reference (targets IField[T])."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | IField[T] | None) -> None:
        """Set the Target reference by target ID or IField[T] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<T>'),
            )

    @property
    def write_back(self) -> bool | None:
        """The WriteBack field value."""
        member = self.get_member("WriteBack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @write_back.setter
    def write_back(self, value: bool) -> None:
        """Set the WriteBack field value."""
        member = self.get_member("WriteBack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WriteBack", fields.FieldBool(value=value)
            )

    @property
    def default_value(self) -> T | None:
        """The DefaultValue field value (type depends on type parameter)."""
        member = self.get_member("DefaultValue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @default_value.setter
    def default_value(self, value: T) -> None:
        """Set the DefaultValue field value."""
        member = self.get_member("DefaultValue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        elif self._type_info is not None:
            self.set_member(
                "DefaultValue", self._type_info.field_class(value=value)
            )

