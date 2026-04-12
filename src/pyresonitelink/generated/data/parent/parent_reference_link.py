"""Generated component: ParentReferenceLink."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ParentReferenceLink(GenericComponent[T], IComponent, IWorldEventReceiver):
    """The ParentReferenceLink&lt;T&gt; component drives a field depending on the value of a compatible ParentReference as part of a parent value system.

    Category: Data/Parent

    Upon a change of parent, this component will search for ParentReference
    components on the slot's immediate parent that have a matching type and
    tag. If it can find such a component and link to it, it will drive the
    ``Target`` field based on the ``Reference`` of the ParentReference. If
    it can not find such a component, it will use the ``DefaultReference``
    value.

    Parameterize with a value type::

        ParentReferenceLink[primitives.Float]
        ParentReferenceLink[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ParentReferenceLink<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ParentReferenceLink<>"

    def __init__(self, match_tag: primitives.String | None = None, target: str | SyncRef[T] | None = None, write_back: primitives.Bool | None = None, default_reference: str | T | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            match_tag: Initial value for MatchTag.
            target: Initial value for Target.
            write_back: Initial value for WriteBack.
            default_reference: Initial value for DefaultReference.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if match_tag is not None:
            self.match_tag = match_tag
        if target is not None:
            self.target = target
        if write_back is not None:
            self.write_back = write_back
        if default_reference is not None:
            self.default_reference = default_reference

    @property
    def match_tag(self) -> primitives.String | None:
        """The tag to search for on the slot's immediate parent. Compatible ParentReference components must have the same ``Tag``."""
        member = self.get_member("MatchTag")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @match_tag.setter
    def match_tag(self, value: primitives.String) -> None:
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
        """The field to drive using the value of the linked parent."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | SyncRef[T] | None) -> None:
        """Set the Target reference by target ID or SyncRef[T] instance."""
        target_id: str | None = target.id if isinstance(target, SyncRef) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncRef<T>'),
            )

    @property
    def write_back(self) -> primitives.Bool | None:
        """If ``True``, any writes to the driven field will be propagated back to the ``Reference`` provided by the ParentReference. See write backs."""
        member = self.get_member("WriteBack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @write_back.setter
    def write_back(self, value: primitives.Bool) -> None:
        """Set the WriteBack field value."""
        member = self.get_member("WriteBack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "WriteBack", fields.FieldBool(value=value)
            )

    @property
    def default_reference(self) -> str | None:
        """Default value to use if the component can not find a compatible ParentReference."""
        member = self.get_member("DefaultReference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @default_reference.setter
    def default_reference(self, target: str | T | None) -> None:
        """Set the DefaultReference reference by target ID or T instance."""
        target_id: str | None = target.id if hasattr(target, 'id') and not isinstance(target, str) else target  # type: ignore[union-attr,assignment]
        member = self.get_member("DefaultReference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "DefaultReference",
                members.Reference(targetId=target_id, targetType='T'),
            )

