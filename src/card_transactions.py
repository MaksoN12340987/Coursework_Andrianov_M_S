# This is where the functions that process operations on the card are located.
from utils import conversion_xlsx_to_object


def make_a_top_transaction(array_of_operations: list[dict] = [{}]) -> list[dict]:
    result = []
    for i, value in enumerate(array_of_operations):
        try:
            result.append(
                {
                "date": value["Дата платежа"],
                "amount": value["Сумма операции"],
                "category": value["Дата платежа"],
                "description": value["Дата платежа"],
            }
        )
        except Exception:
            pass

    return result


print(make_a_top_transaction())
