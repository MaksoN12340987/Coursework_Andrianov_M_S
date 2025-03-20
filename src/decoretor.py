import json
from functools import wraps


def decorator_for_output_to_console_file(filename: str = "", error_mesage_type: str = "Crinical exeption"):
    """Декоратор log принимает сообщение об ошибке и
    путь к файлу. В случае ошибки выводится сообщение error_mesage_type.
    Декоратор отмечает начало работы функции, выводит результат, в зависимости от наличия аргумента "filename" и
    сообщает об окончании работы

    Args:
        error_mesage_type (_type_): Сообщение о ошибке, вызванной в процессе работы
        filename (str, optional): путь к файлу, если требуется сохранить результат в файл. Defaults to "".
    """

    def decorator_time_name_error(function):
        @wraps(function)
        def execution(*args):
            if filename != "":
                resault = function(*args)
                print(f'''I output the result of the work to a file: "{filename}"''')
                try:
                    with open(filename, "w", encoding="UTF8") as file:
                        json.dump(resault, file, indent=4, ensure_ascii=False)
                except Exception:
                    with open(filename, "w", encoding="UTF8") as file:
                        file.write(f"{resault.to_dict("records")}")
            else:
                print("Start " + f"{function}"[1:-23])
                try:
                    resault = function(*args)
                    print(resault)
                    print("The function has completed")
                except Exception:
                    raise Exception(error_mesage_type)
            return resault

        return execution

    return decorator_time_name_error
