"""Generated component: ModelImportDialog."""

from pyresonitelink.data import fields
from pyresonitelink.data import members
from pyresonitelink.data import primitives
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated._types.slot import Slot
from pyresonitelink.generated._types.icomponent import IComponent
from pyresonitelink.generated._types.iworld_event_receiver import IWorldEventReceiver


class ModelImportDialog(GeneratedComponent, IComponent, IWorldEventReceiver):
    """Wrapper for [FrooxEngine]FrooxEngine.ModelImportDialog.
    """

    COMPONENT_TYPE = "[FrooxEngine]FrooxEngine.ModelImportDialog"

    def __init__(self, content_root: str | Slot | None = None, scale: primitives.Float | None = None, auto_scale: primitives.Bool | None = None, prefer_specular: primitives.Bool | None = None, rig: primitives.Bool | None = None, setup_ik: primitives.Bool | None = None, debug_rig: primitives.Bool | None = None, colliders: primitives.Bool | None = None, animations: primitives.Bool | None = None, snappable: primitives.Bool | None = None, timelapse: primitives.Bool | None = None, external_textures: primitives.Bool | None = None, grabbable: primitives.Bool | None = None, scalable: primitives.Bool | None = None, import_at_origin: primitives.Bool | None = None, force_tpose: primitives.Bool | None = None, assets_on_object: primitives.Bool | None = None, as_point_cloud: primitives.Bool | None = None, import_images_by_name: primitives.Bool | None = None, calculate_normals: primitives.Bool | None = None, calculate_tangents: primitives.Bool | None = None, calculate_texture_alpha: primitives.Bool | None = None, import_vertex_colors: primitives.Bool | None = None, import_albedo_color: primitives.Bool | None = None, import_emissive: primitives.Bool | None = None, import_bones: primitives.Bool | None = None, import_lights: primitives.Bool | None = None, make_dual_sided: primitives.Bool | None = None, make_flat_shaded: primitives.Bool | None = None, deduplicate_instances: primitives.Bool | None = None, optimize_model: primitives.Bool | None = None, split_submeshes: primitives.Bool | None = None, generate_random_colors: primitives.Bool | None = None, spawn_material_orbs: primitives.Bool | None = None, max_texture_size: primitives.Int | None = None, force_point_filtering: primitives.Bool | None = None, force_no_mip_maps: primitives.Bool | None = None, force_uncompressed: primitives.Bool | None = None, force_as_point_cloud: primitives.Bool | None = None, potential_gaussian_splat: primitives.Bool | None = None, flip_y: primitives.Bool | None = None, encode_spz: primitives.Bool | None = None, *, component: workers.Component | None = None) -> None:
        """Initialize with optional member values.

        Args:
            content_root: Initial value for _contentRoot.
            scale: Initial value for _scale.
            auto_scale: Initial value for _autoScale.
            prefer_specular: Initial value for _preferSpecular.
            rig: Initial value for _rig.
            setup_ik: Initial value for _setupIK.
            debug_rig: Initial value for _debugRig.
            colliders: Initial value for _colliders.
            animations: Initial value for _animations.
            snappable: Initial value for _snappable.
            timelapse: Initial value for _timelapse.
            external_textures: Initial value for _externalTextures.
            grabbable: Initial value for _grabbable.
            scalable: Initial value for _scalable.
            import_at_origin: Initial value for _importAtOrigin.
            force_tpose: Initial value for _forceTpose.
            assets_on_object: Initial value for _assetsOnObject.
            as_point_cloud: Initial value for _asPointCloud.
            import_images_by_name: Initial value for _importImagesByName.
            calculate_normals: Initial value for _calculateNormals.
            calculate_tangents: Initial value for _calculateTangents.
            calculate_texture_alpha: Initial value for _calculateTextureAlpha.
            import_vertex_colors: Initial value for _importVertexColors.
            import_albedo_color: Initial value for _importAlbedoColor.
            import_emissive: Initial value for _importEmissive.
            import_bones: Initial value for _importBones.
            import_lights: Initial value for _importLights.
            make_dual_sided: Initial value for _makeDualSided.
            make_flat_shaded: Initial value for _makeFlatShaded.
            deduplicate_instances: Initial value for _deduplicateInstances.
            optimize_model: Initial value for _optimizeModel.
            split_submeshes: Initial value for _splitSubmeshes.
            generate_random_colors: Initial value for _generateRandomColors.
            spawn_material_orbs: Initial value for _spawnMaterialOrbs.
            max_texture_size: Initial value for _maxTextureSize.
            force_point_filtering: Initial value for _forcePointFiltering.
            force_no_mip_maps: Initial value for _forceNoMipMaps.
            force_uncompressed: Initial value for _forceUncompressed.
            force_as_point_cloud: Initial value for ForceAsPointCloud.
            potential_gaussian_splat: Initial value for PotentialGaussianSplat.
            flip_y: Initial value for _flipY.
            encode_spz: Initial value for _encodeSPZ.
            component: Existing Component to wrap.
        """
        super().__init__(component)
        if content_root is not None:
            self.content_root = content_root
        if scale is not None:
            self.scale = scale
        if auto_scale is not None:
            self.auto_scale = auto_scale
        if prefer_specular is not None:
            self.prefer_specular = prefer_specular
        if rig is not None:
            self.rig = rig
        if setup_ik is not None:
            self.setup_ik = setup_ik
        if debug_rig is not None:
            self.debug_rig = debug_rig
        if colliders is not None:
            self.colliders = colliders
        if animations is not None:
            self.animations = animations
        if snappable is not None:
            self.snappable = snappable
        if timelapse is not None:
            self.timelapse = timelapse
        if external_textures is not None:
            self.external_textures = external_textures
        if grabbable is not None:
            self.grabbable = grabbable
        if scalable is not None:
            self.scalable = scalable
        if import_at_origin is not None:
            self.import_at_origin = import_at_origin
        if force_tpose is not None:
            self.force_tpose = force_tpose
        if assets_on_object is not None:
            self.assets_on_object = assets_on_object
        if as_point_cloud is not None:
            self.as_point_cloud = as_point_cloud
        if import_images_by_name is not None:
            self.import_images_by_name = import_images_by_name
        if calculate_normals is not None:
            self.calculate_normals = calculate_normals
        if calculate_tangents is not None:
            self.calculate_tangents = calculate_tangents
        if calculate_texture_alpha is not None:
            self.calculate_texture_alpha = calculate_texture_alpha
        if import_vertex_colors is not None:
            self.import_vertex_colors = import_vertex_colors
        if import_albedo_color is not None:
            self.import_albedo_color = import_albedo_color
        if import_emissive is not None:
            self.import_emissive = import_emissive
        if import_bones is not None:
            self.import_bones = import_bones
        if import_lights is not None:
            self.import_lights = import_lights
        if make_dual_sided is not None:
            self.make_dual_sided = make_dual_sided
        if make_flat_shaded is not None:
            self.make_flat_shaded = make_flat_shaded
        if deduplicate_instances is not None:
            self.deduplicate_instances = deduplicate_instances
        if optimize_model is not None:
            self.optimize_model = optimize_model
        if split_submeshes is not None:
            self.split_submeshes = split_submeshes
        if generate_random_colors is not None:
            self.generate_random_colors = generate_random_colors
        if spawn_material_orbs is not None:
            self.spawn_material_orbs = spawn_material_orbs
        if max_texture_size is not None:
            self.max_texture_size = max_texture_size
        if force_point_filtering is not None:
            self.force_point_filtering = force_point_filtering
        if force_no_mip_maps is not None:
            self.force_no_mip_maps = force_no_mip_maps
        if force_uncompressed is not None:
            self.force_uncompressed = force_uncompressed
        if force_as_point_cloud is not None:
            self.force_as_point_cloud = force_as_point_cloud
        if potential_gaussian_splat is not None:
            self.potential_gaussian_splat = potential_gaussian_splat
        if flip_y is not None:
            self.flip_y = flip_y
        if encode_spz is not None:
            self.encode_spz = encode_spz

    @property
    def content_root(self) -> str | None:
        """Target ID of the _contentRoot reference (targets Slot)."""
        member = self.get_member("_contentRoot")
        if isinstance(member, members.Reference):
            return member.targetId
        return None

    @content_root.setter
    def content_root(self, target: str | Slot | None) -> None:
        """Set the _contentRoot reference by target ID or Slot instance."""
        target_id: str | None = target.id if isinstance(target, Slot) else target  # type: ignore[assignment]
        member = self.get_member("_contentRoot")
        if isinstance(member, members.Reference):
            member.targetId = target_id
        else:
            self.set_member(
                "_contentRoot",
                members.Reference(targetId=target_id, targetType='[FrooxEngine]FrooxEngine.Slot'),
            )

    @property
    def scale(self) -> primitives.Float | None:
        """The _scale field value."""
        member = self.get_member("_scale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scale.setter
    def scale(self, value: primitives.Float) -> None:
        """Set the _scale field value."""
        member = self.get_member("_scale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_scale", fields.FieldFloat(value=value)
            )

    @property
    def auto_scale(self) -> primitives.Bool | None:
        """The _autoScale field value."""
        member = self.get_member("_autoScale")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @auto_scale.setter
    def auto_scale(self, value: primitives.Bool) -> None:
        """Set the _autoScale field value."""
        member = self.get_member("_autoScale")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_autoScale", fields.FieldBool(value=value)
            )

    @property
    def material(self) -> members.FieldEnum | None:
        """The _material member."""
        member = self.get_member("_material")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @material.setter
    def material(self, value: members.FieldEnum) -> None:
        """Set the _material member."""
        self.set_member("_material", value)

    @property
    def prefer_specular(self) -> primitives.Bool | None:
        """The _preferSpecular field value."""
        member = self.get_member("_preferSpecular")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @prefer_specular.setter
    def prefer_specular(self, value: primitives.Bool) -> None:
        """Set the _preferSpecular field value."""
        member = self.get_member("_preferSpecular")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_preferSpecular", fields.FieldBool(value=value)
            )

    @property
    def rig(self) -> primitives.Bool | None:
        """The _rig field value."""
        member = self.get_member("_rig")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @rig.setter
    def rig(self, value: primitives.Bool) -> None:
        """Set the _rig field value."""
        member = self.get_member("_rig")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_rig", fields.FieldBool(value=value)
            )

    @property
    def setup_ik(self) -> primitives.Bool | None:
        """The _setupIK field value."""
        member = self.get_member("_setupIK")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @setup_ik.setter
    def setup_ik(self, value: primitives.Bool) -> None:
        """Set the _setupIK field value."""
        member = self.get_member("_setupIK")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_setupIK", fields.FieldBool(value=value)
            )

    @property
    def debug_rig(self) -> primitives.Bool | None:
        """The _debugRig field value."""
        member = self.get_member("_debugRig")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @debug_rig.setter
    def debug_rig(self, value: primitives.Bool) -> None:
        """Set the _debugRig field value."""
        member = self.get_member("_debugRig")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_debugRig", fields.FieldBool(value=value)
            )

    @property
    def colliders(self) -> primitives.Bool | None:
        """The _colliders field value."""
        member = self.get_member("_colliders")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @colliders.setter
    def colliders(self, value: primitives.Bool) -> None:
        """Set the _colliders field value."""
        member = self.get_member("_colliders")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_colliders", fields.FieldBool(value=value)
            )

    @property
    def animations(self) -> primitives.Bool | None:
        """The _animations field value."""
        member = self.get_member("_animations")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @animations.setter
    def animations(self, value: primitives.Bool) -> None:
        """Set the _animations field value."""
        member = self.get_member("_animations")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_animations", fields.FieldBool(value=value)
            )

    @property
    def snappable(self) -> primitives.Bool | None:
        """The _snappable field value."""
        member = self.get_member("_snappable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @snappable.setter
    def snappable(self, value: primitives.Bool) -> None:
        """Set the _snappable field value."""
        member = self.get_member("_snappable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_snappable", fields.FieldBool(value=value)
            )

    @property
    def timelapse(self) -> primitives.Bool | None:
        """The _timelapse field value."""
        member = self.get_member("_timelapse")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @timelapse.setter
    def timelapse(self, value: primitives.Bool) -> None:
        """Set the _timelapse field value."""
        member = self.get_member("_timelapse")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_timelapse", fields.FieldBool(value=value)
            )

    @property
    def external_textures(self) -> primitives.Bool | None:
        """The _externalTextures field value."""
        member = self.get_member("_externalTextures")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @external_textures.setter
    def external_textures(self, value: primitives.Bool) -> None:
        """Set the _externalTextures field value."""
        member = self.get_member("_externalTextures")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_externalTextures", fields.FieldBool(value=value)
            )

    @property
    def grabbable(self) -> primitives.Bool | None:
        """The _grabbable field value."""
        member = self.get_member("_grabbable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @grabbable.setter
    def grabbable(self, value: primitives.Bool) -> None:
        """Set the _grabbable field value."""
        member = self.get_member("_grabbable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_grabbable", fields.FieldBool(value=value)
            )

    @property
    def scalable(self) -> primitives.Bool | None:
        """The _scalable field value."""
        member = self.get_member("_scalable")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @scalable.setter
    def scalable(self, value: primitives.Bool) -> None:
        """Set the _scalable field value."""
        member = self.get_member("_scalable")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_scalable", fields.FieldBool(value=value)
            )

    @property
    def import_at_origin(self) -> primitives.Bool | None:
        """The _importAtOrigin field value."""
        member = self.get_member("_importAtOrigin")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @import_at_origin.setter
    def import_at_origin(self, value: primitives.Bool) -> None:
        """Set the _importAtOrigin field value."""
        member = self.get_member("_importAtOrigin")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_importAtOrigin", fields.FieldBool(value=value)
            )

    @property
    def force_tpose(self) -> primitives.Bool | None:
        """The _forceTpose field value."""
        member = self.get_member("_forceTpose")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_tpose.setter
    def force_tpose(self, value: primitives.Bool) -> None:
        """Set the _forceTpose field value."""
        member = self.get_member("_forceTpose")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_forceTpose", fields.FieldBool(value=value)
            )

    @property
    def assets_on_object(self) -> primitives.Bool | None:
        """The _assetsOnObject field value."""
        member = self.get_member("_assetsOnObject")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @assets_on_object.setter
    def assets_on_object(self, value: primitives.Bool) -> None:
        """Set the _assetsOnObject field value."""
        member = self.get_member("_assetsOnObject")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_assetsOnObject", fields.FieldBool(value=value)
            )

    @property
    def as_point_cloud(self) -> primitives.Bool | None:
        """The _asPointCloud field value."""
        member = self.get_member("_asPointCloud")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @as_point_cloud.setter
    def as_point_cloud(self, value: primitives.Bool) -> None:
        """Set the _asPointCloud field value."""
        member = self.get_member("_asPointCloud")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_asPointCloud", fields.FieldBool(value=value)
            )

    @property
    def import_images_by_name(self) -> primitives.Bool | None:
        """The _importImagesByName field value."""
        member = self.get_member("_importImagesByName")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @import_images_by_name.setter
    def import_images_by_name(self, value: primitives.Bool) -> None:
        """Set the _importImagesByName field value."""
        member = self.get_member("_importImagesByName")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_importImagesByName", fields.FieldBool(value=value)
            )

    @property
    def import_image_alignment(self) -> members.FieldEnum | None:
        """The _importImageAlignment member."""
        member = self.get_member("_importImageAlignment")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @import_image_alignment.setter
    def import_image_alignment(self, value: members.FieldEnum) -> None:
        """Set the _importImageAlignment member."""
        self.set_member("_importImageAlignment", value)

    @property
    def calculate_normals(self) -> primitives.Bool | None:
        """The _calculateNormals field value."""
        member = self.get_member("_calculateNormals")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @calculate_normals.setter
    def calculate_normals(self, value: primitives.Bool) -> None:
        """Set the _calculateNormals field value."""
        member = self.get_member("_calculateNormals")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_calculateNormals", fields.FieldBool(value=value)
            )

    @property
    def calculate_tangents(self) -> primitives.Bool | None:
        """The _calculateTangents field value."""
        member = self.get_member("_calculateTangents")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @calculate_tangents.setter
    def calculate_tangents(self, value: primitives.Bool) -> None:
        """Set the _calculateTangents field value."""
        member = self.get_member("_calculateTangents")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_calculateTangents", fields.FieldBool(value=value)
            )

    @property
    def calculate_texture_alpha(self) -> primitives.Bool | None:
        """The _calculateTextureAlpha field value."""
        member = self.get_member("_calculateTextureAlpha")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @calculate_texture_alpha.setter
    def calculate_texture_alpha(self, value: primitives.Bool) -> None:
        """Set the _calculateTextureAlpha field value."""
        member = self.get_member("_calculateTextureAlpha")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_calculateTextureAlpha", fields.FieldBool(value=value)
            )

    @property
    def import_vertex_colors(self) -> primitives.Bool | None:
        """The _importVertexColors field value."""
        member = self.get_member("_importVertexColors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @import_vertex_colors.setter
    def import_vertex_colors(self, value: primitives.Bool) -> None:
        """Set the _importVertexColors field value."""
        member = self.get_member("_importVertexColors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_importVertexColors", fields.FieldBool(value=value)
            )

    @property
    def import_albedo_color(self) -> primitives.Bool | None:
        """The _importAlbedoColor field value."""
        member = self.get_member("_importAlbedoColor")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @import_albedo_color.setter
    def import_albedo_color(self, value: primitives.Bool) -> None:
        """Set the _importAlbedoColor field value."""
        member = self.get_member("_importAlbedoColor")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_importAlbedoColor", fields.FieldBool(value=value)
            )

    @property
    def import_emissive(self) -> primitives.Bool | None:
        """The _importEmissive field value."""
        member = self.get_member("_importEmissive")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @import_emissive.setter
    def import_emissive(self, value: primitives.Bool) -> None:
        """Set the _importEmissive field value."""
        member = self.get_member("_importEmissive")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_importEmissive", fields.FieldBool(value=value)
            )

    @property
    def import_bones(self) -> primitives.Bool | None:
        """The _importBones field value."""
        member = self.get_member("_importBones")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @import_bones.setter
    def import_bones(self, value: primitives.Bool) -> None:
        """Set the _importBones field value."""
        member = self.get_member("_importBones")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_importBones", fields.FieldBool(value=value)
            )

    @property
    def import_lights(self) -> primitives.Bool | None:
        """The _importLights field value."""
        member = self.get_member("_importLights")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @import_lights.setter
    def import_lights(self, value: primitives.Bool) -> None:
        """Set the _importLights field value."""
        member = self.get_member("_importLights")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_importLights", fields.FieldBool(value=value)
            )

    @property
    def make_dual_sided(self) -> primitives.Bool | None:
        """The _makeDualSided field value."""
        member = self.get_member("_makeDualSided")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @make_dual_sided.setter
    def make_dual_sided(self, value: primitives.Bool) -> None:
        """Set the _makeDualSided field value."""
        member = self.get_member("_makeDualSided")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_makeDualSided", fields.FieldBool(value=value)
            )

    @property
    def make_flat_shaded(self) -> primitives.Bool | None:
        """The _makeFlatShaded field value."""
        member = self.get_member("_makeFlatShaded")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @make_flat_shaded.setter
    def make_flat_shaded(self, value: primitives.Bool) -> None:
        """Set the _makeFlatShaded field value."""
        member = self.get_member("_makeFlatShaded")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_makeFlatShaded", fields.FieldBool(value=value)
            )

    @property
    def deduplicate_instances(self) -> primitives.Bool | None:
        """The _deduplicateInstances field value."""
        member = self.get_member("_deduplicateInstances")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @deduplicate_instances.setter
    def deduplicate_instances(self, value: primitives.Bool) -> None:
        """Set the _deduplicateInstances field value."""
        member = self.get_member("_deduplicateInstances")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_deduplicateInstances", fields.FieldBool(value=value)
            )

    @property
    def optimize_model(self) -> primitives.Bool | None:
        """The _optimizeModel field value."""
        member = self.get_member("_optimizeModel")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @optimize_model.setter
    def optimize_model(self, value: primitives.Bool) -> None:
        """Set the _optimizeModel field value."""
        member = self.get_member("_optimizeModel")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_optimizeModel", fields.FieldBool(value=value)
            )

    @property
    def split_submeshes(self) -> primitives.Bool | None:
        """The _splitSubmeshes field value."""
        member = self.get_member("_splitSubmeshes")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @split_submeshes.setter
    def split_submeshes(self, value: primitives.Bool) -> None:
        """Set the _splitSubmeshes field value."""
        member = self.get_member("_splitSubmeshes")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_splitSubmeshes", fields.FieldBool(value=value)
            )

    @property
    def generate_random_colors(self) -> primitives.Bool | None:
        """The _generateRandomColors field value."""
        member = self.get_member("_generateRandomColors")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @generate_random_colors.setter
    def generate_random_colors(self, value: primitives.Bool) -> None:
        """Set the _generateRandomColors field value."""
        member = self.get_member("_generateRandomColors")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_generateRandomColors", fields.FieldBool(value=value)
            )

    @property
    def spawn_material_orbs(self) -> primitives.Bool | None:
        """The _spawnMaterialOrbs field value."""
        member = self.get_member("_spawnMaterialOrbs")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @spawn_material_orbs.setter
    def spawn_material_orbs(self, value: primitives.Bool) -> None:
        """Set the _spawnMaterialOrbs field value."""
        member = self.get_member("_spawnMaterialOrbs")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_spawnMaterialOrbs", fields.FieldBool(value=value)
            )

    @property
    def max_texture_size(self) -> primitives.Int | None:
        """The _maxTextureSize field value."""
        member = self.get_member("_maxTextureSize")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @max_texture_size.setter
    def max_texture_size(self, value: primitives.Int) -> None:
        """Set the _maxTextureSize field value."""
        member = self.get_member("_maxTextureSize")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_maxTextureSize", fields.FieldInt(value=value)
            )

    @property
    def texture_conversion(self) -> members.FieldEnum | None:
        """The _textureConversion member."""
        member = self.get_member("_textureConversion")
        if isinstance(member, members.FieldEnum):
            return member
        return None

    @texture_conversion.setter
    def texture_conversion(self, value: members.FieldEnum) -> None:
        """Set the _textureConversion member."""
        self.set_member("_textureConversion", value)

    @property
    def force_point_filtering(self) -> primitives.Bool | None:
        """The _forcePointFiltering field value."""
        member = self.get_member("_forcePointFiltering")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_point_filtering.setter
    def force_point_filtering(self, value: primitives.Bool) -> None:
        """Set the _forcePointFiltering field value."""
        member = self.get_member("_forcePointFiltering")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_forcePointFiltering", fields.FieldBool(value=value)
            )

    @property
    def force_no_mip_maps(self) -> primitives.Bool | None:
        """The _forceNoMipMaps field value."""
        member = self.get_member("_forceNoMipMaps")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_no_mip_maps.setter
    def force_no_mip_maps(self, value: primitives.Bool) -> None:
        """Set the _forceNoMipMaps field value."""
        member = self.get_member("_forceNoMipMaps")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_forceNoMipMaps", fields.FieldBool(value=value)
            )

    @property
    def force_uncompressed(self) -> primitives.Bool | None:
        """The _forceUncompressed field value."""
        member = self.get_member("_forceUncompressed")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_uncompressed.setter
    def force_uncompressed(self, value: primitives.Bool) -> None:
        """Set the _forceUncompressed field value."""
        member = self.get_member("_forceUncompressed")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_forceUncompressed", fields.FieldBool(value=value)
            )

    @property
    def force_as_point_cloud(self) -> primitives.Bool | None:
        """The ForceAsPointCloud field value."""
        member = self.get_member("ForceAsPointCloud")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @force_as_point_cloud.setter
    def force_as_point_cloud(self, value: primitives.Bool) -> None:
        """Set the ForceAsPointCloud field value."""
        member = self.get_member("ForceAsPointCloud")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "ForceAsPointCloud", fields.FieldBool(value=value)
            )

    @property
    def potential_gaussian_splat(self) -> primitives.Bool | None:
        """The PotentialGaussianSplat field value."""
        member = self.get_member("PotentialGaussianSplat")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @potential_gaussian_splat.setter
    def potential_gaussian_splat(self, value: primitives.Bool) -> None:
        """Set the PotentialGaussianSplat field value."""
        member = self.get_member("PotentialGaussianSplat")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "PotentialGaussianSplat", fields.FieldBool(value=value)
            )

    @property
    def flip_y(self) -> primitives.Bool | None:
        """The _flipY field value."""
        member = self.get_member("_flipY")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @flip_y.setter
    def flip_y(self, value: primitives.Bool) -> None:
        """Set the _flipY field value."""
        member = self.get_member("_flipY")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_flipY", fields.FieldBool(value=value)
            )

    @property
    def encode_spz(self) -> primitives.Bool | None:
        """The _encodeSPZ field value."""
        member = self.get_member("_encodeSPZ")
        if member is None:
            return None
        return getattr(member, 'value', None)

    @encode_spz.setter
    def encode_spz(self, value: primitives.Bool) -> None:
        """Set the _encodeSPZ field value."""
        member = self.get_member("_encodeSPZ")
        if member is not None:
            member.value = value  # type: ignore[attr-defined]
        else:
            self.set_member(
                "_encodeSPZ", fields.FieldBool(value=value)
            )

    async def preset_3d_model(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Call the Preset_3DModel sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Preset_3DModel", {"button": button, "eventData": event_data}, debug,
        )

    async def preset_vertex_color_model(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Call the Preset_VertexColorModel sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Preset_VertexColorModel", {"button": button, "eventData": event_data}, debug,
        )

    async def preset_3d_scan(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Call the Preset_3DScan sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Preset_3DScan", {"button": button, "eventData": event_data}, debug,
        )

    async def preset_cad_model(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Call the Preset_CADModel sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Preset_CADModel", {"button": button, "eventData": event_data}, debug,
        )

    async def preset_point_cloud(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Call the Preset_PointCloud sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Preset_PointCloud", {"button": button, "eventData": event_data}, debug,
        )

    async def preset_gaussian_splat(self, resolink: protocols.ResoniteLinkClient, button: str, event_data: str, debug: bool = False) -> dict:
        """Call the Preset_GaussianSplat sync method.

        Args:
            resolink: Connected ResoniteLink client.
            button: The button parameter.
            event_data: The eventData parameter.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        return await self.call_method(
            resolink, "Preset_GaussianSplat", {"button": button, "eventData": event_data}, debug,
        )

