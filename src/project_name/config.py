import os


def get_postgres_uri() -> str:
    host = os.environ.get("DB_HOST", "localhost")
    port = 5432
    password = os.environ.get("DB_PASSWORD", "abc123")
    user, db_name = "olca_org", "olca_org"
    return f"postgresql://{user}:{password}@{host}:{port}/{db_name}"


def get_api_url() -> str:
    host = os.environ.get("API_HOST", "localhost")
    port = 8000 if host == "localhost" else 80
    return f"http://{host}:{port}"


def get_allowed_cors_origins() -> list[str]:
    cors = [get_api_url()]
    return cors
