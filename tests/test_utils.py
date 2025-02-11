import pytest

from src.utils import dataframe_from_file, conversion_json_to_object, conversion_xlsx_to_object, user_greeting


def test_ataframe_from_file_ok():
    assert str(type(dataframe_from_file())) == "<class 'pandas.core.frame.DataFrame'>"


def test_ataframe_from_file_exeption():
    with pytest.raises(Exception):
        assert dataframe_from_file("src/decoretor.py") == "Exceptional error"


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
