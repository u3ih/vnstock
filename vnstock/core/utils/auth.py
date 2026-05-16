# vnstock/core/utils/auth.py

"""
User authentication and API key registration for vnstock.
"""

import logging
from typing import Optional

logger = logging.getLogger(__name__)

_API_KEY: Optional[str] = None


def register_user(api_key: Optional[str] = None) -> bool:
    """Register API key for authenticated requests."""
    if not api_key:
        print("✗ API key không được cung cấp (✗ API key not provided)")
        return False
    return change_api_key(api_key)


def change_api_key(api_key: str) -> bool:
    """Change the active API key."""
    global _API_KEY
    if not api_key or len(api_key) < 10:
        print("✗ API key không hợp lệ (✗ Invalid API key)")
        return False
    _API_KEY = api_key
    masked = f"{api_key[:4]}***{api_key[-4:]}" if len(api_key) > 8 else "****"
    print(f"✓ API key đã được lưu ({masked})")
    return True


def check_status() -> Optional[dict]:
    """Return current API key registration status."""
    if _API_KEY:
        masked = f"{_API_KEY[:4]}***{_API_KEY[-4:]}" if len(_API_KEY) > 8 else "****"
        status = {"has_api_key": True, "api_key_preview": masked}
        print(f"✓ API key: {masked}")
    else:
        status = {"has_api_key": False}
        print("✗ Chưa đăng ký API key (✗ API key not registered)")
    return status
