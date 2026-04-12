"""Generated component: GrabToolSnapper."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.igrab_event_receiver import IGrabEventReceiver
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class GrabToolSnapper(GeneratedComponent, IGrabEventReceiver, IWorldEventReceiver):
    """The GrabToolSnapper component snaps a grabbable component's slot on the same slot as this component to the tip of a tool or your tooltip anchor when the Grabbable is grabbed.

    Category: Transform/Interaction

    This component is mostly for internal use, it is what is responsible for
    the ReferenceProxy text that appears when you grab slots and fields in
    the inspector. You can still use it if you would like, please check the
    behavior section. = Behavior = If this component is added to a
    IGrabbable Object, when this object is grabbed it will be positioned at
    the tip of your Tool plus any offset specified in the offset field. On
    it's own this is not that usable but this is used internally with some
    UI Fields and Proxies to provide the blue text as shown above.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.GrabToolSnapper"

    def __init__(self, offset: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            offset: Initial value for Offset.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if offset is not None:
            self.offset = offset

    @property
    def offset(self) -> primitives.Float3 | None:
        """How far away from the tool the object should be upon grab."""
        member = self.get_member("Offset")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @offset.setter
    def offset(self, value: primitives.Float3) -> None:
        """Set the Offset field value."""
        member = self.get_member("Offset")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Offset", fields.FieldFloat3(value=value)
            )

