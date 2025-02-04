import pytest

from src.utils import conversion_json_to_object, conversion_xlsx_to_object


@pytest.mark.parametrize(
    "key, expected",
    [("", []), (None, [])],
)
def test_conversion_xlsx_to_object_no_valid(key, expected):
    assert conversion_xlsx_to_object(key) == expected


@pytest.mark.parametrize(
    "key, expected",
    [("", []), (None, [])],
)
def test_conversion_json_to_object_no_valid(key, expected):
    assert conversion_json_to_object(key) == expected
