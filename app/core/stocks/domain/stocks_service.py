from abc import ABC, abstractmethod

class ExternalStockService(ABC):
    @abstractmethod
    def fetch_stock_data(self, symbol: str):
        pass
