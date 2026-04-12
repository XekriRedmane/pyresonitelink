"""Stub enum for System.Type.

System.Type is not a real enum in Resonite — it's a .NET class.
TypeObjectInput uses it as a field type exposed as FieldEnum in the
wire format.  This stub allows the import to succeed.
"""

from enum import StrEnum


class Type(StrEnum):
    """Stub for System.Type values (passed as strings)."""
