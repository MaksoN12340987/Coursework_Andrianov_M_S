import datetime

from src.views import reply_to_main_page
from src.reports import spending_by_category
from src.services import favorable_categories_increased_cashback
from src.utils import conversion_xlsx_to_object, dataframe_from_file


# Execution of the main block
def main():
    date_time_now = datetime.datetime.now()
    xlsx_data = conversion_xlsx_to_object()
    xlsx_dataframe = dataframe_from_file()

    choice = True
    while choice:
        user_selection_program = input(
            """      Привет!
            Вот, что я могу:
            1. Сформировать JSON-ответ для страницы "Главная"
            2. Показать выгодные категории повышенного кешбэка
            из xlsx отчета ваших трат
            3. Сформировать отчет трат по категориям

            Введите "1", "2" или "3", для выбора соответствующего
            пункта, или нажмите любую клавишу для продолжения
            """
        )
        try:
            triger_apruve = False
            if user_selection_program == "1":
                result = reply_to_main_page(date_time_now.strftime("%Y-%m-%d %H:%M:%S"))
                triger_apruve = True

            elif user_selection_program == "2":
                user_coll = input("Введите количество категорий для вывода:\n")
                result = favorable_categories_increased_cashback(xlsx_data, int(user_coll))
                triger_apruve = True

            elif user_selection_program == "3":
                user_category = input("Введите название категории:\n")
                result = spending_by_category(xlsx_dataframe, user_category)
                triger_apruve = True

            if triger_apruve:
                print(result)
        except Exception:
            print("Хм, что-то пошло не так(")

        triger = input(
            """
        Хотите вернуться в главное меню?
        Введите "да", оставьте поле пустым если желаете завершить работу
        """
        ).lower()

        if triger == "да":
            pass
        else:
            choice = False


if __name__ == "__main__":
    main()
