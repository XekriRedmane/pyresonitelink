"""Generated component: ReferenceMultiplexer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GenericComponent, T
from pyresonitelink.generated._types.sync_ref import SyncRef
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceMultiplexer(GenericComponent[T], IComponent, IWorldEventReceiver):
    """ReferenceMultiplexers allow to curate a list of references and drive a target with one of them.

Unlike ValueMultiplexers they don't implement IValue and therefore can't be accessed directly within ProtoFlux.

    Category: Utility

    The component behaves similar to a ReferenceCopy with the list entry
    indicated by ``Index`` as its ``Source``. Changes to ``Index`` or the
    list entries will affect ``Target`` whenever the drive is evaluated.

    Parameterize with a value type::

        ReferenceMultiplexer[primitives.Float]
        ReferenceMultiplexer[primitives.Float3]
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReferenceMultiplexer<>"
    _GENERIC_TYPE_TEMPLATE = "[FrooxEngine]FrooxEngine.ReferenceMultiplexer<>"

    def __init__(self, target: str | SyncRef[T] | None = None, index: primitives.Int | None = None, allow_write_back: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target: Initial value for Target.
            index: Initial value for Index.
            allow_write_back: Initial value for AllowWriteBack.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target is not None:
            self.target = target
        if index is not None:
            self.index = index
        if allow_write_back is not None:
            self.allow_write_back = allow_write_back

    @property
    def target(self) -> str | None:
        """A SyncRef which is driven with the currently selected reference"""
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
    def index(self) -> primitives.Int | None:
        """0-based index that determines which reference of ``References`` has been selected; values outside the range ``[0;length-1]`` are wrapped around internally."""
        member = self.get_member("Index")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @index.setter
    def index(self, value: primitives.Int) -> None:
        """Set the Index field value."""
        member = self.get_member("Index")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Index", fields.FieldInt(value=value)
            )

    @property
    def references(self) -> members.SyncList | None:
        """A list of references which can also individually be driven or written to"""
        member = self.get_member("References")
        if isinstance(member, members.SyncList):
            return member
        return None

    @references.setter
    def references(self, value: members.SyncList) -> None:
        """Set References. A list of references which can also individually be driven or written to"""
        self.set_member("References", value)

    @property
    def allow_write_back(self) -> primitives.Bool | None:
        """Setting this to ``true`` redirects writes from ``Target`` to the currently indexed list entry."""
        member = self.get_member("AllowWriteBack")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @allow_write_back.setter
    def allow_write_back(self, value: primitives.Bool) -> None:
        """Set the AllowWriteBack field value."""
        member = self.get_member("AllowWriteBack")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AllowWriteBack", fields.FieldBool(value=value)
            )

