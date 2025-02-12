# This is where the functions that process operations on the card are located.
import logging

logger_card_trans = logging.getLogger("card_transactions")
file_handler = logging.FileHandler("log/card_transactions.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_card_trans.addHandler(file_handler)
logger_card_trans.setLevel(logging.INFO)

# from utils import conversion_xlsx_to_object
# from decoretor import decorator_for_output_to_console_file


def array_of_transactions_for_top_selection(array_of_operations: list[dict] = [{}]) -> list[dict]:
    """Функция подготовки данных, для двльнейешй выборки в make_a_top_transaction

    Args:
        array_of_operations (list[dict], optional): _description_. Defaults to [{}].

    Returns:
        list[dict]: _description_
    """
    result = []
    for i, value in enumerate(array_of_operations):
        try:
            result.append(
                {
                    "date": str(value["Дата платежа"]),
                    "amount": value["Сумма операции"],
                    "category": str(value["Категория"]),
                    "description": str(value["Описание"]),
                }
            )
        except Exception:
            pass
    logger_card_trans.info(f"{result}")
    return result

# @decorator_for_output_to_console_file("card.py")
def make_a_top_transaction(operations_list: list[dict] = [{}], number_top_elements: int = 5) -> list[dict]:
    """_summary_

    Args:
        operations_list (list[dict], optional): _description_. Defaults to [{}].
        number_top_elements (int, optional): _description_. Defaults to 5.

    Returns:
        list[dict]: _description_
    """
    result = []
    items_amount = 0.00

    for index, value in enumerate(operations_list):
        items_amount = value["amount"]
        if items_amount < 0:
            items_amount = items_amount * -1

        if len(result) != number_top_elements:
            for i, comparison_meaning in enumerate(operations_list):

                comparison = comparison_meaning["amount"]
                if comparison < 0:
                    comparison = comparison * -1

                if items_amount < comparison:
                    items_amount = comparison
                    index_largest_element = i

            result.append(operations_list[index_largest_element])
            del operations_list[index_largest_element]
    return result
# make_a_top_transaction(array_of_transactions_for_top_selection(conversion_xlsx_to_object()))


def make_a_card_list(operations_list: list[dict] = [{}]) -> list[dict]:
    """_summary_

    Args:
        operations_list (list[dict], optional): _description_. Defaults to [{}].

    Returns:
        list[dict]: _description_
    """
    result = []
    out = {}

    for i, value in enumerate(operations_list):
        carrd_number = str(value["Номер карты"])[-4:]
        sum_operation = 0.00

        for count, comparison_meaning in enumerate(operations_list):
            if carrd_number == str(comparison_meaning["Номер карты"])[-4:]:
                if comparison_meaning["Сумма операции"] < 0:
                    sum_operation += comparison_meaning["Сумма операции"]
                    out[carrd_number] = sum_operation

    for i, value in enumerate(out):
        if value != "nan":
            result.append(
                {
                    "last_digits": value,
                    "total_spent": round(out[value], 2),
                    "cashback": round(((out[value] * -1) / 100), 2),
                }
            )

    return result
