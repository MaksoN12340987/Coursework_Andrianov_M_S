# Module of additional functions required for the operation of the "Home" page
import logging

import pandas as pd

logger_utils = logging.getLogger(__name__)
file_handler = logging.FileHandler(f"log/{__name__}.log", mode="a")
file_formatter = logging.Formatter(
    "\n%(asctime)s %(levelname)s %(name)s %(funcName)s %(lineno)d: \n%(message)s", datefmt="%H:%M:%S %d-%m-%Y"
)
file_handler.setFormatter(file_formatter)
logger_utils.addHandler(file_handler)
logger_utils.setLevel(logging.INFO)


def conversion_xlsx_to_object(file_name=""):
    """Принимает на вход путь до файла xlsx, который читает и
    возвращает объект Python"""
    logger_utils.info("Get started conversion_json_to_object")
    try:
        with open(file_name, "rb") as f:
            return pd.read_excel(f).to_dict("records")

    except Exception:
        logger_utils.warning("Exceptional error, return []")
        return []
