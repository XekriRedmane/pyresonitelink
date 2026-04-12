"""Generated component: DiagnosticGaussianSplat."""

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


class DiagnosticGaussianSplat(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The Diagnostic Gaussian Splat component is used to render diagnostic info on Gaussian Splats.

    Category: Assets/Procedural Gaussian Splats
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.DiagnosticGaussianSplat"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, splat_color_profile: ColorProfile | str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            splat_color_profile: Initial value for SplatColorProfile.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if splat_color_profile is not None:
            self.splat_color_profile = splat_color_profile

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
    def splat_color_profile(self) -> ColorProfile | None:
        """The SplatColorProfile enum value."""
        member = self.get_member("SplatColorProfile")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return ColorProfile(member.value)
        return None

    @splat_color_profile.setter
    def splat_color_profile(self, value: ColorProfile | str) -> None:
        """Set the SplatColorProfile enum value."""
        member = self.get_member("SplatColorProfile")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "SplatColorProfile",
                members.FieldEnum(value=str(value)),
            )

    @property
    def splats(self) -> members.SyncList | None:
        """A list of splats to render diagnostics for."""
        member = self.get_member("Splats")
        if isinstance(member, members.SyncList):
            return member
        return None

    @splats.setter
    def splats(self, value: members.SyncList) -> None:
        """Set Splats. A list of splats to render diagnostics for."""
        self.set_member("Splats", value)

    async def bake_gaussian_splat(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeGaussianSplat sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeGaussianSplat", {}, debug,
        )

