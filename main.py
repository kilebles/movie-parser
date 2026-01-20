import sys
from pathlib import Path

from src.config import Settings
from src.exporters import ExcelExporter
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

        output_path = Path("top_movies.xlsx")
        exporter = ExcelExporter()
        exporter.export(movies, output_path)
        print(f"\nExported to {output_path}")

        return 0
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
