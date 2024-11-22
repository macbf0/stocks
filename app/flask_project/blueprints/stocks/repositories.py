from app.core.stocks.domain.stocks_repository import StockRepository
from app.database.database import db
from app.flask_project.blueprints.stocks.models import Stock

class StockRepository(StockRepository):
    def get_stock(self, symbol: str):
        teste = Stock.query.filter_by(symbol=symbol.upper()).order_by(Stock.id.desc()).first()
        return teste

    def save_stock(self, stock):
        stock_model = StockModelMapper.to_model(stock)
        db.session.add(stock_model)
        db.session.commit()

        return stock_model

class StockModelMapper:
    @staticmethod
    def to_model(model: Stock) -> Stock:
        return Stock(
            after_hours=model.after_hours,
            close=model.close,
            date=model.date,
            high=model.high,
            low=model.low,
            open_price=model.open_price,
            pre_market=model.pre_market,
            status=model.status,
            symbol=model.symbol,
            volume=model.volume,
            performance=model.performance,
            amount=model.amount
        )