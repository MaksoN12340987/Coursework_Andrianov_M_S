import pytest
from unittest.mock import patch

from src.utils import conversion_json_to_object, conversion_xlsx_to_object, user_greeting


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


@pytest.mark.parametrize(
    "key, expected",
    [
        ("04:00:35", "Доброй ночи"),
        ("05:00:35", "Доброе утро"),
        ("12:00:35", "Добрый день"),
        ("18:00:35", "Добрый вечер"),
        ("04,00:35", "Доброго времени суток"),
    ],
)
def test_user_greeting(key, expected):
    assert user_greeting(key) == expected
