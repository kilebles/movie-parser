from collections.abc import Sequence

from src.entities import Movie
from src.parsers.base import BaseParser


class MovieService:
    """Service layer for movie operations."""

    def __init__(self, parser: BaseParser) -> None:
        self._parser = parser

    def get_top_movies(self, limit: int = 10) -> Sequence[Movie]:
        """Get top movies using the configured parser."""
        return self._parser.get_top_movies(limit)

    def display_movies(self, movies: Sequence[Movie]) -> str:
        """Format movies for display."""
        if not movies:
            return "No movies found."

        lines = ["", "Top Movies from Kinopoisk:", "=" * 50]
        for movie in movies:
            lines.append(f"{movie.rank:>3}. {movie.title} ({movie.year}) - {movie.rating}")
        lines.append("=" * 50)
        return "\n".join(lines)
