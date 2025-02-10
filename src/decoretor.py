from functools import wraps


def log(error_mesage_type, filename: str = ""):
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
                with open(filename, "a") as file:
                    file.write(f"{function} ok\n")

            else:
                print("Start " + f"{function}"[1:-23])
                try:
                    resault = function(*args)
                    print(resault)
                    print("The function has completed")
                except Exception:
                    print(error_mesage_type)
            return resault

        return execution

    return decorator_time_name_error
