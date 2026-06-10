# =====================================================
# EduAI - AI-Powered Study Assistant
# SDG 4: Quality Education
# Built for Lenovo LEAP AI Internship 2026
# =====================================================

import streamlit as st
import google.generativeai as genai

# ─── PAGE SETUP ────────────────────────────────────
st.set_page_config(
    page_title="EduAI - Smart Study Assistant",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ─── STYLING ───────────────────────────────────────
st.markdown("""
<style>
    .hero {
        background: linear-gradient(135deg, #4f46e5, #7c3aed);
        color: white;
        padding: 2rem 2.5rem;
        border-radius: 16px;
        margin-bottom: 2rem;
        text-align: center;
    }
    .hero h1 { font-size: 2.2rem; margin: 0 0 0.4rem; }
    .hero p  { font-size: 1rem; opacity: 0.88; margin: 0; }
    .sdg-tag {
        display: inline-block;
        background: #166534;
        color: #dcfce7;
        padding: 0.25rem 0.75rem;
        border-radius: 20px;
        font-size: 0.78rem;
        font-weight: 600;
        margin-bottom: 1rem;
    }
    .feature-card {
        background: #f8fafc;
        border-left: 4px solid #6366f1;
        padding: 1rem 1.2rem;
        border-radius: 0 10px 10px 0;
        margin-bottom: 0.75rem;
    }
    .feature-card strong { color: #4338ca; }
    .stat-box {
        background: white;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 1rem;
        text-align: center;
        box-shadow: 0 1px 3px rgba(0,0,0,0.06);
    }
    .stat-box h2 { margin: 0; color: #4f46e5; font-size: 1.8rem; }
    .stat-box p  { margin: 0.2rem 0 0; color: #64748b; font-size: 0.85rem; }
</style>
""", unsafe_allow_html=True)

# ─── GEMINI API ────────────────────────────────────
# IMPORTANT: Replace with your actual Gemini API key
API_KEY = "YOUR_GEMINI_API_KEY_HERE"

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel('gemini-3.5-flash')
    api_ready = True
except Exception as e:
    api_ready = False
    print(f"API Error: {e}")

# ─── SESSION STATE ──────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "questions_asked" not in st.session_state:
    st.session_state.questions_asked = 0
if "topics_covered" not in st.session_state:
    st.session_state.topics_covered = []

# ─── HELPER ─────────────────────────────────────────
def ask_gemini(prompt):
    if not api_ready:
        return "⚠️ Please add your Gemini API key in app.py to enable AI responses."
    try:
        response = model.generate_content(prompt)
        st.session_state.questions_asked += 1
        return response.text
    except Exception as e:
        return f"Error: {str(e)}. Please check your API key."

# ─── SIDEBAR ─────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🎓 EduAI")
    st.markdown("*Your AI Study Companion*")
    st.markdown('<div class="sdg-tag">🌍 SDG 4: Quality Education</div>', unsafe_allow_html=True)
    st.markdown("---")

    page = st.radio("Navigate", [
        "🏠  Home",
        "💬  AI Tutor Chat",
        "📖  Concept Explainer",
        "❓  Quiz Generator",
        "📝  Text Summarizer",
        "💡  Study Tips"
    ])

    st.markdown("---")
    st.markdown("### 📊 Your Session")
    col1, col2 = st.columns(2)
    col1.metric("Questions", st.session_state.questions_asked)
    col2.metric("Topics", len(st.session_state.topics_covered))

    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

    st.markdown("---")
    st.caption("Built for Lenovo LEAP 2026\nBy: Minnath Kailas Tambat")

# ════════════════════════════════════════════════════
# PAGE: HOME
# ════════════════════════════════════════════════════
if "Home" in page:
    st.markdown("""
    <div class="hero">
        <h1>🎓 EduAI</h1>
        <p>AI-Powered Study Assistant for Every Student</p>
    </div>
    """, unsafe_allow_html=True)

    # Stats
    c1, c2, c3, c4 = st.columns(4)
    c1.markdown('<div class="stat-box"><h2>🌍</h2><p>SDG 4: Quality Education</p></div>', unsafe_allow_html=True)
    c2.markdown('<div class="stat-box"><h2>5</h2><p>AI-Powered Features</p></div>', unsafe_allow_html=True)
    c3.markdown('<div class="stat-box"><h2>24/7</h2><p>Available Anytime</p></div>', unsafe_allow_html=True)
    c4.markdown('<div class="stat-box"><h2>Free</h2><p>Zero Cost for Students</p></div>', unsafe_allow_html=True)

    st.markdown("---")

    col_left, col_right = st.columns([1.2, 1])

    with col_left:
        st.subheader("🎯 The Problem We Solve")
        st.markdown("""
        In India, millions of students — especially in **tier 2 and tier 3 cities** —
        do not have access to personalized tutoring. Private coaching is expensive,
        and teachers in classrooms cannot address every student's doubts individually.

        **EduAI** gives every student a free, 24/7 AI tutor that explains concepts,
        generates quizzes, summarizes notes, and provides study guidance — directly
        addressing **SDG Goal 4: Quality Education**.
        """)

        st.subheader("✨ Features")
        features = [
            ("💬 AI Tutor Chat",      "Chat with your AI tutor. Ask anything about any subject."),
            ("📖 Concept Explainer",   "Enter any topic — get a clear explanation with examples."),
            ("❓ Quiz Generator",      "Auto-generate MCQ quizzes to test your understanding."),
            ("📝 Text Summarizer",     "Paste long notes and get a crisp, organized summary."),
            ("💡 Study Tips",          "Get personalized strategies to study smarter.")
        ]
        for title, desc in features:
            st.markdown(
                f'<div class="feature-card"><strong>{title}</strong><br>'
                f'<span style="color:#475569;font-size:0.9rem">{desc}</span></div>',
                unsafe_allow_html=True
            )

    with col_right:
        st.subheader("🚀 Get Started")
        st.info("👈 Use the sidebar to navigate between features.")
        st.markdown("""
        **Recommended order for first time:**
        1. Try **AI Tutor Chat** — ask any question
        2. Use **Concept Explainer** for your toughest topic
        3. Test yourself with **Quiz Generator**
        4. Summarize your notes with **Text Summarizer**
        5. Get **Study Tips** for your next exam
        """)

        st.subheader("🏗️ Technology Stack")
        st.markdown("""
        | Layer | Technology |
        |-------|-----------|
        | Language | Python 3.10+ |
        | UI Framework | Streamlit |
        | AI Model | Google Gemini 1.5 Flash |
        | Deployment | Streamlit Cloud (free) |
        """)

# ════════════════════════════════════════════════════
# PAGE: AI TUTOR CHAT
# ════════════════════════════════════════════════════
elif "Tutor" in page:
    st.title("💬 AI Tutor Chat")
    st.markdown("Your personal AI teacher. Ask questions on **any subject, any time!**")

    TUTOR_SYSTEM = """You are EduAI, a friendly and patient AI tutor helping Indian college students.
You explain every concept in simple, clear language using step-by-step breakdowns and real-world analogies.
You are encouraging, never make students feel bad for not knowing something.
You answer questions about science, math, programming, history, economics, and any other subject.
Always end your response with one follow-up suggestion like "Want me to quiz you on this?" or "Should I give you a simpler example?" """

    # Display chat history
    for msg in st.session_state.chat_history:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if not st.session_state.chat_history:
        st.info("👋 Hi! I'm your EduAI tutor. Ask me anything — a topic you're confused about, a concept you want explained, or a subject you're studying!")

    # Input
    if user_input := st.chat_input("Ask your tutor anything..."):
        st.session_state.chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)

        # Build prompt with history
        history_str = "\n".join(
            [f"{m['role'].upper()}: {m['content']}" for m in st.session_state.chat_history[-6:]]
        )
        prompt = f"{TUTOR_SYSTEM}\n\nConversation so far:\n{history_str}\n\nPlease respond as the ASSISTANT:"

        with st.spinner("EduAI is thinking..."):
            reply = ask_gemini(prompt)

        st.session_state.chat_history.append({"role": "assistant", "content": reply})
        with st.chat_message("assistant"):
            st.markdown(reply)

