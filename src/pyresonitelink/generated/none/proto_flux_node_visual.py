"""Generated component: ProtoFluxNodeVisual."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.proto_flux_node import ProtoFluxNode
from pyresonitelink.generated._types.hover_area import HoverArea
from pyresonitelink.generated._types.image import Image
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ProtoFluxNodeVisual(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxNodeVisual.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxNodeVisual"

    def __init__(self, node: str | ProtoFluxNode | None = None, is_selected: primitives.Bool | None = None, is_highlighted: primitives.Bool | None = None, node_hover_area: str | HoverArea | None = None, bg_image: str | Image | None = None, inputs_root: str | Slot | None = None, outputs_root: str | Slot | None = None, references_root: str | Slot | None = None, overview_visual: str | IField[primitives.Bool] | None = None, overview_bg: str | IField[primitives.ColorX] | None = None, label_bg: str | IField[primitives.Bool] | None = None, label_text: str | IField[primitives.Bool] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            node: Initial value for Node.
            is_selected: Initial value for IsSelected.
            is_highlighted: Initial value for IsHighlighted.
            node_hover_area: Initial value for _nodeHoverArea.
            bg_image: Initial value for _bgImage.
            inputs_root: Initial value for _inputsRoot.
            outputs_root: Initial value for _outputsRoot.
            references_root: Initial value for _referencesRoot.
            overview_visual: Initial value for _overviewVisual.
            overview_bg: Initial value for _overviewBg.
            label_bg: Initial value for _labelBg.
            label_text: Initial value for _labelText.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if node is not None:
            self.node = node
        if is_selected is not None:
            self.is_selected = is_selected
        if is_highlighted is not None:
            self.is_highlighted = is_highlighted
        if node_hover_area is not None:
            self.node_hover_area = node_hover_area
        if bg_image is not None:
            self.bg_image = bg_image
        if inputs_root is not None:
            self.inputs_root = inputs_root
        if outputs_root is not None:
            self.outputs_root = outputs_root
        if references_root is not None:
            self.references_root = references_root
        if overview_visual is not None:
            self.overview_visual = overview_visual
        if overview_bg is not None:
            self.overview_bg = overview_bg
        if label_bg is not None:
            self.label_bg = label_bg
        if label_text is not None:
            self.label_text = label_text

    @property
    def node(self) -> str | None:
        """Target ID of the Node reference (targets ProtoFluxNode)."""
        member = self.get_member("Node")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @node.setter
    def node(self, target: str | ProtoFluxNode | None) -> None:
        """Set the Node reference by target ID or ProtoFluxNode instance."""
        target_id: str | None = target.id if isinstance(target, ProtoFluxNode) else target  # type: ignore[assignment]
        member = self.get_member("Node")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Node",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ProtoFlux.ProtoFluxNode'),
            )

    @property
    def is_selected(self) -> primitives.Bool | None:
        """The IsSelected field value."""
        member = self.get_member("IsSelected")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_selected.setter
    def is_selected(self, value: primitives.Bool) -> None:
        """Set the IsSelected field value."""
        member = self.get_member("IsSelected")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsSelected", fields.FieldBool(value=value)
            )

    @property
    def is_highlighted(self) -> primitives.Bool | None:
        """The IsHighlighted field value."""
        member = self.get_member("IsHighlighted")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @is_highlighted.setter
    def is_highlighted(self, value: primitives.Bool) -> None:
        """Set the IsHighlighted field value."""
        member = self.get_member("IsHighlighted")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "IsHighlighted", fields.FieldBool(value=value)
            )

    @property
    def node_hover_area(self) -> str | None:
        """Target ID of the _nodeHoverArea reference (targets HoverArea)."""
        member = self.get_member("_nodeHoverArea")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @node_hover_area.setter
    def node_hover_area(self, target: str | HoverArea | None) -> None:
        """Set the _nodeHoverArea reference by target ID or HoverArea instance."""
        target_id: str | None = target.id if isinstance(target, HoverArea) else target  # type: ignore[assignment]
        member = self.get_member("_nodeHoverArea")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_nodeHoverArea",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.HoverArea'),
            )

    @property
    def bg_image(self) -> str | None:
        """Target ID of the _bgImage reference (targets Image)."""
        member = self.get_member("_bgImage")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @bg_image.setter
    def bg_image(self, target: str | Image | None) -> None:
        """Set the _bgImage reference by target ID or Image instance."""
        target_id: str | None = target.id if isinstance(target, Image) else target  # type: ignore[assignment]
        member = self.get_member("_bgImage")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_bgImage",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Image'),
            )

    @property
    def inputs_root(self) -> str | None:
        """Target ID of the _inputsRoot reference (targets Slot)."""
        member = self.get_member("_inputsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @inputs_root.setter
    def inputs_root(self, target: str | Slot | None) -> None:
        """Set the _inputsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_inputsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_inputsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def outputs_root(self) -> str | None:
        """Target ID of the _outputsRoot reference (targets Slot)."""
        member = self.get_member("_outputsRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @outputs_root.setter
    def outputs_root(self, target: str | Slot | None) -> None:
        """Set the _outputsRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_outputsRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_outputsRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def references_root(self) -> str | None:
        """Target ID of the _referencesRoot reference (targets Slot)."""
        member = self.get_member("_referencesRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @references_root.setter
    def references_root(self, target: str | Slot | None) -> None:
        """Set the _referencesRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_referencesRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_referencesRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def overview_visual(self) -> str | None:
        """Target ID of the _overviewVisual reference (targets IField[primitives.Bool])."""
        member = self.get_member("_overviewVisual")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @overview_visual.setter
    def overview_visual(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _overviewVisual reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_overviewVisual")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_overviewVisual",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def overview_bg(self) -> str | None:
        """Target ID of the _overviewBg reference (targets IField[primitives.ColorX])."""
        member = self.get_member("_overviewBg")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @overview_bg.setter
    def overview_bg(self, target: str | IField[primitives.ColorX] | None) -> None:
        """Set the _overviewBg reference by target ID or IField[primitives.ColorX] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_overviewBg")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_overviewBg",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<colorX>'),
            )

    @property
    def label_bg(self) -> str | None:
        """Target ID of the _labelBg reference (targets IField[primitives.Bool])."""
        member = self.get_member("_labelBg")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @label_bg.setter
    def label_bg(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _labelBg reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_labelBg")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_labelBg",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def label_text(self) -> str | None:
        """Target ID of the _labelText reference (targets IField[primitives.Bool])."""
        member = self.get_member("_labelText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @label_text.setter
    def label_text(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _labelText reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_labelText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_labelText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

