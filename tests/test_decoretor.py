import sys
from src.decoretor import decorator_for_output_to_console_file


@decorator_for_output_to_console_file("out.py")
def function_decorator_testing_to_file():
    return [
        {
            "greeting": "Добрый вечер",
            "currency_rates": [{"currency": "USD", "price": "99.616325"}, {"currency": "EUR", "price": "99.616325"}],
            "stock_prices": [
                {"stock": "AAPL", "price": "228.8500"},
                {"stock": "AMZN", "price": "228.8500"},
                {"stock": "GOOGL", "price": "228.8500"},
                {"stock": "MSFT", "price": "228.8500"},
                {"stock": "TSLA", "price": "228.8500"},
            ],
        }
    ]


@decorator_for_output_to_console_file("")
def function_decorator_testing_to_console():
    return [
        {
            "greeting": "Добрый вечер",
            "currency_rates": [{"currency": "USD", "price": "99.616325"}, {"currency": "EUR", "price": "99.616325"}],
            "stock_prices": [
                {"stock": "AAPL", "price": "228.8500"},
                {"stock": "AMZN", "price": "228.8500"},
                {"stock": "GOOGL", "price": "228.8500"},
                {"stock": "MSFT", "price": "228.8500"},
                {"stock": "TSLA", "price": "228.8500"},
            ],
        }
    ]


def test_function_decorator_testing_to_file_stdout(capsys):
    function_decorator_testing_to_file()
    captured = capsys.readouterr()
    assert captured.out == """I output the result of the work to a file: "out.py"\n"""


def test_function_decorator_testing_to_console(capsys):
    function_decorator_testing_to_console()
    captured = capsys.readouterr()
    assert captured.out == (
        "Start function function_decorator_testing_to_console\n"
        + "[{'greeting': 'Добрый вечер', 'currency_rates': [{'currency': 'USD', 'price': '99.616325'}, "
        + "{'currency': 'EUR', 'price': '99.616325'}], 'stock_prices': [{'stock': 'AAPL', 'price': '228.8500'}, "
        + "{'stock': 'AMZN', 'price': '228.8500'}, {'stock': 'GOOGL', 'price': '228.8500'}, "
        + "{'stock': 'MSFT', 'price': '228.8500'}, {'stock': 'TSLA', 'price': '228.8500'}]}]\n"
        + "The function has completed\n"
    )
