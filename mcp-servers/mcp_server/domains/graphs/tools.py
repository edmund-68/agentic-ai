from mcp.server.fastmcp import FastMCP
from typing import Dict, Any

import plotly.express as px
import pandas as pd
import logging

logger = logging.getLogger(__name__)

def register_plotly_tools(mcp: FastMCP):
    
    @mcp.tool(
        description="""
        Create a scatter plot using the server-side dataset.

        The dataset is already loaded and available.
        Do NOT ask the user for data.

        Parameters:
        - x: Column name for X axis.
        - y: Column name for Y axis.
        """
    )
    def build_scatter_by_df(x: str, y: str) -> Dict[str, Any]:
        logger.info(f"Showing scatter plot for dataframe with x={x} and y={y}")
        data = {
            "ayam": [1, 2, 3, 4, 5],
            "sapi": [10, 20, 30, 40, 50]
        }
        df = pd.DataFrame(data)
        fig = px.scatter(df, x=x, y=y)
        return fig.to_dict()