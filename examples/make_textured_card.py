"""Writes TexturedCard.glb, the card that textured_card.py places in Resonite.

The card is a printed order form. A thin box carries an opaque paper
texture, and quads just in front of it carry decals with transparent
backgrounds: a target mark, a shell with its type, a diagram of elevation
and bearing, and a check mark in a scaled group. Every decal has text or
an asymmetric shape, so a texture that is upside down or mirrored is
obvious at a glance.

The file also has the features of real exports that an importer must
handle. The paper box is rotated 90 degrees and scaled unevenly, a group
node has a nonuniform scale, one mesh is shown by two nodes, one part has
a plain color and no texture, and three nodes are marked hidden with
{"hidden": true} in their extras. One of the hidden nodes is a grey guide
plane that stands across the card, so an importer that doesn't check the
mark draws it.

The card faces +Z, as glTF specifies for the front of an asset, and its
center is at the origin. All sizes are in meters.

Usage:
    python examples/make_textured_card.py
"""

import io
import json
import os
import struct
from collections.abc import Callable
from typing import Any

import numpy as np
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

GLB_PATH = os.path.join(os.path.dirname(__file__), "TexturedCard.glb")

CARD_WIDTH = 0.22
CARD_HEIGHT = 0.11
CARD_THICKNESS = 0.0006
# The decals sit this far in front of the paper.
DECAL_Z = CARD_THICKNESS / 2 + 0.0002

# Textures are drawn this many times larger and then reduced, which
# smooths their edges.
SUPERSAMPLE = 4

INK = (35, 32, 30)
RED = (170, 40, 35)
GREEN = (60, 150, 60)

# glTF constants.
FLOAT = 5126
UNSIGNED_SHORT = 5123
CLAMP_TO_EDGE = 33071
LINEAR = 9729
LINEAR_MIPMAP_LINEAR = 9987


def _font(size: float) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
    """Returns Pillow's built-in font at a size given in texture pixels.

    Args:
        size (float): The font size before supersampling.

    Returns:
        The font, at size * SUPERSAMPLE.
    """
    return ImageFont.load_default(size=size * SUPERSAMPLE)


def _s(*values: float) -> list[float]:
    """Scales coordinates from texture pixels to supersampled canvas pixels.

    Args:
        *values (float): Coordinates, in texture pixels.

    Returns:
        The coordinates, in canvas pixels.
    """
    return [v * SUPERSAMPLE for v in values]


def _pt(x: float, y: float) -> tuple[float, float]:
    """Scales a point from texture pixels to supersampled canvas pixels.

    Args:
        x (float): The point's x, in texture pixels.
        y (float): The point's y, in texture pixels.

    Returns:
        The point, in canvas pixels.
    """
    return (x * SUPERSAMPLE, y * SUPERSAMPLE)


def _texture(
    width: int,
    height: int,
    paint: Callable[[ImageDraw.ImageDraw], None],
    background: tuple[int, int, int, int] = (255, 255, 255, 0),
) -> Image.Image:
    """Draws an RGBA texture at SUPERSAMPLE times its size and reduces it.

    Args:
        width (int): The texture's width, in pixels.
        height (int): The texture's height, in pixels.
        paint (Callable): Draws the texture on the drawing context it is
            called with, scaling its coordinates with _s and _pt.
        background (tuple[int, int, int, int]): The canvas color. A
            transparent background is white, so that edges don't darken
            when the texture is reduced.

    Returns:
        The texture.
    """
    image = Image.new("RGBA", (width * SUPERSAMPLE, height * SUPERSAMPLE), background)
    paint(ImageDraw.Draw(image))
    return image.resize((width, height), Image.Resampling.LANCZOS)


