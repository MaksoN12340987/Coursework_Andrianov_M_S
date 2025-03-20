from unittest.mock import patch

import pytest

from src.get_api_information import get_stock_price_from_api, getting_exchange_rates


@patch("requests.get")
def test_get_stock_price_from_api_default(mock_api, return_api_stock_price_from_api_defolt_setings):
    mock_api.return_value.json.return_value = return_api_stock_price_from_api_defolt_setings
    assert get_stock_price_from_api() == {"stock": "AAPL", "price": "228.8500"}
    mock_api.assert_called()


@patch("requests.get")
def test_get_stock_price_from_api_uncorrect_url(mock_api, return_api_url_uncorrect):
    mock_api.return_value.json.return_value = return_api_url_uncorrect
    with pytest.raises(Exception):
        assert (
            str(type(get_stock_price_from_api("AAPL", "https://www.alphavantage.co")))
            == "Error, invalid data or not correct url"
        )
    mock_api.assert_called()


@patch("requests.get")
def test_getting_exchange_rates_default(mock_api, return_api_eur_rub_usd):
    mock_api.return_value.json.return_value = return_api_eur_rub_usd
    assert getting_exchange_rates() == {"currency": "USD", "price": "99.616325"}
    mock_api.assert_called()


@patch("requests.get")
def test_getting_exchange_rates_uncorrect_url(mock_api, return_api_url_uncorrect):
    mock_api.return_value.json.return_value = return_api_url_uncorrect
    with pytest.raises(Exception):
        assert (
            str(type(getting_exchange_rates("EUR", "https://www.alphavantage.co")))
            == "Error, invalid data or not correct url"
        )
    mock_api.assert_called()
