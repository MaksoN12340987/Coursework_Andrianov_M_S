import datetime

from src.utils import (
    dataframe_from_file,
    conversion_json_to_object,
    conversion_xlsx_to_object,
    user_greeting,
    reply_to_main_page,
)


# Execution of the main block
def main():
    date_time_now = datetime.datetime.now()

    print(reply_to_main_page(date_time_now.strftime("%Y-%m-%d %H:%M:%S")))
    # dataframe_from_file()


if __name__ == "__main__":
    main()
