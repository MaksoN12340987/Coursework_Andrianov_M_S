from src.card_transactions import make_a_card_list, make_a_top_transaction
from src.utils import conversion_xlsx_to_object


def test_make_a_top_transaction_ok(return_make_a_top_transaction):
    assert make_a_top_transaction(conversion_xlsx_to_object()) == return_make_a_top_transaction


def test_make_a_card_list(return_make_a_card_list):
    assert make_a_card_list(conversion_xlsx_to_object()) == return_make_a_card_list
