from flask import Flask
from dotenv import load_dotenv

from app.flask_project.cache import cache
from app.database.database import db
from app.flask_project.blueprints.stocks.routes import stock_blueprint


def load_environment():
    """Load environment variables."""
    load_dotenv()


def initialize_cache(app):
    """Initialize cache for the Flask app."""
    app.config['CACHE_TYPE'] = 'SimpleCache'
    cache.init_app(app)


def initialize_database(app):
    """Initialize the database for the Flask app."""
    db.init_app(app)
    with app.app_context():
        db.create_all()


def register_blueprints(app):
    """Register all blueprints for the Flask app."""
    app.register_blueprint(stock_blueprint, url_prefix="/api/v1/stocks")


def create_app():
    """Create and configure the Flask application."""
    load_environment()

    app = Flask(__name__)
    app.config.from_object("app.config.config.Config")

    initialize_cache(app)
    initialize_database(app)
    register_blueprints(app)

    return app
