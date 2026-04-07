"""Reflection data types for ResoniteLink component definitions.

This module contains dataclasses representing Resonite's reflection model,
used to describe component type structures, members, and generic parameters.
"""

from dataclasses import dataclass, field


# =============================================================================
# Type References and Generic Parameters
# =============================================================================


@dataclass
class TypeReference:
    """A reference to a type, potentially with generic arguments.

    Args:
        type: The full type name. For generic types, this is the generic
            type definition.
        isGenericParameter: Whether this reference is a generic parameter
            placeholder.
        genericArguments: Generic arguments for generic referenced types.
    """

    type: str | None = None
    isGenericParameter: bool = False
    genericArguments: list["TypeReference"] | None = None


@dataclass
class GenericParameter:
    """A generic parameter with its constraints.

    Args:
        name: Name of the generic parameter.
        types: Type constraints the parameter must satisfy.
        unmanaged: Whether the unmanaged constraint is applied.
        struct: Whether the struct constraint is applied.
        enum: Whether the enum constraint is applied.
        class_: Whether the class constraint is applied. Serialized as
            "class" in JSON.
    """

    name: str | None = None
    types: list[TypeReference] | None = None
    unmanaged: bool = False
    struct: bool = False
    enum: bool = False
    # "class" is a Python keyword, so we use class_ and handle it in codec
    class_: bool = False


# =============================================================================
# Type Definition
# =============================================================================


@dataclass
class TypeDefinition:
    """Full structured definition of a type.

    Args:
        baseType: Reference to the base type.
        fullTypeName: Fully qualified type name.
        assemblyName: Name of the assembly containing this type.
        namespace: Namespace of the type.
        name: Short name of the type.
        isAbstract: Whether the type is abstract.
        isInterface: Whether the type is an interface.
        isGenericType: Whether the type is a generic type.
        isGenericTypeDefinition: Whether the type is a generic type definition.
        directGenericParameterCount: Number of generic parameters declared
            directly on this type.
        isEnginePrimitive: Whether the type is an engine primitive.
        isValueType: Whether the type is a value type.
        isEnum: Whether the type is an enum.
        isComponent: Whether the type is a component.
        isSyncObject: Whether the type is a sync object.
        isWorldElement: Whether the type is a world element.
        isNested: Whether the type is nested inside another type.
        declaringType: The declaring type if nested.
        genericArguments: Generic arguments for this type.
        genericParameters: Generic parameter definitions with constraints.
        interfaces: Interfaces implemented by this type.
    """

    baseType: TypeReference | None = None
    fullTypeName: str | None = None
    assemblyName: str | None = None
    namespace: str | None = None
    name: str | None = None
    isAbstract: bool = False
    isInterface: bool = False
    isGenericType: bool = False
    isGenericTypeDefinition: bool = False
    directGenericParameterCount: int = 0
    isEnginePrimitive: bool = False
    isValueType: bool = False
    isEnum: bool = False
    isComponent: bool = False
    isSyncObject: bool = False
    isWorldElement: bool = False
    isNested: bool = False
    declaringType: str | None = None
    genericArguments: list[TypeReference] | None = None
    genericParameters: list[GenericParameter] | None = None
    interfaces: list[TypeReference] | None = None


# =============================================================================
# Member Definitions
# =============================================================================


@dataclass
class MemberDefinition:
    """Base class for member definitions.

    Args:
        type: The full type of the member itself.
    """

    type: TypeReference | None = None


@dataclass
class FieldDefinition(MemberDefinition):
    """A field member definition.

    Args:
        valueType: The data type of the value this field holds.
    """

    valueType: TypeReference | None = None


@dataclass
class ReferenceDefinition(MemberDefinition):
    """A reference member definition.

    Args:
        targetType: The data type of the reference target.
    """

    targetType: TypeReference | None = None


@dataclass
class ListDefinition(MemberDefinition):
    """A list member definition.

    Args:
        elementDefinition: Definition of the elements in this list.
    """

    elementDefinition: MemberDefinition | None = None


@dataclass
class ArrayDefinition(MemberDefinition):
    """An array member definition.

    Args:
        valueType: The data type of elements in the array.
    """

    valueType: TypeReference | None = None


@dataclass
class DictionaryDefinition(MemberDefinition):
    """A dictionary member definition.

    Args:
        keyType: The data type used for dictionary keys.
        elementDefinition: Definition of the elements in this dictionary.
    """

    keyType: TypeReference | None = None
    elementDefinition: MemberDefinition | None = None


@dataclass
class SyncObjectMemberDefinition(MemberDefinition):
    """A sync object embedded as a member.

    Contains no additional properties beyond MemberDefinition.
    """


@dataclass
class EmptyMemberDefinition(MemberDefinition):
    """An empty member that contains no data but can be referenced.

    Used for linking things like ProtoFlux nodes.
    """


@dataclass
class SyncPlaybackDefinition(MemberDefinition):
    """A playback state member.

    Has a fixed definition with no additional properties.
    """


# =============================================================================
# Sync Method Definition
# =============================================================================


@dataclass
class SyncMethodDefinition:
    """Definition of a sync method on a component.

    Args:
        name: Name of the method.
        parameters: Method parameters mapped by name to their type.
        returnType: Return type of the method.
        isStatic: Whether the method is static.
        isAsync: Whether the method is async.
    """

    name: str | None = None
    parameters: dict[str, TypeReference] | None = field(default=None)
    returnType: TypeReference | None = None
    isStatic: bool = False
    isAsync: bool = False


# =============================================================================
# Component Definition
# =============================================================================


@dataclass
class ComponentDefinition:
    """Full definition of a component type.

    Args:
        type: Structured type definition of this component.
        members: All members and their definitions.
        methods: All supported sync methods.
        baseTypeIsComponent: Whether the base type is also a component.
        categoryPath: The organizational category path for this component.
    """

    type: TypeDefinition | None = None
    members: dict[str, MemberDefinition] | None = None
    methods: list[SyncMethodDefinition] | None = None
    baseTypeIsComponent: bool = False
    categoryPath: str | None = None
