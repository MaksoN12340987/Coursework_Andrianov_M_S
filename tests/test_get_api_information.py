from unittest.mock import patch

import pytest

from src.get_api_information import get_stock_price_from_api


@patch("requests.get")
def test_get_stock_price_from_api_default(mock_api, return_api_defolt_setings):
    mock_api.return_value.json.return_value = return_api_defolt_setings
    assert str(type(get_stock_price_from_api())) == "<class 'float'>"
    mock_api.assert_called()


@patch("requests.get")
def test_get_stock_price_from_api_uncorrect_url(mock_api, return_api_url_uncorrect):
    mock_api.return_value.json.return_value = return_api_url_uncorrect
    with pytest.raises(Exception):
        assert (
            str(type(get_stock_price_from_api(0, "https://www.alphavantage.co")))
            == "Error, invalid data or not correct url"
        )
    mock_api.assert_called()
