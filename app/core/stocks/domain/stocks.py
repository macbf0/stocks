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
        if not isinstance(self.symbol, str) or len(self.symbol) > 10:
            raise ValueError("O símbolo deve ser uma string com no máximo 10 caracteres.")

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
                raise ValueError(f"O campo {field_name} deve ser um número não negativo.")

        if not isinstance(self.status, str) or len(self.status) > 50:
            raise ValueError("O status deve ser uma string com no máximo 50 caracteres.")

        if not isinstance(self.volume, int) or self.volume < 0:
            raise ValueError("O volume deve ser um número inteiro não negativo.")

        if not isinstance(self.performance, dict):
            raise ValueError("O campo 'performance' deve ser um dicionário.")

        if not isinstance(self.amount, int):
            print(self.amount)
            raise ValueError("O valor do campo 'amount' deve ser um inteiro não negativo.")

        date_regex = r"^\d{4}-\d{2}-\d{2}$"
        if not isinstance(self.date, str) or not re.match(date_regex, self.date):
            raise ValueError("A data deve estar no formato 'YYYY-MM-DD'.")
