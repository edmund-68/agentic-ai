# orders/tools.py

from mcp.server.fastmcp import FastMCP
from typing import List
from .models import Order

import logging

logger = logging.getLogger(__name__)


def register_order_tools(mcp: FastMCP):

    @mcp.tool(description="Search orders by minimum amount in USD.")
    def search_orders(min_amount: float) -> List[Order]: # pyright: ignore[reportUnusedFunction]

        logger.info(f"search_orders called with min_amount={min_amount}")

        orders: List[Order] = [
            Order(order_id="o1", amount=100.0),
            Order(order_id="o2", amount=250.0),
            Order(order_id="o3", amount=50.0),
        ]

        return [o for o in orders if o.amount >= min_amount]