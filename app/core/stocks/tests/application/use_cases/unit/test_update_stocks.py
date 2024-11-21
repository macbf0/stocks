import pytest

from app.core.stocks.application.use_cases.update_stocks import (
    UpdateStockAmount
)
from app.core.stocks.domain.stocks import Stock
from app.flask_project.blueprints.stocks.models import Stock as ORMStock
from unittest.mock import MagicMock

@pytest.fixture
def stock_repository_mock():
    return MagicMock()

def test_execute_with_existing_stock(stock_repository_mock: MagicMock):
    symbol = "AAPL"
    amount_to_add = 50

    stock_repository_mock.get_stock.return_value = ORMStock(
        id=1,
        symbol=symbol,
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
        amount=100
    )

    updated_stock = ORMStock(
        id=1,
        symbol=symbol,
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
        amount=150
    )
    
    stock_repository_mock.save_stock.return_value = updated_stock

    update_stock_use_case = UpdateStockAmount(stock_repository_mock)
    result = update_stock_use_case.execute(symbol, amount_to_add)

    stock_repository_mock.get_stock.assert_called_once_with(symbol)
    stock_repository_mock.save_stock.assert_called_once()

    assert result["symbol"] == symbol
    assert result["amount"] == 150

def test_execute_with_non_existing_stock(stock_repository_mock: MagicMock):
    symbol = "GOOG"
    amount_to_add = 50

    stock_repository_mock.get_stock.return_value = None

    update_stock_use_case = UpdateStockAmount(stock_repository_mock)

    with pytest.raises(ValueError, match=f"Stock {symbol} not found."):
        update_stock_use_case.execute(symbol, amount_to_add)

    stock_repository_mock.get_stock.assert_called_once_with(symbol)
    stock_repository_mock.save_stock.assert_not_called()
