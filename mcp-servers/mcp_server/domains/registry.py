from mcp.server.fastmcp import FastMCP

from .orders import register_order_tools
from .mathematics import register_math_tools
from .users import register_user_resources, register_user_prompts
from .graphs import register_plotly_tools
from .documents import register_document_tools


def register_all_tools(mcp: FastMCP) -> None:
    # register_order_tools(mcp)
    # register_math_tools(mcp)
    # register_user_resources(mcp)
    # register_user_prompts(mcp)
    register_plotly_tools(mcp)
    register_document_tools(mcp)
