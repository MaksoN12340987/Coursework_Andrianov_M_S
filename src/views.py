import json
import logging

from src.card_transactions import make_a_card_list, make_a_top_transaction
from src.get_api_information import get_stock_price_from_api, getting_exchange_rates
from src.utils import conversion_json_to_object, conversion_xlsx_to_object, user_greeting

logger_utils = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="w", encoding="UTF8")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_utils.addHandler(file_handler)
logger_utils.setLevel(logging.INFO)


# Functional module of the page "Home"
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
        "top_transactions": [make_a_top_transaction(result_xlsx)],
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
    return json.dumps([json_response], ensure_ascii=False)
    # return [
    #     {
    #         "greeting": "Доброй ночи",
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
    #         "currency_rates": [{"currency": "USD", "price": "93.998672"}, {"currency": "EUR", "price": "97.700485"}],
    #         "stock_prices": [
    #             {"stock": "AAPL", "price": "232.8100"},
    #             {"stock": "AMZN", "price": "232.7700"},
    #             {"stock": "GOOGL", "price": "185.2500"},
    #             {"stock": "MSFT", "price": "411.3050"},
    #             {"stock": "TSLA", "price": "326.7500"},
    #         ],
    #     }
    # ]
