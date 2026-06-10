# 🎓 EduAI — AI-Powered Study Assistant

> SDG 4: Quality Education | Lenovo LEAP AI Internship 2026

EduAI is a free, AI-powered study assistant built to help Indian students
learn any subject through personalized explanations, quizzes, summaries,
and 24/7 tutoring — directly addressing the UN SDG Goal 4: Quality Education.

---

## 🌍 Problem Statement

Millions of students in India — especially in tier 2 and tier 3 cities like Wani —
lack access to affordable, personalized tutoring. Private coaching is expensive,
and classroom teachers cannot address every student's doubts. EduAI fills this
gap by providing free, intelligent tutoring to any student with internet access.

---

## ✨ Features

| Feature | Description |
|---------|-------------|
| 💬 AI Tutor Chat | Have a full conversation with your AI tutor on any subject |
| 📖 Concept Explainer | Get clear, structured explanations of any topic |
| ❓ Quiz Generator | Auto-generate MCQ quizzes to test your knowledge |
| 📝 Text Summarizer | Summarize long notes into concise bullet points |
| 💡 Study Tips | Get personalized study strategies and routines |

---

## 🏗️ Tech Stack

- **Language**: Python 3.10+
- **UI Framework**: Streamlit
- **AI Model**: Google Gemini 1.5 Flash (via Google Generative AI API)
- **Deployment**: Streamlit Cloud (free)

---

## 🚀 How to Run Locally

### Step 1: Clone the repository
```bash
git clone https://github.com/YOUR_USERNAME/eduai-study-assistant.git
cd eduai-study-assistant
```

### Step 2: Install dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Add your Gemini API key
Open `app.py` and replace:
```python
API_KEY = "YOUR_GEMINI_API_KEY_HERE"
```
with your actual API key from https://aistudio.google.com

### Step 4: Run the app
```bash
streamlit run app.py
```

The app will open at `http://localhost:8501`

---

## 🔑 Getting a Free Gemini API Key

1. Go to https://aistudio.google.com
2. Sign in with your Google account
3. Click "Get API Key"
4. Copy the key and paste it in `app.py`

No credit card required!

---

## 📁 Project Structure

```
eduai-study-assistant/
│
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
```

---

## 🔮 Future Scope

- Add multilingual support (Hindi, Marathi)
- Voice input/output for accessibility
- Mobile app version
- Track student progress over time
- Add subject-specific modules (JEE, NEET prep)
- Integrate with college LMS systems

---

## 👤 Author

**Minnath Kailas Tambat**  
First Year B.Tech Student | Maharashtra  
Lenovo LEAP AI Internship 2026  
CSRBOX / BharatCares

---

## 📄 License

This project is open source and available under the MIT License.
