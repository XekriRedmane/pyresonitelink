"""Tests for client coercion helpers."""

import numpy as np

from pyresonitelink.client import (
    _coerce_composite_field,
    _coerce_scalar_field,
)
from pyresonitelink.data import fields
from pyresonitelink.data import primitives


# =========================================================================
# _coerce_scalar_field
# =========================================================================


class TestCoerceScalarFieldString:
    """Tests for _coerce_scalar_field with FieldString."""

    def test_passthrough(self) -> None:
        f = fields.FieldString(value="hello")
        assert _coerce_scalar_field(f, fields.FieldString) is f

    def test_from_str(self) -> None:
        result = _coerce_scalar_field("hello", fields.FieldString)
        assert isinstance(result, fields.FieldString)
        assert result.value == "hello"

    def test_empty_str(self) -> None:
        result = _coerce_scalar_field("", fields.FieldString)
        assert isinstance(result, fields.FieldString)
        assert result.value == ""


class TestCoerceScalarFieldBool:
    """Tests for _coerce_scalar_field with FieldBool."""

    def test_passthrough(self) -> None:
        f = fields.FieldBool(value=True)
        assert _coerce_scalar_field(f, fields.FieldBool) is f

    def test_from_true(self) -> None:
        result = _coerce_scalar_field(True, fields.FieldBool)
        assert isinstance(result, fields.FieldBool)
        assert result.value is True

    def test_from_false(self) -> None:
        result = _coerce_scalar_field(False, fields.FieldBool)
        assert isinstance(result, fields.FieldBool)
        assert result.value is False


class TestCoerceScalarFieldLong:
    """Tests for _coerce_scalar_field with FieldLong and np_type."""

    def test_passthrough(self) -> None:
        f = fields.FieldLong(value=np.int64(42))
        assert _coerce_scalar_field(f, fields.FieldLong, np.int64) is f

    def test_from_int(self) -> None:
        result = _coerce_scalar_field(42, fields.FieldLong, np.int64)
        assert isinstance(result, fields.FieldLong)
        assert result.value == np.int64(42)


class TestCoerceScalarFieldFloat:
    """Tests for _coerce_scalar_field with FieldFloat and np_type."""

    def test_passthrough(self) -> None:
        f = fields.FieldFloat(value=np.float32(1.5))
        assert _coerce_scalar_field(f, fields.FieldFloat, np.float32) is f

    def test_from_float(self) -> None:
        result = _coerce_scalar_field(1.5, fields.FieldFloat, np.float32)
        assert isinstance(result, fields.FieldFloat)
        assert result.value == np.float32(1.5)

    def test_from_int(self) -> None:
        result = _coerce_scalar_field(3, fields.FieldFloat, np.float32)
        assert isinstance(result, fields.FieldFloat)
        assert result.value == np.float32(3.0)


class TestCoerceScalarFieldInt:
    """Tests for _coerce_scalar_field with FieldInt and np_type."""

    def test_from_int(self) -> None:
        result = _coerce_scalar_field(99, fields.FieldInt, np.int32)
        assert isinstance(result, fields.FieldInt)
        assert result.value == np.int32(99)


# =========================================================================
# _coerce_composite_field — 3-component vectors
# =========================================================================


