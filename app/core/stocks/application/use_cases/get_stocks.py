from app.core.stocks.domain.stocks import Stock
from app.core.stocks.services.service import StockService


class GetStockData:
    def __init__(self, stock_repository):
        self.stock_repository = stock_repository

    def _build_stock(self, stock_data, amount=0):
        return Stock(
            after_hours=stock_data.get("after_hours"),
            close=stock_data.get("close"),
            date=stock_data.get("date"),
            high=stock_data.get("high"),
            low=stock_data.get("low"),
            open_price=stock_data.get("open_price"),
            pre_market=stock_data.get("pre_market"),
            status=stock_data.get("status"),
            symbol=stock_data.get("symbol"),
            volume=int(stock_data.get("volume", 0)),
            performance=stock_data.get("performance"),
            amount=amount
        )

    def execute(self, symbol: str):
        stock = self.stock_repository.get_stock(symbol)
        stock_data = StockService().fetch_stock_data(symbol)
        
        if not stock:
            stock_domain = self._build_stock(stock_data)
        else:
            stock_domain = self._build_stock(stock_data, stock.amount)

        stock = self.stock_repository.save_stock(stock_domain)
        return stock.to_dict()
