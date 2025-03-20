# Obtaining stock price data
import logging
import os

import requests
from dotenv import load_dotenv  # type: ignore

logger_get_api = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_get_api.addHandler(file_handler)
logger_get_api.setLevel(logging.INFO)


def get_stock_price_from_api(
    user_stocks: str = "AAPL",
    url: str = "https://www.alphavantage.co/query",
) -> dict:
    """Принимает на вход наименование кампании типа: "RUB"
    Возвращает число типа "float" - стоимость акций
    Также имеет 1 доп параметр:зне
    - url ссылка на апи

    Args:
        user_stocks (int, optional): _description_. Defaults to 0.
        url (_type_, optional): _description_. Defaults to "https://www.alphavantage.co/query".

    Raises:
        ValueError: _description_

    Returns:
        float: _description_
    """
    try:
        load_dotenv()
        api_key = os.getenv("API_KEY_alphavantage")
        payload = {
            "function": "TIME_SERIES_INTRADAY",
            "symbol": user_stocks,
            "interval": "60min",
            "apikey": f"{api_key}",
        }
        temp = requests.get(url, params=payload).json()

        logger_get_api.info(f"OUTPUT DATA:\n{temp}\n")
        keys_fime_series = list(temp["Time Series (60min)"])
        return {"stock": user_stocks, "price": temp["Time Series (60min)"][keys_fime_series[0]]["4. close"]}

    except Exception:
        logger_get_api.warning(f"ERROR:\n{temp.json()}\n")
        raise ValueError("Error, invalid data or not correct url")


def getting_exchange_rates(
    currency: str = "USD",
    default_currency: str = "RUB",
    url: str = "https://api.apilayer.com/exchangerates_data/latest",
) -> dict:
    """Принимает на вход наименование валюты "USD", цену которых необходимо получить
    Возвращает словарь {'currency' = 'валюта', 'price' : 'цена валюты'}
    Также имеет параметры:
    - default_currency желаемая валюта эквивалент стоимости единицы currency
    - url ссылка на апи

    Args:
        default_currency (str, optional): желаемая валюта Defaults to "RUB".
        url (_type_, optional): ссылка на апи. Defaults to "https://api.apilayer.com/exchangerates_data/latest".

    Exception:
        Exception: прерывание в случае

    Returns:
        dict: словарь {'currency' = 'валюта', 'price' : 'цена валюты'}
    """
    payload = {"symbols": f"{default_currency}", "base": f"{currency}"}

    try:
        load_dotenv()
        api_key = os.getenv("API_KEY_apilayer")
        headers = {"apikey": api_key}
        temp = requests.get(url, headers=headers, params=payload).json()["rates"]

        logger_get_api.info(f"OUTPUT DATA:\n{temp}\n")
        return {"currency": currency, "price": f"{float(temp["RUB"])}"}

    except Exception:
        logger_get_api.warning(f"ERROR:\n{payload}\n")
        raise ValueError("Error, invalid data or not correct url")
