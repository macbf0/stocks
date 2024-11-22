from flask import Blueprint, jsonify, request

from app.flask_project.cache import cache
from app.flask_project.blueprints.stocks.repositories import StockRepository
from app.core.stocks.application.use_cases.get_stocks import GetStockData
from app.core.stocks.application.use_cases.update_stocks import UpdateStockAmount

stock_blueprint = Blueprint("stocks", __name__)

stock_repo = StockRepository()

@stock_blueprint.route("/<symbol>", methods=["GET"])
@cache.memoize(timeout=300)
def get_stock(symbol):
    use_case = GetStockData(stock_repo)
    stock = use_case.execute(symbol)
    return jsonify(stock)

@stock_blueprint.route("/<symbol>", methods=["POST"])
def update_stock(symbol):
    data = request.get_json()
    amount = data.get("amount", 0)

    use_case = UpdateStockAmount(stock_repo)
    stock = use_case.execute(symbol, amount)
    return jsonify(
        {"message": f"{amount} units of stock {symbol} were added to your stock record"}
    )
