"""Generated component: UnwrappableBoxDriver."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class UnwrappableBoxDriver(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.UnwrappableBoxDriver.

    Category: Transform/Drivers
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.UnwrappableBoxDriver"

    def __init__(self, unwrap: np.float32 | None = None, side_size: np.float32 | None = None, scale_content: bool | None = None, side0rotation: str | IField[primitives.FloatQ] | None = None, side1rotation: str | IField[primitives.FloatQ] | None = None, side2rotation: str | IField[primitives.FloatQ] | None = None, side3rotation: str | IField[primitives.FloatQ] | None = None, top_rotation: str | IField[primitives.FloatQ] | None = None, side0offset: str | IField[primitives.Float3] | None = None, side1offset: str | IField[primitives.Float3] | None = None, side2offset: str | IField[primitives.Float3] | None = None, side3offset: str | IField[primitives.Float3] | None = None, top_offset: str | IField[primitives.Float3] | None = None, side0content_offset: str | IField[primitives.Float3] | None = None, side1content_offset: str | IField[primitives.Float3] | None = None, side2content_offset: str | IField[primitives.Float3] | None = None, side3content_offset: str | IField[primitives.Float3] | None = None, top_content_offset: str | IField[primitives.Float3] | None = None, side0content_scale: str | IField[primitives.Float3] | None = None, side1content_scale: str | IField[primitives.Float3] | None = None, side2content_scale: str | IField[primitives.Float3] | None = None, side3content_scale: str | IField[primitives.Float3] | None = None, bottom_content_scale: str | IField[primitives.Float3] | None = None, top_content_scale: str | IField[primitives.Float3] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            unwrap: Initial value for Unwrap.
            side_size: Initial value for SideSize.
            scale_content: Initial value for ScaleContent.
            side0rotation: Initial value for _side0rotation.
            side1rotation: Initial value for _side1rotation.
            side2rotation: Initial value for _side2rotation.
            side3rotation: Initial value for _side3rotation.
            top_rotation: Initial value for _topRotation.
            side0offset: Initial value for _side0offset.
            side1offset: Initial value for _side1offset.
            side2offset: Initial value for _side2offset.
            side3offset: Initial value for _side3offset.
            top_offset: Initial value for _topOffset.
            side0content_offset: Initial value for _side0contentOffset.
            side1content_offset: Initial value for _side1contentOffset.
            side2content_offset: Initial value for _side2contentOffset.
            side3content_offset: Initial value for _side3contentOffset.
            top_content_offset: Initial value for _topContentOffset.
            side0content_scale: Initial value for _side0contentScale.
            side1content_scale: Initial value for _side1contentScale.
            side2content_scale: Initial value for _side2contentScale.
            side3content_scale: Initial value for _side3contentScale.
            bottom_content_scale: Initial value for _bottomContentScale.
            top_content_scale: Initial value for _topContentScale.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if unwrap is not None:
            self.unwrap = unwrap
        if side_size is not None:
            self.side_size = side_size
        if scale_content is not None:
            self.scale_content = scale_content
        if side0rotation is not None:
            self.side0rotation = side0rotation
        if side1rotation is not None:
            self.side1rotation = side1rotation
        if side2rotation is not None:
            self.side2rotation = side2rotation
        if side3rotation is not None:
            self.side3rotation = side3rotation
        if top_rotation is not None:
            self.top_rotation = top_rotation
        if side0offset is not None:
            self.side0offset = side0offset
        if side1offset is not None:
            self.side1offset = side1offset
        if side2offset is not None:
            self.side2offset = side2offset
        if side3offset is not None:
            self.side3offset = side3offset
        if top_offset is not None:
            self.top_offset = top_offset
        if side0content_offset is not None:
            self.side0content_offset = side0content_offset
        if side1content_offset is not None:
            self.side1content_offset = side1content_offset
        if side2content_offset is not None:
            self.side2content_offset = side2content_offset
        if side3content_offset is not None:
            self.side3content_offset = side3content_offset
        if top_content_offset is not None:
            self.top_content_offset = top_content_offset
        if side0content_scale is not None:
            self.side0content_scale = side0content_scale
        if side1content_scale is not None:
            self.side1content_scale = side1content_scale
        if side2content_scale is not None:
            self.side2content_scale = side2content_scale
        if side3content_scale is not None:
            self.side3content_scale = side3content_scale
        if bottom_content_scale is not None:
            self.bottom_content_scale = bottom_content_scale
        if top_content_scale is not None:
            self.top_content_scale = top_content_scale

    @property
    def unwrap(self) -> np.float32 | None:
        """The Unwrap field value."""
        member = self.get_member("Unwrap")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @unwrap.setter
    def unwrap(self, value: np.float32) -> None:
        """Set the Unwrap field value."""
        member = self.get_member("Unwrap")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Unwrap", fields.FieldFloat(value=value)
            )

    @property
    def side_size(self) -> np.float32 | None:
        """The SideSize field value."""
        member = self.get_member("SideSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @side_size.setter
    def side_size(self, value: np.float32) -> None:
        """Set the SideSize field value."""
        member = self.get_member("SideSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "SideSize", fields.FieldFloat(value=value)
            )

    @property
    def scale_content(self) -> bool | None:
        """The ScaleContent field value."""
        member = self.get_member("ScaleContent")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale_content.setter
    def scale_content(self, value: bool) -> None:
        """Set the ScaleContent field value."""
        member = self.get_member("ScaleContent")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ScaleContent", fields.FieldBool(value=value)
            )

    @property
    def side0rotation(self) -> str | None:
        """Target ID of the _side0rotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_side0rotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side0rotation.setter
    def side0rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _side0rotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_side0rotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_side0rotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def side1rotation(self) -> str | None:
        """Target ID of the _side1rotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_side1rotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side1rotation.setter
    def side1rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _side1rotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_side1rotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_side1rotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def side2rotation(self) -> str | None:
        """Target ID of the _side2rotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_side2rotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side2rotation.setter
    def side2rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _side2rotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_side2rotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_side2rotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def side3rotation(self) -> str | None:
        """Target ID of the _side3rotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_side3rotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side3rotation.setter
    def side3rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _side3rotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_side3rotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_side3rotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def top_rotation(self) -> str | None:
        """Target ID of the _topRotation reference (targets IField[primitives.FloatQ])."""
        member = self.get_member("_topRotation")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @top_rotation.setter
    def top_rotation(self, target: str | IField[primitives.FloatQ] | None) -> None:
        """Set the _topRotation reference by target ID or IField[primitives.FloatQ] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_topRotation")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_topRotation",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<floatQ>'),
            )

    @property
    def side0offset(self) -> str | None:
        """Target ID of the _side0offset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_side0offset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side0offset.setter
    def side0offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _side0offset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_side0offset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_side0offset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def side1offset(self) -> str | None:
        """Target ID of the _side1offset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_side1offset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side1offset.setter
    def side1offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _side1offset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_side1offset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_side1offset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def side2offset(self) -> str | None:
        """Target ID of the _side2offset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_side2offset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side2offset.setter
    def side2offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _side2offset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_side2offset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_side2offset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def side3offset(self) -> str | None:
        """Target ID of the _side3offset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_side3offset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side3offset.setter
    def side3offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _side3offset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_side3offset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_side3offset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def top_offset(self) -> str | None:
        """Target ID of the _topOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_topOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @top_offset.setter
    def top_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _topOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_topOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_topOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def side0content_offset(self) -> str | None:
        """Target ID of the _side0contentOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_side0contentOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side0content_offset.setter
    def side0content_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _side0contentOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_side0contentOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_side0contentOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def side1content_offset(self) -> str | None:
        """Target ID of the _side1contentOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_side1contentOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side1content_offset.setter
    def side1content_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _side1contentOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_side1contentOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_side1contentOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def side2content_offset(self) -> str | None:
        """Target ID of the _side2contentOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_side2contentOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side2content_offset.setter
    def side2content_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _side2contentOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_side2contentOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_side2contentOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def side3content_offset(self) -> str | None:
        """Target ID of the _side3contentOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_side3contentOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side3content_offset.setter
    def side3content_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _side3contentOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_side3contentOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_side3contentOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def top_content_offset(self) -> str | None:
        """Target ID of the _topContentOffset reference (targets IField[primitives.Float3])."""
        member = self.get_member("_topContentOffset")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @top_content_offset.setter
    def top_content_offset(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _topContentOffset reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_topContentOffset")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_topContentOffset",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def side0content_scale(self) -> str | None:
        """Target ID of the _side0contentScale reference (targets IField[primitives.Float3])."""
        member = self.get_member("_side0contentScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side0content_scale.setter
    def side0content_scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _side0contentScale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_side0contentScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_side0contentScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def side1content_scale(self) -> str | None:
        """Target ID of the _side1contentScale reference (targets IField[primitives.Float3])."""
        member = self.get_member("_side1contentScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side1content_scale.setter
    def side1content_scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _side1contentScale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_side1contentScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_side1contentScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def side2content_scale(self) -> str | None:
        """Target ID of the _side2contentScale reference (targets IField[primitives.Float3])."""
        member = self.get_member("_side2contentScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side2content_scale.setter
    def side2content_scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _side2contentScale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_side2contentScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_side2contentScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def side3content_scale(self) -> str | None:
        """Target ID of the _side3contentScale reference (targets IField[primitives.Float3])."""
        member = self.get_member("_side3contentScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @side3content_scale.setter
    def side3content_scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _side3contentScale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_side3contentScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_side3contentScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def bottom_content_scale(self) -> str | None:
        """Target ID of the _bottomContentScale reference (targets IField[primitives.Float3])."""
        member = self.get_member("_bottomContentScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bottom_content_scale.setter
    def bottom_content_scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _bottomContentScale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_bottomContentScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_bottomContentScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def top_content_scale(self) -> str | None:
        """Target ID of the _topContentScale reference (targets IField[primitives.Float3])."""
        member = self.get_member("_topContentScale")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @top_content_scale.setter
    def top_content_scale(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _topContentScale reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_topContentScale")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_topContentScale",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

