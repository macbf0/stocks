from app.core.stocks.domain.stocks import Stock


class UpdateStockAmount:
    def __init__(self, stock_repository):
        self.stock_repository = stock_repository

    def execute(self, symbol: str, amount: int):
        stock = self.stock_repository.get_stock(symbol)
        if not stock:
            raise ValueError(f"Stock {symbol} not found.")
        
        new_stock = Stock(
            symbol=stock.symbol,
            after_hours=stock.after_hours,
            close=stock.close,
            date=stock.date,
            high=stock.high,
            low=stock.low,
            open_price=stock.open_price,
            pre_market=stock.pre_market,
            status=stock.status,
            volume=stock.volume,
            performance=stock.performance,
            amount=stock.amount + amount
        )


        stock_return = self.stock_repository.save_stock(new_stock)

        return stock_return.to_dict()
