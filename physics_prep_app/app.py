"""Physics JEE & NSEP Prep Streamlit application."""

from __future__ import annotations

import time

import streamlit as st

from content import SYLLABUS_CONTENT, get_chapters, get_sections
from progress_tracker import ProgressTracker
from question_bank import QUESTION_BANK, get_all_questions
from utils import get_mock_test_questions, get_random_question

st.set_page_config(page_title="Physics JEE & NSEP Prep", page_icon="⚛️", layout="wide")

tracker = ProgressTracker()


def initialize_state() -> None:
    """Initialize session state variables for modes and scoring."""
    defaults = {
        "practice_question": None,
        "practice_selected": None,
        "practice_submitted": False,
        "practice_score": 0,
        "practice_attempted": 0,
        "mock_started": False,
        "mock_questions": [],
        "mock_answers": {},
        "mock_submitted": False,
        "mock_start_time": None,
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)


def render_study_mode(section: str, chapter: str) -> None:
    chapter_data = SYLLABUS_CONTENT[section]["chapters"][chapter]
    st.subheader(f"{chapter} — Study Notes")
    st.markdown(f"**Chapter Weightage:** {chapter_data['weightage']}")

    st.markdown("### Important Formulas")
    for formula in chapter_data["formulas"]:
        st.latex(formula)

    st.markdown("### Key Concepts")
    for concept in chapter_data["concepts"]:
        st.markdown(f"- {concept}")


def render_practice_mode(chapter: str) -> None:
    questions = QUESTION_BANK.get(chapter, [])
    st.subheader(f"Practice: {chapter}")

    if not questions:
        st.warning("No questions available for this chapter.")
        return

    if st.button("🎯 Generate Random Question") or st.session_state.practice_question is None:
        st.session_state.practice_question = get_random_question(questions)
        st.session_state.practice_selected = None
        st.session_state.practice_submitted = False

    question = st.session_state.practice_question
    st.markdown(f"**Difficulty:** {question['difficulty']} | **Tag:** {question['tag']}")
    st.markdown(f"### {question['question']}")

    st.session_state.practice_selected = st.radio(
        "Choose an answer:",
        question["options"],
        index=None,
        key="practice_option",
    )

    if st.button("Submit Practice Answer") and st.session_state.practice_selected:
        is_correct = st.session_state.practice_selected == question["answer"]
        st.session_state.practice_submitted = True
        st.session_state.practice_attempted += 1
        if is_correct:
            st.session_state.practice_score += 1
            st.success("✅ Correct answer!")
        else:
            st.error(f"❌ Incorrect. Correct answer: {question['answer']}")

        tracker.record_attempt(chapter, is_correct)

    st.info(
        f"Practice Session Score: {st.session_state.practice_score} / "
        f"{st.session_state.practice_attempted}"
    )


def render_mock_mode() -> None:
    st.subheader("Mock Test Mode")
    all_questions = get_all_questions()

    if not st.session_state.mock_started:
        if st.button("🚀 Start 10-Question Mock Test"):
            st.session_state.mock_questions = get_mock_test_questions(all_questions, 10)
            st.session_state.mock_answers = {}
            st.session_state.mock_submitted = False
            st.session_state.mock_started = True
            st.session_state.mock_start_time = time.time()

    if not st.session_state.mock_started:
        st.info("Start the mock test to begin.")
        return

    elapsed = int(time.time() - st.session_state.mock_start_time)
    st.markdown(f"⏱️ **Timer:** {elapsed} seconds")

    for idx, question in enumerate(st.session_state.mock_questions, start=1):
        st.markdown(
            f"**Q{idx}. {question['question']}**  "+
            f"(Chapter: {question['chapter']} | {question['difficulty']} | {question['tag']})"
        )
        selected = st.radio(
            f"Select answer for Q{idx}",
            question["options"],
            index=None,
            key=f"mock_q_{idx}",
        )
        st.session_state.mock_answers[idx] = selected

    if st.button("Submit Mock Test"):
        st.session_state.mock_submitted = True

    if st.session_state.mock_submitted:
        correct = 0
        wrong = 0

        st.markdown("## Mock Test Result")
        for idx, question in enumerate(st.session_state.mock_questions, start=1):
            selected = st.session_state.mock_answers.get(idx)
            is_correct = selected == question["answer"]
            if is_correct:
                correct += 1
                st.success(f"Q{idx}: Correct")
            else:
                wrong += 1
                st.error(f"Q{idx}: Wrong | Correct: {question['answer']}")

            tracker.record_attempt(question["chapter"], is_correct)

        st.metric("Score", f"{correct}/10")
        st.write(f"Correct: {correct} | Wrong: {wrong}")


def render_progress() -> None:
    st.sidebar.markdown("---")
    st.sidebar.subheader("📊 Progress Tracker")
    summary = tracker.summary()

    st.sidebar.write(f"Total Attempted: {summary['total_attempted']}")
    st.sidebar.write(f"Correct Answers: {summary['correct_answers']}")
    st.sidebar.write(f"Accuracy: {summary['accuracy']:.2f}%")

    if summary["weak_chapters"]:
        st.sidebar.write("Weak Chapters (<60%):")
        for chapter, score in summary["weak_chapters"][:5]:
            st.sidebar.write(f"- {chapter}: {score:.1f}%")


def main() -> None:
    initialize_state()

    st.title("⚛️ Physics JEE & NSEP Prep")
    st.write("Structured study, chapter-wise practice, and timed mock tests for Physics only.")

    section = st.sidebar.selectbox("Select Topic", get_sections())
    st.sidebar.caption(f"Section Weightage: {SYLLABUS_CONTENT[section]['section_weightage']}")

    chapter = st.sidebar.selectbox("Select Chapter", get_chapters(section))
    mode = st.sidebar.radio("Mode", ["Study Mode", "Practice Mode", "Mock Test Mode"])

    render_progress()

    if mode == "Study Mode":
        render_study_mode(section, chapter)
    elif mode == "Practice Mode":
        render_practice_mode(chapter)
    else:
        render_mock_mode()


if __name__ == "__main__":
    main()
