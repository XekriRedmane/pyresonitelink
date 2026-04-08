"""Generated component: LegacySessionOrbsController."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacySessionOrbsController(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacySessionOrbsController.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacySessionOrbsController"

    def __init__(self, spawn_radius: primitives.Float | None = None, spawn_height: primitives.Float | None = None, spawn_offset: primitives.Float3 | None = None, root: str | Slot | None = None, max_orbs: primitives.Int | None = None, show_headless: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            spawn_radius: Initial value for SpawnRadius.
            spawn_height: Initial value for SpawnHeight.
            spawn_offset: Initial value for SpawnOffset.
            root: Initial value for _root.
            max_orbs: Initial value for MaxOrbs.
            show_headless: Initial value for ShowHeadless.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if spawn_radius is not None:
            self.spawn_radius = spawn_radius
        if spawn_height is not None:
            self.spawn_height = spawn_height
        if spawn_offset is not None:
            self.spawn_offset = spawn_offset
        if root is not None:
            self.root = root
        if max_orbs is not None:
            self.max_orbs = max_orbs
        if show_headless is not None:
            self.show_headless = show_headless

    @property
    def spawn_radius(self) -> primitives.Float | None:
        """The SpawnRadius field value."""
        member = self.get_member("SpawnRadius")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spawn_radius.setter
    def spawn_radius(self, value: primitives.Float) -> None:
        """Set the SpawnRadius field value."""
        member = self.get_member("SpawnRadius")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpawnRadius", fields.FieldFloat(value=value)
            )

    @property
    def spawn_height(self) -> primitives.Float | None:
        """The SpawnHeight field value."""
        member = self.get_member("SpawnHeight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spawn_height.setter
    def spawn_height(self, value: primitives.Float) -> None:
        """Set the SpawnHeight field value."""
        member = self.get_member("SpawnHeight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpawnHeight", fields.FieldFloat(value=value)
            )

    @property
    def spawn_offset(self) -> primitives.Float3 | None:
        """The SpawnOffset field value."""
        member = self.get_member("SpawnOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spawn_offset.setter
    def spawn_offset(self, value: primitives.Float3) -> None:
        """Set the SpawnOffset field value."""
        member = self.get_member("SpawnOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SpawnOffset", fields.FieldFloat3(value=value)
            )

    @property
    def root(self) -> str | None:
        """Target ID of the _root reference (targets Slot)."""
        member = self.get_member("_root")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root.setter
    def root(self, target: str | Slot | None) -> None:
        """Set the _root reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_root")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_root",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def max_orbs(self) -> primitives.Int | None:
        """The MaxOrbs field value."""
        member = self.get_member("MaxOrbs")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_orbs.setter
    def max_orbs(self, value: primitives.Int) -> None:
        """Set the MaxOrbs field value."""
        member = self.get_member("MaxOrbs")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "MaxOrbs", fields.FieldInt(value=value)
            )

    @property
    def show_headless(self) -> primitives.Bool | None:
        """The ShowHeadless field value."""
        member = self.get_member("ShowHeadless")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_headless.setter
    def show_headless(self, value: primitives.Bool) -> None:
        """Set the ShowHeadless field value."""
        member = self.get_member("ShowHeadless")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowHeadless", fields.FieldBool(value=value)
            )

