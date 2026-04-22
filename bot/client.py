from __future__ import annotations

import os

from binance.client import Client
from dotenv import load_dotenv


def get_client() -> Client:
    """Create and return a Binance client configured for Futures Testnet."""
    load_dotenv()

    api_key = os.getenv("BINANCE_API_KEY")
    api_secret = os.getenv("BINANCE_API_SECRET")

    if not api_key or not api_secret:
        raise ValueError(
            "Missing API credentials. Set BINANCE_API_KEY and BINANCE_API_SECRET in .env."
        )

    return Client(api_key=api_key, api_secret=api_secret, testnet=True)
