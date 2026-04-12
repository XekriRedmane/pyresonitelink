"""Generated component: DebugFeatureUpgrade."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugFeatureUpgrade(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The DebugFeatureUpgrade is used to test upgrading features which is an Elements.Core.dll C# tag function.

    Debug.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugFeatureUpgrade"

    def __init__(self, test: primitives.Int | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            test: Initial value for Test.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if test is not None:
            self.test = test

    @property
    def test(self) -> primitives.Int | None:
        """The Feature to test upgrade."""
        member = self.get_member("Test")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @test.setter
    def test(self, value: primitives.Int) -> None:
        """Set the Test field value."""
        member = self.get_member("Test")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Test", fields.FieldInt(value=value)
            )

