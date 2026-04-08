"""Generated component: LegacyPanel."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.legacy_ui_style import LegacyUIStyle
from pyresonitelink.generated._types.pbs_rim_metallic import PBS_RimMetallic
from pyresonitelink.generated._types.bevel_plane_mesh import BevelPlaneMesh
from pyresonitelink.generated._types.ifield import IField
from pyresonitelink.generated._types.bevel_stripe_mesh import BevelStripeMesh
from pyresonitelink.generated._types.text_renderer import TextRenderer
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.title_button import TitleButton
from pyresonitelink.generated._types.iobject_root import IObjectRoot
from pyresonitelink.generated._types.iui_interface import IUIInterface
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class LegacyPanel(GeneratedComponent, IObjectRoot, IUIInterface, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.LegacyPanel.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.LegacyPanel"

    def __init__(self, style: str | LegacyUIStyle | None = None, accept_physical_touch: primitives.Bool | None = None, accept_remote_touch: primitives.Bool | None = None, show_header: primitives.Bool | None = None, show_handle: primitives.Bool | None = None, padding: primitives.Float | None = None, zpadding: primitives.Float | None = None, thickness: primitives.Float | None = None, color: primitives.ColorX | None = None, material: str | PBS_RimMetallic | None = None, panel_mesh: str | BevelPlaneMesh | None = None, panel_pos: str | IField[primitives.Float3] | None = None, handle_active: str | IField[primitives.Bool] | None = None, header_active: str | IField[primitives.Bool] | None = None, handle_mesh: str | BevelStripeMesh | None = None, handle_pos: str | IField[primitives.Float3] | None = None, handle_collider_size: str | IField[primitives.Float3] | None = None, header_title_mesh: str | BevelStripeMesh | None = None, header_button_mesh: str | BevelStripeMesh | None = None, header_collider: str | IField[primitives.Float3] | None = None, header_pos: str | IField[primitives.Float3] | None = None, header_title_pos: str | IField[primitives.Float3] | None = None, title: primitives.String | None = None, title_text: str | TextRenderer | None = None, indicate_private: primitives.Bool | None = None, title_pos: str | IField[primitives.Float3] | None = None, title_bounds: str | IField[primitives.Float2] | None = None, content_slot: str | Slot | None = None, header_root: str | Slot | None = None, handle_anchor_point: str | Slot | None = None, handle_anchor_point_position: str | IField[primitives.Float3] | None = None, highlighted_button: str | TitleButton | None = None, pin_button: str | TitleButton | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            style: Initial value for Style.
            accept_physical_touch: Initial value for AcceptPhysicalTouch.
            accept_remote_touch: Initial value for AcceptRemoteTouch.
            show_header: Initial value for ShowHeader.
            show_handle: Initial value for ShowHandle.
            padding: Initial value for Padding.
            zpadding: Initial value for ZPadding.
            thickness: Initial value for Thickness.
            color: Initial value for Color.
            material: Initial value for _material.
            panel_mesh: Initial value for _panelMesh.
            panel_pos: Initial value for _panelPos.
            handle_active: Initial value for _handleActive.
            header_active: Initial value for _headerActive.
            handle_mesh: Initial value for _handleMesh.
            handle_pos: Initial value for _handlePos.
            handle_collider_size: Initial value for _handleColliderSize.
            header_title_mesh: Initial value for _headerTitleMesh.
            header_button_mesh: Initial value for _headerButtonMesh.
            header_collider: Initial value for _headerCollider.
            header_pos: Initial value for _headerPos.
            header_title_pos: Initial value for _headerTitlePos.
            title: Initial value for _title.
            title_text: Initial value for _titleText.
            indicate_private: Initial value for _indicatePrivate.
            title_pos: Initial value for _titlePos.
            title_bounds: Initial value for _titleBounds.
            content_slot: Initial value for _contentSlot.
            header_root: Initial value for _headerRoot.
            handle_anchor_point: Initial value for _handleAnchorPoint.
            handle_anchor_point_position: Initial value for _handleAnchorPointPosition.
            highlighted_button: Initial value for _highlightedButton.
            pin_button: Initial value for _pinButton.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if style is not None:
            self.style = style
        if accept_physical_touch is not None:
            self.accept_physical_touch = accept_physical_touch
        if accept_remote_touch is not None:
            self.accept_remote_touch = accept_remote_touch
        if show_header is not None:
            self.show_header = show_header
        if show_handle is not None:
            self.show_handle = show_handle
        if padding is not None:
            self.padding = padding
        if zpadding is not None:
            self.zpadding = zpadding
        if thickness is not None:
            self.thickness = thickness
        if color is not None:
            self.color = color
        if material is not None:
            self.material = material
        if panel_mesh is not None:
            self.panel_mesh = panel_mesh
        if panel_pos is not None:
            self.panel_pos = panel_pos
        if handle_active is not None:
            self.handle_active = handle_active
        if header_active is not None:
            self.header_active = header_active
        if handle_mesh is not None:
            self.handle_mesh = handle_mesh
        if handle_pos is not None:
            self.handle_pos = handle_pos
        if handle_collider_size is not None:
            self.handle_collider_size = handle_collider_size
        if header_title_mesh is not None:
            self.header_title_mesh = header_title_mesh
        if header_button_mesh is not None:
            self.header_button_mesh = header_button_mesh
        if header_collider is not None:
            self.header_collider = header_collider
        if header_pos is not None:
            self.header_pos = header_pos
        if header_title_pos is not None:
            self.header_title_pos = header_title_pos
        if title is not None:
            self.title = title
        if title_text is not None:
            self.title_text = title_text
        if indicate_private is not None:
            self.indicate_private = indicate_private
        if title_pos is not None:
            self.title_pos = title_pos
        if title_bounds is not None:
            self.title_bounds = title_bounds
        if content_slot is not None:
            self.content_slot = content_slot
        if header_root is not None:
            self.header_root = header_root
        if handle_anchor_point is not None:
            self.handle_anchor_point = handle_anchor_point
        if handle_anchor_point_position is not None:
            self.handle_anchor_point_position = handle_anchor_point_position
        if highlighted_button is not None:
            self.highlighted_button = highlighted_button
        if pin_button is not None:
            self.pin_button = pin_button

    @property
    def style(self) -> str | None:
        """Target ID of the Style reference (targets LegacyUIStyle)."""
        member = self.get_member("Style")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @style.setter
    def style(self, target: str | LegacyUIStyle | None) -> None:
        """Set the Style reference by target ID or LegacyUIStyle instance."""
        target_id: str | None = target.id if isinstance(target, LegacyUIStyle) else target  # type: ignore[assignment]
        member = self.get_member("Style")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Style",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyUIStyle'),
            )

    @property
    def accept_physical_touch(self) -> primitives.Bool | None:
        """The AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_physical_touch.setter
    def accept_physical_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptPhysicalTouch field value."""
        member = self.get_member("AcceptPhysicalTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptPhysicalTouch", fields.FieldBool(value=value)
            )

    @property
    def accept_remote_touch(self) -> primitives.Bool | None:
        """The AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @accept_remote_touch.setter
    def accept_remote_touch(self, value: primitives.Bool) -> None:
        """Set the AcceptRemoteTouch field value."""
        member = self.get_member("AcceptRemoteTouch")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "AcceptRemoteTouch", fields.FieldBool(value=value)
            )

    @property
    def show_header(self) -> primitives.Bool | None:
        """The ShowHeader field value."""
        member = self.get_member("ShowHeader")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_header.setter
    def show_header(self, value: primitives.Bool) -> None:
        """Set the ShowHeader field value."""
        member = self.get_member("ShowHeader")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowHeader", fields.FieldBool(value=value)
            )

    @property
    def show_handle(self) -> primitives.Bool | None:
        """The ShowHandle field value."""
        member = self.get_member("ShowHandle")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @show_handle.setter
    def show_handle(self, value: primitives.Bool) -> None:
        """Set the ShowHandle field value."""
        member = self.get_member("ShowHandle")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ShowHandle", fields.FieldBool(value=value)
            )

    @property
    def padding(self) -> primitives.Float | None:
        """The Padding field value."""
        member = self.get_member("Padding")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @padding.setter
    def padding(self, value: primitives.Float) -> None:
        """Set the Padding field value."""
        member = self.get_member("Padding")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Padding", fields.FieldFloat(value=value)
            )

    @property
    def zpadding(self) -> primitives.Float | None:
        """The ZPadding field value."""
        member = self.get_member("ZPadding")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @zpadding.setter
    def zpadding(self, value: primitives.Float) -> None:
        """Set the ZPadding field value."""
        member = self.get_member("ZPadding")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ZPadding", fields.FieldFloat(value=value)
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
    def white_list(self) -> members.SyncList | None:
        """The WhiteList member."""
        member = self.get_member("WhiteList")
        if isinstance(member, members.SyncList):
            return member
        return None

    @white_list.setter
    def white_list(self, value: members.SyncList) -> None:
        """Set the WhiteList member."""
        self.set_member("WhiteList", value)

    @property
    def black_list(self) -> members.SyncList | None:
        """The BlackList member."""
        member = self.get_member("BlackList")
        if isinstance(member, members.SyncList):
            return member
        return None

    @black_list.setter
    def black_list(self, value: members.SyncList) -> None:
        """Set the BlackList member."""
        self.set_member("BlackList", value)

    @property
    def color(self) -> primitives.ColorX | None:
        """The Color field value."""
        member = self.get_member("Color")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @color.setter
    def color(self, value: primitives.ColorX) -> None:
        """Set the Color field value."""
        member = self.get_member("Color")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "Color", fields.FieldColorX(value=value)
            )

    @property
    def material(self) -> str | None:
        """Target ID of the _material reference (targets PBS_RimMetallic)."""
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | PBS_RimMetallic | None) -> None:
        """Set the _material reference by target ID or PBS_RimMetallic instance."""
        target_id: str | None = target.id if isinstance(target, PBS_RimMetallic) else target  # type: ignore[assignment]
        member = self.get_member("_material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.PBS_RimMetallic'),
            )

    @property
    def panel_mesh(self) -> str | None:
        """Target ID of the _panelMesh reference (targets BevelPlaneMesh)."""
        member = self.get_member("_panelMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @panel_mesh.setter
    def panel_mesh(self, target: str | BevelPlaneMesh | None) -> None:
        """Set the _panelMesh reference by target ID or BevelPlaneMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelPlaneMesh) else target  # type: ignore[assignment]
        member = self.get_member("_panelMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_panelMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelPlaneMesh'),
            )

    @property
    def panel_pos(self) -> str | None:
        """Target ID of the _panelPos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_panelPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @panel_pos.setter
    def panel_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _panelPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_panelPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_panelPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def handle_active(self) -> str | None:
        """Target ID of the _handleActive reference (targets IField[primitives.Bool])."""
        member = self.get_member("_handleActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @handle_active.setter
    def handle_active(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _handleActive reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_handleActive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_handleActive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def header_active(self) -> str | None:
        """Target ID of the _headerActive reference (targets IField[primitives.Bool])."""
        member = self.get_member("_headerActive")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @header_active.setter
    def header_active(self, target: str | IField[primitives.Bool] | None) -> None:
        """Set the _headerActive reference by target ID or IField[primitives.Bool] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_headerActive")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_headerActive",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<bool>'),
            )

    @property
    def handle_mesh(self) -> str | None:
        """Target ID of the _handleMesh reference (targets BevelStripeMesh)."""
        member = self.get_member("_handleMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @handle_mesh.setter
    def handle_mesh(self, target: str | BevelStripeMesh | None) -> None:
        """Set the _handleMesh reference by target ID or BevelStripeMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelStripeMesh) else target  # type: ignore[assignment]
        member = self.get_member("_handleMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_handleMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelStripeMesh'),
            )

    @property
    def handle_pos(self) -> str | None:
        """Target ID of the _handlePos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_handlePos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @handle_pos.setter
    def handle_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _handlePos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_handlePos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_handlePos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def handle_collider_size(self) -> str | None:
        """Target ID of the _handleColliderSize reference (targets IField[primitives.Float3])."""
        member = self.get_member("_handleColliderSize")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @handle_collider_size.setter
    def handle_collider_size(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _handleColliderSize reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_handleColliderSize")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_handleColliderSize",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def header_title_mesh(self) -> str | None:
        """Target ID of the _headerTitleMesh reference (targets BevelStripeMesh)."""
        member = self.get_member("_headerTitleMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @header_title_mesh.setter
    def header_title_mesh(self, target: str | BevelStripeMesh | None) -> None:
        """Set the _headerTitleMesh reference by target ID or BevelStripeMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelStripeMesh) else target  # type: ignore[assignment]
        member = self.get_member("_headerTitleMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_headerTitleMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelStripeMesh'),
            )

    @property
    def header_button_mesh(self) -> str | None:
        """Target ID of the _headerButtonMesh reference (targets BevelStripeMesh)."""
        member = self.get_member("_headerButtonMesh")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @header_button_mesh.setter
    def header_button_mesh(self, target: str | BevelStripeMesh | None) -> None:
        """Set the _headerButtonMesh reference by target ID or BevelStripeMesh instance."""
        target_id: str | None = target.id if isinstance(target, BevelStripeMesh) else target  # type: ignore[assignment]
        member = self.get_member("_headerButtonMesh")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_headerButtonMesh",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.BevelStripeMesh'),
            )

    @property
    def header_collider(self) -> str | None:
        """Target ID of the _headerCollider reference (targets IField[primitives.Float3])."""
        member = self.get_member("_headerCollider")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @header_collider.setter
    def header_collider(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _headerCollider reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_headerCollider")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_headerCollider",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def header_pos(self) -> str | None:
        """Target ID of the _headerPos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_headerPos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @header_pos.setter
    def header_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _headerPos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_headerPos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_headerPos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def header_title_pos(self) -> str | None:
        """Target ID of the _headerTitlePos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_headerTitlePos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @header_title_pos.setter
    def header_title_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _headerTitlePos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_headerTitlePos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_headerTitlePos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def title(self) -> primitives.String | None:
        """The _title field value."""
        member = self.get_member("_title")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @title.setter
    def title(self, value: primitives.String) -> None:
        """Set the _title field value."""
        member = self.get_member("_title")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_title", fields.FieldString(value=value)
            )

    @property
    def title_text(self) -> str | None:
        """Target ID of the _titleText reference (targets TextRenderer)."""
        member = self.get_member("_titleText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @title_text.setter
    def title_text(self, target: str | TextRenderer | None) -> None:
        """Set the _titleText reference by target ID or TextRenderer instance."""
        target_id: str | None = target.id if isinstance(target, TextRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_titleText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_titleText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.TextRenderer'),
            )

    @property
    def indicate_private(self) -> primitives.Bool | None:
        """The _indicatePrivate field value."""
        member = self.get_member("_indicatePrivate")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @indicate_private.setter
    def indicate_private(self, value: primitives.Bool) -> None:
        """Set the _indicatePrivate field value."""
        member = self.get_member("_indicatePrivate")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_indicatePrivate", fields.FieldBool(value=value)
            )

    @property
    def title_pos(self) -> str | None:
        """Target ID of the _titlePos reference (targets IField[primitives.Float3])."""
        member = self.get_member("_titlePos")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @title_pos.setter
    def title_pos(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _titlePos reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_titlePos")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_titlePos",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def title_bounds(self) -> str | None:
        """Target ID of the _titleBounds reference (targets IField[primitives.Float2])."""
        member = self.get_member("_titleBounds")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @title_bounds.setter
    def title_bounds(self, target: str | IField[primitives.Float2] | None) -> None:
        """Set the _titleBounds reference by target ID or IField[primitives.Float2] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_titleBounds")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_titleBounds",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float2>'),
            )

    @property
    def content_slot(self) -> str | None:
        """Target ID of the _contentSlot reference (targets Slot)."""
        member = self.get_member("_contentSlot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content_slot.setter
    def content_slot(self, target: str | Slot | None) -> None:
        """Set the _contentSlot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_contentSlot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_contentSlot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def header_root(self) -> str | None:
        """Target ID of the _headerRoot reference (targets Slot)."""
        member = self.get_member("_headerRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @header_root.setter
    def header_root(self, target: str | Slot | None) -> None:
        """Set the _headerRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_headerRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_headerRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def handle_anchor_point(self) -> str | None:
        """Target ID of the _handleAnchorPoint reference (targets Slot)."""
        member = self.get_member("_handleAnchorPoint")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @handle_anchor_point.setter
    def handle_anchor_point(self, target: str | Slot | None) -> None:
        """Set the _handleAnchorPoint reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_handleAnchorPoint")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_handleAnchorPoint",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def handle_anchor_point_position(self) -> str | None:
        """Target ID of the _handleAnchorPointPosition reference (targets IField[primitives.Float3])."""
        member = self.get_member("_handleAnchorPointPosition")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @handle_anchor_point_position.setter
    def handle_anchor_point_position(self, target: str | IField[primitives.Float3] | None) -> None:
        """Set the _handleAnchorPointPosition reference by target ID or IField[primitives.Float3] instance."""
        target_id: str | None = target.id if isinstance(target, IField) else target  # type: ignore[assignment]
        member = self.get_member("_handleAnchorPointPosition")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_handleAnchorPointPosition",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IField<float3>'),
            )

    @property
    def userspace_owner(self) -> members.SyncObject | None:
        """The _userspaceOwner member."""
        member = self.get_member("_userspaceOwner")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @userspace_owner.setter
    def userspace_owner(self, value: members.SyncObject) -> None:
        """Set the _userspaceOwner member."""
        self.set_member("_userspaceOwner", value)

    @property
    def title_buttons(self) -> members.SyncList | None:
        """The _titleButtons member."""
        member = self.get_member("_titleButtons")
        if isinstance(member, members.SyncList):
            return member
        return None

    @title_buttons.setter
    def title_buttons(self, value: members.SyncList) -> None:
        """Set the _titleButtons member."""
        self.set_member("_titleButtons", value)

    @property
    def highlighted_button(self) -> str | None:
        """Target ID of the _highlightedButton reference (targets TitleButton)."""
        member = self.get_member("_highlightedButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @highlighted_button.setter
    def highlighted_button(self, target: str | TitleButton | None) -> None:
        """Set the _highlightedButton reference by target ID or TitleButton instance."""
        target_id: str | None = target.id if isinstance(target, TitleButton) else target  # type: ignore[assignment]
        member = self.get_member("_highlightedButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_highlightedButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyPanel+TitleButton'),
            )

    @property
    def pin_button(self) -> str | None:
        """Target ID of the _pinButton reference (targets TitleButton)."""
        member = self.get_member("_pinButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @pin_button.setter
    def pin_button(self, target: str | TitleButton | None) -> None:
        """Set the _pinButton reference by target ID or TitleButton instance."""
        target_id: str | None = target.id if isinstance(target, TitleButton) else target  # type: ignore[assignment]
        member = self.get_member("_pinButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_pinButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.LegacyPanel+TitleButton'),
            )

