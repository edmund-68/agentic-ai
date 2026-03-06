import sys

from server import create_server
from domains.registry import register_all_tools
from config import setup_logging
# from mcp import MCPServer
from config import ServerConfig


import logging

logger = logging.getLogger(__name__)

def create_app():
    mcp = create_server()
    register_all_tools(mcp)
    return mcp

server = create_app()

if __name__ == "__main__":
    # setup_logging()
    logger.info("Starting MCP server")
    server.run(transport="streamable-http")



# def main():
#     """
#     Main entry point for the MCP server.
    
#     Supports both direct execution and smithery integration:
#     - When called directly: Starts the server with full lifecycle management
#     - When imported by smithery: Can be used to create server instances
    
#     Orchestrates the complete server lifecycle:
#     1. Load configuration from environment variables and CLI arguments
#     2. Set up logging based on configuration
#     3. Create and configure the MCP server instance
#     4. Register chart generation capabilities
#     5. Start the server with the specified transport
#     6. Handle graceful shutdown on interruption
    
#     Raises:
#         SystemExit: On critical errors that prevent server startup
#     """
#     try:
#         # Load configuration from environment and command line
#         config = ServerConfig.from_env_and_args()
        
#         # Configure logging based on user preferences
#         setup_logging(config.log_level)
#         logger = logging.getLogger(__name__)
        
#         # Log startup information for debugging
#         logger.info("Starting Plots MCP Server...")
#         logger.info(f"Configuration: {config.to_dict()}")
        
#         # Create and configure server with resolved settings
#         server = MCPServer(
#             transport_route=config.transport,
#             stateless_http=config.stateless_http,
#             host=config.host,
#             port=config.port,
#             log_level=config.log_level,
#             debug=config.debug,
#         )
        
#         # Initialize MCP capabilities (tools, prompts, resources)
#         mcp_server_instance = server.setup_mcp_server_and_capabilities()
        
#         # Start the server - this blocks until interrupted
#         server.run()
        
#     except KeyboardInterrupt:
#         # Graceful shutdown on Ctrl+C
#         logger.info("Server stopped by user.")
#     except Exception as e:
#         # Log critical errors and exit with error code
#         logger.critical(f"Server failed to start: {e}", exc_info=True)
#         sys.exit(1)


# if __name__ == "__main__":
#     main()