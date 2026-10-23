"""Adds ProtoFlux nodes and wires them together.

ProtoFlux nodes are components whose inputs are references to other nodes.
add_node adds a node with no references and then wires them with
update_references, sending each reference's targetType as the new node's
own data reports it. The server often leaves references unwired when they
are sent with AddComponent, and a reference sent without a targetType, or
with a guessed one, can fail its type check. For example, one input of
Add_DateTime_TimeSpan targets INodeValueOutput<DateTime> and the other
targets INodeValueOutput<TimeSpan>.

A ValueFieldDrive<T> node has only a Value input. The server adds a
FieldDriveBase<T>+Proxy component beside it, and the field that the node
drives is the Proxy's Drive reference. The Proxy's Node reference
identifies the node it belongs to. drive_field finds the Proxy and sets
its Drive.

    add = operators.ValueAdd[primitives.Float]()
    await wiring.add_node(resolink, slot, add, {"A": a, "B": b})
    drive = core.ValueFieldDrive[primitives.Float]()
    await wiring.add_node(resolink, slot, drive, {"Value": add})
    await wiring.drive_field(resolink, slot, drive, field_member_id)

drive_from does the last three lines in one call. add_reference_input adds
a RefObjectInput<T> node, which outputs a reference to a world element such
as a component. A node input that takes an INodeObjectOutput<T> of an
interface, such as IsGrabbableGrabbed's Grabbable, is fed by one, and the
generated RefObjectInput class can't be given an interface as T.
"""

import asyncio
from collections.abc import Mapping

from pyresonitelink.data import members
from pyresonitelink.data import protocols
from pyresonitelink.data import workers
from pyresonitelink.generated._base import GeneratedComponent
from pyresonitelink.generated.protoflux.runtimes.execution.nodes.core import value_field_drive

# The time between adding a node and wiring it. With no pause, the
# references all arrive but the graph doesn't run (measured 18 Oct 2026).
# The nodes apparently have to be registered in an engine update before
# they're wired.
WIRE_DELAY = 0.05  # seconds

# The targetType sent for a member whose data reports none.
_DEFAULT_TARGET_TYPE = "[FrooxEngine]FrooxEngine.ProtoFlux.INodeValueOutput<T>"

_REF_INPUT_TYPE = (
    "[ProtoFluxBindings]FrooxEngine.ProtoFlux.Runtimes.Execution.Nodes.RefObjectInput<{}>"
)

# How often and how many times drive_field looks for the Proxy.
_PROXY_POLL_INTERVAL = 0.05  # seconds
_PROXY_POLLS = 20


async def add_node(
    resolink: protocols.ResoniteLinkClient,
    slot: str | workers.Slot,
    node: GeneratedComponent,
    references: Mapping[str, str | GeneratedComponent] | None = None,
    *,
    debug: bool = False,
) -> None:
    """Adds a ProtoFlux node to a slot, then wires its references.

    The node is added as constructed, so field values set in its
    constructor are sent with it. Its references are best left unset in
    the constructor and given here instead.

    Args:
        resolink (protocols.ResoniteLinkClient): The connected client.
        slot (str | workers.Slot): The slot to add the node to, as an ID or
            a Slot.
        node (GeneratedComponent): The node, which has no ID yet. Its id is
            set when it has been added.
        references (Mapping[str, str | GeneratedComponent] | None): The
            node's reference members, by their Resonite names (e.g. "A"),
            and the IDs or components they point to.
        debug (bool): Print request and response JSON.

    Raises:
        RuntimeError: The server refused the references.
    """
    await node.add_to_slot(resolink, slot, debug=debug)
    await asyncio.sleep(WIRE_DELAY)
    if not references:
        return
    typed: dict[str, str | members.Reference] = {}
    for name, target in references.items():
        target_id = target if isinstance(target, str) else target.id
        member = node.get_member(name)
        target_type = (
            member.targetType
            if isinstance(member, members.Reference) and member.targetType
            else _DEFAULT_TARGET_TYPE
        )
        typed[name] = members.Reference(targetId=target_id, targetType=target_type)
    assert node.id is not None
    resp = await resolink.update_references(
        componentId=node.id, references=typed, debug=debug,
    )
    if not resp.success:
        raise RuntimeError(
            f"Failed to wire {type(node).__name__} {node.id}: {resp.errorInfo}"
        )


async def find_drive_proxy(
    resolink: protocols.ResoniteLinkClient,
    slot: str | workers.Slot,
    drive: str | GeneratedComponent,
) -> workers.Component:
    """Finds the Proxy component of a field drive node.

    The server adds the Proxy when it adds the node, so it may take a few
    requests to appear.

    Args:
        resolink (protocols.ResoniteLinkClient): The connected client.
        slot (str | workers.Slot): The slot that holds the node.
        drive (str | GeneratedComponent): The drive node, or its ID.

    Returns:
        The Proxy's data, including its Drive reference.

    Raises:
        RuntimeError: No Proxy for the node appeared within a second.
    """
    drive_id = drive if isinstance(drive, str) else drive.id
    for _ in range(_PROXY_POLLS):
        data = (await resolink.get_slot(slot, includeComponentData=True)).data
        for component in data.components if data is not None else []:
            node = (component.members or {}).get("Node")
            if ((component.componentType or "").endswith("+Proxy")
                    and isinstance(node, members.Reference)
                    and node.targetId == drive_id):
                return component
        await asyncio.sleep(_PROXY_POLL_INTERVAL)
    raise RuntimeError(f"No Proxy component appeared for the drive {drive_id}.")


