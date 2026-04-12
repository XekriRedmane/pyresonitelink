"""Generated component: VolumeUnlitMaterial."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.display_mode import DisplayMode
from pyresonitelink.generated._enums.blend_mode import BlendMode
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.shader import Shader
from pyresonitelink.generated._types.texture_3d import Texture3D
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class VolumeUnlitMaterial(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The VolumeUnlitMaterial component is used to display 3D Textures like Xrays, sunbeams, MRIs, CT scans, or any other 3D texture in a volumetric 3D cube that can optionally be sliced. Can also be used for volumetric lighting, but high texture resolutions can be large and cause considerable render lag.

This is a raymarched material, which means that a ray is stepped iteratively closer and closer to the volume in order to determine what is shown or not.

    Category: Assets/Materials/Volume
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.VolumeUnlitMaterial"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, shader: str | IAssetProvider[Shader] | None = None, mode: DisplayMode | str | None = None, blend_mode: BlendMode | str | None = None, render_queue: primitives.Int | None = None, volume: str | IAssetProvider[Texture3D] | None = None, step_size: primitives.Float | None = None, gain: primitives.Float | None = None, exp: primitives.Float | None = None, accumulation_cutoff: primitives.Float | None = None, hit_threshold: primitives.Float | None = None, input_range: primitives.Float | None = None, input_offset: primitives.Float | None = None, use_alpha_channel: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            shader: Initial value for _shader.
            mode: Initial value for Mode.
            blend_mode: Initial value for BlendMode.
            render_queue: Initial value for RenderQueue.
            volume: Initial value for Volume.
            step_size: Initial value for StepSize.
            gain: Initial value for Gain.
            exp: Initial value for Exp.
            accumulation_cutoff: Initial value for AccumulationCutoff.
            hit_threshold: Initial value for HitThreshold.
            input_range: Initial value for InputRange.
            input_offset: Initial value for InputOffset.
            use_alpha_channel: Initial value for UseAlphaChannel.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if shader is not None:
            self.shader = shader
        if mode is not None:
            self.mode = mode
        if blend_mode is not None:
            self.blend_mode = blend_mode
        if render_queue is not None:
            self.render_queue = render_queue
        if volume is not None:
            self.volume = volume
        if step_size is not None:
            self.step_size = step_size
        if gain is not None:
            self.gain = gain
        if exp is not None:
            self.exp = exp
        if accumulation_cutoff is not None:
            self.accumulation_cutoff = accumulation_cutoff
        if hit_threshold is not None:
            self.hit_threshold = hit_threshold
        if input_range is not None:
            self.input_range = input_range
        if input_offset is not None:
            self.input_offset = input_offset
        if use_alpha_channel is not None:
            self.use_alpha_channel = use_alpha_channel

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
    def shader(self) -> str | None:
        """Target ID of the _shader reference (targets IAssetProvider[Shader])."""
        member = self.get_member("_shader")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @shader.setter
    def shader(self, target: str | IAssetProvider[Shader] | None) -> None:
        """Set the _shader reference by target ID or IAssetProvider[Shader] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("_shader")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_shader",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Shader>'),
            )

    @property
    def mode(self) -> DisplayMode | None:
        """The Mode enum value."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return DisplayMode(member.value)
        return None

    @mode.setter
    def mode(self, value: DisplayMode | str) -> None:
        """Set the Mode enum value."""
        member = self.get_member("Mode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Mode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def blend_mode(self) -> BlendMode | None:
        """The BlendMode enum value."""
        member = self.get_member("BlendMode")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return BlendMode(member.value)
        return None

    @blend_mode.setter
    def blend_mode(self, value: BlendMode | str) -> None:
        """Set the BlendMode enum value."""
        member = self.get_member("BlendMode")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "BlendMode",
                members.FieldEnum(value=str(value)),
            )

    @property
    def render_queue(self) -> primitives.Int | None:
        """The RenderQueue field value."""
        member = self.get_member("RenderQueue")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @render_queue.setter
    def render_queue(self, value: primitives.Int) -> None:
        """Set the RenderQueue field value."""
        member = self.get_member("RenderQueue")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "RenderQueue", fields.FieldInt(value=value)
            )

    @property
    def volume(self) -> str | None:
        """Target ID of the Volume reference (targets IAssetProvider[Texture3D])."""
        member = self.get_member("Volume")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @volume.setter
    def volume(self, target: str | IAssetProvider[Texture3D] | None) -> None:
        """Set the Volume reference by target ID or IAssetProvider[Texture3D] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Volume")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Volume",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Texture3D>'),
            )

    @property
    def step_size(self) -> primitives.Float | None:
        """The StepSize field value."""
        member = self.get_member("StepSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @step_size.setter
    def step_size(self, value: primitives.Float) -> None:
        """Set the StepSize field value."""
        member = self.get_member("StepSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "StepSize", fields.FieldFloat(value=value)
            )

    @property
    def gain(self) -> primitives.Float | None:
        """The Gain field value."""
        member = self.get_member("Gain")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @gain.setter
    def gain(self, value: primitives.Float) -> None:
        """Set the Gain field value."""
        member = self.get_member("Gain")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Gain", fields.FieldFloat(value=value)
            )

    @property
    def exp(self) -> primitives.Float | None:
        """The Exp field value."""
        member = self.get_member("Exp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @exp.setter
    def exp(self, value: primitives.Float) -> None:
        """Set the Exp field value."""
        member = self.get_member("Exp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Exp", fields.FieldFloat(value=value)
            )

    @property
    def accumulation_cutoff(self) -> primitives.Float | None:
        """The AccumulationCutoff field value."""
        member = self.get_member("AccumulationCutoff")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accumulation_cutoff.setter
    def accumulation_cutoff(self, value: primitives.Float) -> None:
        """Set the AccumulationCutoff field value."""
        member = self.get_member("AccumulationCutoff")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AccumulationCutoff", fields.FieldFloat(value=value)
            )

    @property
    def hit_threshold(self) -> primitives.Float | None:
        """The HitThreshold field value."""
        member = self.get_member("HitThreshold")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @hit_threshold.setter
    def hit_threshold(self, value: primitives.Float) -> None:
        """Set the HitThreshold field value."""
        member = self.get_member("HitThreshold")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "HitThreshold", fields.FieldFloat(value=value)
            )

    @property
    def input_range(self) -> primitives.Float | None:
        """The InputRange field value."""
        member = self.get_member("InputRange")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @input_range.setter
    def input_range(self, value: primitives.Float) -> None:
        """Set the InputRange field value."""
        member = self.get_member("InputRange")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InputRange", fields.FieldFloat(value=value)
            )

    @property
    def input_offset(self) -> primitives.Float | None:
        """The InputOffset field value."""
        member = self.get_member("InputOffset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @input_offset.setter
    def input_offset(self, value: primitives.Float) -> None:
        """Set the InputOffset field value."""
        member = self.get_member("InputOffset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "InputOffset", fields.FieldFloat(value=value)
            )

    @property
    def use_alpha_channel(self) -> primitives.Bool | None:
        """The UseAlphaChannel field value."""
        member = self.get_member("UseAlphaChannel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_alpha_channel.setter
    def use_alpha_channel(self, value: primitives.Bool) -> None:
        """Set the UseAlphaChannel field value."""
        member = self.get_member("UseAlphaChannel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseAlphaChannel", fields.FieldBool(value=value)
            )

    @property
    def slices(self) -> members.SyncList | None:
        """The Slices member."""
        member = self.get_member("Slices")
        if isinstance(member, members.SyncList):
            return member
        return None

    @slices.setter
    def slices(self, value: members.SyncList) -> None:
        """Set the Slices member."""
        self.set_member("Slices", value)

    @property
    def highlights(self) -> members.SyncList | None:
        """The Highlights member."""
        member = self.get_member("Highlights")
        if isinstance(member, members.SyncList):
            return member
        return None

    @highlights.setter
    def highlights(self, value: members.SyncList) -> None:
        """Set the Highlights member."""
        self.set_member("Highlights", value)

