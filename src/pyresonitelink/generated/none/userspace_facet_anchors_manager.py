"""Generated component: UserspaceFacetAnchorsManager."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.generated._enums.chirality import Chirality
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.userspace_radiant_dash import UserspaceRadiantDash
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UserspaceFacetAnchorsManager(GeneratedComponent, IComponent, IWorldEventReceiver):
    """To know what this controls, see Facet Anchors.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UserspaceFacetAnchorsManager"

    def __init__(self, open: primitives.Bool | None = None, use_facet_anchors: primitives.Bool | None = None, toggle: Chirality | str | None = None, anim_speed: primitives.Float | None = None, dash: str | UserspaceRadiantDash | None = None, profile_name: primitives.String | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            open: Initial value for Open.
            use_facet_anchors: Initial value for UseFacetAnchors.
            toggle: Initial value for Toggle.
            anim_speed: Initial value for AnimSpeed.
            dash: Initial value for Dash.
            profile_name: Initial value for ProfileName.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if open is not None:
            self.open = open
        if use_facet_anchors is not None:
            self.use_facet_anchors = use_facet_anchors
        if toggle is not None:
            self.toggle = toggle
        if anim_speed is not None:
            self.anim_speed = anim_speed
        if dash is not None:
            self.dash = dash
        if profile_name is not None:
            self.profile_name = profile_name

    @property
    def open(self) -> primitives.Bool | None:
        """Whether the facet anchors are open or closed."""
        member = self.get_member("Open")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @open.setter
    def open(self, value: primitives.Bool) -> None:
        """Set the Open field value."""
        member = self.get_member("Open")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Open", fields.FieldBool(value=value)
            )

    @property
    def use_facet_anchors(self) -> primitives.Bool | None:
        """Whether to allow the use of facet anchors."""
        member = self.get_member("UseFacetAnchors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @use_facet_anchors.setter
    def use_facet_anchors(self, value: primitives.Bool) -> None:
        """Set the UseFacetAnchors field value."""
        member = self.get_member("UseFacetAnchors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "UseFacetAnchors", fields.FieldBool(value=value)
            )

    @property
    def toggle(self) -> Chirality | None:
        """What controller toggles facet anchors when opening dash."""
        member = self.get_member("Toggle")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return Chirality(member.value)
        return None

    @toggle.setter
    def toggle(self, value: Chirality | str) -> None:
        """Set Toggle. What controller toggles facet anchors when opening dash."""
        member = self.get_member("Toggle")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "Toggle",
                members.FieldEnum(value=str(value)),
            )

    @property
    def anim_speed(self) -> primitives.Float | None:
        """How fast the facet anchors should open or close."""
        member = self.get_member("AnimSpeed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @anim_speed.setter
    def anim_speed(self, value: primitives.Float) -> None:
        """Set the AnimSpeed field value."""
        member = self.get_member("AnimSpeed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AnimSpeed", fields.FieldFloat(value=value)
            )

    @property
    def dash(self) -> str | None:
        """The dash that is in the world this component is managing facet anchors for."""
        member = self.get_member("Dash")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @dash.setter
    def dash(self, target: str | UserspaceRadiantDash | None) -> None:
        """Set the Dash reference by target ID or UserspaceRadiantDash instance."""
        target_id: str | None = target.id if isinstance(target, UserspaceRadiantDash) else target  # type: ignore[assignment]
        member = self.get_member("Dash")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Dash",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UserspaceRadiantDash'),
            )

    @property
    def profile_name(self) -> primitives.String | None:
        """The name of the profile to use when loading the facet anchors."""
        member = self.get_member("ProfileName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @profile_name.setter
    def profile_name(self, value: primitives.String) -> None:
        """Set the ProfileName field value."""
        member = self.get_member("ProfileName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProfileName", fields.FieldString(value=value)
            )

    @property
    def anchors(self) -> members.SyncList | None:
        """A list of facet anchors and their data."""
        member = self.get_member("Anchors")
        if isinstance(member, members.SyncList):
            return member
        return None

    @anchors.setter
    def anchors(self, value: members.SyncList) -> None:
        """Set Anchors. A list of facet anchors and their data."""
        self.set_member("Anchors", value)

