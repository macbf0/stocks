import pytest
from app.core.stocks.domain.stocks import Stock


class TestStock:
    def test_symbol_valid(self):
        stock = Stock(
            symbol="NFLX",
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
        assert stock.symbol == "NFLX"

    def test_symbol_invalid(self):
        with pytest.raises(ValueError):
            Stock(
                symbol="GOOGLE",
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

    def test_float_field_valid(self):
        stock = Stock(
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
            amount=100
        )
        assert stock.after_hours == 150.0

    def test_float_field_invalid(self):
        with pytest.raises(ValueError):
            Stock(
                symbol="AAPL",
                after_hours=-150.0,
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

    def test_status_valid(self):
        stock = Stock(
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
            amount=100
        )
        assert stock.status == "active"

    def test_status_invalid(self):
        with pytest.raises(ValueError):
            Stock(
                symbol="AAPL",
                after_hours=150.0,
                close=148.0,
                date="2024-11-21",
                high=152.0,
                low=147.0,
                open_price=149.0,
                pre_market=149.5,
                status="a" * 51,
                volume=1000000,
                performance={"change": 2.5},
                amount=100
            )

    def test_volume_valid(self):
        stock = Stock(
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
            amount=100
        )
        assert stock.volume == 1000000  # Volume válido

    def test_volume_invalid(self):
        with pytest.raises(ValueError):
            Stock(
                symbol="AAPL",
                after_hours=150.0,
                close=148.0,
                date="2024-11-21",
                high=152.0,
                low=147.0,
                open_price=149.0,
                pre_market=149.5,
                status="active",
                volume=-1000000,  # Volume negativo
                performance={"change": 2.5},
                amount=100
            )

    def test_performance_valid(self):
        stock = Stock(
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
            amount=100
        )
        assert isinstance(stock.performance, dict)

    def test_performance_invalid(self):
        with pytest.raises(ValueError):
            Stock(
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
                performance=[],
                amount=100
            )

    def test_amount_valid(self):
        stock = Stock(
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
            amount=100
        )
        assert stock.amount == 100

    def test_amount_invalid(self):
        with pytest.raises(ValueError):
            Stock(
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
                amount=-10
            )

    # Testando a validação da data
    def test_date_valid(self):
        stock = Stock(
            symbol="AAPL",
            after_hours=150.0,
            close=148.0,
            date="2024-11-21",
            high=152.0,
            low=147.0,
            open_price=149.0,
            pre_market=149.1495,
            status="active",
            volume=1000000,
            performance={"change": 2.5},
            amount=100
        )
        assert stock.date == "2024-11-21"

    def test_date_invalid(self):
        with pytest.raises(ValueError):
            Stock(
                symbol="AAPL",
                after_hours=150.0,
                close=148.0,
                date="11-01-2024",
                high=152.0,
                low=147.0,
                open_price=149.0,
                pre_market=149.1495,
                status="active",
                volume=1000000,
                performance={"change": 2.5},
                amount=100
            )

