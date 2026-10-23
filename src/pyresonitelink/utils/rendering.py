"""Shows meshes on slots with a MeshRenderer and a list of materials.

A MeshRenderer draws each submesh of its mesh with the material at the same
index in its Materials list. The renderer starts with an empty list, and
the server adds a list element for each member ID in an update that the
list doesn't have yet, so add_renderer appends a reference for each
material and sends one update.

add_mesh also imports the mesh from a glb.Mesh, which is how a mesh read
from a glTF file reaches Resonite.

    m = glb.to_resonite(glb.read_node(glb.load("model.glb"), "Body"))
    paint = pbs_metallic.PBS_Metallic()
    await paint.add_to_slot(resolink, slot)
    await rendering.add_mesh(resolink, slot, m, [paint] * len(m.submeshes))
"""

from collections.abc import Sequence

from pyresonitelink import client
from pyresonitelink.data import members
from pyresonitelink.data import mesh
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types import iasset_provider
from pyresonitelink.generated._types import mesh as mesh_asset
from pyresonitelink.generated.assets import static_mesh
from pyresonitelink.generated.rendering import mesh_renderer
from pyresonitelink.utils import glb


async def add_renderer(
    resolink: client.Client,
    slot: str | workers.Slot,
    mesh_provider: iasset_provider.IAssetProvider[mesh_asset.Mesh],
    materials: Sequence[GeneratedComponent],
) -> mesh_renderer.MeshRenderer:
    """Adds a MeshRenderer that draws a mesh with a list of materials.

    Args:
        resolink (client.Client): The connected client.
        slot (str | workers.Slot): The slot to add the renderer to, as an
            ID or a Slot.
        mesh_provider (iasset_provider.IAssetProvider[mesh_asset.Mesh]):
            The mesh component, such as a
            StaticMesh or a BoxMesh, already added to a slot.
        materials (Sequence[GeneratedComponent]): The material of each
            submesh, in order, each already added to a slot. The same
            material may appear more than once.

    Returns:
        The renderer.

    Raises:
        RuntimeError: The server refused the materials.
    """
    renderer = mesh_renderer.MeshRenderer(mesh=mesh_provider)
    await renderer.add_to_slot(resolink, slot)
    if not materials:
        return renderer
    renderer_materials = renderer.materials
    assert renderer_materials is not None
    for material in materials:
        assert material.id is not None, "Add each material to a slot first."
        renderer_materials.elements.append(members.Reference(targetId=material.id))
    resp = await renderer.update(resolink)
    if not resp.success:
        raise RuntimeError(
            f"Failed to set the materials of renderer {renderer.id}: {resp.errorInfo}"
        )
    return renderer


async def add_mesh(
    resolink: client.Client,
    slot: str | workers.Slot,
    m: glb.Mesh,
    materials: Sequence[GeneratedComponent],
) -> mesh_renderer.MeshRenderer:
    """Imports a mesh and adds a StaticMesh and a MeshRenderer that show it.

    The mesh's positions, normals, and texture coordinates, if it has any,
    are imported. The mesh must already be in Resonite's coordinates (see
    glb.to_resonite) and in the slot's own space.

    Args:
        resolink (client.Client): The connected client.
        slot (str | workers.Slot): The slot to add the components to, as an
            ID or a Slot.
        m (glb.Mesh): The mesh.
        materials (Sequence[GeneratedComponent]): The material of each
            submesh, in the order of m.submeshes, each already added to a
            slot.

    Returns:
        The renderer. Its Mesh reference is the new StaticMesh.

    Raises:
        ValueError: The number of materials differs from the number of
            submeshes.
        RuntimeError: The server refused the materials.
    """
    if len(materials) != len(m.submeshes):
        raise ValueError(
            f"There are {len(materials)} materials for {len(m.submeshes)} submeshes."
        )
    asset = await resolink.import_mesh_raw_data(
        m.positions,
        [mesh.RawTriangles(t) for t in m.submeshes],
        normals=m.normals,
        uvs=[] if m.uvs is None else [m.uvs],
    )
    provider = static_mesh.StaticMesh(url=asset.assetURL)
    await provider.add_to_slot(resolink, slot)
    return await add_renderer(resolink, slot, provider, materials)