# ════════════════════════════════════════════════════
# PAGE: CONCEPT EXPLAINER
# ════════════════════════════════════════════════════
elif "Concept" in page:
    st.title("📖 Concept Explainer")
    st.markdown("Enter any topic and get a **detailed, beginner-friendly explanation** with examples.")
    st.markdown("---")

    topic = st.text_input("📚 Topic:", placeholder="e.g., Photosynthesis, Newton's Laws, Python Functions, Indian Constitution...")
    
    col1, col2 = st.columns(2)
    subject  = col1.selectbox("Subject:", ["General", "Science", "Mathematics", "Programming / CS", "History", "Economics", "English", "Other"])
    level    = col2.radio("Level:", ["Beginner (simple)", "Intermediate", "Advanced"], horizontal=True)

    if st.button("✨ Explain This Topic", type="primary", use_container_width=True) and topic:
        with st.spinner(f"Generating explanation for '{topic}'..."):
            prompt = f"""Explain "{topic}" (subject: {subject}) at {level} level for an Indian college student.

Structure your response EXACTLY like this:

## 📌 Simple Definition
(2–3 lines. As if explaining to a 10-year-old.)

## 🔍 Full Explanation
(Clear step-by-step breakdown with sub-headings if needed.)

## 💡 Real-World Example
(A relatable example from daily life or Indian context.)

## 🧠 Key Points to Remember
(5 bullet points of the most important things.)

## ❓ Common Student Questions About This
(2–3 questions students usually have, with short answers.)

Use simple language. Make it engaging and easy to follow!"""

            explanation = ask_gemini(prompt)

            if topic not in st.session_state.topics_covered:
                st.session_state.topics_covered.append(topic)

        st.markdown("---")
        st.markdown(explanation)

        st.download_button(
            "📥 Download Explanation",
            data=explanation,
            file_name=f"explanation_{topic.replace(' ', '_')}.txt",
            mime="text/plain"
        )

