# This is where the functions that process operations on the card are located. 
from src.utils import conversion_xlsx_to_object


def make_a_top_transaction():
    conversion_xlsx_to_object("data/operations.xlsx")
    pass
