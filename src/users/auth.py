"""
Authentication
"""

from fastapi_users.authentication import (
    BearerTransport,
    JWTStrategy,
    AuthenticationBackend
)

bearer_transport = BearerTransport(tokenUrl="auth/jwt/login")

SECRET = "SECRET"


def get_jwt_strategy() -> JWTStrategy:
    return JWTStrategy(secret=SECRET, lifetime_seconds=3600)


auth_backend = AuthenticationBackend(
    name="jwt",
    transport=bearer_transport,
    get_strategy=get_jwt_strategy,
)
