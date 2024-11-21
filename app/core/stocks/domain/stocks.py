import re

from dataclasses import dataclass


@dataclass
class Stock:
    symbol: str
    after_hours: float
    close: float
    date: str
    high: float
    low: float
    open_price: float
    pre_market: float
    status: str
    volume: int
    performance: dict
    amount: int = 0

    def __post_init__(self):
        self.validate()
    
    def validate(self):
        if not isinstance(self.symbol, str) or len(self.symbol) > 4:
            raise ValueError(
                "The symbol must be a string with a maximum of 4 characters"
            )

        float_fields = {
            "after_hours": self.after_hours,
            "close": self.close,
            "high": self.high,
            "low": self.low,
            "open_price": self.open_price,
            "pre_market": self.pre_market,
        }
        for field_name, value in float_fields.items():
            if not isinstance(value, (float, int)) or value < 0:
                raise ValueError(
                    f"The field {field_name} must be a non-negative number"
                )

        if not isinstance(self.status, str) or len(self.status) > 50:
            raise ValueError(
                "The status must be a string with a maximum of 50 characters"
            )

        if not isinstance(self.volume, int) or self.volume < 0:
            raise ValueError("The volume must be a non-negative integer")

        if not isinstance(self.performance, dict):
            raise ValueError("The 'performance' field must be a dictionary")

        if not isinstance(self.amount, int) or self.amount < 0:
            print(self.amount)
            raise ValueError(
                "The value of the 'amount' field must be a non-negative integer"
            )

        date_regex = r"^\d{4}-\d{2}-\d{2}$"
        if not isinstance(self.date, str) or not re.match(date_regex, self.date):
            raise ValueError("The date must be in the format 'YYYY-MM-DD'")
