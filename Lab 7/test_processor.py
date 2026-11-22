from hypothesis import given, strategies as st
from processor import sanitize_license_plate, parse_trip_mileage, format_rental_invoice


@given(st.text() | st.none())
def test_sanitize_license_plate_no_crash(s):
    try:
        result = sanitize_license_plate(s)
    except Exception as e:
        assert False, f"sanitize_license_plate crashed with: {e!r} for input {s!r}"
    # Extra property: output is always a string with no delimiters left
    assert isinstance(result, str)
    for ch in ['-', ' ', '_', '#']:
        assert ch not in result


@given(st.text() | st.none())
def test_parse_trip_mileage_safe(s):
    try:
        result = parse_trip_mileage(s)
    except Exception as e:
        assert False, f"parse_trip_mileage crashed with: {e!r} for input {s!r}"
    # Extra property: always a list of non-negative finite floats
    assert isinstance(result, list)
    assert all(isinstance(x, float) and x >= 0 and x == x and x != float("inf") for x in result)


@given(st.text() | st.none())
def test_format_rental_invoice_safe(s):
    try:
        result = format_rental_invoice(s)
    except Exception as e:
        assert False, f"format_rental_invoice crashed with: {e!r} for input {s!r}"
    # Extra property: always returns a string
    assert isinstance(result, str)