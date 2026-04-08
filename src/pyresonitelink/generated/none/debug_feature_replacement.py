"""Generated component: DebugFeatureReplacement."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class DebugFeatureReplacement(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.DebugFeatureReplacement.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DebugFeatureReplacement"

    def __init__(self, test: np.int32 | None = None, test2: np.float32 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            test: Initial value for Test.
            test2: Initial value for Test2.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if test is not None:
            self.test = test
        if test2 is not None:
            self.test2 = test2

    @property
    def test(self) -> np.int32 | None:
        """The Test field value."""
        member = self.get_member("Test")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @test.setter
    def test(self, value: np.int32) -> None:
        """Set the Test field value."""
        member = self.get_member("Test")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Test", fields.FieldInt(value=value)
            )

    @property
    def test2(self) -> np.float32 | None:
        """The Test2 field value."""
        member = self.get_member("Test2")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @test2.setter
    def test2(self, value: np.float32) -> None:
        """Set the Test2 field value."""
        member = self.get_member("Test2")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Test2", fields.FieldFloat(value=value)
            )

