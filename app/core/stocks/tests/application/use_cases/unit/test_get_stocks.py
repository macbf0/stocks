from typing import Any
import pytest
from unittest.mock import MagicMock, patch
from app.core.stocks.domain.stocks import Stock
from app.core.stocks.services.service import StockService
from app.core.stocks.application.use_cases.get_stocks import GetStockData
from app.flask_project.blueprints.stocks.models import Stock as ORMStock


@pytest.fixture
def stock_repository_mock():
    return MagicMock()


@pytest.fixture
def get_stock_data(stock_repository_mock: MagicMock):
    return GetStockData(stock_repository=stock_repository_mock)


def test_execute_with_existing_stock(stock_repository_mock: MagicMock):
    stock_repository_mock.get_stock.return_value = MagicMock(
        symbol="AAPL",
        amount=50
    )

    stock_repository_mock.save_stock.return_value = ORMStock(
        id=1,
        symbol="AAPL",
        after_hours=150.0,
        close=148.0,
        date="2024-11-21",
        high=152.0,
        low=147.0,
        open_price=149.0,
        pre_market=149.5,
        status="active",
        volume=1000000,
        performance={"change": 2.5},
        amount=50
    )

    result = GetStockData(stock_repository_mock).execute("AAPL")

    assert result["symbol"] == "AAPL"
    assert result["amount"] == 50


def test_execute_with_non_existing_stock(
        get_stock_data: GetStockData,
        stock_repository_mock: MagicMock
):
    symbol = "GOOG"

    stock_repository_mock.get_stock.return_value = None

    stock_repository_mock.save_stock.return_value = ORMStock(
        id=2,
        symbol=symbol,
        after_hours=2800,
        close=2780,
        date="2024-11-21",
        high=2810,
        low=2775,
        open_price=2785,
        pre_market=2782,
        status="active",
        volume=1500000,
        performance={},
        amount=0
    )

    result = get_stock_data.execute(symbol)

    # Verificações
    stock_repository_mock.get_stock.assert_called_once_with(symbol)
    stock_repository_mock.save_stock.assert_called_once()

    # Assertivas
    assert result["symbol"] == symbol
    assert result["amount"] == 0 


def test_build_stock_with_amount(get_stock_data: GetStockData):
    stock_data = {
        "after_hours": 2800,
        "close": 2780,
        "date": "2024-11-21",
        "high": 2810,
        "low": 2775,
        "open_price": 2785,
        "pre_market": 2782,
        "status": "active",
        "symbol": "GOOG",
        "volume": 1500000,
        "performance": {}
    }

    stock = get_stock_data._build_stock(stock_data, amount=10)

    assert stock.symbol == "GOOG"
    assert stock.amount == 10

def test_build_stock_without_amount(get_stock_data: GetStockData):
    stock_data = {
        "after_hours": 2800,
        "close": 2780,
        "date": "2024-11-21",
        "high": 2810,
        "low": 2775,
        "open_price": 2785,
        "pre_market": 2782,
        "status": "active",
        "symbol": "GOOG",
        "volume": 1500000,
        "performance": {}
    }

    stock = get_stock_data._build_stock(stock_data)

    assert stock.symbol == "GOOG"
    assert stock.amount == 0
