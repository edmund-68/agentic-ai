from mcp.server.fastmcp import FastMCP

import logging

logger = logging.getLogger(__name__)

def register_math_tools(mcp: FastMCP):

    @mcp.tool(description="Add two integers together.")
    def add_numbers(a: int, b: int) -> int: # pyright: ignore[reportUnusedFunction]
        logger.info(f"Adding {a} and {b}")
        return a + b