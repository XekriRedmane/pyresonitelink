"""Generated component: FontAtlasTexture."""

from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.itexture_2d_provider import ITexture2DProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class FontAtlasTexture(GeneratedComponent, ITexture2DProvider, ICustomInspector, IWorldEventReceiver):
    """The FontAtlasTexture component makes a GlyphAtlas containing an atlas of Glyphs representing characters into one large texture that can be used. The internal mechanisms of this component are not assignable directly.

    Not used directly by the user.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.FontAtlasTexture"

    pass

