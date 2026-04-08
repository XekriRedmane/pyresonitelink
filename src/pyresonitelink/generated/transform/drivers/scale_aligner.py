"""Generated component: ScaleAligner."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ScaleAligner(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ScaleAligner.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ScaleAligner"

    def __init__(self, auto_add_children: primitives.Bool | None = None, base_size: primitives.Float3 | None = None, increment: primitives.Float3 | None = None, multiplier: primitives.Float3 | None = None, non_uniform: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            auto_add_children: Initial value for AutoAddChildren.
            base_size: Initial value for BaseSize.
            increment: Initial value for Increment.
            multiplier: Initial value for Multiplier.
            non_uniform: Initial value for NonUniform.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if auto_add_children is not None:
            self.auto_add_children = auto_add_children
        if base_size is not None:
            self.base_size = base_size
        if increment is not None:
            self.increment = increment
        if multiplier is not None:
            self.multiplier = multiplier
        if non_uniform is not None:
            self.non_uniform = non_uniform

    @property
    def auto_add_children(self) -> primitives.Bool | None:
        """The AutoAddChildren field value."""
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
        """The AutoAddIgnoreTags member."""
        member = self.get_member("AutoAddIgnoreTags")
        if isinstance(member, members.SyncList):
            return member
        return None

    @auto_add_ignore_tags.setter
    def auto_add_ignore_tags(self, value: members.SyncList) -> None:
        """Set the AutoAddIgnoreTags member."""
        self.set_member("AutoAddIgnoreTags", value)

    @property
    def base_size(self) -> primitives.Float3 | None:
        """The BaseSize field value."""
        member = self.get_member("BaseSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_size.setter
    def base_size(self, value: primitives.Float3) -> None:
        """Set the BaseSize field value."""
        member = self.get_member("BaseSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseSize", fields.FieldFloat3(value=value)
            )

    @property
    def increment(self) -> primitives.Float3 | None:
        """The Increment field value."""
        member = self.get_member("Increment")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @increment.setter
    def increment(self, value: primitives.Float3) -> None:
        """Set the Increment field value."""
        member = self.get_member("Increment")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Increment", fields.FieldFloat3(value=value)
            )

    @property
    def multiplier(self) -> primitives.Float3 | None:
        """The Multiplier field value."""
        member = self.get_member("Multiplier")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @multiplier.setter
    def multiplier(self, value: primitives.Float3) -> None:
        """Set the Multiplier field value."""
        member = self.get_member("Multiplier")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Multiplier", fields.FieldFloat3(value=value)
            )

    @property
    def non_uniform(self) -> primitives.Bool | None:
        """The NonUniform field value."""
        member = self.get_member("NonUniform")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @non_uniform.setter
    def non_uniform(self, value: primitives.Bool) -> None:
        """Set the NonUniform field value."""
        member = self.get_member("NonUniform")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "NonUniform", fields.FieldBool(value=value)
            )

    @property
    def targets(self) -> members.SyncList | None:
        """The _targets member."""
        member = self.get_member("_targets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @targets.setter
    def targets(self, value: members.SyncList) -> None:
        """Set the _targets member."""
        self.set_member("_targets", value)

