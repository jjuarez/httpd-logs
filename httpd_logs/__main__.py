"""A basic HTTP server without logs"""
from typing import Type
from http.server import HTTPServer, BaseHTTPRequestHandler
from httpd_logs.config import EnvHTTPConfig
from httpd_logs.handler import SimpleRequestHandler


def run() -> None:
    """Starts the HTTP server"""
    config: EnvHTTPConfig = EnvHTTPConfig()
    handler_class: Type[BaseHTTPRequestHandler] = SimpleRequestHandler

    try:
        print(f"Server running: http://{config.host}:{config.port}...")
        HTTPServer(config.get(), handler_class).serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        print("Server stopped.")


if __name__ == "__main__":
    run()
