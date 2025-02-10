# Additional services module
import re

from utils import conversion_xlsx_to_object


def favorable_categories_increased_cashback(
    bank_operations: list[dict] = [], reversed: bool = True, coll: int = 3
) -> list:
    out = {}
    result = {}

    for i, value in enumerate(bank_operations):
        name_category = value["Категория"]
        sum_operation = 0.00

        for count, comparison_meaning in enumerate(bank_operations):
            if name_category == str(comparison_meaning["Категория"]):
                sum_operation += comparison_meaning["Бонусы (включая кэшбэк)"]
                out[name_category] = sum_operation

    time = {k: v for k, v in sorted(out.items(), key=lambda item: item[1], reverse=reversed)}
    for i, value in enumerate(time):
        if i < coll:
            result[value] = time[value]
    return result
