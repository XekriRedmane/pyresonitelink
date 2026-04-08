"""Generated component: StaticGaussianSplat."""

import numpy as np

from pyresonitelink.data import fields
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.istatic_asset_provider import IStaticAssetProvider
from pyresonitelink.generated._types.icustom_inspector import ICustomInspector
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class StaticGaussianSplat(GeneratedComponent, IStaticAssetProvider, ICustomInspector, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.StaticGaussianSplat.

    Category: Assets
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.StaticGaussianSplat"

    def __init__(self, url: str | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            url: Initial value for URL.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if url is not None:
            self.url = url

    @property
    def url(self) -> str | None:
        """The URL field value."""
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

    async def clip_with_bounding_box(self, resolink: protocols.ResoniteLinkClient, bounds: primitives.BoundingBox, debug: bool = False) -> dict:
        """Call the ClipWithBoundingBox sync method.

        Args:
            resolink: Connected ResoniteLink client.
            bounds: The bounds parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ClipWithBoundingBox", {"bounds": bounds}, debug,
        )

    async def clip_with_bounding_box_2(self, resolink: protocols.ResoniteLinkClient, bounds: primitives.BoundingBox, bounds_orientation: primitives.FloatQ, debug: bool = False) -> dict:
        """Call the ClipWithBoundingBox sync method.

        Args:
            resolink: Connected ResoniteLink client.
            bounds: The bounds parameter.
            bounds_orientation: The boundsOrientation parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ClipWithBoundingBox", {"bounds": bounds, "boundsOrientation": bounds_orientation}, debug,
        )

    async def clip_with_sphere(self, resolink: protocols.ResoniteLinkClient, center: primitives.Float3, radius: np.float32, debug: bool = False) -> dict:
        """Call the ClipWithSphere sync method.

        Args:
            resolink: Connected ResoniteLink client.
            center: The center parameter.
            radius: The radius parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ClipWithSphere", {"center": center, "radius": radius}, debug,
        )

    async def clip_with_cylinder(self, resolink: protocols.ResoniteLinkClient, center: primitives.Float3, radius: np.float32, height: np.float32, orientation: primitives.FloatQ, debug: bool = False) -> dict:
        """Call the ClipWithCylinder sync method.

        Args:
            resolink: Connected ResoniteLink client.
            center: The center parameter.
            radius: The radius parameter.
            height: The height parameter.
            orientation: The orientation parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "ClipWithCylinder", {"center": center, "radius": radius, "height": height, "orientation": orientation}, debug,
        )

