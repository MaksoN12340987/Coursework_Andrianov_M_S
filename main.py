import datetime
import json

from src.utils import reply_to_main_page
from src.decoretor import decorator_for_output_to_console_file


# Execution of the main block
@decorator_for_output_to_console_file("report_main.json")
def main():
    date_time_now = datetime.datetime.now()

    return reply_to_main_page(date_time_now.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    main()
