from app.database.database import db

class Stock(db.Model):
    __tablename__ = 'stocks'

    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), nullable=False)
    after_hours = db.Column(db.Float)
    close = db.Column(db.Float)
    date = db.Column(db.String)
    high = db.Column(db.Float)
    low = db.Column(db.Float)
    open_price = db.Column(db.Float)
    pre_market = db.Column(db.Float)
    status = db.Column(db.String(50))
    volume = db.Column(db.Integer)
    performance = db.Column(db.JSON)
    amount = db.Column(db.Integer, default=0)

    def to_dict(self):
        return {
            "id": self.id,
            "symbol": self.symbol,
            "after_hours": self.after_hours,
            "close": self.close,
            "date": self.date,
            "high": self.high,
            "low": self.low,
            "open_price": self.open_price,
            "pre_market": self.pre_market,
            "status": self.status,
            "volume": self.volume,
            "performance": self.performance,
            "amount": self.amount,
        }
