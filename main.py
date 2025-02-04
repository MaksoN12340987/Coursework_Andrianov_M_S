import datetime

from src.utils import reply_to_main_page


# Execution of the main block
def main():
    date_time_now = datetime.datetime.now()

    return reply_to_main_page(date_time_now.strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == "__main__":
    print(main())
