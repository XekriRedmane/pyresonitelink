"""Generated component: DebugTestMeshThroughput."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.generated._enums.color_profile import ColorProfile
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugTestMeshThroughput(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The DebugTestMeshThroughput component is used in code by parallel jamming quads into a MeshX object via multithreading to test how much can be done at once.

The mesh generated is a Spiral fan of quads that goes up in a circle pattern.

    Category: Debug

    Debugging MeshX parallel speed.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugTestMeshThroughput"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, profile: ColorProfile | str | None = None, count_: primitives.Int | None = None, progress: primitives.Float | None = None, update_time: primitives.Float | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            profile: Initial value for Profile.
            count_: Initial value for Count.
            progress: Initial value for Progress.
            update_time: Initial value for UpdateTime.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if profile is not None:
            self.profile = profile
        if count_ is not None:
            self.count_ = count_
        if progress is not None:
            self.progress = progress
        if update_time is not None:
            self.update_time = update_time

    @property
    def high_priority_integration(self) -> primitives.Bool | None:
        """The HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @high_priority_integration.setter
    def high_priority_integration(self, value: primitives.Bool) -> None:
        """Set the HighPriorityIntegration field value."""
        member = self.get_member("HighPriorityIntegration")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HighPriorityIntegration", fields.FieldBool(value=value)
            )

    @property
    def override_bounding_box(self) -> primitives.Bool | None:
        """The OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @override_bounding_box.setter
    def override_bounding_box(self, value: primitives.Bool) -> None:
        """Set the OverrideBoundingBox field value."""
        member = self.get_member("OverrideBoundingBox")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverrideBoundingBox", fields.FieldBool(value=value)
            )

    @property
    def overriden_bounding_box(self) -> primitives.BoundingBox | None:
        """The OverridenBoundingBox field value."""
        member = self.get_member("OverridenBoundingBox")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @overriden_bounding_box.setter
    def overriden_bounding_box(self, value: primitives.BoundingBox) -> None:
        """Set the OverridenBoundingBox field value."""
        member = self.get_member("OverridenBoundingBox")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "OverridenBoundingBox", fields.FieldBoundingBox(value=value)
            )

    @property
    def profile(self) -> ColorProfile | None:
        """The Profile enum value."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ColorProfile(member.value)
        return None

    @profile.setter
    def profile(self, value: ColorProfile | str) -> None:
        """Set the Profile enum value."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Profile",
                members.FieldEnum(value=str(value)),
            )

    @property
    def count_(self) -> primitives.Int | None:
        """How many mesh quads to parrallel jam into the meshx data."""
        member = self.get_member("Count")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @count_.setter
    def count_(self, value: primitives.Int) -> None:
        """Set the Count field value."""
        member = self.get_member("Count")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Count", fields.FieldInt(value=value)
            )

    @property
    def progress(self) -> primitives.Float | None:
        """How much to offset the quads by in rotation."""
        member = self.get_member("Progress")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @progress.setter
    def progress(self, value: primitives.Float) -> None:
        """Set the Progress field value."""
        member = self.get_member("Progress")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Progress", fields.FieldFloat(value=value)
            )

    @property
    def update_time(self) -> primitives.Float | None:
        """How long it took for the Asset to update."""
        member = self.get_member("UpdateTime")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @update_time.setter
    def update_time(self, value: primitives.Float) -> None:
        """Set the UpdateTime field value."""
        member = self.get_member("UpdateTime")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UpdateTime", fields.FieldFloat(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

