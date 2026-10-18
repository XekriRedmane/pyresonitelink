"""Utility functions for the data module."""

from dataclasses import field
from typing import Any

# Metadata key for marking fields to ignore during JSON encoding/decoding
JSON_IGNORE_KEY = "__json_ignore__"

# Metadata key for a field whose JSON key differs from its Python name
JSON_NAME_KEY = "__json_name__"


def json_name(name: str, **kwargs: Any) -> Any:
    """Create a dataclass field whose JSON key is name.

    For a JSON key that can't be a Python identifier, such as the keyword
    "class".

    Args:
        name: The key the field has in JSON.
        **kwargs: Arguments passed to dataclasses.field() (e.g., default).

    Returns:
        A dataclass field with json_name metadata.
    """
    metadata = kwargs.pop("metadata", {})
    metadata[JSON_NAME_KEY] = name
    return field(metadata=metadata, **kwargs)  # pylint: disable=invalid-field-call


def json_ignore(**kwargs: Any) -> Any:
    """Create a dataclass field that is ignored during JSON encoding/decoding.

    This is a wrapper around dataclasses.field() that adds metadata to mark
    the field as ignored by the JSON codec.

    Args:
        **kwargs: Arguments passed to dataclasses.field() (e.g., default, default_factory).

    Returns:
        A dataclass field with json_ignore metadata.

    Example:
        @dataclass
        class MyMessage(Message):
            name: str = ""
            payload: bytearray = json_ignore(default_factory=bytearray)
    """
    metadata = kwargs.pop("metadata", {})
    metadata[JSON_IGNORE_KEY] = True
    return field(metadata=metadata, **kwargs)  # pylint: disable=invalid-field-call
