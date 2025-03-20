import datetime
from typing import Optional

import pandas as pd


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """_summary_

    Args:
        transactions (pd.DataFrame): _description_
        category (str): _description_
        date (Optional[str], optional): _description_. Defaults to None.

    Returns:
        pd.DataFrame: _description_
    """
    if date == None:
        date = datetime.datetime.now().strftime("%m.%Y")

    month_time = int(date[:2])
    year_time = int(date[3:])
    if month_time < 3:
        year = year_time - 1
        temp = 3 - month_time
        month = 12 - temp
    else:
        month = month_time
        year = year_time - 3
    day = 1
    hour = 00
    minute = 00
    second = 00
    date_start = datetime.datetime(year, month, day, hour, minute, second)

    result = {"Category": category, "Sum": 0.00}
    summ = 0.00
    i = 0
    for i, value in enumerate(transactions.to_dict("records")):
        try:
            if datetime.datetime.strptime(str(value["Дата операции"]), "%d.%m.%Y %H:%M:%S") > date_start:
                if value["Категория"] == category:
                    summ += value["Сумма платежа"]
        except Exception:
            pass

    result["Sum"] = round((summ * -1), 2)
    return pd.DataFrame([result])
