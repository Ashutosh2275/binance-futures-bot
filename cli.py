from __future__ import annotations

import argparse
import sys
from typing import Any

from binance.exceptions import BinanceAPIException, BinanceRequestException

from bot.client import get_client
from bot.logging_config import setup_logger
from bot.orders import place_order
from bot.validators import validate_order_inputs


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Place MARKET or LIMIT orders on Binance Futures Testnet (USDT-M)."
    )
    parser.add_argument("--symbol", required=True, help="Trading symbol, e.g. BTCUSDT")
    parser.add_argument("--side", required=True, help="Order side: BUY or SELL")
    parser.add_argument("--type", required=True, help="Order type: MARKET or LIMIT")
    parser.add_argument("--quantity", required=True, type=float, help="Order quantity")
    parser.add_argument("--price", type=float, help="Limit price (required for LIMIT)")
    return parser.parse_args()


def print_order_request(
    symbol: str, side: str, order_type: str, quantity: float, price: float | None
) -> None:
    print("===== ORDER REQUEST =====")
    print(f"Symbol: {symbol}")
    print(f"Side: {side}")
    print(f"Type: {order_type}")
    print(f"Quantity: {quantity}")
    if order_type == "LIMIT":
        print(f"Price: {price}")
    print()


def print_order_response(response: dict[str, Any]) -> None:
    avg_price = response.get("avgPrice") or response.get("price") or "N/A"
    print("===== RESPONSE =====")
    print(f"Order ID: {response.get('orderId', 'N/A')}")
    print(f"Status: {response.get('status', 'N/A')}")
    print(f"Executed Qty: {response.get('executedQty', 'N/A')}")
    print(f"Avg Price: {avg_price}")
    print()


def main() -> int:
    logger = setup_logger()

    try:
        args = parse_args()
        symbol = args.symbol.upper().strip()
        side = args.side.upper().strip()
        order_type = args.type.upper().strip()
        quantity = args.quantity
        price = args.price

        validate_order_inputs(symbol, side, order_type, quantity, price)

        logger.info(
            "Order request: symbol=%s side=%s type=%s quantity=%s price=%s",
            symbol,
            side,
            order_type,
            quantity,
            price,
        )

        print_order_request(symbol, side, order_type, quantity, price)

        client = get_client()
        response = place_order(
            client=client,
            symbol=symbol,
            side=side,
            order_type=order_type,
            quantity=quantity,
            price=price,
        )

        logger.info("API response: %s", response)
        print_order_response(response)
        print("Result: SUCCESS")
        return 0

    except ValueError as exc:
        logger.error("Validation error: %s", exc)
        print(f"Validation Error: {exc}")
        print("Result: FAILED")
        return 1
    except BinanceAPIException as exc:
        logger.error("Binance API error: %s", exc)
        print(f"Binance API Error: {exc}")
        print("Result: FAILED")
        return 1
    except BinanceRequestException as exc:
        logger.error("Network error: %s", exc)
        print(f"Network Error: {exc}")
        print("Result: FAILED")
        return 1
    except Exception as exc:  # pragma: no cover
        logger.exception("Unexpected error: %s", exc)
        print("Unexpected Error: Something went wrong while placing the order.")
        print("Result: FAILED")
        return 1


if __name__ == "__main__":
    sys.exit(main())