async def drive_field(
    resolink: protocols.ResoniteLinkClient,
    slot: str | workers.Slot,
    drive: str | GeneratedComponent,
    field_id: str,
) -> None:
    """Makes a field drive node drive a field.

    The Drive reference is sent with the targetType that the Proxy's data
    reports, such as IField<floatQ>.

    Args:
        resolink (protocols.ResoniteLinkClient): The connected client.
        slot (str | workers.Slot): The slot that holds the drive node.
        drive (str | GeneratedComponent): The drive node, such as a
            ValueFieldDrive<T>, or its ID.
        field_id (str): The member ID of the field to drive, e.g. the ID of
            a slot's Rotation field, not the ID of the slot or component.

    Raises:
        RuntimeError: No Proxy appeared, or the server refused the
            reference.
    """
    drive_id = drive if isinstance(drive, str) else drive.id
    proxy = await find_drive_proxy(resolink, slot, drive)
    assert proxy.id is not None
    target = (proxy.members or {}).get("Drive")
    resp = await resolink.update_references(
        componentId=proxy.id,
        references={"Drive": members.Reference(
            targetId=field_id,
            targetType=target.targetType if isinstance(target, members.Reference) else None,
        )},
    )
    if not resp.success:
        raise RuntimeError(
            f"Failed to set the field that drive {drive_id} drives: {resp.errorInfo}"
        )


async def drive_from(
    resolink: protocols.ResoniteLinkClient,
    slot: str | workers.Slot,
    source: str | GeneratedComponent,
    field_id: str,
    value_type: type,
    *,
    debug: bool = False,
) -> GeneratedComponent:
    """Adds a ValueFieldDrive<T> that drives a field from a node's output.

    The field takes the node's value in every engine update. A ValueDisplay
    can't take its place for a value that changes every frame, such as the
    ViewRotation node's, since it wrote its field only once, when it was
    wired (measured 23 Oct 2026).

    Args:
        resolink (protocols.ResoniteLinkClient): The connected client.
        slot (str | workers.Slot): The slot to add the drive node to.
        source (str | GeneratedComponent): The node whose output drives
            the field, or its ID.
        field_id (str): The member ID of the field to drive.
        value_type (type): The field's value type, such as
            primitives.Float or primitives.Bool.
        debug (bool): Print request and response JSON.

    Returns:
        The drive node.

    Raises:
        RuntimeError: The server refused a reference, or no Proxy appeared.
    """
    drive = value_field_drive.ValueFieldDrive[value_type]()  # type: ignore[valid-type]
    await add_node(resolink, slot, drive, {"Value": source}, debug=debug)
    await drive_field(resolink, slot, drive, field_id)
    return drive


async def add_reference_input(
    resolink: protocols.ResoniteLinkClient,
    slot: str | workers.Slot,
    target: str | GeneratedComponent | workers.Slot,
    type_name: str,
    *,
    debug: bool = False,
) -> str:
    """Adds a RefObjectInput<T> node that outputs a reference to a world element.

    Args:
        resolink (protocols.ResoniteLinkClient): The connected client.
        slot (str | workers.Slot): The slot to add the node to.
        target (str | GeneratedComponent | workers.Slot): The element the
            node refers to, such as a component, or its ID.
        type_name (str): T, the assembly-qualified Resonite type of the
            reference, e.g. "[FrooxEngine]FrooxEngine.IGrabbable".
        debug (bool): Print request and response JSON.

    Returns:
        The new node's ID.

    Raises:
        RuntimeError: The server refused the node or its reference.
    """
    added = await resolink.add_component(
        slot, data=workers.Component(componentType=_REF_INPUT_TYPE.format(type_name)), debug=debug,
    )
    if not added.success or added.entityId is None:
        raise RuntimeError(f"Failed to add RefObjectInput<{type_name}>: {added.errorInfo}")
    node_id = added.entityId
    await asyncio.sleep(WIRE_DELAY)
    data = (await resolink.get_component(componentId=node_id, debug=debug)).data
    reported = (data.members or {}).get("Target") if data is not None else None
    target_id = target if isinstance(target, str) else target.id
    resp = await resolink.update_references(
        componentId=node_id,
        references={"Target": members.Reference(
            targetId=target_id,
            targetType=reported.targetType if isinstance(reported, members.Reference) else None,
        )},
        debug=debug,
    )
    if not resp.success:
        raise RuntimeError(f"Failed to set the target of {node_id}: {resp.errorInfo}")
    return node_id
