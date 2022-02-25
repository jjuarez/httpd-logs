"""The configuration module"""
import os
import abc
from typing import Final, Tuple

DEFAULT_HTTP_SERVER_HOST: Final = "0.0.0.0"
DEFAULT_HTTP_SERVER_PORT: Final = "8125"


class HTTPConfigError(Exception):
    """The custom error for the module"""


class HTTPConfig(metaclass=abc.ABCMeta):
    """The HTTP minimal server configuration"""

    @classmethod
    def __subclasshook__(cls, subclass):
        return (
            hasattr(subclass, "get") and callable(subclass.get)
        ) or NotImplementedError

    def get(self) -> Tuple[str, int]:
        """Return the configuration dictionary"""
        raise NotImplementedError


class EnvHTTPConfig(HTTPConfig):
    """HTTPConfig from environment"""

    HTTP_SERVER_HOST_KEY: Final = "HTTP_SERVER_HOST"
    HTTP_SERVER_PORT_KEY: Final = "HTTP_SERVER_PORT"

    def __init__(self) -> None:
        self._host = os.environ.get(self.HTTP_SERVER_HOST_KEY, DEFAULT_HTTP_SERVER_HOST)
        try:
            self._port = int(
                os.environ.get(self.HTTP_SERVER_PORT_KEY, DEFAULT_HTTP_SERVER_PORT)
            )
        except ValueError as value_error:
            raise HTTPConfigError from value_error

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(host={self._host}, port={self._port})"

    @property
    def host(self) -> str:
        """The server host"""
        return self._host

    @property
    def port(self) -> int:
        """The server port"""
        return self._port

    def get(self) -> Tuple[str, int]:
        """Returns the HTTP server configuration"""
        return (self.host, self.port)
