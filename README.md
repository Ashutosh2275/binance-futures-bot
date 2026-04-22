# Binance Futures Testnet Trading Bot

Minimal Python CLI bot to place Binance USDT-M Futures Testnet orders.

The bot supports:
- BUY and SELL sides
- MARKET orders
- LIMIT orders (GTC)

## Features

- Validates order inputs before sending requests
- Uses Binance Futures Testnet credentials from environment variables
- Prints clear request/response output in the terminal
- Writes logs to logs/bot.log
- Handles validation, API, and network errors with readable messages

## Project Structure

```text
trading_bot/
  bot/
    __init__.py
    client.py
    logging_config.py
    orders.py
    validators.py
  logs/
  cli.py
  README.md
  requirements.txt
```

## Requirements

- Python 3.10 or newer
- Binance Futures Testnet API key and secret

## Installation

1. Open a terminal in the project folder.
2. Create and activate a virtual environment (recommended).
3. Install dependencies:

```bash
pip install -r requirements.txt
```

## Environment Variables

Create a .env file in the project root with:

```env
BINANCE_API_KEY=your_testnet_api_key
BINANCE_API_SECRET=your_testnet_api_secret
```

The bot loads these values automatically using python-dotenv.

## Usage

Run from the project folder:

```bash
python cli.py --symbol SYMBOL --side BUY_OR_SELL --type MARKET_OR_LIMIT --quantity QTY [--price PRICE]
```

### Market order example

```bash
python cli.py --symbol BTCUSDT --side BUY --type MARKET --quantity 0.001
```

### Limit order example

```bash
python cli.py --symbol BTCUSDT --side SELL --type LIMIT --quantity 0.001 --price 70000
```

Notes:
- --price is required only for LIMIT orders
- --quantity must be greater than 0

## Example Output

```text
===== ORDER REQUEST =====
Symbol: BTCUSDT
Side: BUY
Type: MARKET
Quantity: 0.001

===== RESPONSE =====
Order ID: 123456789
Status: FILLED
Executed Qty: 0.001
Avg Price: 68250.1

Result: SUCCESS
```

On failures, the bot prints a clear error and ends with:

```text
Result: FAILED
```

## Logging

All runtime logs are written to:

- logs/bot.log

Logged events include:
- Request parameters
- Binance API responses
- Validation, API, network, and unexpected errors

## Disclaimer

This project is for educational and testnet use. Do not use it as-is for live trading without additional risk controls, safeguards, and testing.
