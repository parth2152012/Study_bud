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

SECTION_IMAGES = {
    "Mechanics": "https://images.unsplash.com/photo-1532187863486-abf9dbad1b69?auto=format&fit=crop&w=1400&q=80",
    "Heat & Thermodynamics": "https://images.unsplash.com/photo-1573164574572-cb89e39749b4?auto=format&fit=crop&w=1400&q=80",
    "Oscillations & Waves": "https://images.unsplash.com/photo-1518779578993-ec3579fee39f?auto=format&fit=crop&w=1400&q=80",
    "Electricity & Magnetism": "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=1400&q=80",
    "Optics": "https://images.unsplash.com/photo-1520637836862-4d197d17c90a?auto=format&fit=crop&w=1400&q=80",
}


def inject_styles() -> None:
    """Inject modern styling and animation."""
    st.markdown(
        """
        <style>
            .stApp {
                background:
                    radial-gradient(circle at 12% 18%, rgba(0, 178, 255, 0.14), transparent 26%),
                    radial-gradient(circle at 82% 12%, rgba(160, 112, 255, 0.18), transparent 28%),
                    radial-gradient(circle at 82% 78%, rgba(80, 255, 200, 0.10), transparent 30%),
                    linear-gradient(120deg, #080d1b 0%, #0f1832 45%, #161336 100%);
                color: #f6f8ff;
            }

            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, rgba(9, 16, 33, 0.94), rgba(11, 17, 38, 0.88));
                border-right: 1px solid rgba(255, 255, 255, 0.1);
                backdrop-filter: blur(14px);
            }

            .hero {
                border-radius: 20px;
                border: 1px solid rgba(255,255,255,0.18);
                background: linear-gradient(135deg, rgba(55, 96, 255, 0.36), rgba(0, 204, 255, 0.15));
                padding: 1.2rem 1.4rem;
                box-shadow: 0 12px 28px rgba(0,0,0,0.26);
                animation: fadeLift .8s ease;
            }

            .mode-chip {
                display: inline-block;
                border-radius: 999px;
                border: 1px solid rgba(255,255,255,0.25);
                background: rgba(255,255,255,0.11);
                padding: .22rem .7rem;
                margin-right: .4rem;
                margin-top: .4rem;
                font-size: .78rem;
                font-weight: 700;
            }

            .glass {
                border-radius: 14px;
                border: 1px solid rgba(255,255,255,0.18);
                background: rgba(255,255,255,0.07);
                padding: .9rem 1rem;
                margin-bottom: .7rem;
                animation: fadeLift .5s ease;
            }

            .formula-card {
                border-radius: 14px;
                border: 1px solid rgba(255,255,255,0.16);
                background: rgba(255,255,255,0.05);
                padding: 0.2rem 0.9rem;
                margin-bottom: .45rem;
            }

            .question-card {
                border-radius: 14px;
                border: 1px solid rgba(255,255,255,0.18);
                background: linear-gradient(135deg, rgba(28, 42, 89, 0.75), rgba(25, 63, 99, 0.56));
                padding: 1rem;
                margin-bottom: .6rem;
            }

            @keyframes fadeLift {
                from { opacity: 0; transform: translateY(10px); }
                to { opacity: 1; transform: translateY(0); }
            }
        </style>
        """,
        unsafe_allow_html=True,
    )


def initialize_state() -> None:
    """Initialize session state variables for modes and scoring."""
    defaults = {
        "practice_question": None,
        "practice_selected": None,
        "practice_score": 0,
        "practice_attempted": 0,
        "mock_started": False,
        "mock_questions": [],
        "mock_answers": {},
        "mock_submitted": False,
        "mock_scored": False,
        "mock_start_time": None,
    }
    for key, value in defaults.items():
        st.session_state.setdefault(key, value)


def render_top_metrics(section: str, chapter: str, mode: str) -> None:
    """Render high-level dashboard cards."""
    summary = tracker.summary()
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Section", section)
    c2.metric("Chapter", chapter)
    c3.metric("Global Accuracy", f"{summary['accuracy']:.1f}%")
    c4.metric("Mode", mode.replace(" Mode", ""))


