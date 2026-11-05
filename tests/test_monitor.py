
import pytest
import requests
from unittest.mock import Mock

from app.monitor import validate_url, check_website


# Test URL validation
def test_valid_http_url():
    assert validate_url("http://example.com") is True


def test_valid_https_url():
    assert validate_url("https://github.com") is True


def test_invalid_url():
    assert validate_url("not-a-valid-url") is False


def test_invalid_scheme():
    assert validate_url("ftp://example.com") is False


# Test successful website check
def test_website_is_up(monkeypatch):
    mock_response = Mock()
    mock_response.status_code = 200

    monkeypatch.setattr(
        requests,
        "get",
        lambda *args, **kwargs: mock_response
    )

    result = check_website("https://example.com")

    assert result["status"] == "UP"
    assert result["is_up"] is True
    assert result["status_code"] == 200
    assert result["response_time_ms"] is not None


# Test website returning an error status
def test_website_is_down(monkeypatch):
    mock_response = Mock()
    mock_response.status_code = 500

    monkeypatch.setattr(
        requests,
        "get",
        lambda *args, **kwargs: mock_response
    )

    result = check_website("https://example.com")

    assert result["status"] == "DOWN"
    assert result["is_up"] is False
    assert result["status_code"] == 500


# Test connection failure
def test_connection_error(monkeypatch):
    def mock_get(*args, **kwargs):
        raise requests.ConnectionError("Connection failed")

    monkeypatch.setattr(requests, "get", mock_get)

    result = check_website("https://example.com")

    assert result["status"] == "DOWN"
    assert result["is_up"] is False
    assert result["error"] is not None


# Test invalid URL without making a network request
def test_check_invalid_url():
    result = check_website("invalid-url")

    assert result["status"] == "DOWN"
    assert result["is_up"] is False
    assert result["error"] == "Invalid URL"
