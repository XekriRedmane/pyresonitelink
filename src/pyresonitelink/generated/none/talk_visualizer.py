"""Generated component: TalkVisualizer."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.raw_output import RawOutput
from pyresonitelink.generated._types.sync import Sync
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class TalkVisualizer(GeneratedComponent, IComponent, IWorldEventReceiver):
    """This component takes a float value and a colorX value, and multiplies the float value by the colorX value, and outputs a colorX.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.TalkVisualizer"

    def __init__(self, input_: str | RawOutput[primitives.Float] | None = None, base_color: primitives.ColorX | None = None, material_color: str | Sync[primitives.ColorX] | None = None, light_intensity: str | Sync[primitives.Float] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            input_: Initial value for Input.
            base_color: Initial value for BaseColor.
            material_color: Initial value for MaterialColor.
            light_intensity: Initial value for LightIntensity.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if input_ is not None:
            self.input_ = input_
        if base_color is not None:
            self.base_color = base_color
        if material_color is not None:
            self.material_color = material_color
        if light_intensity is not None:
            self.light_intensity = light_intensity

    @property
    def input_(self) -> str | None:
        """A value that constantly changes to visualize the color for. For example, the ``Volume`` field of a Volume Meter."""
        member = self.get_member("Input")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @input_.setter
    def input_(self, target: str | RawOutput[primitives.Float] | None) -> None:
        """Set the Input reference by target ID or RawOutput[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, RawOutput) else target  # type: ignore[assignment]
        member = self.get_member("Input")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Input",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.RawOutput<float>'),
            )

    @property
    def base_color(self) -> primitives.ColorX | None:
        """The original color."""
        member = self.get_member("BaseColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @base_color.setter
    def base_color(self, value: primitives.ColorX) -> None:
        """Set the BaseColor field value."""
        member = self.get_member("BaseColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "BaseColor", fields.FieldColorX(value=value)
            )

    @property
    def material_color(self) -> str | None:
        """The color to drive with an amplified ``BaseColor`` value based on ``Input``"""
        member = self.get_member("MaterialColor")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material_color.setter
    def material_color(self, target: str | Sync[primitives.ColorX] | None) -> None:
        """Set the MaterialColor reference by target ID or Sync[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("MaterialColor")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "MaterialColor",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<colorX>'),
            )

    @property
    def light_intensity(self) -> str | None:
        """How bright the output color is beyond 1 gain."""
        member = self.get_member("LightIntensity")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @light_intensity.setter
    def light_intensity(self, target: str | Sync[primitives.Float] | None) -> None:
        """Set the LightIntensity reference by target ID or Sync[primitives.Float] instance."""
        target_id: str | None = target.id if isinstance(target, Sync) else target  # type: ignore[assignment]
        member = self.get_member("LightIntensity")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "LightIntensity",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Sync<float>'),
            )

