# Module of additional functions required for the operation of the "Home" page
import json
import logging

import pandas as pd

from get_api_information import get_stock_price_from_api, getting_exchange_rates

logger_utils = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_utils.addHandler(file_handler)
logger_utils.setLevel(logging.INFO)


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
    time = 1000000 + int(time_now.replace(":", ""))
    print(time)
    if time >= 1050000 and time < 1120000:
        result = "Доброе утро"
    elif time >= 1120000 and time < 1180000:
        result = "Добрый день"
    elif time >= 1180000 and time < 1220000:
        result = "Добрый вечер"
    else:
        result = "Доброй ночи"
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
    json_response = {"greeting": "", "cards": [], "top_transactions": [], "currency_rates": [], "stock_prices": []}
    json_response["greeting"] = user_greeting(time_now[10:])

    temp = []
    for i, value in enumerate(conversion_json_to_object("user_settings.json")["user_currencies"]):
        temp.append((getting_exchange_rates(value)))

    json_response["currency_rates"] = temp

    temp = []
    for i, value in enumerate(conversion_json_to_object("user_settings.json")["user_stocks"]):
        temp.append((get_stock_price_from_api(value)))

    json_response["stock_prices"] = temp
    return json_response
