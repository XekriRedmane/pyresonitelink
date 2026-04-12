"""Generated component: BoundingBoxDriver."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ibounded import IBounded
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BoundingBoxDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """The BoundingBoxDriver component is commonly used in Basic text objects to size the collider based on the text. This takes any IBounded and turns its Bounding box data into its local space center point and local space size. This is useful for auto generating the size and center of a BoxCollider around a procedural mesh.

    Category: Transform/Drivers

    Attach to a slot and provide ``BoundedSource``. The output fields are
    best used to drive a BoxCollider.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BoundingBoxDriver"

    def __init__(self, bounded_source: str | IBounded | None = None, size: str | IField[primitives.Float3] | None = None, center: str | IField[primitives.Float3] | None = None, padding: primitives.Float3 | None = None, scale: primitives.Float3 | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            bounded_source: Initial value for BoundedSource.
            size: Initial value for Size.
            center: Initial value for Center.
            padding: Initial value for Padding.
            scale: Initial value for Scale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if bounded_source is not None:
            self.bounded_source = bounded_source
        if size is not None:
            self.size = size
        if center is not None:
            self.center = center
        if padding is not None:
            self.padding = padding
        if scale is not None:
            self.scale = scale

    @property
    def bounded_source(self) -> str | None:
        """The object to get Bounding box data from."""
        member = self.get_member("BoundedSource")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bounded_source.setter
    def bounded_source(self, target: str | IBounded | None) -> None:
        """Set the BoundedSource reference by target ID or IBounded instance."""
        target_id: str | None = target.id if isinstance(target, IBounded) else target  # type: ignore[assignment]
        member = self.get_member("BoundedSource")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "BoundedSource",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IBounded'),
            )

    @property
    def size(self) -> str | None:
        """The field to drive with the local space size of the bounding box of ``BoundedSource``."""
        member = self.get_member("Size")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @size.setter
    def size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the Size reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Size")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Size",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def center(self) -> str | None:
        """The field to drive with the local space center of the bounding box of ``BoundedSource``."""
        member = self.get_member("Center")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @center.setter
    def center(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the Center reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("Center")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Center",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def padding(self) -> primitives.Float3 | None:
        """how much to add to the output of ``Size``"""
        member = self.get_member("Padding")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @padding.setter
    def padding(self, value: primitives.Float3) -> None:
        """Set the Padding field value."""
        member = self.get_member("Padding")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Padding", fields.FieldFloat3(value=value)
            )

    @property
    def scale(self) -> primitives.Float3 | None:
        """how much to multiply the output of ``Size``"""
        member = self.get_member("Scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale.setter
    def scale(self, value: primitives.Float3) -> None:
        """Set the Scale field value."""
        member = self.get_member("Scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Scale", fields.FieldFloat3(value=value)
            )

