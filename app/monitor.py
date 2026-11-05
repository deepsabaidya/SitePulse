
import requests
import time
from datetime import datetime, timezone
from urllib.parse import urlparse


def validate_url(url):
    """Validate the website URL."""

    parsed = urlparse(url)

    return (
        parsed.scheme in ("http", "https")
        and bool(parsed.netloc)
    )


def check_website(url):
    """Check website availability and measure response time."""

    if not validate_url(url):
        return {
            "url": url,
            "status": "DOWN",
            "is_up": False,
            "status_code": None,
            "response_time_ms": None,
            "error": "Invalid URL",
            "checked_at": datetime.now(timezone.utc).isoformat()
        }

    start_time = time.perf_counter()

    try:
        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True
        )

        end_time = time.perf_counter()

        response_time = round(
            (end_time - start_time) * 1000, 2
        )

        is_up = 200 <= response.status_code < 400

        return {
            "url": url,
            "status": "UP" if is_up else "DOWN",
            "is_up": is_up,
            "status_code": response.status_code,
            "response_time_ms": response_time,
            "error": None,
            "checked_at": datetime.now(timezone.utc).isoformat()
        }

    except requests.RequestException as error:

        return {
            "url": url,
            "status": "DOWN",
            "is_up": False,
            "status_code": None,
            "response_time_ms": None,
            "error": str(error),
            "checked_at": datetime.now(timezone.utc).isoformat()
        }
