import requests
from datetime import datetime, timedelta

from app.config import Config as config
from app.core.stocks.domain.stocks_service import ExternalStockService
from app.core.utils.scraper import scrape_performance


class StockService(ExternalStockService):
    def fetch_stock_data(self, symbol: str):
        api_key = config.API_KEY
        base_url = config.POLYGON_API_BASE
        date = (datetime.now() - timedelta(days=1)).strftime("%Y-%m-%d")

        url = f"{base_url}/v1/open-close/{symbol.upper()}/{date}?adjusted=true&apiKey={api_key}"
        response = requests.get(url)
        response.raise_for_status()
        stock_data = response.json()

        performance = scrape_performance(symbol)

        return {
            "after_hours": stock_data.get("afterHours"),
            "close": stock_data.get("close"),
            "date": stock_data.get("from"),
            "high": stock_data.get("high"),
            "low": stock_data.get("low"),
            "open_price": stock_data.get("open"),
            "pre_market": stock_data.get("preMarket"),
            "status": stock_data.get("status"),
            "symbol": stock_data.get("symbol"),
            "volume": int(stock_data.get("volume", 0)),
            "performance": performance
        }
