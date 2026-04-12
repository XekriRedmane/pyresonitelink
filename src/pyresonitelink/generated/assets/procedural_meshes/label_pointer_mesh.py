"""Generated component: LabelPointerMesh."""

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


class LabelPointerMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """The LabelPointerMesh component is used by the labeler tool to point to a position and underline some generated text elements.

    Category: Assets/Procedural Meshes
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LabelPointerMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, profile: ColorProfile | str | None = None, label_point: primitives.Float3 | None = None, target_point: primitives.Float3 | None = None, label_rotation: primitives.FloatQ | None = None, label_width: primitives.Float | None = None, width: primitives.Float | None = None, expand_lerp: primitives.Float | None = None, dual_sided: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            profile: Initial value for Profile.
            label_point: Initial value for LabelPoint.
            target_point: Initial value for TargetPoint.
            label_rotation: Initial value for LabelRotation.
            label_width: Initial value for LabelWidth.
            width: Initial value for Width.
            expand_lerp: Initial value for ExpandLerp.
            dual_sided: Initial value for DualSided.
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
        if label_point is not None:
            self.label_point = label_point
        if target_point is not None:
            self.target_point = target_point
        if label_rotation is not None:
            self.label_rotation = label_rotation
        if label_width is not None:
            self.label_width = label_width
        if width is not None:
            self.width = width
        if expand_lerp is not None:
            self.expand_lerp = expand_lerp
        if dual_sided is not None:
            self.dual_sided = dual_sided

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
    def label_point(self) -> primitives.Float3 | None:
        """Where the label should render in local space."""
        member = self.get_member("LabelPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @label_point.setter
    def label_point(self, value: primitives.Float3) -> None:
        """Set the LabelPoint field value."""
        member = self.get_member("LabelPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LabelPoint", fields.FieldFloat3(value=value)
            )

    @property
    def target_point(self) -> primitives.Float3 | None:
        """Where the line from the label should point to."""
        member = self.get_member("TargetPoint")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @target_point.setter
    def target_point(self, value: primitives.Float3) -> None:
        """Set the TargetPoint field value."""
        member = self.get_member("TargetPoint")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "TargetPoint", fields.FieldFloat3(value=value)
            )

    @property
    def label_rotation(self) -> primitives.FloatQ | None:
        """The rotation of the label visual."""
        member = self.get_member("LabelRotation")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @label_rotation.setter
    def label_rotation(self, value: primitives.FloatQ) -> None:
        """Set the LabelRotation field value."""
        member = self.get_member("LabelRotation")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LabelRotation", fields.FieldFloatQ(value=value)
            )

    @property
    def label_width(self) -> primitives.Float | None:
        """The width of the label visual."""
        member = self.get_member("LabelWidth")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @label_width.setter
    def label_width(self, value: primitives.Float) -> None:
        """Set the LabelWidth field value."""
        member = self.get_member("LabelWidth")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "LabelWidth", fields.FieldFloat(value=value)
            )

    @property
    def width(self) -> primitives.Float | None:
        """The width of the line going from the label to ``TargetPoint``"""
        member = self.get_member("Width")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @width.setter
    def width(self, value: primitives.Float) -> None:
        """Set the Width field value."""
        member = self.get_member("Width")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Width", fields.FieldFloat(value=value)
            )

    @property
    def expand_lerp(self) -> primitives.Float | None:
        """How long the label underline should be."""
        member = self.get_member("ExpandLerp")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @expand_lerp.setter
    def expand_lerp(self, value: primitives.Float) -> None:
        """Set the ExpandLerp field value."""
        member = self.get_member("ExpandLerp")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ExpandLerp", fields.FieldFloat(value=value)
            )

    @property
    def dual_sided(self) -> primitives.Bool | None:
        """Whether the mesh should have duplicate geometry with the fronts facing the opposite direction."""
        member = self.get_member("DualSided")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @dual_sided.setter
    def dual_sided(self, value: primitives.Bool) -> None:
        """Set the DualSided field value."""
        member = self.get_member("DualSided")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "DualSided", fields.FieldBool(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

