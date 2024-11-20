from dataclasses import dataclass
from datetime import date


@dataclass
class Stock:
    symbol: str
    after_hours: str
    close: str
    date: str
    high: str
    low: str
    open_price: str
    pre_market: str
    status: str
    volume: str
    performance: str
    amount: int = 0

    def __post_init__(self):
        self.validate()
    
    def validate(self):
        pass
