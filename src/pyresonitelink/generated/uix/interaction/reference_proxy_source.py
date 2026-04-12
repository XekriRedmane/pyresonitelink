"""Generated component: ReferenceProxySource."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iworld_element import IWorldElement
from pyresonitelink.generated._types.iui_grabbable import IUIGrabbable
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ReferenceProxySource(GeneratedComponent, IUIGrabbable, IWorldEventReceiver):
    """The ReferenceProxySource component allows for the user to grab a reference off from a UIX element. This requires a Button component to work.

}}

    Category: UIX/Interaction

    This is used to carry references to other fields that are looking for
    it. Using this component along with the ReferenceGrabReceiver and
    ReferenceField of the type IWorldElement will allow the user to carry
    the reference from source to receiver directly.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ReferenceProxySource"

    def __init__(self, reference: str | IWorldElement | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            reference: Initial value for Reference.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if reference is not None:
            self.reference = reference

    @property
    def reference(self) -> str | None:
        """The reference itself."""
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @reference.setter
    def reference(self, target: str | IWorldElement | None) -> None:
        """Set the Reference reference by target ID or IWorldElement instance."""
        target_id: str | None = target.id if isinstance(target, IWorldElement) else target  # type: ignore[assignment]
        member = self.get_member("Reference")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Reference",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IWorldElement'),
            )

