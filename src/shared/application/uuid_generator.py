from uuid import uuid4

def generate_uuid(prefix: str = "") -> str:
    """Generates a UUID with an optional prefix."""
    return f"{prefix}{uuid4().hex[:6]}".upper()