# ════════════════════════════════════════════════════
# PAGE: QUIZ GENERATOR
# ════════════════════════════════════════════════════
elif "Quiz" in page:
    st.title("❓ Quiz Generator")
    st.markdown("Auto-generate **MCQ practice quizzes** on any topic to test your knowledge!")
    st.markdown("---")

    quiz_topic  = st.text_input("📚 Quiz Topic:", placeholder="e.g., Python loops, Photosynthesis, World War 2...")
    
    col1, col2 = st.columns(2)
    num_q       = col1.slider("Number of Questions:", 3, 10, 5)
    difficulty  = col2.select_slider("Difficulty:", ["Easy", "Medium", "Hard", "Mixed"])

    if st.button("🎯 Generate Quiz", type="primary", use_container_width=True) and quiz_topic:
        with st.spinner(f"Creating {num_q} questions on '{quiz_topic}'..."):
            prompt = f"""Create a {difficulty} difficulty MCQ quiz with EXACTLY {num_q} questions about "{quiz_topic}" for Indian engineering students.

For EACH question use this EXACT format:

**Q[number]. [Question text]**
- A) [Option A]
- B) [Option B]
- C) [Option C]
- D) [Option D]

✅ **Answer: [Letter]) [Correct Option]**
*Why: [One-line explanation of why this answer is correct]*

---

Make questions that test real understanding. Avoid trick questions."""

            quiz = ask_gemini(prompt)

        st.markdown("---")
        st.subheader(f"📋 Quiz: {quiz_topic}")
        st.markdown(quiz)
        st.success(f"✅ {num_q} questions generated! Read all options carefully before checking the answer.")
        
        st.download_button(
            "📥 Download Quiz",
            data=quiz,
            file_name=f"quiz_{quiz_topic.replace(' ', '_')}.txt",
            mime="text/plain"
        )

# ════════════════════════════════════════════════════
# PAGE: TEXT SUMMARIZER
# ════════════════════════════════════════════════════
elif "Summarizer" in page:
    st.title("📝 Text Summarizer")
    st.markdown("Paste your long notes or textbook content — get a **clean, organized summary** instantly.")
    st.markdown("---")

    text_in = st.text_area("📄 Paste your text here:", height=220,
                            placeholder="Paste notes, article, textbook chapter, or any text here...")

    col1, col2 = st.columns(2)
    style = col1.radio("Summary format:", ["📌 Bullet Points", "📄 Short Paragraph", "🗂️ Key Terms Only"])
    lang  = col2.radio("Language:", ["English", "Simple English (easy words)"])

    if st.button("📝 Summarize Now", type="primary", use_container_width=True) and text_in:
        with st.spinner("Summarizing your text..."):
            prompt = f"""Summarize the following text.
Format: {style}
Language style: {lang}

Rules:
- If Bullet Points: Use clear, concise bullets. Group related points.
- If Short Paragraph: Write a 3–4 sentence summary capturing the key message.
- If Key Terms Only: List the most important terms with one-line definitions.

Text:
{text_in}"""
            summary = ask_gemini(prompt)

        st.markdown("---")
        st.subheader("📋 Your Summary")
        st.markdown(summary)

        # Word count stats
        w_orig  = len(text_in.split())
        w_summ  = len(summary.split())
        w_pct   = round((1 - w_summ / max(w_orig, 1)) * 100)

        c1, c2, c3 = st.columns(3)
        c1.metric("Original words", w_orig)
        c2.metric("Summary words", w_summ)
        c3.metric("Reduction", f"{w_pct}%")

        st.download_button(
            "📥 Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain"
        )

# ════════════════════════════════════════════════════
# PAGE: STUDY TIPS
# ════════════════════════════════════════════════════
elif "Tips" in page:
    st.title("💡 Study Tips & Strategies")
    st.markdown("Get **personalized, actionable study advice** tailored to your situation.")
    st.markdown("---")

    challenge = st.selectbox("What do you need help with?", [
        "How to study effectively in less time",
        "How to prepare for semester exams",
        "How to manage time between college and self-study",
        "How to improve memory and retention",
        "How to stay focused and avoid distractions",
        "How to deal with exam stress and anxiety",
        "How to learn programming and coding faster",
        "How to prepare for internship/placement",
        "How to build a study routine that actually works"
    ])

    year = st.radio("Your year:", ["1st Year", "2nd Year", "3rd Year", "4th Year"], horizontal=True)

    if st.button("💡 Get My Study Tips", type="primary", use_container_width=True):
        with st.spinner("Generating personalized tips for you..."):
            prompt = f"""Give practical, specific study tips for the challenge: "{challenge}"
For a {year} engineering student in India.

Structure your response as:

## 🎯 Your 5 Key Tips
(5 specific, actionable tips — not generic. Explain HOW to do each one.)

## ⚡ What To Do TODAY
(One very specific action they can take in the next 30 minutes.)

## 📅 Suggested Daily Schedule
(A practical schedule showing when to study, rest, and review.)

## 🚫 Mistakes to Avoid
(3 common mistakes students make with this challenge.)

Be direct, encouraging, and realistic. Use Indian context where helpful."""

            tips = ask_gemini(prompt)

        st.markdown("---")
        st.markdown(tips)
