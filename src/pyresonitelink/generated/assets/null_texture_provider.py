"""Generated component: NullTextureProvider."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.iasset_provider import IAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class NullTextureProvider(GeneratedComponent, IAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Null texture providers are automatically added to the Root as a way of telling the render engine of FrooxEngine what to use as a null texture when a material is missing. This texture is a procedural gray and dark gray checkerboard texture.

    Category: Assets
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.NullTextureProvider"

    pass

