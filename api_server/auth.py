import os

VALID_API_KEYS = set(os.getenv("PLATFORM_API_KEYS", "").split(","))

def verify_api_key(key: str) -> bool:
    return key in VALID_API_KEYS
