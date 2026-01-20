#!/usr/bin/env python3
"""Kinopoisk top movies parser."""

import sys

from src.config import Settings
from src.parsers import KinopoiskParser
from src.services import MovieService


def main() -> int:
    """Main entry point."""
    try:
        settings = Settings.from_env()
        parser = KinopoiskParser(settings)
        service = MovieService(parser)

        movies = service.get_top_movies(limit=10)
        print(service.display_movies(movies))

        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