class TestCoerceCompositeFloat3:
    """Tests for _coerce_composite_field with FieldFloat3 / Float3."""

    def test_passthrough(self) -> None:
        f = fields.FieldFloat3(value=primitives.Float3(x=1, y=2, z=3))
        assert _coerce_composite_field(f, fields.FieldFloat3, primitives.Float3) is f

    def test_from_primitive(self) -> None:
        v = primitives.Float3(x=1, y=2, z=3)
        result = _coerce_composite_field(v, fields.FieldFloat3, primitives.Float3)
        assert isinstance(result, fields.FieldFloat3)
        assert result.value is v

    def test_from_list(self) -> None:
        result = _coerce_composite_field(
            [1.0, 2.0, 3.0], fields.FieldFloat3, primitives.Float3,
        )
        assert isinstance(result, fields.FieldFloat3)
        assert result.value is not None
        assert float(result.value.x) == 1.0
        assert float(result.value.y) == 2.0
        assert float(result.value.z) == 3.0

    def test_from_tuple(self) -> None:
        result = _coerce_composite_field(
            (4.0, 5.0, 6.0), fields.FieldFloat3, primitives.Float3,
        )
        assert isinstance(result, fields.FieldFloat3)
        assert result.value is not None
        assert float(result.value.x) == 4.0
        assert float(result.value.y) == 5.0
        assert float(result.value.z) == 6.0

    def test_from_ndarray(self) -> None:
        arr = np.array([7.0, 8.0, 9.0], dtype=np.float32)
        result = _coerce_composite_field(
            arr, fields.FieldFloat3, primitives.Float3,
        )
        assert isinstance(result, fields.FieldFloat3)
        assert result.value is not None
        assert float(result.value.x) == 7.0
        assert float(result.value.y) == 8.0
        assert float(result.value.z) == 9.0


class TestCoerceCompositeInt3:
    """Tests for _coerce_composite_field with FieldInt3 / Int3."""

    def test_from_primitive(self) -> None:
        v = primitives.Int3(x=10, y=20, z=30)
        result = _coerce_composite_field(v, fields.FieldInt3, primitives.Int3)
        assert isinstance(result, fields.FieldInt3)
        assert result.value is v

    def test_from_list(self) -> None:
        result = _coerce_composite_field(
            [10, 20, 30], fields.FieldInt3, primitives.Int3,
        )
        assert isinstance(result, fields.FieldInt3)
        assert result.value is not None
        assert int(result.value.x) == 10
        assert int(result.value.y) == 20
        assert int(result.value.z) == 30

    def test_from_tuple(self) -> None:
        result = _coerce_composite_field(
            (1, 2, 3), fields.FieldInt3, primitives.Int3,
        )
        assert isinstance(result, fields.FieldInt3)
        assert result.value is not None
        assert int(result.value.x) == 1


# =========================================================================
# _coerce_composite_field — 2-component vectors
# =========================================================================


class TestCoerceCompositeFloat2:
    """Tests for _coerce_composite_field with FieldFloat2 / Float2."""

    def test_from_primitive(self) -> None:
        v = primitives.Float2(x=1, y=2)
        result = _coerce_composite_field(v, fields.FieldFloat2, primitives.Float2)
        assert isinstance(result, fields.FieldFloat2)
        assert result.value is v

    def test_from_list(self) -> None:
        result = _coerce_composite_field(
            [3.0, 4.0], fields.FieldFloat2, primitives.Float2,
        )
        assert isinstance(result, fields.FieldFloat2)
        assert result.value is not None
        assert float(result.value.x) == 3.0
        assert float(result.value.y) == 4.0


class TestCoerceCompositeInt2:
    """Tests for _coerce_composite_field with FieldInt2 / Int2."""

    def test_from_list(self) -> None:
        result = _coerce_composite_field(
            [5, 6], fields.FieldInt2, primitives.Int2,
        )
        assert isinstance(result, fields.FieldInt2)
        assert result.value is not None
        assert int(result.value.x) == 5
        assert int(result.value.y) == 6


# =========================================================================
# _coerce_composite_field — 4-component vectors and quaternions
# =========================================================================


