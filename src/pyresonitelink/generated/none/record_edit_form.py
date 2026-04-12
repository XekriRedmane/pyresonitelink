"""Generated component: RecordEditForm."""

from pyresonitelink.data import members
from pyresonitelink.generated._enums.public_setting import PublicSetting
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.world_orb import WorldOrb
from pyresonitelink.generated._types.text_field import TextField
from pyresonitelink.generated._types.checkbox import Checkbox
from pyresonitelink.generated._types.text import Text
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class RecordEditForm(GeneratedComponent, IComponent, IWorldEventReceiver):
    """See World.

The RecordEditForm component is used to edit the details and info/metadata for a world.

    See World.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.RecordEditForm"

    def __init__(self, world_orb: str | WorldOrb | None = None, name: str | TextField | None = None, description: str | TextField | None = None, path: str | TextField | None = None, tags: str | TextField | None = None, public_setting: PublicSetting | str | None = None, readonly: str | Checkbox | None = None, private_option_text: str | Text | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            world_orb: Initial value for _worldOrb.
            name: Initial value for _name.
            description: Initial value for _description.
            path: Initial value for _path.
            tags: Initial value for _tags.
            public_setting: Initial value for _publicSetting.
            readonly: Initial value for _readonly.
            private_option_text: Initial value for _privateOptionText.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if world_orb is not None:
            self.world_orb = world_orb
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if path is not None:
            self.path = path
        if tags is not None:
            self.tags = tags
        if public_setting is not None:
            self.public_setting = public_setting
        if readonly is not None:
            self.readonly = readonly
        if private_option_text is not None:
            self.private_option_text = private_option_text

    @property
    def world_orb(self) -> str | None:
        """The world orb that created this dialog."""
        member = self.get_member("_worldOrb")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @world_orb.setter
    def world_orb(self, target: str | WorldOrb | None) -> None:
        """Set the _worldOrb reference by target ID or WorldOrb instance."""
        target_id: str | None = target.id if isinstance(target, WorldOrb) else target  # type: ignore[assignment]
        member = self.get_member("_worldOrb")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_worldOrb",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.WorldOrb'),
            )

    @property
    def name(self) -> str | None:
        """The field to edit the name of the world."""
        member = self.get_member("_name")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @name.setter
    def name(self, target: str | TextField | None) -> None:
        """Set the _name reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_name")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_name",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def description(self) -> str | None:
        """The field to edit the description of the world."""
        member = self.get_member("_description")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @description.setter
    def description(self, target: str | TextField | None) -> None:
        """Set the _description reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_description")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_description",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def path(self) -> str | None:
        """The field to edit the path of the world."""
        member = self.get_member("_path")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @path.setter
    def path(self, target: str | TextField | None) -> None:
        """Set the _path reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_path")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_path",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def tags(self) -> str | None:
        """The field to edit the tags of the world."""
        member = self.get_member("_tags")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @tags.setter
    def tags(self, target: str | TextField | None) -> None:
        """Set the _tags reference by target ID or TextField instance."""
        target_id: str | None = target.id if isinstance(target, TextField) else target  # type: ignore[assignment]
        member = self.get_member("_tags")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_tags",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.TextField'),
            )

    @property
    def public_setting(self) -> PublicSetting | None:
        """The field to edit the of the world."""
        member = self.get_member("_publicSetting")
        if isinstance(member, members.FieldEnum) and member.value is not None:
            return PublicSetting(member.value)
        return None

    @public_setting.setter
    def public_setting(self, value: PublicSetting | str) -> None:
        """Set _publicSetting. The field to edit the of the world."""
        member = self.get_member("_publicSetting")
        if isinstance(member, members.FieldEnum):
            member.value = str(value)
        else:
            self.set_member(
                "_publicSetting",
                members.FieldEnum(value=str(value)),
            )

    @property
    def readonly(self) -> str | None:
        """The checkbox to edit the read only property of the world."""
        member = self.get_member("_readonly")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @readonly.setter
    def readonly(self, target: str | Checkbox | None) -> None:
        """Set the _readonly reference by target ID or Checkbox instance."""
        target_id: str | None = target.id if isinstance(target, Checkbox) else target  # type: ignore[assignment]
        member = self.get_member("_readonly")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_readonly",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Checkbox'),
            )

    @property
    def owner_user(self) -> members.SyncObject | None:
        """The field to show the owner of the world."""
        member = self.get_member("_ownerUser")
        if isinstance(member, members.SyncObject):
            return member
        return None

    @owner_user.setter
    def owner_user(self, value: members.SyncObject) -> None:
        """Set _ownerUser. The field to show the owner of the world."""
        self.set_member("_ownerUser", value)

    @property
    def private_option_text(self) -> str | None:
        """The field to show the private options of the world."""
        member = self.get_member("_privateOptionText")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @private_option_text.setter
    def private_option_text(self, target: str | Text | None) -> None:
        """Set the _privateOptionText reference by target ID or Text instance."""
        target_id: str | None = target.id if isinstance(target, Text) else target  # type: ignore[assignment]
        member = self.get_member("_privateOptionText")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_privateOptionText",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Text'),
            )

