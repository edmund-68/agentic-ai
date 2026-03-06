import logging

from pydantic.dataclasses import dataclass


def setup_logging(level) -> None:
    logging.basicConfig(
        level=getattr(logging, level.upper()),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


@dataclass
class ServerConfig:
    
    # MCP Server Configuration
    transport: str = "streamable-http"
    stateless_http: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    log_level: str = "INFO"
    debug: bool = False

    @classmethod
    def from_env_and_args(cls) -> "ServerConfig":
        import os
        import argparse

        # Load defaults from environment variables
        config = cls(
            transport=os.getenv("MCP_TRANSPORT", "streamable-http"),
            host=os.getenv("MCP_HOST", "0.0.0.0"),
            port=int(os.getenv("MCP_PORT", "8000")),
            log_level=os.getenv("LOG_LEVEL", "INFO"),
            debug=os.getenv("MCP_DEBUG", "false").lower() in ("true", "1", "yes", "on")
        )


        parser = argparse.ArgumentParser(description="MCP Server Configuration")
        parser.add_argument("--transport", type=str, help="Transport protocol")
        parser.add_argument("--stateless_http", action="store_true", help="Enable stateless HTTP")
        parser.add_argument("--host", type=str, help="Host to bind the server")
        parser.add_argument("--port", type=int, help="Port to bind the server")
        parser.add_argument("--log_level", type=str, help="Logging level")
        parser.add_argument("--debug", action="store_true", help="Enable debug mode")

        args = parser.parse_args()

        config.transport = os.getenv("MCP_TRANSPORT", config.transport)
        config.stateless_http = os.getenv("MCP_STATELESS_HTTP", str(config.stateless_http)).lower() in ("true", "1", "yes") or args.stateless_http
        config.host = os.getenv("MCP_HOST", config.host)
        config.port = int(os.getenv("MCP_PORT", config.port))
        config.log_level = os.getenv("MCP_LOG_LEVEL", config.log_level)
        config.debug = os.getenv("MCP_DEBUG", str(config.debug)).lower() in ("true", "1", "yes") or args.debug

        return config
    
    def to_dict(self) -> dict:
        return {
            "transport": self.transport,
            "stateless_http": self.stateless_http,
            "host": self.host,
            "port": self.port,
            "log_level": self.log_level,
            "debug": self.debug
        }
