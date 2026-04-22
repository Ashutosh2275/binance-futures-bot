from __future__ import annotations


VALID_SIDES = {"BUY", "SELL"}
VALID_TYPES = {"MARKET", "LIMIT"}


def validate_order_inputs(
    symbol: str,
    side: str,
    order_type: str,
    quantity: float,
    price: float | None,
) -> None:
    """Validate CLI order parameters and raise ValueError when invalid."""
    if not symbol or not symbol.strip():
        raise ValueError("Invalid symbol: symbol is required.")

    normalized_side = side.upper()
    if normalized_side not in VALID_SIDES:
        raise ValueError("Invalid side: must be BUY or SELL.")

    normalized_type = order_type.upper()
    if normalized_type not in VALID_TYPES:
        raise ValueError("Invalid type: must be MARKET or LIMIT.")

    if quantity <= 0:
        raise ValueError("Invalid quantity: must be greater than 0.")

    if normalized_type == "LIMIT":
        if price is None:
            raise ValueError("Invalid price: --price is required for LIMIT orders.")
        if price <= 0:
            raise ValueError("Invalid price: must be greater than 0 for LIMIT orders.")
