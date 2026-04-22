from __future__ import annotations

from typing import Any


def place_order(
    client: Any,
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float | None = None,
) -> dict:
    """Place a Binance Futures Testnet order and return the API response."""
    order_payload = {
        "symbol": symbol.upper(),
        "side": side.upper(),
        "type": order_type.upper(),
        "quantity": quantity,
    }

    if order_payload["type"] == "MARKET":
        return client.futures_create_order(**order_payload)

    order_payload["price"] = price
    order_payload["timeInForce"] = "GTC"
    return client.futures_create_order(**order_payload)
