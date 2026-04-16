"""Configuration — reads API key and base URL from environment."""

import os

YAPARAI_API_KEY = os.environ.get("YAPARAI_API_KEY", "")
YAPARAI_BASE_URL = os.environ.get("YAPARAI_BASE_URL", "https://api.yaparai.com")