def _arc_arrow(
    draw: ImageDraw.ImageDraw,
    center: tuple[float, float],
    radius: float,
    start: float,
    end: float,
) -> None:
    """Draws a red arc with an arrowhead at its end.

    Args:
        draw (ImageDraw.ImageDraw): The drawing context.
        center (tuple[float, float]): The arc's center, in texture pixels.
        radius (float): The arc's radius, in texture pixels.
        start (float): The angle the arc starts at, in degrees, clockwise
            from +X as PIL measures them.
        end (float): The angle the arc ends at, where the arrowhead points.
    """
    cx, cy = center
    draw.arc(_s(cx - radius, cy - radius, cx + radius, cy + radius),
             min(start, end), max(start, end), fill=RED, width=int(_s(12)[0]))
    # The head points along the arc's direction of travel at its end.
    a = np.radians(end)
    tip = np.array([cx + radius * np.cos(a), cy + radius * np.sin(a)])
    direction = np.sign(end - start) * np.array([-np.sin(a), np.cos(a)])
    side = np.array([-direction[1], direction[0]])
    points = [tip + 22 * direction, tip - 8 * direction + 20 * side,
              tip - 8 * direction - 20 * side]
    draw.polygon([_pt(*p) for p in points], fill=RED)


def paper_texture() -> Image.Image:
    """Draws the card's paper, with a printed heading.

    The texture is portrait, because the card's box is portrait and the
    card node turns it 90 degrees counterclockwise. The paper is drawn
    landscape and turned the other way here.

    Returns:
        The 512 x 1024 RGBA texture.
    """
    width, height = 1024, 512
    rng = np.random.default_rng(7)
    # Mottled paper that darkens and browns toward the edges.
    y, x = np.mgrid[0:height, 0:width]
    edge = np.minimum(np.minimum(x, width - 1 - x) / 60, np.minimum(y, height - 1 - y) / 60)
    edge = np.clip(edge, 0, 1)
    noise = rng.normal(0, 6, (height, width))
    base = np.array([232, 222, 196], dtype=np.float64)
    burnt = np.array([150, 110, 70], dtype=np.float64)
    rgb = base * edge[..., None] + burnt * (1 - edge[..., None]) + noise[..., None]
    pixels = np.dstack([np.clip(rgb, 0, 255), np.full((height, width), 255)]).astype(np.uint8)
    paper = Image.fromarray(pixels, "RGBA")
    draw = ImageDraw.Draw(paper)
    draw.text((width / 2, 20), "FIRE ORDER  No. 0042", fill=INK,
              font=ImageFont.load_default(size=22), anchor="mt")
    return paper.rotate(-90, expand=True)


def target_texture() -> Image.Image:
    """Draws a red target mark with a "1" beside it.

    Returns:
        The 256 x 256 RGBA texture.
    """
    def paint(draw: ImageDraw.ImageDraw) -> None:
        """Draws the target."""
        draw.ellipse(_s(28, 28, 228, 228), outline=RED, width=int(_s(14)[0]))
        draw.ellipse(_s(108, 108, 148, 148), fill=RED)
        for x0, y0, x1, y1 in ((128, 8, 128, 80), (128, 176, 128, 248),
                               (8, 128, 80, 128), (176, 128, 248, 128)):
            draw.line(_s(x0, y0, x1, y1), fill=RED, width=int(_s(12)[0]))
        draw.text(_pt(176, 176), "1", fill=INK, font=_font(44), anchor="mm")

    return _texture(256, 256, paint)


def shell_texture() -> Image.Image:
    """Draws a shell pointing left, with its type to the right.

    Returns:
        The 1024 x 256 RGBA texture.
    """
    def paint(draw: ImageDraw.ImageDraw) -> None:
        """Draws the shell and its label."""
        width = int(_s(8)[0])
        # The nose is a pointed arch from the tip at x = 60 to the body.
        nose = [(60 + 200 * t, 128 - 52 * np.sin(np.pi / 2 * t) ** 0.6) for t in np.linspace(0, 1, 30)]
        outline = nose + [(520, 76), (520, 180)] + [(x, 256 - y) for x, y in reversed(nose)]
        draw.polygon([_pt(x, y) for x, y in outline], outline=INK, width=width)
        # The driving band.
        draw.rectangle(_s(520, 72, 580, 184), outline=INK, width=width)
        draw.line(_s(536, 72, 536, 184), fill=INK, width=width)
        draw.text(_pt(640, 128), "HE 155", fill=INK, font=_font(96), anchor="lm")

    return _texture(1024, 256, paint)


