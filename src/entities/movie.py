from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Movie:
    """Immutable movie entity."""

    rank: int
    title: str
    year: int
    rating: float
    url: str

    def __str__(self) -> str:
        return f"{self.rank}. {self.title} ({self.year}) - {self.rating}"
