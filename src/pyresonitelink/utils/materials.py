"""Makes PBS_Metallic materials from a color, a metalness, and a smoothness.

Most surfaces of a model read from a glTF file can be given a plain color
and a sheen, without textures. A Finish holds those settings, and
add_materials adds one PBS_Metallic for each entry of a table of them.
Keying the table by the glTF material names lets rendering.add_part give
each submesh its material by name.

    table = {
        "Paint": materials.Finish((0.47, 0.6, 0.57), metallic=0.3, smoothness=0.35),
        "Chrome": materials.Finish((0.6, 0.6, 0.6), metallic=0.8, smoothness=0.5),
    }
    mats = await materials.add_materials(resolink, slot, table)
"""

import dataclasses
from collections.abc import Mapping

from pyresonitelink import client
from pyresonitelink.data import primitives
from pyresonitelink.data import workers
from pyresonitelink.generated.assets.materials import pbs_metallic


@dataclasses.dataclass(frozen=True)
class Finish:
    """Represents the settings of an opaque, untextured PBS_Metallic material.

    The colors are linear, which is how glTF gives a material's base color
    factor, so a glTF color can be copied in unchanged.

    Attributes:
        color (tuple[float, float, float]): The linear albedo color, each
            component from 0 to 1.
        metallic (float): How metallic the surface is, from 0 to 1.
        smoothness (float): How smooth the surface is, from 0 to 1.
        emissive (tuple[float, float, float]): The linear emissive color,
            which is added to the lit color. The default is black.
    """

    color: tuple[float, float, float]
    metallic: float
    smoothness: float
    emissive: tuple[float, float, float] = (0.0, 0.0, 0.0)

    def material(self) -> pbs_metallic.PBS_Metallic:
        """Returns a new PBS_Metallic with these settings, not yet added to a slot."""
        return pbs_metallic.PBS_Metallic(
            albedo_color=primitives.ColorX(*self.color, 1, "Linear"),
            emissive_color=primitives.ColorX(*self.emissive, 1, "Linear"),
            metallic=primitives.Float(self.metallic),
            smoothness=primitives.Float(self.smoothness),
        )


async def add_materials(
    resolink: client.Client,
    slot: str | workers.Slot,
    table: Mapping[str, Finish],
) -> dict[str, pbs_metallic.PBS_Metallic]:
    """Adds one PBS_Metallic to a slot for each entry of a table of finishes.

    Args:
        resolink (client.Client): The connected client.
        slot (str | workers.Slot): The slot to add the materials to, as an
            ID or a Slot.
        table (Mapping[str, Finish]): The finish of each material, by name.

    Returns:
        The materials, under the same names as in table.
    """
    materials: dict[str, pbs_metallic.PBS_Metallic] = {}
    for name, finish in table.items():
        material = finish.material()
        await material.add_to_slot(resolink, slot)
        materials[name] = material
    return materials
