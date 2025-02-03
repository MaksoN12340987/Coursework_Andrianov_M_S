# Obtaining stock price data
import logging
import os

import requests
from dotenv import load_dotenv

from src.utils import conversion_json_to_object

logger_get_api = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_get_api.addHandler(file_handler)
logger_get_api.setLevel(logging.INFO)


def get_stock_price_from_api(
    user_stocks: int = 0,
    url: str = "https://www.alphavantage.co/query",
) -> float:
    """Принимает на вход наименование валюты типа: "RUB"
    Возвращает число типа "float" - стоимость акций
    Также имеет 1 доп параметр:зне
    - url ссылка на апи"""
    data = conversion_json_to_object("user_settings.json")
    result = 0.00

    try:
        load_dotenv()
        api_key = os.getenv("API_KEY_alphavantage")
        payload = {
            "symbol": f"{data["user_stocks"][user_stocks]}",
        }
        temp = requests.get(url, params=payload).json()

        logger_get_api.info(f"OUTPUT DATA:\n{temp}\n")
        keys_fime_series = list(temp["Time Series (60min)"])

        result = temp["Time Series (60min)"][keys_fime_series[0]]["4. close"]
        return float(result)

    except Exception:
        logger_get_api.warning(f"ERROR:\n{temp.json()}\n")
        raise ValueError("Error, invalid data or not correct url")


def conversion_from_usd_eur_in_rub(
    transaction_sum: int = 0,
    currency: str = "",
    url: str = "https://api.apilayer.com/exchangerates_data/convert",
) -> float:
    """Принимает на вход сумму в валюте и наименование валюты "RUB" или "USD"
    Возвращает число типа "float" - валюта, конвертированная в рубли
    Также имеет 1 доп параметр:
    - url ссылка на апи"""

    if currency == "USD" or currency == "EUR":
        payload = {"to": "RUB", "from": currency, "amount": str(transaction_sum)}

        try:
            load_dotenv()
            api_key = os.getenv("API_KEY_apilayer")
            headers = {"apikey": api_key}
            temp = requests.get(url, headers=headers, params=payload).json()
            
            logger_get_api.info(f"OUTPUT DATA:\n{temp}\n")
            return float(temp["result"])

        except Exception:
            logger_get_api.warning(f"ERROR:\n{payload}\n")
            raise ValueError("Error, invalid data or not correct url")
    else:
        logger_get_api.warning(f"ERROR:\n{payload}\n")
        raise ValueError('''Укажите валюту в нужном формате "USD" или "EUR"''')
