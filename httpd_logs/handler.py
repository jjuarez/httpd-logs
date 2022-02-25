"""The handler module"""
import json
from typing import Final
from http.server import BaseHTTPRequestHandler


class SimpleRequestHandler(BaseHTTPRequestHandler):
    """The simplest request handler"""

    HTTP_OK: Final = 200
    HTTP_NOT_FOUND: Final = 404
    CONTENT_TYPE: Final = "application/json"
    RESPONSE: Final = bytes(json.dumps({"response": "pong"}), "utf-8")

    def _set_headers(self, http_code=HTTP_OK) -> None:
        self.send_response(http_code)
        self.send_header("Content-type", self.CONTENT_TYPE)
        self.end_headers()

    def do_GET(self) -> None:
        """GET"""
        if self.path == "/":
            self._set_headers()
            self.wfile.write(
                bytes(json.dumps({"response": "Try the /ping endpoint"}), "utf-8")
            )
        elif self.path == "/ping":
            self._set_headers()
            self.wfile.write(bytes(json.dumps({"response": "PONG"}), "utf-8"))
        else:
            self._set_headers(http_code=SimpleRequestHandler.HTTP_NOT_FOUND)

    def log_message(self, *args) -> None:
        """Avoid to show the logs"""
