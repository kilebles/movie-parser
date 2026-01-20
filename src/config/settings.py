import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class Settings:
    """Application settings loaded from env."""

    base_url: str
    api_key: str
    user_agent: str = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36"
    )
    timeout: int = 30

    @classmethod
    def from_env(cls, env_path: Path | None = None) -> "Settings":
        """Load settings from .env file."""
        if env_path is None:
            env_path = Path(__file__).parent.parent.parent / ".env"

        env_vars: dict[str, str] = {}
        if env_path.exists():
            with open(env_path) as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith("#") and "=" in line:
                        key, _, value = line.partition("=")
                        env_vars[key.strip()] = value.strip()

        base_url = env_vars.get("site") or os.getenv("SITE", "https://www.kinopoisk.ru/")
        api_key = env_vars.get("api_key") or os.getenv("API_KEY", "")

        if not api_key:
            raise ValueError("API_KEY is required. Get one at https://kinopoiskapiunofficial.tech")

        return cls(base_url=base_url.rstrip("/"), api_key=api_key)
