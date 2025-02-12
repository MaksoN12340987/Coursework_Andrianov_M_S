# Module of additional functions required for the operation of the "Home" page
import json
import logging

import pandas as pd

logger_utils = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_utils.addHandler(file_handler)
logger_utils.setLevel(logging.INFO)


def dataframe_from_file(file_name: str = "data/operations.xlsx") -> pd.DataFrame:
    try:
        with open(file_name, "rb") as f:
            return pd.read_excel(f)

    except Exception:
        raise Exception("Exceptional error")


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
