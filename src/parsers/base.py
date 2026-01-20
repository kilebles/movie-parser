from abc import ABC, abstractmethod
from collections.abc import Sequence

from src.entities import Movie


class BaseParser(ABC):
    @abstractmethod
    def get_top_movies(self, limit: int = 10) -> Sequence[Movie]:
        """Fetch top movies from the source."""
        ...
