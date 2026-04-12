"""Generated component: MaterialSet."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.sync_asset_list import SyncAssetList
from pyresonitelink.generated._types.material import Material
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class MaterialSet(GeneratedComponent, ICustomInspector, IComponent, IWorldEventReceiver):
    """Material set allows for switching the list of materials being used on a mesh dynamically at any given moment. It also allows for lengthening or shortening the list in real time, which can be used to material stack (things to avoid).

    Category: Rendering/Drivers

    Attach this component to the same slot as a Mesh Renderer or a Skinned
    Mesh Renderer and hit the ``Setup From Mesh Renderer()`` sync delegate
    to attach it to the material list. Next add a list
    (SyncAssetList`1&lt;Material&gt;) of each material list to ``Sets`` you
    want to switch between. Lastly use ``ActiveSetIndex`` to switch between
    each list in ``Sets`` for ``Target``.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.MaterialSet"

    def __init__(self, active_set_index: primitives.Int | None = None, target: str | SyncAssetList[Material] | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            active_set_index: Initial value for ActiveSetIndex.
            target: Initial value for Target.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if active_set_index is not None:
            self.active_set_index = active_set_index
        if target is not None:
            self.target = target

    @property
    def active_set_index(self) -> primitives.Int | None:
        """The index into the Sets list of the materials to apply to the target renderer."""
        member = self.get_member("ActiveSetIndex")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @active_set_index.setter
    def active_set_index(self, value: primitives.Int) -> None:
        """Set the ActiveSetIndex field value."""
        member = self.get_member("ActiveSetIndex")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ActiveSetIndex", fields.FieldInt(value=value)
            )

    @property
    def target(self) -> str | None:
        """The list of materials in a renderer to swap out."""
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @target.setter
    def target(self, target: str | SyncAssetList[Material] | None) -> None:
        """Set the Target reference by target ID or SyncAssetList[Material] instance."""
        target_id: str | None = target.id if isinstance(target, SyncAssetList) else target  # type: ignore[assignment]
        member = self.get_member("Target")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "Target",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.SyncAssetList<[FrooxEngine]FrooxEngine.Material>'),
            )

    @property
    def sets(self) -> members.SyncList | None:
        """The list of lists of materials in a renderer to swap out."""
        member = self.get_member("Sets")
        if isinstance(member, members.SyncList):
            return member
        return None

    @sets.setter
    def sets(self, value: members.SyncList) -> None:
        """Set Sets. The list of lists of materials in a renderer to swap out."""
        self.set_member("Sets", value)

