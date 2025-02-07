import pytest

from src.card_transactions import array_of_transactions_for_top_selection
from src.utils import conversion_xlsx_to_object


@pytest.mark.parametrize(
    "key, expected",
    [("", []), (None, [])],
)
def test_array_of_transactions_for_top_selection_no_valid(key, expected):
    assert array_of_transactions_for_top_selection(conversion_xlsx_to_object(key)) == expected


def test_array_of_transactions_for_top_selection_ok(return_array_of_transactions_for_top_selection):
    assert (
        array_of_transactions_for_top_selection(conversion_xlsx_to_object())
        == return_array_of_transactions_for_top_selection
    )
