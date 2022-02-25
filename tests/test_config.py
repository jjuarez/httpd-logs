import pytest
from httpd_logs.config import (
    HTTPConfigError,
    EnvHTTPConfig,
    DEFAULT_HTTP_SERVER_HOST,
    DEFAULT_HTTP_SERVER_PORT,
)


@pytest.fixture
def default_config(monkeypatch) -> EnvHTTPConfig:
    """Default config fixture"""
    return EnvHTTPConfig()


class TestDefaultEnvHTTPConfig:
    """Test suite for the EnvHTTPConfig class"""

    def test_host(self, default_config: EnvHTTPConfig):
        assert default_config.host == DEFAULT_HTTP_SERVER_HOST

    def test_port(self, default_config):
        assert default_config.port == int(DEFAULT_HTTP_SERVER_PORT)

    def test_get(self, default_config):
        assert default_config.get() == (
            DEFAULT_HTTP_SERVER_HOST,
            int(DEFAULT_HTTP_SERVER_PORT),
        )


@pytest.fixture
def custom_host(monkeypatch) -> EnvHTTPConfig:
    monkeypatch.setenv("HTTP_SERVER_HOST", "192.168.1.64")
    return EnvHTTPConfig()


class TestCustomHostEnvHTTPConfig:
    """Test suite for the EnvHTTPConfig class"""

    def test_host(self, custom_host: EnvHTTPConfig):
        assert custom_host.host == "192.168.1.64"


@pytest.fixture
def custom_port(monkeypatch) -> EnvHTTPConfig:
    monkeypatch.setenv("HTTP_SERVER_PORT", "8888")
    return EnvHTTPConfig()


class TestCustomPortEnvHTTPConfig:
    """Test suite for the EnvHTTPConfig class"""

    def test_port(self, custom_port: EnvHTTPConfig):
        assert custom_port.port == 8888


class TestBadPortEnvHTTPConfig:
    """Test suite for a bad port"""

    def test_port(self, monkeypatch):
        with pytest.raises(HTTPConfigError):
            monkeypatch.setenv("HTTP_SERVER_PORT", "888X")
            EnvHTTPConfig()
