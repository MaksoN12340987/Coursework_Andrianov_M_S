import pytest

from src.card_transactions import array_of_transactions_for_top_selection, make_a_top_transaction, make_a_card_list
from src.utils import conversion_xlsx_to_object


@pytest.mark.parametrize(
    "key, expected",
    [("", []), (None, [])],
)
def test_array_of_transactions_for_top_selection_no_valid(key, expected):
    assert array_of_transactions_for_top_selection(conversion_xlsx_to_object(key)) == expected


def test_array_of_transactions_for_top_selection_ok():
    assert array_of_transactions_for_top_selection(conversion_xlsx_to_object())[1] == {
        "date": "31.12.2021",
        "amount": -64.0,
        "category": "Супермаркеты",
        "description": "Колхоз",
    }


def test_array_of_transactions_for_top_selection_no_valid(return_make_a_top_transaction):
    assert make_a_top_transaction(array_of_transactions_for_top_selection(conversion_xlsx_to_object())) == return_make_a_top_transaction
