"""Generated component: BevelStripeMesh."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BevelStripeMesh(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.BevelStripeMesh.

    Category: Assets/Procedural Meshes/Legacy UI
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BevelStripeMesh"

    def __init__(self, high_priority_integration: primitives.Bool | None = None, override_bounding_box: primitives.Bool | None = None, overriden_bounding_box: primitives.BoundingBox | None = None, width: primitives.Float | None = None, height: primitives.Float | None = None, thickness: primitives.Float | None = None, slant_left: primitives.Float | None = None, slant_right: primitives.Float | None = None, relief: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            high_priority_integration: Initial value for HighPriorityIntegration.
            override_bounding_box: Initial value for OverrideBoundingBox.
            overriden_bounding_box: Initial value for OverridenBoundingBox.
            width: Initial value for Width.
            height: Initial value for Height.
            thickness: Initial value for Thickness.
            slant_left: Initial value for SlantLeft.
            slant_right: Initial value for SlantRight.
            relief: Initial value for Relief.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if high_priority_integration is not None:
            self.high_priority_integration = high_priority_integration
        if override_bounding_box is not None:
            self.override_bounding_box = override_bounding_box
        if overriden_bounding_box is not None:
            self.overriden_bounding_box = overriden_bounding_box
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if thickness is not None:
            self.thickness = thickness
        if slant_left is not None:
            self.slant_left = slant_left
        if slant_right is not None:
            self.slant_right = slant_right
        if relief is not None:
            self.relief = relief

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
    def profile(self) -> members.FieldEnum | None:
        """The Profile member."""
        member = self.get_member("Profile")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @profile.setter
    def profile(self, value: members.FieldEnum) -> None:
        """Set the Profile member."""
        self.set_member("Profile", value)

    @property
    def width(self) -> primitives.Float | None:
        """The Width field value."""
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
    def height(self) -> primitives.Float | None:
        """The Height field value."""
        member = self.get_member("Height")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @height.setter
    def height(self, value: primitives.Float) -> None:
        """Set the Height field value."""
        member = self.get_member("Height")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Height", fields.FieldFloat(value=value)
            )

    @property
    def thickness(self) -> primitives.Float | None:
        """The Thickness field value."""
        member = self.get_member("Thickness")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @thickness.setter
    def thickness(self, value: primitives.Float) -> None:
        """Set the Thickness field value."""
        member = self.get_member("Thickness")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Thickness", fields.FieldFloat(value=value)
            )

    @property
    def slant_left(self) -> primitives.Float | None:
        """The SlantLeft field value."""
        member = self.get_member("SlantLeft")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @slant_left.setter
    def slant_left(self, value: primitives.Float) -> None:
        """Set the SlantLeft field value."""
        member = self.get_member("SlantLeft")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SlantLeft", fields.FieldFloat(value=value)
            )

    @property
    def slant_right(self) -> primitives.Float | None:
        """The SlantRight field value."""
        member = self.get_member("SlantRight")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @slant_right.setter
    def slant_right(self, value: primitives.Float) -> None:
        """Set the SlantRight field value."""
        member = self.get_member("SlantRight")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SlantRight", fields.FieldFloat(value=value)
            )

    @property
    def relief(self) -> primitives.Bool | None:
        """The Relief field value."""
        member = self.get_member("Relief")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @relief.setter
    def relief(self, value: primitives.Bool) -> None:
        """Set the Relief field value."""
        member = self.get_member("Relief")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Relief", fields.FieldBool(value=value)
            )

    async def bake_mesh(self, resolink: protocols.ResoniteLinkClient, debug: bool = False) -> dict:
        """Call the BakeMesh sync method.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "BakeMesh", {}, debug,
        )

