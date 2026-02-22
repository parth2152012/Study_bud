# Physics JEE & NSEP Prep

A production-ready Streamlit web application focused exclusively on Physics preparation for **JEE Main** and **NSEP**.

## Project Overview

This app provides a structured preparation workflow with complete chapter categorization, formula sheets, concept highlights, chapter-wise MCQ practice, timed mock tests, and persistent performance tracking.

## Features

- Modular Python architecture with separate files for UI, content, questions, utilities, and progress tracking.
- Full syllabus sections with chapter-level weightage.
- Study Mode with formulas rendered in LaTeX and concise concept notes.
- Modern UI theme with animated abstract gradient background, glassmorphism cards, and section banner imagery.
- Practice Mode with random chapter-wise MCQs, answer validation, and live scoring.
- Mock Test Mode with 10 mixed questions, timer, and result summary.
- JSON-backed progress tracker with:
  - total attempted
  - correct answers
  - accuracy percentage
  - weak chapter detection

## Installation

1. Clone the repository.
2. Move into the project folder:
   ```bash
   cd physics_prep_app
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

From inside `physics_prep_app`:

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal (usually `http://localhost:8501`).

## Future Roadmap

- User authentication and cloud-sync progress.
- Previous year papers with filters.
- Adaptive recommendation engine by weak topics.
- Topic-wise revision planner and streak tracking.
- Rich analytics dashboard with downloadable reports.
