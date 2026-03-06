from mcp.server.fastmcp import FastMCP
from .service import get_user_by_id

import logging

logger = logging.getLogger(__name__)

def register_user_resources(mcp: FastMCP):

    @mcp.resource(
        uri="user://{user_id}",
        description="Get user information by user_id."
    )
    def get_user(user_id: str) -> dict[str, str]: # pyright: ignore[reportUnusedFunction]

        logger.info(f"get_user called with {user_id}")

        user = get_user_by_id(user_id)

        if not user:
            return {"error": "User not found"}

        return user