def render_study_mode(section: str, chapter: str) -> None:
    """Render chapter formulas and concept notes."""
    chapter_data = SYLLABUS_CONTENT[section]["chapters"][chapter]

    st.image(SECTION_IMAGES.get(section), use_container_width=True)
    st.markdown(
        f"""
        <div class="hero">
            <h2 style="margin:0;">{chapter}</h2>
            <p style="margin:.4rem 0 0;">Section: <b>{section}</b> • Chapter Weightage: <b>{chapter_data['weightage']}</b></p>
            <span class="mode-chip">Study Mode</span>
            <span class="mode-chip">JEE Main</span>
            <span class="mode-chip">NSEP</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([1.2, 1])
    with col1:
        st.markdown("### ✨ Important Formulas")
        for formula in chapter_data["formulas"]:
            st.markdown("<div class='formula-card'>", unsafe_allow_html=True)
            st.latex(formula)
            st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("### 🧠 Key Concepts")
        for concept in chapter_data["concepts"]:
            st.markdown(f"<div class='glass'>• {concept}</div>", unsafe_allow_html=True)


def render_practice_mode(chapter: str) -> None:
    """Render random chapter-wise question practice with scoring."""
    questions = QUESTION_BANK.get(chapter, [])
    st.markdown(f"## 🎯 Practice Arena — {chapter}")

    if not questions:
        st.warning("No questions available for this chapter.")
        return

    with st.container(border=True):
        left, right = st.columns([1, 2])
        with left:
            if st.button("🎲 New Random Question") or st.session_state.practice_question is None:
                st.session_state.practice_question = get_random_question(questions)
                st.session_state.practice_selected = None
        with right:
            st.progress(
                st.session_state.practice_score / st.session_state.practice_attempted
                if st.session_state.practice_attempted
                else 0.0,
                text=f"Session Score: {st.session_state.practice_score}/{st.session_state.practice_attempted}",
            )

    question = st.session_state.practice_question
    st.markdown(
        f"""
        <div class='question-card'>
            <b>Difficulty:</b> {question['difficulty']} &nbsp;&nbsp; <b>Tag:</b> {question['tag']}
            <h4 style='margin:.55rem 0 0'>{question['question']}</h4>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.session_state.practice_selected = st.radio(
        "Choose your answer:",
        question["options"],
        index=None,
        key="practice_option",
    )

    if st.button("✅ Submit Practice Answer") and st.session_state.practice_selected:
        is_correct = st.session_state.practice_selected == question["answer"]
        st.session_state.practice_attempted += 1

        if is_correct:
            st.session_state.practice_score += 1
            st.success("Correct! Great work ⚡")
        else:
            st.error(f"Not quite. Correct answer: {question['answer']}")

        tracker.record_attempt(chapter, is_correct)


def render_mock_mode() -> None:
    """Render timed 10-question mixed mock test."""
    st.markdown("## 🧪 Mock Test Mode")
    all_questions = get_all_questions()

    if not st.session_state.mock_started:
        st.info("Launch a timed 10-question mixed test.")
        if st.button("🚀 Start Mock Test"):
            st.session_state.mock_questions = get_mock_test_questions(all_questions, 10)
            st.session_state.mock_answers = {}
            st.session_state.mock_submitted = False
            st.session_state.mock_scored = False
            st.session_state.mock_started = True
            st.session_state.mock_start_time = time.time()
        return

    elapsed = int(time.time() - st.session_state.mock_start_time)
    st.markdown(f"### ⏱️ Elapsed Time: `{elapsed}` seconds")

    for idx, question in enumerate(st.session_state.mock_questions, start=1):
        st.markdown(
            f"<div class='glass'><b>Q{idx}.</b> {question['question']}<br/>"
            f"<small>{question['chapter']} • {question['difficulty']} • {question['tag']}</small></div>",
            unsafe_allow_html=True,
        )
        selected = st.radio(
            f"Answer Q{idx}",
            question["options"],
            index=None,
            key=f"mock_q_{idx}",
        )
        st.session_state.mock_answers[idx] = selected

    action1, action2 = st.columns(2)
    if action1.button("📤 Submit Mock Test"):
        st.session_state.mock_submitted = True
    if action2.button("🔁 Reset Mock"):
        st.session_state.mock_started = False
        st.session_state.mock_submitted = False
        st.session_state.mock_scored = False
        st.rerun()

    if st.session_state.mock_submitted:
        correct = 0
        wrong = 0

        st.markdown("## 🏁 Mock Result")
        for idx, question in enumerate(st.session_state.mock_questions, start=1):
            selected = st.session_state.mock_answers.get(idx)
            is_correct = selected == question["answer"]
            if is_correct:
                correct += 1
                st.success(f"Q{idx}: Correct")
            else:
                wrong += 1
                st.error(f"Q{idx}: Wrong • Correct: {question['answer']}")

            if not st.session_state.mock_scored:
                tracker.record_attempt(question["chapter"], is_correct)

        col1, col2, col3 = st.columns(3)
        col1.metric("Score", f"{correct}/10")
        col2.metric("Correct", correct)
        col3.metric("Wrong", wrong)
        st.session_state.mock_scored = True


def render_progress() -> None:
    """Render progress summary in sidebar."""
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
    """Main Streamlit app entry point."""
    initialize_state()
    inject_styles()

    st.markdown(
        """
        <div class="hero">
            <h1 style="margin:0;">⚛️ Physics JEE & NSEP Prep</h1>
            <p style="margin:.45rem 0 0; opacity:.95;">Modern dashboard for focused Physics study, chapter practice, and timed mocks.</p>
            <span class="mode-chip">Structured Syllabus</span>
            <span class="mode-chip">Formula-first Revision</span>
            <span class="mode-chip">Exam-style MCQs</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    section = st.sidebar.selectbox("Select Topic", get_sections())
    st.sidebar.caption(f"Section Weightage: {SYLLABUS_CONTENT[section]['section_weightage']}")
    chapter = st.sidebar.selectbox("Select Chapter", get_chapters(section))
    mode = st.sidebar.radio("Mode", ["Study Mode", "Practice Mode", "Mock Test Mode"])

    render_progress()
    render_top_metrics(section, chapter, mode)

    if mode == "Study Mode":
        render_study_mode(section, chapter)
    elif mode == "Practice Mode":
        render_practice_mode(chapter)
    else:
        render_mock_mode()


if __name__ == "__main__":
    main()
