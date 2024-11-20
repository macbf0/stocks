from abc import ABC, abstractmethod

from app.core.stocks.domain.stocks import Stock

class StockRepository(ABC):
    @abstractmethod
    def get_stock(self, symbol: str):
        raise NotImplementedError

    @abstractmethod
    def save_stock(self, stock: Stock):
        raise NotImplementedError
