"""Base class for generated component wrappers.

Generated components wrap the raw Component dataclass and provide typed
property access to members. They can be:

- Constructed manually (creates a Component with default members)
- Constructed from a ComponentData response (wraps existing data)
- Converted to a Component for AddComponent/UpdateComponent requests

Generic components (like ``ValueField<>``) use ``Generic[T]`` and
``__class_getitem__`` to produce concrete parameterized classes at
runtime::

    from pyresonitelink.generated.data.value_field import ValueField
    import numpy as np

    # Parameterize with a Python value type
    FloatField = ValueField[np.float32]

    # Use it — type checkers know vf.value is np.float32 | None
    vf = FloatField()
    vf.component.componentType  # "[FrooxEngine]FrooxEngine.ValueField<float>"
"""

from __future__ import annotations

from typing import Any, ClassVar, Generic, TypeVar, TYPE_CHECKING

from pyresonitelink.data import codec
from pyresonitelink.data import members
from pyresonitelink.data import messages
from pyresonitelink.data import responses
from pyresonitelink.data import workers
from pyresonitelink.generated import _type_map

if TYPE_CHECKING:
    from pyresonitelink import client

T = TypeVar("T")


class GeneratedComponent:
    """Base class for all generated component wrappers.

    Subclasses define COMPONENT_TYPE and get typed properties generated
    for each member.

    Attributes:
        COMPONENT_TYPE: The fully-qualified Resonite component type string.
            For generic components, this is the generic type definition
            (e.g. ``"[FrooxEngine]FrooxEngine.ValueField<>"``). Concrete
            parameterized subclasses override this with the concrete type.
    """

    COMPONENT_TYPE: ClassVar[str] = ""

    def __init__(self, component: workers.Component | None = None) -> None:
        """Initialize from an existing Component or create a new one.

        Args:
            component: An existing Component to wrap. If None, creates a
                new Component with the correct componentType and no members
                (they will be populated by the server on AddComponent).
        """
        if component is not None:
            if component.componentType != self.COMPONENT_TYPE:
                raise ValueError(
                    f"Component type mismatch: expected {self.COMPONENT_TYPE}, "
                    f"got {component.componentType}"
                )
            self._component = component
        else:
            self._component = workers.Component(
                componentType=self.COMPONENT_TYPE,
            )

    @property
    def component(self) -> workers.Component:
        """The underlying Component dataclass."""
        return self._component

    @property
    def id(self) -> str | None:
        """The component's unique ID."""
        return self._component.id

    @id.setter
    def id(self, value: str | None) -> None:
        self._component.id = value

    def get_member(self, name: str) -> members.Member | None:
        """Get a raw member by its Resonite name.

        Args:
            name: The member name as it appears in the Resonite data.

        Returns:
            The Member instance, or None if not present.
        """
        return self._component.members.get(name)

    def set_member(self, name: str, value: members.Member) -> None:
        """Set a raw member by its Resonite name.

        Args:
            name: The member name as it appears in the Resonite data.
            value: The Member instance to set.
        """
        self._component.members[name] = value

    async def add_to_slot(
        self,
        resolink: client.Client,
        slot: str | workers.Slot,
        debug: bool = False,
    ) -> responses.NewEntityId:
        """Add this component to a slot on the server.

        After this call, ``self.id`` is set to the new component's ID
        and ``self._component`` is refreshed with server data (including
        member IDs needed for updates).

        Args:
            resolink: Connected ResoniteLink client.
            slot: The slot to add this component to — either a slot ID
                string or a ``Slot`` instance (whose ``id`` is used).
            debug: Print request/response JSON.

        Returns:
            The NewEntityId response.
        """
        slot_id = slot.id if isinstance(slot, workers.Slot) else slot
        assert slot_id is not None, "Slot has no ID"
        resp = await resolink.add_component(
            containerSlotId=slot_id, data=self._component, debug=debug,
        )
        assert resp.entityId is not None, resp.errorInfo
        # Refresh from server to get member IDs
        get_resp = await resolink.get_component(
            componentId=resp.entityId, debug=debug,
        )
        assert get_resp.data is not None
        self._component = get_resp.data
        return resp

    async def update(
        self, resolink: client.Client, debug: bool = False,
    ) -> responses.Response:
        """Send the current state to the server.

        The component must already exist on the server (i.e. ``self.id``
        must be set, typically from ``add_to_slot`` or ``refresh``).

        Args:
            resolink: Connected ResoniteLink client.
            debug: Print request/response JSON.

        Returns:
            The server response.
        """
        return await resolink.update_component(
            data=self._component, debug=debug,
        )

    async def refresh(
        self, resolink: client.Client, debug: bool = False,
    ) -> None:
        """Refresh this component's data from the server.

        Overwrites all local member values with the server's current
        state. The component must already exist (``self.id`` must be set).

        Args:
            resolink: Connected ResoniteLink client.
            debug: Print request/response JSON.
        """
        assert self.id is not None, "Component has no ID; add_to_slot first"
        get_resp = await resolink.get_component(
            componentId=self.id, debug=debug,
        )
        assert get_resp.data is not None
        self._component = get_resp.data

    async def call_method(
        self,
        resolink: client.Client,
        method_name: str,
        arguments: dict[str, object] | None = None,
        debug: bool = False,
    ) -> dict[str, codec.JsonValue]:
        """Call a sync method on this component.

        The component must already exist on the server (``self.id``
        must be set).  Only methods listed in the component's
        definition (from ``GetComponentDefinition``) can be called.

        Args:
            resolink: Connected ResoniteLink client.
            method_name: Name of the method to call (PascalCase, as
                defined by Resonite).
            arguments: Named arguments mapping parameter name to value.
            debug: Print request/response JSON.

        Returns:
            The raw JSON response dict.
        """
        assert self.id is not None, "Component has no ID; add_to_slot first"
        return await resolink.request_json(
            messages.CallSyncMethod(
                targetID=self.id,
                methodName=method_name,
                arguments=arguments or {},
            ),
            debug=debug,
        )

    def __repr__(self) -> str:
        """Return a string representation."""
        cls_name = type(self).__name__
        return f"{cls_name}(id={self.id!r}, type={self.COMPONENT_TYPE!r})"


