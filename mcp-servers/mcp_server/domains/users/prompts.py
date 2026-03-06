from mcp.server.fastmcp import FastMCP

import logging

logger = logging.getLogger(__name__)

def register_user_prompts(mcp: FastMCP):

    @mcp.prompt()
    def summarize_user_prompt(user_name: str): # pyright: ignore[reportUnusedFunction]

        logger.info(f"summarize_user_prompt called with {user_name}")

        return f"""
        You are an expert analyst.
        Summarize the profile of {user_name}
        in a professional tone.
        """
    
