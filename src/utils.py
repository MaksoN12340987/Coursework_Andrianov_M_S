# Module of additional functions required for the operation of the "Home" page
import json
import logging

import pandas as pd

from src.card_transactions import array_of_transactions_for_top_selection, make_a_card_list, make_a_top_transaction
from src.get_api_information import get_stock_price_from_api, getting_exchange_rates


from src.decoretor import decorator_for_output_to_console_file


logger_utils = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_utils.addHandler(file_handler)
logger_utils.setLevel(logging.INFO)


# @decorator_for_output_to_console_file("out.py")
def dataframe_from_file(file_name: str = "data/operations.xlsx") -> pd.DataFrame:
    try:
        with open(file_name, "rb") as f:
            return pd.read_excel(f)

    except Exception:
        raise Exception(f"Exceptional error")


def conversion_xlsx_to_object(file_name: str = "data/operations.xlsx") -> list:
    """Принимает на вход путь до файла xlsx, который читает и
    возвращает объект Python"""
    logger_utils.info("Get started conversion_json_to_object")
    try:
        with open(file_name, "rb") as f:
            return pd.read_excel(f).to_dict("records")

    except Exception:
        logger_utils.warning("Exceptional error, return []")
        return []


def conversion_json_to_object(file_name: str = "") -> list:
    """Принимает на вход путь до файла .json, который читает и
    возвращает список"""
    logger_utils.info("Get started conversion_json_to_object")
    try:
        with open(file_name, "rb") as f:
            data_bank_operation = json.load(f)

    except Exception:
        logger_utils.warning("Exceptional error, return []")
        data_bank_operation = []

    return data_bank_operation


def user_greeting(time_now: str = "") -> str:
    try:
        time = 1000000 + int(time_now.replace(":", ""))
        if time >= 1050000 and time < 1120000:
            result = "Доброе утро"
        elif time >= 1120000 and time < 1180000:
            result = "Добрый день"
        elif time >= 1180000 and time < 1220000:
            result = "Добрый вечер"
        else:
            result = "Доброй ночи"
    except Exception:
        result = "Доброго времени суток"
    return result


def reply_to_main_page(time_now=""):
    """Функция генерирует словарь для дальнейшей конвертации в щбъект json
    на вход принимается DataFrame с текущей датой

    Словарь содержит приветствие пользователю, данные о банковских операциях по карте,
    курсы валют и стоимости акций кампаний, которые содержаться в модуле user_settings.json

    Args:
        time_now (str, optional): На вход принимается DataFrame  с текущей датой. Defaults to "".

    Returns:
        dict : сдоварь, подготовленный для конвертации в ответ json
    """
    result_xlsx = conversion_xlsx_to_object()
    logger_utils.info(f"{result_xlsx}")

    json_response = {
        "greeting": "",
        "cards": [make_a_card_list(result_xlsx)],
        "top_transactions": [make_a_top_transaction(array_of_transactions_for_top_selection(result_xlsx))],
        "currency_rates": [],
        "stock_prices": [],
    }
    json_response["greeting"] = user_greeting(time_now[10:])

    temp = []
    for i, value in enumerate(conversion_json_to_object("user_settings.json")["user_currencies"]):
        temp.append((getting_exchange_rates(value)))

    json_response["currency_rates"] = temp

    temp = []
    for i, value in enumerate(conversion_json_to_object("user_settings.json")["user_stocks"]):
        temp.append((get_stock_price_from_api(value)))

    json_response["stock_prices"] = temp
    return [json_response]
    # return [
    #     {
    #         "greeting": "Добрый вечер",
    #         "cards": [
    #             [
    #                 {"last_digits": "7197", "total_spent": -2389912.73, "cashback": 23899.13},
    #                 {"last_digits": "5091", "total_spent": -17367.5, "cashback": 173.68},
    #                 {"last_digits": "4556", "total_spent": -1768837.24, "cashback": 17688.37},
    #                 {"last_digits": "1112", "total_spent": -46207.08, "cashback": 462.07},
    #                 {"last_digits": "5507", "total_spent": -84000.0, "cashback": 840.0},
    #                 {"last_digits": "6002", "total_spent": -69200.0, "cashback": 692.0},
    #                 {"last_digits": "5441", "total_spent": -470854.8, "cashback": 4708.55},
    #             ]
    #         ],
    #         "top_transactions": [
    #             [
    #                 {
    #                     "date": "21.03.2019",
    #                     "amount": 190044.51,
    #                     "category": "Переводы",
    #                     "description": "Перевод Кредитная карта. ТП 10.2 RUR",
    #                 },
    #                 {
    #                     "date": "21.03.2019",
    #                     "amount": -190044.51,
    #                     "category": "Переводы",
    #                     "description": "Перевод Кредитная карта. ТП 10.2 RUR",
    #                 },
    #                 {
    #                     "date": "28.07.2018",
    #                     "amount": -179571.56,
    #                     "category": "nan",
    #                     "description": "Перевод средств с брокерского счета",
    #                 },
    #                 {
    #                     "date": "27.07.2018",
    #                     "amount": -179571.56,
    #                     "category": "nan",
    #                     "description": "Перевод средств с брокерского счета",
    #                 },
    #                 {
    #                     "date": "27.07.2018",
    #                     "amount": -179571.56,
    #                     "category": "nan",
    #                     "description": "Перевод средств с брокерского счета",
    #                 },
    #             ]
    #         ],
    #         "currency_rates": [{"currency": "USD", "price": "99.616325"}, {"currency": "EUR", "price": "99.616325"}],
    #         "stock_prices": [
    #             {"stock": "AAPL", "price": "228.8500"},
    #             {"stock": "AMZN", "price": "228.8500"},
    #             {"stock": "GOOGL", "price": "228.8500"},
    #             {"stock": "MSFT", "price": "228.8500"},
    #             {"stock": "TSLA", "price": "228.8500"},
    #         ],
    #     }
    # ]