class TestCoerceCompositeFloatQ:
    """Tests for _coerce_composite_field with FieldFloatQ / FloatQ."""

    def test_passthrough(self) -> None:
        f = fields.FieldFloatQ(
            value=primitives.FloatQ(x=0, y=0, z=0, w=1),
        )
        assert _coerce_composite_field(f, fields.FieldFloatQ, primitives.FloatQ) is f

    def test_from_primitive(self) -> None:
        v = primitives.FloatQ(x=0, y=0, z=0, w=1)
        result = _coerce_composite_field(v, fields.FieldFloatQ, primitives.FloatQ)
        assert isinstance(result, fields.FieldFloatQ)
        assert result.value is v

    def test_from_list(self) -> None:
        result = _coerce_composite_field(
            [0.1, 0.2, 0.3, 0.9], fields.FieldFloatQ, primitives.FloatQ,
        )
        assert isinstance(result, fields.FieldFloatQ)
        assert result.value is not None
        assert abs(float(result.value.x) - 0.1) < 1e-6
        assert abs(float(result.value.y) - 0.2) < 1e-6
        assert abs(float(result.value.z) - 0.3) < 1e-6
        assert abs(float(result.value.w) - 0.9) < 1e-6

    def test_from_tuple(self) -> None:
        result = _coerce_composite_field(
            (0.0, 0.0, 0.0, 1.0), fields.FieldFloatQ, primitives.FloatQ,
        )
        assert isinstance(result, fields.FieldFloatQ)
        assert result.value is not None
        assert float(result.value.w) == 1.0

    def test_from_ndarray(self) -> None:
        arr = np.array([0.1, 0.2, 0.3, 0.4], dtype=np.float32)
        result = _coerce_composite_field(
            arr, fields.FieldFloatQ, primitives.FloatQ,
        )
        assert isinstance(result, fields.FieldFloatQ)
        assert result.value is not None
        assert abs(float(result.value.x) - 0.1) < 1e-6


class TestCoerceCompositeFloat4:
    """Tests for _coerce_composite_field with FieldFloat4 / Float4."""

    def test_from_list(self) -> None:
        result = _coerce_composite_field(
            [1.0, 2.0, 3.0, 4.0], fields.FieldFloat4, primitives.Float4,
        )
        assert isinstance(result, fields.FieldFloat4)
        assert result.value is not None
        assert float(result.value.x) == 1.0
        assert float(result.value.w) == 4.0


class TestCoerceCompositeInt4:
    """Tests for _coerce_composite_field with FieldInt4 / Int4."""

    def test_from_list(self) -> None:
        result = _coerce_composite_field(
            [1, 2, 3, 4], fields.FieldInt4, primitives.Int4,
        )
        assert isinstance(result, fields.FieldInt4)
        assert result.value is not None
        assert int(result.value.x) == 1
        assert int(result.value.w) == 4


# =========================================================================
# _coerce_composite_field — colours
# =========================================================================


class TestCoerceCompositeColor:
    """Tests for _coerce_composite_field with FieldColor / Color."""

    def test_from_primitive(self) -> None:
        v = primitives.Color(r=1, g=0, b=0, a=1)
        result = _coerce_composite_field(v, fields.FieldColor, primitives.Color)
        assert isinstance(result, fields.FieldColor)
        assert result.value is v

    def test_from_list(self) -> None:
        result = _coerce_composite_field(
            [0.5, 0.6, 0.7, 1.0], fields.FieldColor, primitives.Color,
        )
        assert isinstance(result, fields.FieldColor)
        assert result.value is not None
        assert abs(float(result.value.r) - 0.5) < 1e-6
        assert abs(float(result.value.a) - 1.0) < 1e-6


# =========================================================================
# _coerce_composite_field — matrices
# =========================================================================


class TestCoerceCompositeFloat2x2:
    """Tests for _coerce_composite_field with FieldFloat2x2 / Float2x2."""

    def test_from_list(self) -> None:
        result = _coerce_composite_field(
            [1.0, 0.0, 0.0, 1.0],
            fields.FieldFloat2x2,
            primitives.Float2x2,
        )
        assert isinstance(result, fields.FieldFloat2x2)
        assert result.value is not None
        assert float(result.value.m00) == 1.0
        assert float(result.value.m11) == 1.0
