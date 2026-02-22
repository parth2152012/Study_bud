"""Progress persistence and analytics utilities."""

from __future__ import annotations

import json
from pathlib import Path


class ProgressTracker:
    """Track user attempts and chapter-level performance in a JSON file."""

    def __init__(self, file_path: str = "progress.json") -> None:
        self.file_path = Path(file_path)
        self.data = self._load()

    def _default_data(self) -> dict:
        return {
            "total_attempted": 0,
            "correct_answers": 0,
            "chapter_stats": {},
        }

    def _load(self) -> dict:
        if self.file_path.exists():
            with self.file_path.open("r", encoding="utf-8") as file:
                return json.load(file)
        return self._default_data()

    def _save(self) -> None:
        with self.file_path.open("w", encoding="utf-8") as file:
            json.dump(self.data, file, indent=2)

    def record_attempt(self, chapter: str, is_correct: bool) -> None:
        """Store a single attempt and update counters."""
        self.data["total_attempted"] += 1
        if is_correct:
            self.data["correct_answers"] += 1

        chapter_stat = self.data["chapter_stats"].setdefault(
            chapter,
            {"attempted": 0, "correct": 0},
        )
        chapter_stat["attempted"] += 1
        if is_correct:
            chapter_stat["correct"] += 1

        self._save()

    def accuracy(self) -> float:
        """Return global accuracy percentage."""
        attempted = self.data["total_attempted"]
        if attempted == 0:
            return 0.0
        return (self.data["correct_answers"] / attempted) * 100

    def weak_chapters(self, threshold: float = 60.0) -> list[tuple[str, float]]:
        """Return chapters with accuracy lower than threshold."""
        weak = []
        for chapter, stats in self.data["chapter_stats"].items():
            if stats["attempted"] == 0:
                continue
            chapter_accuracy = (stats["correct"] / stats["attempted"]) * 100
            if chapter_accuracy < threshold:
                weak.append((chapter, chapter_accuracy))
        return sorted(weak, key=lambda item: item[1])

    def summary(self) -> dict:
        """Return user progress summary data."""
        return {
            "total_attempted": self.data["total_attempted"],
            "correct_answers": self.data["correct_answers"],
            "accuracy": self.accuracy(),
            "weak_chapters": self.weak_chapters(),
        }
