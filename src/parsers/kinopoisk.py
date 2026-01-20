import json
from collections.abc import Sequence
from urllib.request import Request, urlopen

from src.config import Settings
from src.entities import Movie

from .base import BaseParser


class KinopoiskParser(BaseParser):
    """Parser for Kinopoisk top 250 movies via unofficial API."""

    API_URL = "https://kinopoiskapiunofficial.tech/api/v2.2/films/collections"

    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def get_top_movies(self, limit: int = 10) -> Sequence[Movie]:
        """Fetch top movies from Kinopoisk."""
        data = self._fetch_api()
        return self._parse_movies(data, limit)

    def _fetch_api(self) -> dict:
        """Fetch data from the Kinopoisk unofficial API."""
        url = f"{self.API_URL}?type=TOP_250_MOVIES&page=1"
        request = Request(
            url,
            headers={
                "X-API-KEY": self._settings.api_key,
                "Accept": "application/json",
                "User-Agent": self._settings.user_agent,
            },
        )
        with urlopen(request, timeout=self._settings.timeout) as response:
            return json.loads(response.read().decode("utf-8"))

    def _parse_movies(self, data: dict, limit: int) -> list[Movie]:
        """Parse movie data from API response."""
        movies: list[Movie] = []
        items = data.get("items", [])

        for rank, item in enumerate(items[:limit], start=1):
            title = item.get("nameRu") or item.get("nameOriginal") or "Unknown"
            movies.append(
                Movie(
                    rank=rank,
                    title=title,
                    year=item.get("year", 0),
                    rating=item.get("ratingKinopoisk", 0.0) or 0.0,
                    url=f"https://www.kinopoisk.ru/film/{item.get('kinopoiskId', '')}/",
                )
            )

        return movies