def diagram_texture() -> Image.Image:
    """Draws a gun from the side with an elevation arrow, and from above with bearing arrows.

    Returns:
        The 1024 x 384 RGBA texture.
    """
    def paint(draw: ImageDraw.ImageDraw) -> None:
        """Draws both views and their labels."""
        # Side view: the hull and turret on the ground, and the barrel
        # raised toward the upper right.
        draw.line(_s(30, 250, 470, 250), fill=INK, width=int(_s(10)[0]))
        draw.rectangle(_s(70, 180, 300, 250), fill=INK)
        draw.rectangle(_s(120, 140, 260, 185), fill=INK)
        draw.line(_s(240, 160, 400, 60), fill=INK, width=int(_s(18)[0]))
        draw.line(_s(440, 230, 440, 70), fill=RED, width=int(_s(14)[0]))
        draw.polygon([_pt(*p) for p in ((440, 40), (418, 80), (462, 80))], fill=RED)
        draw.text(_pt(250, 330), "ELEVATION", fill=INK, font=_font(48), anchor="mm")
        # Top view: the turret with two barrels pointing up, and arrows
        # turning it either way.
        draw.line(_s(554, 250, 994, 250), fill=INK, width=int(_s(10)[0]))
        draw.rounded_rectangle(_s(724, 150, 824, 250), radius=_s(18)[0], fill=INK)
        draw.rectangle(_s(752, 40, 764, 150), fill=INK)
        draw.rectangle(_s(784, 40, 796, 150), fill=INK)
        _arc_arrow(draw, (774, 220), 150, 200, 240)
        _arc_arrow(draw, (774, 220), 150, 340, 300)
        draw.text(_pt(774, 330), "BEARING", fill=INK, font=_font(48), anchor="mm")

    return _texture(1024, 384, paint)


def check_texture() -> Image.Image:
    """Draws a green check mark with a dark outline.

    Returns:
        The 256 x 256 RGBA texture.
    """
    def paint(draw: ImageDraw.ImageDraw) -> None:
        """Draws the check mark."""
        points = [_pt(*p) for p in ((40, 140), (100, 210), (220, 40))]
        draw.line(points, fill=INK, width=int(_s(44)[0]), joint="curve")
        draw.line(points, fill=GREEN, width=int(_s(30)[0]), joint="curve")

    return _texture(256, 256, paint)


def cross_texture() -> Image.Image:
    """Draws a red cross with a dark outline.

    Returns:
        The 256 x 256 RGBA texture.
    """
    def paint(draw: ImageDraw.ImageDraw) -> None:
        """Draws the cross."""
        for line in (((50, 50), (206, 206)), ((206, 50), (50, 206))):
            points = [_pt(*p) for p in line]
            draw.line(points, fill=INK, width=int(_s(44)[0]))
            draw.line(points, fill=RED, width=int(_s(30)[0]))

    return _texture(256, 256, paint)


