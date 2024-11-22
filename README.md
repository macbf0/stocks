# Stock API

This API is developed to fetch stock data from an external financial API and perform data scraping from the Marketwatch website. It exposes two main endpoints that provide stock information and allow registering the purchased amounts of stocks.

## Technologies Used

- **Python 3.10+**
- **Flask** - Framework for building the REST API.
- **SQLAlchemy** - ORM for data persistence in the database.
- **Polygon.io API** - For retrieving stock data.
- **BeautifulSoup** - For scraping data from Marketwatch.
- **SQLite/PostgreSQL** - For data persistence.
- **Docker** - For containerizing the application.

## Endpoints

The API exposes two main endpoints related to the `Stock` resource:

### 1. **GET `/stock/{stock_symbol}`**
- **Description:** Returns data for a specific stock, such as the closing price, volume, performance, and other attributes.
- **Parameters:**
  - `stock_symbol`: The symbol of the stock (e.g., `AAPL` for Apple).
- **Response:**
  - A JSON object containing all the fields of the `Stock` model, such as:
    ```json
    {
      "symbol": "AAPL",
      "afterHours": 145.60,
      "close": 145.32,
      "from": "Polygon.io",
      "high": 146.25,
      "low": 144.85,
      "open": 145.10,
      "preMarket": 144.90,
      "status": "active",
      "volume": 200000,
      "performance": {"5 Day": "0.72%", "1 Month": "-1.74%", "3 Month": "0.15%", "YTD": "17.77%", "1 Year": "18.52%"},
      "amount": 0
    }
    ```
- **Additional Functionality:**
  - The response is cached to avoid fetching the data again in short intervals.

### 2. **POST `/stock/{stock_symbol}`**
- **Description:** Updates the amount of purchased stock for the given symbol.
- **Parameters:**
  - A JSON body containing the `amount` key, which represents the number of stocks purchased.
    ```json
    {
      "amount": 5
    }
    ```
- **Response:**
  - Status 201 with a message indicating the number of stocks added:
    ```json
    {
      "message": "5 units of stock AAPL were added to your stock record"
    }
    ```
- **Additional Functionality:**
  - The purchased amount is persisted in the database (SQLite or PostgreSQL).

## Requirements

- **Stock Model:**
  The `Stock` class contains the following fields, all fetched from the Polygon.io API and the Marketwatch scraping:
  
  - `afterHours`: float
  - `close`: float
  - `from`: str
  - `high`: float
  - `low`: float
  - `open`: float
  - `preMarket`: float
  - `status`: str
  - `symbol`: str
  - `volume`: int
  - `performance`: dict
  - `amount`: int (user input, default value is 0)

- **Database:**
  The database stores stocks and their purchased amounts. The POST `/stock/{stock_symbol}` route persists the purchase transactions.

## Setup and Running

### Step 1: Clone the Repository

Clone the repository to your local environment:

git clone https://github.com/macbf0/stocks.git


### Step 2: You can create a Docker image to run the application in a container

docker build -t stock_api .
docker run -p 8000:8000 stock_api

## Testing

The application includes unit tests to ensure the implementation is correct:

pytest -v

## How the api Works

- Data Fetching Process
  - When a user makes a GET request to /stock/{stock_symbol}, the API retrieves stock data from two sources:
  - Polygon.io API: For financial data (close price, volume, etc.).
  - Marketwatch: For scraping additional performance data.
  - The data from these sources is combined and returned to the user.

- Data Persistence
  - When a user makes a POST request to /stock/{stock_symbol}, the purchased amount of stock is persisted in the database. The purchased amount is associated with the stock symbol and can be queried later.

- Caching
  - Stock data is stored in cache to avoid frequent external API calls, improving the performance of the application.

- Final Considerations
  - The API is built following good software architecture practices.
  - Caching and persistence mechanisms ensure the application is scalable and efficient.
  - Dockerization allows for easy execution and distribution of the application.
