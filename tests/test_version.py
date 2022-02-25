"""Test the version related stuff"""
from httpd_logs import __version__


class TestVersion:
    """Version testsuite"""

    def test_version(self):
        """Test the version number"""
        assert __version__ == "0.1.0"
