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
    "Mechanics": "https://images.unsplash.com/photo-1635070041078-e363dbe005cb?auto=format&fit=crop&w=1400&q=80",
    "Heat & Thermodynamics": "https://images.unsplash.com/photo-1462331940025-496dfbfc7564?auto=format&fit=crop&w=1400&q=80",
    "Oscillations & Waves": "https://images.unsplash.com/photo-1518770660439-4636190af475?auto=format&fit=crop&w=1400&q=80",
    "Electricity & Magnetism": "https://images.unsplash.com/photo-1555664424-778a1e5e1b48?auto=format&fit=crop&w=1400&q=80",
    "Optics": "https://images.unsplash.com/photo-1517048676732-d65bc937f952?auto=format&fit=crop&w=1400&q=80",
}


def inject_styles() -> None:
    """Inject modern UI styling, animations, and a subtle abstract background."""
    st.markdown(
        """
        <style>
            .stApp {
                background:
                    radial-gradient(circle at 10% 20%, rgba(0, 194, 255, 0.15), transparent 30%),
                    radial-gradient(circle at 85% 10%, rgba(123, 97, 255, 0.18), transparent 28%),
                    radial-gradient(circle at 80% 80%, rgba(0, 255, 170, 0.10), transparent 32%),
                    linear-gradient(120deg, #0b1020 0%, #12192f 40%, #171435 100%);
                color: #f8fbff;
            }

            [data-testid="stSidebar"] {
                background: linear-gradient(180deg, rgba(13, 20, 39, 0.95), rgba(11, 16, 32, 0.88));
                backdrop-filter: blur(14px);
                border-right: 1px solid rgba(255, 255, 255, 0.08);
            }

            .hero-card {
                background: linear-gradient(135deg, rgba(41, 82, 255, 0.35), rgba(0, 198, 255, 0.14));
                border: 1px solid rgba(255, 255, 255, 0.2);
                border-radius: 20px;
                padding: 1.2rem 1.4rem;
                box-shadow: 0 12px 30px rgba(0, 0, 0, 0.25);
                animation: floatIn 0.8s ease-out;
            }

            .mode-chip {
                display: inline-block;
                padding: 0.2rem 0.7rem;
                margin-right: 0.4rem;
                border-radius: 999px;
                font-size: 0.78rem;
                font-weight: 600;
                border: 1px solid rgba(255, 255, 255, 0.22);
                background: rgba(255, 255, 255, 0.10);
            }

            .glass-panel {
                background: rgba(255, 255, 255, 0.07);
                border: 1px solid rgba(255, 255, 255, 0.18);
                border-radius: 16px;
                padding: 1rem;
            }

            @keyframes floatIn {
                0% { opacity: 0; transform: translateY(12px); }
                100% { opacity: 1; transform: translateY(0); }
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
        "practice_submitted": False,
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


def render_study_mode(section: str, chapter: str) -> None:
    chapter_data = SYLLABUS_CONTENT[section]["chapters"][chapter]
    st.image(SECTION_IMAGES.get(section), use_container_width=True)
    st.markdown(
        f"""
        <div class="hero-card">
            <h2 style="margin:0;">{chapter} — Study Notes</h2>
            <p style="margin:0.4rem 0 0; opacity:0.9;">Section: {section} • Chapter Weightage: <b>{chapter_data['weightage']}</b></p>
            <div style="margin-top:0.65rem;">
                <span class="mode-chip">JEE Main</span>
                <span class="mode-chip">NSEP</span>
                <span class="mode-chip">Formula Revision</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("### ✨ Important Formulas")
    for formula in chapter_data["formulas"]:
        st.latex(formula)

    st.markdown("### 🧠 Key Concepts")
    for concept in chapter_data["concepts"]:
        st.markdown(f"- {concept}")


def render_practice_mode(chapter: str) -> None:
    questions = QUESTION_BANK.get(chapter, [])
    st.markdown(f"## 🎯 Practice Arena — {chapter}")

    if not questions:
        st.warning("No questions available for this chapter.")
        return

    if st.button("🎲 Generate Random Question") or st.session_state.practice_question is None:
        st.session_state.practice_question = get_random_question(questions)
        st.session_state.practice_selected = None
        st.session_state.practice_submitted = False

    question = st.session_state.practice_question
    st.markdown(
        f"<div class='glass-panel'><b>Difficulty:</b> {question['difficulty']} &nbsp;|&nbsp; "
        f"<b>Tag:</b> {question['tag']}<br/><br/><h4 style='margin:0'>{question['question']}</h4></div>",
        unsafe_allow_html=True,
    )

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
    st.markdown("## 🧪 Mock Test Mode")
    all_questions = get_all_questions()

    if not st.session_state.mock_started:
        if st.button("🚀 Start 10-Question Mock Test"):
            st.session_state.mock_questions = get_mock_test_questions(all_questions, 10)
            st.session_state.mock_answers = {}
            st.session_state.mock_submitted = False
            st.session_state.mock_scored = False
            st.session_state.mock_started = True
            st.session_state.mock_start_time = time.time()

    if not st.session_state.mock_started:
        st.info("Start the mock test to begin.")
        return

    elapsed = int(time.time() - st.session_state.mock_start_time)
    st.markdown(f"### ⏱️ Timer: `{elapsed}` seconds")

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

            if not st.session_state.mock_scored:
                tracker.record_attempt(question["chapter"], is_correct)

        st.metric("Score", f"{correct}/10")
        st.write(f"Correct: {correct} | Wrong: {wrong}")
        st.session_state.mock_scored = True


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
    inject_styles()

    st.markdown(
        """
        <div class="hero-card">
            <h1 style="margin:0;">⚛️ Physics JEE & NSEP Prep</h1>
            <p style="margin:0.4rem 0 0;opacity:0.95;">A modern prep cockpit for formulas, concepts, chapter-wise practice, and timed mock tests.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

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
