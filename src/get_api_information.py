# Obtaining stock price data
import os

import requests
from dotenv import load_dotenv


def conversion_from_usd_eur_in_rub(
    transaction_sum: int = 0,
    currency: str = "",
    url: str = "https://api.apilayer.com/exchangerates_data/convert",
    filename: str = "log/ex_api.log",
) -> float:
    """Принимает на вход наименование валюты типа: "RUB"
    Возвращает число типа "float" - стоимость акций
    Также имеет 1 доп параметр:зне
    - url ссылка на апи"""

    try:
        load_dotenv()
        api_key = os.getenv("API_KEY")
        headers = {"apikey": api_key}
        temp = requests.get(url, headers=headers, params=payload)
        with open(filename, "a") as file:
             file.write(f"OUTPUT DATA:\n{temp.json()["result"]}\n")
        return float(temp.json()["result"])
    except Exception:
        with open(filename, "a") as file:
            file.write(f"ERROR:\n{temp.json()}\n")
        raise ValueError("Error, invalid data or not correct url")
