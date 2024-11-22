import os

class Config:

    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI', 'sqlite:///stocks.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    API_KEY = os.getenv('API_KEY', 'default_api_key')
    POLYGON_API_BASE = os.getenv('POLYGON_API_BASE', 'https://api.polygon.io')
    
    SECRET_KEY = os.getenv('SECRET_KEY', 'default_secret_key')
    DEBUG = os.getenv('DEBUG', 'True') == 'True'
