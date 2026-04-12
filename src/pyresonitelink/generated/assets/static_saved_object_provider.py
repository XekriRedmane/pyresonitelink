"""Generated component: StaticSavedObjectProvider."""

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.istatic_asset_provider import IStaticAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StaticSavedObjectProvider(GeneratedComponent, IStaticAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Not currently usable.

    Category: Assets
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StaticSavedObjectProvider"

    def __init__(self, url: str | None = None, pre_gather: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            pre_gather: Initial value for PreGather.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if url is not None:
            self.url = url
        if pre_gather is not None:
            self.pre_gather = pre_gather

    @property
    def url(self) -> str | None:
        """Enter the Uri (e.g. resrec:///) link of the saved object"""
        member = self.get_member("URL")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @url.setter
    def url(self, value: str) -> None:
        """Set the URL field value."""
        member = self.get_member("URL")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "URL", fields.FieldUri(value=value)
            )

    @property
    def pre_gather(self) -> primitives.Bool | None:
        """Whether to pregather the object's assets or not."""
        member = self.get_member("PreGather")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @pre_gather.setter
    def pre_gather(self, value: primitives.Bool) -> None:
        """Set the PreGather field value."""
        member = self.get_member("PreGather")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PreGather", fields.FieldBool(value=value)
            )