class GenericComponent(GeneratedComponent, Generic[T]):
    """Base for generated components that have generic type parameters.

    Subclasses must set ``_GENERIC_TYPE_TEMPLATE`` to the component type
    string with ``<>`` as the placeholder for the type argument, e.g.
    ``"[FrooxEngine]FrooxEngine.ValueField<>"``.

    Use subscript syntax with a Python value type to get a concrete class::

        ValueField[np.float32]  # class with COMPONENT_TYPE "...ValueField<float>"

    The concrete class can also be constructed from an existing Component
    whose componentType already has the concrete type argument.

    Attributes:
        _GENERIC_TYPE_TEMPLATE: The component type with ``<>`` placeholder.
        _type_info: The resolved TypeInfo for the concrete type parameter,
            or None if this is the unparameterized generic class.
    """

    _GENERIC_TYPE_TEMPLATE: ClassVar[str] = ""
    _type_info: ClassVar[_type_map.TypeInfo | None] = None

    # Cache of already-created concrete classes, keyed by Python type.
    _concrete_cache: ClassVar[dict[type, type["GenericComponent[Any]"]]] = {}

    def __init_subclass__(cls, **kwargs: Any) -> None:
        """Give each direct subclass its own concrete class cache."""
        super().__init_subclass__(**kwargs)
        if "_concrete_cache" not in cls.__dict__:
            cls._concrete_cache = {}

    def __class_getitem__(
        cls, python_type: type,
    ) -> type["GenericComponent[Any]"]:
        """Create a concrete parameterized class for the given value type.

        Args:
            python_type: A Python value type (e.g. ``np.float32``, ``bool``,
                ``primitives.Float3``).

        Returns:
            A new class with COMPONENT_TYPE set to the concrete Resonite
            type and _type_info set for field resolution.

        Raises:
            KeyError: If python_type is not a known Resonite value type.
        """
        # Let Generic handle TypeVar subscripts (for static analysis)
        if isinstance(python_type, TypeVar):
            return super().__class_getitem__(python_type)  # type: ignore[return-value]

        if python_type in cls._concrete_cache:
            return cls._concrete_cache[python_type]

        info = _type_map.from_python_type(python_type)
        concrete_type = cls._GENERIC_TYPE_TEMPLATE.replace(
            "<>", f"<{info.resonite_name}>"
        )

        concrete_cls = type(
            f"{cls.__name__}_{info.resonite_name}",
            (cls,),
            {
                "COMPONENT_TYPE": concrete_type,
                "_type_info": info,
                "_GENERIC_TYPE_TEMPLATE": cls._GENERIC_TYPE_TEMPLATE,
            },
        )
        cls._concrete_cache[python_type] = concrete_cls
        return concrete_cls

    def __init__(self, component: workers.Component | None = None) -> None:
        """Initialize, inferring the type parameter from component data.

        If this is the unparameterized generic class and a component is
        provided, the concrete type is inferred from the componentType
        string.

        Args:
            component: An existing Component to wrap, or None.

        Raises:
            ValueError: If the component type doesn't match.
        """
        if component is not None and self._type_info is None:
            # Try to infer the concrete type from the component data
            ct = component.componentType or ""
            template_prefix = self._GENERIC_TYPE_TEMPLATE.split("<")[0]
            if ct.startswith(template_prefix) and "<" in ct:
                resonite_name = ct.split("<", 1)[1].rstrip(">")
                try:
                    object.__setattr__(
                        self, "__class__",
                        type(self).__class_getitem__(
                            _type_map.from_resonite_name(resonite_name).python_type
                        ),
                    )
                except KeyError:
                    pass  # Unknown type param, stay generic
        super().__init__(component)