def quad() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Builds a unit square in the XY plane, facing +Z.

    The texture fills the square the right way up when seen from +Z. glTF
    puts v = 0 at the top of a texture, so v runs opposite to y.

    Returns:
        The positions, normals, and texture coordinates of its 4 vertices,
        and its 2 triangles as uint16 indices, counterclockwise from +Z.
    """
    xy = np.array([[-0.5, -0.5], [0.5, -0.5], [0.5, 0.5], [-0.5, 0.5]])
    positions = np.column_stack([xy, np.zeros(4)]).astype(np.float32)
    normals = np.tile([0, 0, 1], (4, 1)).astype(np.float32)
    uvs = np.column_stack([xy[:, 0] + 0.5, 0.5 - xy[:, 1]]).astype(np.float32)
    indices = np.array([0, 1, 2, 0, 2, 3], dtype=np.uint16)
    return positions, normals, uvs, indices


def box() -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """Builds a unit cube centered at the origin, with flat faces.

    Each face has its own 4 vertices, and the texture fills each face the
    right way up when the face is seen from outside, with +Y up on the
    side faces.

    Returns:
        The positions, normals, and texture coordinates of its 24 vertices,
        and its 12 triangles as uint16 indices, counterclockwise from
        outside.
    """
    x, y, z = np.identity(3)
    # (normal, u axis, v axis), with u x v = normal, so that the corners
    # below go counterclockwise around the normal.
    faces = [(z, x, y), (-z, -x, y), (x, -z, y), (-x, z, y), (y, x, -z), (-y, x, z)]
    positions, normals, uvs, indices = [], [], [], []
    for normal, u, v in faces:
        start = len(positions)
        for su, sv in ((-1, -1), (1, -1), (1, 1), (-1, 1)):
            positions.append(0.5 * (normal + su * u + sv * v))
            normals.append(normal)
            uvs.append((0.5 + 0.5 * su, 0.5 - 0.5 * sv))
        indices += [start, start + 1, start + 2, start, start + 2, start + 3]
    return (
        np.array(positions, dtype=np.float32),
        np.array(normals, dtype=np.float32),
        np.array(uvs, dtype=np.float32),
        np.array(indices, dtype=np.uint16),
    )


class GlbWriter:
    """Builds the glTF JSON and the binary chunk of a .glb file."""

    def __init__(self) -> None:
        """Starts an empty glTF asset."""
        self.gltf: dict[str, Any] = {
            "asset": {"version": "2.0", "generator": "pyresonitelink make_textured_card.py"},
            "scene": 0,
            "scenes": [{"nodes": []}],
            "nodes": [],
            "meshes": [],
            "materials": [],
            "textures": [],
            "images": [],
            "samplers": [{
                "magFilter": LINEAR, "minFilter": LINEAR_MIPMAP_LINEAR,
                "wrapS": CLAMP_TO_EDGE, "wrapT": CLAMP_TO_EDGE,
            }],
            "accessors": [],
            "bufferViews": [],
        }
        self.binary = bytearray()

    def _view(self, data: bytes) -> int:
        """Appends data to the binary chunk as a new buffer view.

        Args:
            data (bytes): The data.

        Returns:
            The index of the buffer view.
        """
        # Every view starts on a 4-byte boundary, which all accessor
        # component types need.
        self.binary += b"\0" * (-len(self.binary) % 4)
        self.gltf["bufferViews"].append(
            {"buffer": 0, "byteOffset": len(self.binary), "byteLength": len(data)})
        self.binary += data
        return len(self.gltf["bufferViews"]) - 1

    def _accessor(self, array: np.ndarray, kind: str) -> int:
        """Stores an array as an accessor.

        Args:
            array (np.ndarray): float32 elements shaped (count, components),
                or uint16 indices shaped (count,).
            kind (str): The glTF accessor type, such as "VEC3".

        Returns:
            The index of the accessor.
        """
        accessor: dict[str, Any] = {
            "bufferView": self._view(array.tobytes()),
            "componentType": UNSIGNED_SHORT if array.dtype == np.uint16 else FLOAT,
            "count": len(array),
            "type": kind,
        }
        if kind == "VEC3" and array.dtype == np.float32:
            # The specification requires bounds on positions. Normals get
            # them too, which is allowed.
            accessor["min"] = array.min(axis=0).tolist()
            accessor["max"] = array.max(axis=0).tolist()
        self.gltf["accessors"].append(accessor)
        return len(self.gltf["accessors"]) - 1

    def geometry(self, arrays: tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]) -> dict[str, Any]:
        """Stores a shape's arrays, for any number of meshes to share.

        Args:
            arrays (tuple): The positions, normals, texture coordinates,
                and indices, as quad and box return them.

        Returns:
            A primitive without a material, to be completed by mesh.
        """
        positions, normals, uvs, indices = arrays
        return {
            "attributes": {
                "POSITION": self._accessor(positions, "VEC3"),
                "NORMAL": self._accessor(normals, "VEC3"),
                "TEXCOORD_0": self._accessor(uvs, "VEC2"),
            },
            "indices": self._accessor(indices, "SCALAR"),
        }

    def material(
        self,
        name: str,
        image: Image.Image | None = None,
        color: tuple[float, float, float] = (1.0, 1.0, 1.0),
    ) -> int:
        """Adds a material with a texture or a plain color.

        A material with a texture is blended by the texture's alpha, unless
        the texture is fully opaque.

        Args:
            name (str): The material's name.
            image (Image.Image | None): The base color texture, or None.
            color (tuple[float, float, float]): The base color factor, as
                linear RGB.

        Returns:
            The index of the material.
        """
        pbr: dict[str, Any] = {
            "baseColorFactor": [*color, 1.0],
            "metallicFactor": 0.0,
            "roughnessFactor": 1.0,
        }
        material: dict[str, Any] = {"name": name, "pbrMetallicRoughness": pbr}
        if image is not None:
            png = io.BytesIO()
            image.save(png, format="PNG")
            self.gltf["images"].append(
                {"name": name, "mimeType": "image/png", "bufferView": self._view(png.getvalue())})
            self.gltf["textures"].append({"source": len(self.gltf["images"]) - 1, "sampler": 0})
            pbr["baseColorTexture"] = {"index": len(self.gltf["textures"]) - 1}
            if np.asarray(image.convert("RGBA"))[..., 3].min() < 255:
                material["alphaMode"] = "BLEND"
        self.gltf["materials"].append(material)
        return len(self.gltf["materials"]) - 1

    def mesh(self, name: str, primitive: dict[str, Any], material: int) -> int:
        """Adds a mesh that draws a stored shape with a material.

        Args:
            name (str): The mesh's name.
            primitive (dict[str, Any]): The shape, as geometry returns it.
            material (int): The index of the material.

        Returns:
            The index of the mesh.
        """
        self.gltf["meshes"].append({"name": name, "primitives": [{**primitive, "material": material}]})
        return len(self.gltf["meshes"]) - 1

    def node(
        self,
        name: str,
        *,
        mesh: int | None = None,
        children: list[int] | None = None,
        translation: tuple[float, float, float] | None = None,
        rotation: tuple[float, float, float, float] | None = None,
        scale: tuple[float, float, float] | None = None,
        hidden: bool = False,
    ) -> int:
        """Adds a node.

        Args:
            name (str): The node's name.
            mesh (int | None): The index of the mesh it shows, if any.
            children (list[int] | None): The indices of its children.
            translation (tuple[float, float, float] | None): Its position
                in its parent.
            rotation (tuple[float, float, float, float] | None): Its
                rotation as a unit quaternion (x, y, z, w).
            scale (tuple[float, float, float] | None): Its scale.
            hidden (bool): Whether to mark it {"hidden": true} in its
                extras.

        Returns:
            The index of the node.
        """
        node: dict[str, Any] = {"name": name}
        for key, value in (("mesh", mesh), ("children", children), ("translation", translation),
                           ("rotation", rotation), ("scale", scale)):
            if value is not None:
                node[key] = list(value) if isinstance(value, tuple) else value
        if hidden:
            node["extras"] = {"hidden": True}
        self.gltf["nodes"].append(node)
        return len(self.gltf["nodes"]) - 1

    def write(self, path: str, root: int) -> None:
        """Writes the .glb file, with root as the scene's only root node.

        Args:
            path (str): The file to write.
            root (int): The index of the root node.
        """
        self.gltf["scenes"][0]["nodes"] = [root]
        self.binary += b"\0" * (-len(self.binary) % 4)
        self.gltf["buffers"] = [{"byteLength": len(self.binary)}]
        # The JSON chunk is padded with spaces and the binary chunk with
        # zeros, as the specification requires.
        json_chunk = json.dumps(self.gltf, separators=(",", ":")).encode()
        json_chunk += b" " * (-len(json_chunk) % 4)
        chunks = (
            struct.pack("<II", len(json_chunk), 0x4E4F534A) + json_chunk
            + struct.pack("<II", len(self.binary), 0x004E4942) + bytes(self.binary)
        )
        with open(path, "wb") as f:
            f.write(struct.pack("<III", 0x46546C67, 2, 12 + len(chunks)) + chunks)


def main() -> None:
    """Builds the card and writes it to GLB_PATH."""
    w = GlbWriter()
    square = w.geometry(quad())
    cube = w.geometry(box())

    def decal(name: str, image: Image.Image, center: tuple[float, float], width: float) -> int:
        """Adds a quad showing an image, sized to the image's aspect ratio."""
        mesh = w.mesh(name, square, w.material(name, image))
        height = width * image.height / image.width
        return w.node(name, mesh=mesh, translation=(*center, DECAL_Z), scale=(width, height, 1.0))

    # The paper box is portrait in its own coordinates. Turning it 90
    # degrees counterclockwise about Z makes it landscape.
    s = np.sqrt(0.5)
    paper = w.node(
        "Card", mesh=w.mesh("Card", cube, w.material("Paper", paper_texture())),
        rotation=(0.0, 0.0, s, s), scale=(CARD_HEIGHT, CARD_WIDTH, CARD_THICKNESS),
    )
    target = decal("Target", target_texture(), (-0.088, 0.032), 0.03)
    shell = decal("Shell", shell_texture(), (-0.012, 0.032), 0.11)
    diagram = decal("Diagram", diagram_texture(), (0.0, -0.022), 0.16)
    divider = w.node(
        "Divider", mesh=w.mesh("Divider", cube, w.material("Divider Ink", color=(0.02, 0.02, 0.02))),
        translation=(0.0, 0.012, DECAL_Z), scale=(0.2, 0.0012, 0.0002),
    )
    # The check and the cross are children of a group that scales them
    # unevenly, as an exporter writes a button with a stretched icon. The
    # large check shows the check's mesh a second time.
    check_mesh = w.mesh("Check", square, w.material("Check", check_texture()))
    check = w.node("Check", mesh=check_mesh)
    cross = w.node("Cross", mesh=w.mesh("Cross", square, w.material("Cross", cross_texture())),
                   hidden=True)
    done = w.node("Done", children=[check, cross], translation=(0.088, 0.032, DECAL_Z),
                  scale=(0.026, 0.03, 1.0))
    large_check = w.node("Large Check", mesh=check_mesh, translation=(0.0, -0.01, DECAL_Z + 0.0002),
                         scale=(0.09, 0.1, 1.0), hidden=True)
    # A layout guide that stands across the middle of the card.
    guide = w.node(
        "Guide", mesh=w.mesh("Guide", cube, w.material("Guide Grey", color=(0.2, 0.2, 0.2))),
        scale=(0.0005, 0.14, 0.04), hidden=True,
    )
    root = w.node("TexturedCard", children=[
        paper, target, shell, divider, diagram, done, large_check, guide])
    w.write(GLB_PATH, root)
    print(f"Wrote {GLB_PATH}: {len(w.binary)} bytes of data.")


if __name__ == "__main__":
    main()
