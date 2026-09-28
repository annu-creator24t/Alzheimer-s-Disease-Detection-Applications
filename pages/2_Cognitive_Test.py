import streamlit as st
from utils import load_css
import time
import random

load_css()

# ── Session State Init ──────────────────────────────────────
if "stage" not in st.session_state:
    st.session_state.stage = 0
if "scores" not in st.session_state:
    st.session_state.scores = {}
if "memory_words" not in st.session_state:
    st.session_state.memory_words = random.sample(
        ["Apple", "River", "Pencil", "House", "Sunset", "Mirror", "Clock", "Garden"], 4
    )
if "show_words" not in st.session_state:
    st.session_state.show_words = True
if "word_timer" not in st.session_state:
    st.session_state.word_timer = None
if "distractor_done" not in st.session_state:
    st.session_state.distractor_done = False

# ── Page Header ─────────────────────────────────────────────
st.markdown("""
<div class="assess-header">
    <div class="assess-badge">🧪 Clinical Screening Tool</div>
    <h1 class="assess-title">Mini Cognitive Assessment</h1>
    <p class="assess-desc">
        This assessment screens for early signs of cognitive decline across memory,
        attention, language, and reasoning — key markers in Alzheimer's detection.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Progress Bar ─────────────────────────────────────────────
total_stages = 6
progress = st.session_state.stage / total_stages
st.markdown(f"""
<div class="progress-wrap">
    <div class="progress-label">Section {min(st.session_state.stage + 1, total_stages)} of {total_stages}</div>
    <div class="progress-track">
        <div class="progress-fill" style="width:{progress*100:.0f}%"></div>
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# STAGE 0 — Orientation
# ════════════════════════════════════════════════════════════
if st.session_state.stage == 0:
    st.markdown("""
    <div class="section-card">
        <div class="section-num">01</div>
        <h2>Orientation & Awareness</h2>
        <p class="section-hint">These questions assess your awareness of time and place — a key early indicator.</p>
    </div>
    """, unsafe_allow_html=True)

    from datetime import datetime
    now = datetime.now()

    col1, col2 = st.columns(2)
    with col1:
        day = st.selectbox("What day of the week is it?",
            ["", "Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"])
        month = st.selectbox("What month is it?",
            ["", "January","February","March","April","May","June",
             "July","August","September","October","November","December"])
    with col2:
        year = st.number_input("What year is it?", min_value=2000, max_value=2100,
                               value=2024, step=1)
        season = st.selectbox("What season is it?",
            ["", "Spring", "Summer", "Autumn", "Winter"])

    place = st.text_input("Where are you right now? (city or place)")

    if st.button("Next →", key="next0"):
        score = 0
        correct_day = now.strftime("%A")
        correct_month = now.strftime("%B")
        correct_year = now.year
        if day == correct_day: score += 1
        if month == correct_month: score += 1
        if year == correct_year: score += 1
        if place.strip() != "": score += 1
        # Season scoring
        m = now.month
        correct_season = ("Winter" if m in [12,1,2] else
                          "Spring" if m in [3,4,5] else
                          "Summer" if m in [6,7,8] else "Autumn")
        if season == correct_season: score += 1
        st.session_state.scores["orientation"] = score  # max 5
        st.session_state.stage = 1
        st.rerun()

# ════════════════════════════════════════════════════════════
# STAGE 1 — Word Memory (Encoding)
# ════════════════════════════════════════════════════════════
elif st.session_state.stage == 1:
    words = st.session_state.memory_words
    st.markdown("""
    <div class="section-card">
        <div class="section-num">02</div>
        <h2>Memory — Word Encoding</h2>
        <p class="section-hint">Study the words below carefully. You will be asked to recall them later.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="word-display">
    """ + "".join([f'<span class="word-chip">{w}</span>' for w in words]) + """
    </div>
    """, unsafe_allow_html=True)

    st.info("📌 Take a moment to memorize these words before continuing.")

    if st.button("I've memorized them →", key="next1"):
        st.session_state.stage = 2
        st.rerun()

# ════════════════════════════════════════════════════════════
# STAGE 2 — Attention / Distractor (Serial 7s)
# ════════════════════════════════════════════════════════════
elif st.session_state.stage == 2:
    st.markdown("""
    <div class="section-card">
        <div class="section-num">03</div>
        <h2>Attention & Concentration</h2>
        <p class="section-hint">
            Count backward from 100 by subtracting 7 each time.
            This distractor also tests sustained attention — a key Alzheimer's marker.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3, col4, col5 = st.columns(5)
    answers = []
    expected = [93, 86, 79, 72, 65]
    labels = ["100 − 7", "93 − 7", "86 − 7", "79 − 7", "72 − 7"]

    inputs = []
    for i, col in enumerate([col1, col2, col3, col4, col5]):
        with col:
            val = col.number_input(labels[i], step=1, value=0, key=f"serial_{i}")
            inputs.append(val)

    if st.button("Next →", key="next2"):
        score = sum(1 for i, v in enumerate(inputs) if v == expected[i])
        st.session_state.scores["attention"] = score  # max 5
        st.session_state.stage = 3
        st.rerun()

# ════════════════════════════════════════════════════════════
# STAGE 3 — Word Recall
# ════════════════════════════════════════════════════════════
elif st.session_state.stage == 3:
    st.markdown("""
    <div class="section-card">
        <div class="section-num">04</div>
        <h2>Memory — Word Recall</h2>
        <p class="section-hint">
            Type the words you memorized earlier. Each correctly recalled word scores a point.
        </p>
    </div>
    """, unsafe_allow_html=True)

    recalled = st.text_area("Type the words you remember (separated by commas or spaces):",
                            placeholder="e.g. Apple, River, Clock...")

    if st.button("Next →", key="next3"):
        words = st.session_state.memory_words
        recalled_clean = [w.strip().lower() for w in recalled.replace(",", " ").split()]
        score = sum(1 for w in words if w.lower() in recalled_clean)
        st.session_state.scores["recall"] = score  # max 4
        st.session_state.stage = 4
        st.rerun()

# ════════════════════════════════════════════════════════════
# STAGE 4 — Language & Reasoning
# ════════════════════════════════════════════════════════════
elif st.session_state.stage == 4:
    st.markdown("""
    <div class="section-card">
        <div class="section-num">05</div>
        <h2>Language & Reasoning</h2>
        <p class="section-hint">These questions test verbal reasoning and pattern recognition.</p>
    </div>
    """, unsafe_allow_html=True)

    score = 0

    q1 = st.radio("What do a dog and a cat have in common?",
        ["", "One barks, one meows", "They are both animals", "They have four legs", "They are pets"],
        index=0)

    q2 = st.radio("Complete the sequence: 3, 6, 9, 12, ___",
        ["", "13", "14", "15", "16"], index=0)

    q3 = st.radio("Which word does NOT belong?",
        ["", "Apple", "Banana", "Carrot", "Mango"], index=0)

    q4 = st.text_input('Repeat this phrase exactly: "No ifs, ands, or buts"')

    if st.button("Next →", key="next4"):
        if q1 == "They are both animals": score += 1
        if q2 == "15": score += 1
        if q3 == "Carrot": score += 1
        phrase = "no ifs ands or buts"
        if q4.lower().replace(",","").replace(".","").strip() == phrase: score += 1
        st.session_state.scores["language"] = score  # max 4
        st.session_state.stage = 5
        st.rerun()

# ════════════════════════════════════════════════════════════
# STAGE 5 — Visuospatial (Clock / Shape)
# ════════════════════════════════════════════════════════════
elif st.session_state.stage == 5:
    st.markdown("""
    <div class="section-card">
        <div class="section-num">06</div>
        <h2>Visuospatial & Executive Function</h2>
        <p class="section-hint">These tasks assess spatial reasoning and executive planning.</p>
    </div>
    """, unsafe_allow_html=True)

    score = 0

    q1 = st.radio("A clock shows 3:00. Where is the minute hand pointing?",
        ["", "12", "3", "6", "9"], index=0)

    q2 = st.radio("Which shape has the most sides?",
        ["", "Triangle", "Square", "Pentagon", "Circle"], index=0)

    q3 = st.radio("If you fold a square piece of paper in half diagonally, you get a:",
        ["", "Rectangle", "Triangle", "Pentagon", "Circle"], index=0)

    q4 = st.radio("Mirror image: If your right hand points left, your mirror image points:",
        ["", "Left", "Right", "Up", "Down"], index=0)

    if st.button("Submit Assessment ✓", key="next5"):
        if q1 == "12": score += 1
        if q2 == "Pentagon": score += 1
        if q3 == "Triangle": score += 1
        if q4 == "Right": score += 1
        st.session_state.scores["visuospatial"] = score  # max 4
        st.session_state.stage = 6
        st.rerun()

# ════════════════════════════════════════════════════════════
# STAGE 6 — Results
# ════════════════════════════════════════════════════════════
elif st.session_state.stage == 6:
    s = st.session_state.scores
    orientation  = s.get("orientation", 0)   # /5
    attention    = s.get("attention", 0)      # /5
    recall       = s.get("recall", 0)         # /4
    language     = s.get("language", 0)       # /4
    visuospatial = s.get("visuospatial", 0)   # /4

    raw_total = orientation + attention + recall + language + visuospatial
    max_total = 22
    pct = round((raw_total / max_total) * 100)

    if pct >= 80:
        risk_label = "Low Risk"
        risk_color = "#16a34a"
        risk_bg    = "#f0fdf4"
        risk_icon  = "✅"
        risk_desc  = "Cognitive performance appears normal. Continue routine monitoring."
    elif pct >= 60:
        risk_label = "Mild Concern"
        risk_color = "#d97706"
        risk_bg    = "#fffbeb"
        risk_icon  = "⚠️"
        risk_desc  = "Some areas show mild decline. A clinical follow-up is recommended."
    else:
        risk_label = "High Risk"
        risk_color = "#dc2626"
        risk_bg    = "#fef2f2"
        risk_icon  = "🔴"
        risk_desc  = "Multiple cognitive domains show concern. Please consult a neurologist."

    st.markdown(f"""
    <div class="result-card" style="border-color:{risk_color}; background:{risk_bg};">
        <div class="result-icon">{risk_icon}</div>
        <div class="result-score">{pct}<span style="font-size:1.5rem">%</span></div>
        <div class="result-label" style="color:{risk_color}">{risk_label}</div>
        <div class="result-desc">{risk_desc}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<h3 style='color:#0b3c5d'>📊 Domain Breakdown</h3>", unsafe_allow_html=True)

    domains = {
        "🧭 Orientation":     (orientation, 5),
        "🔢 Attention":       (attention, 5),
        "🧠 Memory Recall":   (recall, 4),
        "💬 Language":        (language, 4),
        "🔷 Visuospatial":    (visuospatial, 4),
    }

    for label, (got, mx) in domains.items():
        bar_pct = int((got / mx) * 100)
        bar_color = "#16a34a" if bar_pct >= 75 else "#d97706" if bar_pct >= 50 else "#dc2626"
        st.markdown(f"""
        <div class="domain-row">
            <div class="domain-label">{label}</div>
            <div class="domain-track">
                <div class="domain-fill" style="width:{bar_pct}%; background:{bar_color};"></div>
            </div>
            <div class="domain-score">{got}/{mx}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.caption("⚠️ This tool is for screening purposes only and does not replace clinical diagnosis.")

    if st.button("🔄 Retake Assessment", key="retake"):
        for key in ["stage","scores","memory_words","show_words","word_timer","distractor_done"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()