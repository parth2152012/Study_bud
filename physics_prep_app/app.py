"""Physics JEE & NSEP Prep Streamlit application."""

from __future__ import annotations

import time

import streamlit as st

from content import SYLLABUS_CONTENT, get_chapters, get_sections
from progress_tracker import ProgressTracker
from question_bank import QUESTION_BANK, get_all_questions
from utils import get_mock_test_questions, get_random_question

st.set_page_config(page_title="Physics Prep", page_icon="⚛️", layout="wide")

tracker = ProgressTracker()


def load_css(file_name: str) -> None:
    """Load and inject custom CSS."""
    with open(file_name, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def initialize_state() -> None:
    """Initialize session state variables."""
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
    """Display study materials with improved layout."""
    chapter_data = SYLLABUS_CONTENT[section]["chapters"][chapter]
    st.header(f"Study Mode: {chapter}")
    st.markdown(f"**Chapter Weightage:** `{chapter_data['weightage']}`")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Important Formulas")
        for formula in chapter_data["formulas"]:
            st.latex(formula)

    with col2:
        st.subheader("Key Concepts")
        for concept in chapter_data["concepts"]:
            st.markdown(f"- {concept}")


def render_practice_mode(chapter: str) -> None:
    """Handle the practice mode with interactive questions."""
    st.header(f"Practice Mode: {chapter}")
    questions = QUESTION_BANK.get(chapter, [])

    if not questions:
        st.warning("No practice questions available for this chapter yet.")
        return

    if st.button("🎯 New Random Question") or st.session_state.practice_question is None:
        st.session_state.practice_question = get_random_question(questions)
        st.session_state.practice_selected = None
        st.session_state.practice_submitted = False

    question = st.session_state.practice_question
    st.markdown(f"**Difficulty:** `{question['difficulty']}` | **Tag:** `{question['tag']}`")
    st.subheader(question["question"])

    st.session_state.practice_selected = st.radio(
        "Your Answer:",
        question["options"],
        index=None if not st.session_state.practice_submitted else question["options"].index(st.session_state.practice_selected),
        key="practice_option",
    )

    if st.button("Submit Answer"):
        if st.session_state.practice_selected:
            st.session_state.practice_submitted = True
            is_correct = st.session_state.practice_selected == question["answer"]
            st.session_state.practice_attempted += 1

            if is_correct:
                st.session_state.practice_score += 1
                st.success("✅ Correct! Well done.")
            else:
                st.error(f"❌ Incorrect. The correct answer is **{question['answer']}**.")

            with st.expander("💡 Explanation"):
                st.markdown(question.get("explanation", "No explanation provided."))

            tracker.record_attempt(chapter, is_correct)
        else:
            st.warning("Please select an answer before submitting.")

    st.sidebar.info(
        f"**Practice Score:** {st.session_state.practice_score} / {st.session_state.practice_attempted}"
    )


def render_mock_mode() -> None:
    """Administer a timed mock test."""
    st.header("Mock Test Mode")
    all_questions = get_all_questions()

    if not st.session_state.mock_started:
        if st.button("🚀 Start 10-Question Mock Test"):
            st.session_state.mock_questions = get_mock_test_questions(all_questions, 10)
            st.session_state.mock_answers = {i: None for i in range(1, 11)}
            st.session_state.mock_submitted = False
            st.session_state.mock_started = True
            st.session_state.mock_start_time = time.time()
            st.experimental_rerun()

    if not st.session_state.mock_started:
        st.info("Click the button above to start a timed mock test.")
        return

    elapsed = int(time.time() - st.session_state.mock_start_time)
    st.sidebar.markdown(f"### ⏱️ Timer: `{elapsed}` seconds")

    for idx, q in enumerate(st.session_state.mock_questions, start=1):
        st.markdown(f"--- \n **Q{idx}: {q['question']}**")
        st.markdown(f"`{q['chapter']}` | `{q['difficulty']}` | `{q['tag']}`")
        st.session_state.mock_answers[idx] = st.radio(
            "Select answer:",
            q["options"],
            key=f"mock_q_{idx}",
        )

    st.markdown("---")
    if st.button("🏁 Submit Mock Test"):
        if all(st.session_state.mock_answers.values()):
            st.session_state.mock_submitted = True
        else:
            st.warning("Please answer all questions before submitting.")

    if st.session_state.mock_submitted:
        render_mock_results()


def render_mock_results() -> None:
    """Display the results of the mock test."""
    st.subheader("Mock Test Results")
    correct, wrong = 0, 0
    results_data = []

    for idx, q in enumerate(st.session_state.mock_questions, start=1):
        selected = st.session_state.mock_answers.get(idx)
        is_correct = selected == q["answer"]
        if is_correct:
            correct += 1
            status = "✅"
        else:
            wrong += 1
            status = "❌"
        results_data.append([f"Q{idx}", q["question"], selected, q["answer"], status])

    st.table(
        (
            (
                "**#**",
                "**Question**",
                "**Your Answer**",
                "**Correct Answer**",
                "**Status**",
            ),
            *results_data,
        )
    )

    st.sidebar.metric("Final Score", f"{correct} / 10")
    st.sidebar.success(f"**Correct:** {correct}")
    st.sidebar.error(f"**Wrong:** {wrong}")
    st.balloons()


def render_progress() -> None:
    """Display user progress and weak chapters."""
    st.sidebar.markdown("---")
    st.sidebar.header("📊 Progress Tracker")
    summary = tracker.summary()

    st.sidebar.metric(
        "Overall Accuracy",
        f"{summary['accuracy']:.2f}%",
        f"{summary['correct_answers']}/{summary['total_attempted']}",
    )

    if summary["weak_chapters"]:
        st.sidebar.markdown("#### Weak Chapters (<60% Accuracy)")
        for chapter, score in summary["weak_chapters"][:5]:
            st.sidebar.write(chapter)
            st.sidebar.progress(int(score))


def main() -> None:
    """Main function to run the Streamlit app."""
    initialize_state()
    load_css("static/styles.css")

    st.title("⚛️ Physics Prep for JEE & NSEP")
    st.caption("A tool for targeted study, practice, and mock tests.")

    st.sidebar.title("Navigation")
    section = st.sidebar.selectbox("Select Topic", get_sections())
    st.sidebar.caption(f"Weightage: {SYLLABUS_CONTENT[section]['section_weightage']}")

    chapter = st.sidebar.selectbox("Select Chapter", get_chapters(section))
    mode = st.sidebar.radio("Select Mode", ["Study Mode", "Practice Mode", "Mock Test Mode"])

    if mode == "Study Mode":
        render_study_mode(section, chapter)
    elif mode == "Practice Mode":
        render_practice_mode(chapter)
    else:
        render_mock_mode()

    render_progress()


if __name__ == "__main__":
    main()
