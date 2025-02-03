# Obtaining stock price data
import os

import requests
import logging
from utils import conversion_json_to_object
from dotenv import load_dotenv


logger_get_api = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_get_api.addHandler(file_handler)
logger_get_api.setLevel(logging.INFO)


def conversion_from_usd_eur_in_rub(
    user_stocks: int = 0,
    url: str = "https://www.alphavantage.co/query",
) -> float:
    """Принимает на вход наименование валюты типа: "RUB"
    Возвращает число типа "float" - стоимость акций
    Также имеет 1 доп параметр:зне
    - url ссылка на апи"""
    data = conversion_json_to_object("user_settings.json")

    try:
        load_dotenv()
        api_key = os.getenv("API_KEY")
        payload = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": f"{data["user_stocks"][user_stocks]}",
            "interval": "60min",
            "apikey": api_key,
        }
        temp = requests.get(url, params=payload)

        logger_get_api.info(f"OUTPUT DATA:\n{temp.json()}\n")
        return temp.json()

    except Exception:
        logger_get_api.warning(f"ERROR:\n{temp.json()}\n")
        raise ValueError("Error, invalid data or not correct url")


print(conversion_from_usd_eur_in_rub())
