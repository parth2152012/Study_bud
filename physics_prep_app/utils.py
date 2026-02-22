"""Shared utility functions for the Streamlit app."""

from __future__ import annotations

import random
from typing import Any


def get_random_question(questions: list[dict[str, Any]]) -> dict[str, Any]:
    """Return a random question from a non-empty list."""
    return random.choice(questions)


def get_mock_test_questions(all_questions: list[dict[str, Any]], count: int = 10) -> list[dict[str, Any]]:
    """Return a random set of questions for mock test."""
    sample_size = min(count, len(all_questions))
    return random.sample(all_questions, sample_size)
