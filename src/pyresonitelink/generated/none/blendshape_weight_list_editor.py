"""Generated component: BlendshapeWeightListEditor."""

from pyresonitelink.data import members
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.isync_list import ISyncList
from pyresonitelink.generated._types.button import Button
from pyresonitelink.generated._types.skinned_mesh_renderer import SkinnedMeshRenderer
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class BlendshapeWeightListEditor(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Weight list editor is a component that is used within inspectors and shouldn't need to be interacted with by the user. Although, it can be used in very niche circumstances.

    Add component to a slot and fill the fields, with the proper data
    explained in the table above. Press the button provided to
    ``_addNewButton`` to add a new blendshape to the targeted skinned Mesh
    renderer.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.BlendshapeWeightListEditor"

    def __init__(self, target_list: str | ISyncList | None = None, add_new_button: str | Button | None = None, target_skin: str | SkinnedMeshRenderer | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            target_list: Initial value for _targetList.
            add_new_button: Initial value for _addNewButton.
            target_skin: Initial value for _targetSkin.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if target_list is not None:
            self.target_list = target_list
        if add_new_button is not None:
            self.add_new_button = add_new_button
        if target_skin is not None:
            self.target_skin = target_skin

    @property
    def target_list(self) -> str | None:
        """The list of blendshapes. This can be acquired through grabbing the "BlendShapes" title at the beginning of a blendshape list inside of a Skinned Mesh Renderer"""
        member = self.get_member("_targetList")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_list.setter
    def target_list(self, target: str | ISyncList | None) -> None:
        """Set the _targetList reference by target ID or ISyncList instance."""
        target_id: str | None = target.id if isinstance(target, ISyncList) else target  # type: ignore[assignment]
        member = self.get_member("_targetList")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetList",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.ISyncList'),
            )

    @property
    def add_new_button(self) -> str | None:
        """The button that when pressed, should add a new blendshape to the end of the ``_targetList``. Whether the new blendshape does anything or not depends on if the ``Mesh`` data inside of ``_targetSkin`` has a blendshape list that reaches as far as the new item."""
        member = self.get_member("_addNewButton")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @add_new_button.setter
    def add_new_button(self, target: str | Button | None) -> None:
        """Set the _addNewButton reference by target ID or Button instance."""
        target_id: str | None = target.id if isinstance(target, Button) else target  # type: ignore[assignment]
        member = self.get_member("_addNewButton")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_addNewButton",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.UIX.Button'),
            )

    @property
    def target_skin(self) -> str | None:
        """The skinned Mesh renderer to add a new blendshape item to. Has to be the same component ``_targetList`` comes from."""
        member = self.get_member("_targetSkin")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target_skin.setter
    def target_skin(self, target: str | SkinnedMeshRenderer | None) -> None:
        """Set the _targetSkin reference by target ID or SkinnedMeshRenderer instance."""
        target_id: str | None = target.id if isinstance(target, SkinnedMeshRenderer) else target  # type: ignore[assignment]
        member = self.get_member("_targetSkin")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_targetSkin",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SkinnedMeshRenderer'),
            )

