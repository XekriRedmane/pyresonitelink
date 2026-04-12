"""Generated component: WorldTextRendererWizard."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.font_set import FontSet
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.ideveloper_interface import IDeveloperInterface
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class WorldTextRendererWizard(GeneratedComponent, IDeveloperInterface, IWorldEventReceiver):
    """See World Text Renderer Wizard.

    Category: Wizards

    See World Text Renderer Wizard.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.WorldTextRendererWizard"

    def __init__(self, root: str | Slot | None = None, material: str | IAssetProvider[Material] | None = None, font: str | IAssetProvider[FontSet] | None = None, process_disabled: primitives.Bool | None = None, process_standalone_renderers: primitives.Bool | None = None, process_uix_renderers: primitives.Bool | None = None, color: primitives.ColorX | None = None, tag: str | TextField | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            root: Initial value for Root.
            material: Initial value for Material.
            font: Initial value for Font.
            process_disabled: Initial value for ProcessDisabled.
            process_standalone_renderers: Initial value for ProcessStandaloneRenderers.
            process_uix_renderers: Initial value for ProcessUIXRenderers.
            color: Initial value for Color.
            tag: Initial value for _tag.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if root is not None:
            self.root = root
        if material is not None:
            self.material = material
        if font is not None:
            self.font = font
        if process_disabled is not None:
            self.process_disabled = process_disabled
        if process_standalone_renderers is not None:
            self.process_standalone_renderers = process_standalone_renderers
        if process_uix_renderers is not None:
            self.process_uix_renderers = process_uix_renderers
        if color is not None:
            self.color = color
        if tag is not None:
            self.tag = tag

    @property
    def root(self) -> str | None:
        """The root to do processing for."""
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @root.setter
    def root(self, target: str | Slot | None) -> None:
        """Set the Root reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("Root")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Root",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def material(self) -> str | None:
        """The material to replace text renderer materials with."""
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @material.setter
    def material(self, target: str | IAssetProvider[Material] | None) -> None:
        """Set the Material reference by target ID or IAssetProvider[Material] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Material")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Material",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.Material>'),
            )

    @property
    def font(self) -> str | None:
        """The font to override texts with."""
        member = self.get_member("Font")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @font.setter
    def font(self, target: str | IAssetProvider[FontSet] | None) -> None:
        """Set the Font reference by target ID or IAssetProvider[FontSet] instance."""
        target_id: str | None = target.id if isinstance(target, IAssetProvider) else target  # type: ignore[assignment]
        member = self.get_member("Font")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Font",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.IAssetProvider<[FrooxEngine]FrooxEngine.FontSet>'),
            )

    @property
    def process_disabled(self) -> primitives.Bool | None:
        """Whether to process disabled texts or not."""
        member = self.get_member("ProcessDisabled")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @process_disabled.setter
    def process_disabled(self, value: primitives.Bool) -> None:
        """Set the ProcessDisabled field value."""
        member = self.get_member("ProcessDisabled")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProcessDisabled", fields.FieldBool(value=value)
            )

    @property
    def process_standalone_renderers(self) -> primitives.Bool | None:
        """Whether to process Component:TextRenderers."""
        member = self.get_member("ProcessStandaloneRenderers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @process_standalone_renderers.setter
    def process_standalone_renderers(self, value: primitives.Bool) -> None:
        """Set the ProcessStandaloneRenderers field value."""
        member = self.get_member("ProcessStandaloneRenderers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProcessStandaloneRenderers", fields.FieldBool(value=value)
            )

    @property
    def process_uix_renderers(self) -> primitives.Bool | None:
        """Whether to process Component:Texts."""
        member = self.get_member("ProcessUIXRenderers")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @process_uix_renderers.setter
    def process_uix_renderers(self, value: primitives.Bool) -> None:
        """Set the ProcessUIXRenderers field value."""
        member = self.get_member("ProcessUIXRenderers")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ProcessUIXRenderers", fields.FieldBool(value=value)
            )

    @property
    def color(self) -> primitives.ColorX | None:
        """What color to change the texts to."""
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
    def tag(self) -> str | None:
        """Only process texts with this tag."""
        member = self.get_member("_tag")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tag.setter
    def tag(self, target: str | TextField | None) -> None:
        """Set the _tag reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_tag")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_tag",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

