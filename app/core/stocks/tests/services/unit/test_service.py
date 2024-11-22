import pytest
import requests
from unittest.mock import patch, MagicMock

from app.core.stocks.services.service import StockService
from app.config.config import Config as config


@pytest.fixture
def stock_service():
    return StockService()


@patch("app.core.stocks.services.service.requests.get")
@patch("app.core.stocks.services.service.scrape_performance")
def test_fetch_stock_data_success(
    mock_scrape_performance,
    mock_requests_get,
    stock_service
):
    symbol = "AAPL"
    api_response = {
        "afterHours": 150.0,
        "close": 148.0,
        "from": "2024-11-21",
        "high": 152.0,
        "low": 147.0,
        "open": 149.0,
        "preMarket": 149.5,
        "status": "success",
        "symbol": symbol,
        "volume": 1000000
    }
    performance_data = {
        "5 Day": "0.72%",
        "1 Month": "-1.74%",
        "3 Month": "0.15%",
        "YTD": "17.77%",
        "1 Year": "18.52%"
    }

    mock_requests_get.return_value.json.return_value = api_response
    mock_requests_get.return_value.raise_for_status = MagicMock()
    mock_scrape_performance.return_value = performance_data

    result = stock_service.fetch_stock_data(symbol)

    mock_requests_get.assert_called_once_with(
        f"{config.POLYGON_API_BASE}/v1/open-close/{symbol}/2024-11-21?adjusted=true&apiKey={config.API_KEY}"
    )
    mock_scrape_performance.assert_called_once_with(symbol)

    assert result["symbol"] == symbol
    assert result["after_hours"] == 150.0
    assert result["performance"] == performance_data
    assert result["volume"] == 1000000

@patch("app.core.stocks.services.service.requests.get")
def test_fetch_stock_data_api_failure(mock_requests_get, stock_service):
    symbol = "AAPL"
    mock_requests_get.side_effect = requests.exceptions.HTTPError("API error")

    with pytest.raises(requests.exceptions.HTTPError):
        stock_service.fetch_stock_data(symbol)

@patch("app.core.stocks.services.service.requests.get")
@patch("app.core.stocks.services.service.scrape_performance")
def test_fetch_stock_data_scrape_failure(
    mock_scrape_performance,
    mock_requests_get,
    stock_service
):
    symbol = "AAPL"
    api_response = {
        "afterHours": 150.0,
        "close": 148.0,
        "from": "2024-11-21",
        "high": 152.0,
        "low": 147.0,
        "open": 149.0,
        "preMarket": 149.5,
        "status": "success",
        "symbol": symbol,
        "volume": 1000000
    }

    mock_requests_get.return_value.json.return_value = api_response
    mock_requests_get.return_value.raise_for_status = MagicMock()
    mock_scrape_performance.side_effect = ValueError("Erro no scraper")

    with pytest.raises(ValueError, match="Erro no scraper"):
        stock_service.fetch_stock_data(symbol)

    mock_requests_get.assert_called_once()
    mock_scrape_performance.assert_called_once_with(symbol)
