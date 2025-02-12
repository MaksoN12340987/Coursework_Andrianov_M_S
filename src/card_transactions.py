# This is where the functions that process operations on the card are located.
import logging

logger_card_trans = logging.getLogger("card_transactions")
file_handler = logging.FileHandler("log/card_transactions.log", mode="w", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_card_trans.addHandler(file_handler)
logger_card_trans.setLevel(logging.INFO)


def make_a_top_transaction(operations_list=[{}], number_top_elements=5):
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
        items_amount = value["Сумма платежа"]
        if items_amount < 0:
            items_amount = items_amount * -1

        if len(result) != number_top_elements:
            for i, comparison_meaning in enumerate(operations_list):

                comparison = comparison_meaning["Сумма платежа"]
                if comparison < 0:
                    comparison = comparison * -1

                if items_amount < comparison:
                    items_amount = comparison
                    index_largest_element = i

            # result.append(operations_list[index_largest_element])
            result.append(
                {
                    "date": str(operations_list[index_largest_element]["Дата платежа"]),
                    "amount": operations_list[index_largest_element]["Сумма операции"],
                    "category": str(operations_list[index_largest_element]["Категория"]),
                    "description": str(operations_list[index_largest_element]["Описание"]),
                }
            )
            del operations_list[index_largest_element]
    return result


def make_a_card_list(operations_list=[{}]):
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
