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
<div class="clinical-header">
    <div class="clinical-badge">Clinical Screening Instrument</div>
    <h1 class="header-title">Mini Cognitive Assessment Protocol</h1>
    <p class="header-desc">
        A standardized screening tool assessing primary cognitive domains: orientation, 
        immediate memory encoding, sustained attention, delayed recall, language, and executive visuospatial function.
    </p>
</div>
""", unsafe_allow_html=True)

# ── Progress Indicator ───────────────────────────────────────
total_stages = 6
current_step = min(st.session_state.stage + 1, total_stages)
progress = st.session_state.stage / total_stages

stage_names = [
    "Orientation & Awareness",
    "Word Encoding",
    "Attention & Concentration",
    "Delayed Word Recall",
    "Language & Verbal Reasoning",
    "Visuospatial & Executive",
    "Assessment Complete"
]

current_stage_title = stage_names[min(st.session_state.stage, len(stage_names)-1)]

if st.session_state.stage < total_stages:
    st.markdown(f"""
    <div class="progress-wrap">
        <div class="progress-header-row">
            <span class="progress-step-text">Section {current_step} of {total_stages}: {current_stage_title}</span>
            <span style="font-size: 0.8rem; font-weight: 600; color: var(--text-muted);">{int(progress*100)}% Complete</span>
        </div>
        <div class="progress-track">
            <div class="progress-fill" style="width:{progress*100:.0f}%"></div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ════════════════════════════════════════════════════════════
# STAGE 0 — Orientation
# ════════════════════════════════════════════════════════════
if st.session_state.stage == 0:
    st.markdown("""
    <div class="task-card">
        <div class="task-step-tag">Section 1 of 6</div>
        <div class="task-title">Temporal & Spatial Orientation</div>
        <div class="task-desc">Please answer the questions below regarding current time, date, and current setting.</div>
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

    place = st.text_input("Where are you right now? (city or facility)")

    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

    if st.button("Continue to Section 2 →", key="next0"):
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
    <div class="task-card">
        <div class="task-step-tag">Section 2 of 6</div>
        <div class="task-title">Memory Encoding</div>
        <div class="task-desc">Study the four words displayed below carefully. You will be asked to recall them in a subsequent section.</div>
        <div class="word-container">
    """ + "".join([f'<div class="word-chip">{w}</div>' for w in words]) + """
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.info("Take a moment to read and commit each word to memory before proceeding.")

    if st.button("I Have Memorized the Words →", key="next1"):
        st.session_state.stage = 2
        st.rerun()

# ════════════════════════════════════════════════════════════
# STAGE 2 — Attention / Distractor (Serial 7s)
# ════════════════════════════════════════════════════════════
elif st.session_state.stage == 2:
    st.markdown("""
    <div class="task-card">
        <div class="task-step-tag">Section 3 of 6</div>
        <div class="task-title">Attention & Concentration (Serial 7s)</div>
        <div class="task-desc">
            Starting from 100, subtract 7 sequentially across five consecutive steps.
        </div>
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

    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

    if st.button("Continue to Section 4 →", key="next2"):
        score = sum(1 for i, v in enumerate(inputs) if v == expected[i])
        st.session_state.scores["attention"] = score  # max 5
        st.session_state.stage = 3
        st.rerun()

# ════════════════════════════════════════════════════════════
# STAGE 3 — Word Recall
# ════════════════════════════════════════════════════════════
elif st.session_state.stage == 3:
    st.markdown("""
    <div class="task-card">
        <div class="task-step-tag">Section 4 of 6</div>
        <div class="task-title">Delayed Memory Recall</div>
        <div class="task-desc">
            Type the words that you studied in Section 2. Separate multiple words with spaces or commas.
        </div>
    </div>
    """, unsafe_allow_html=True)

    recalled = st.text_area("Recalled words:",
                            placeholder="Type all remembered words here...")

    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

    if st.button("Continue to Section 5 →", key="next3"):
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
    <div class="task-card">
        <div class="task-step-tag">Section 5 of 6</div>
        <div class="task-title">Language & Verbal Reasoning</div>
        <div class="task-desc">Select or type the best answer for each cognitive reasoning item below.</div>
    </div>
    """, unsafe_allow_html=True)

    score = 0

    q1 = st.radio("1. Conceptual Similarity: What do a dog and a cat have in common?",
        ["", "One barks, one meows", "They are both animals", "They have four legs", "They are pets"],
        index=0)

    q2 = st.radio("2. Number Sequence: Complete the pattern: 3, 6, 9, 12, ___",
        ["", "13", "14", "15", "16"], index=0)

    q3 = st.radio("3. Category Exclusion: Which word does NOT belong?",
        ["", "Apple", "Banana", "Carrot", "Mango"], index=0)

    q4 = st.text_input('4. Phrase Repetition: Repeat this phrase exactly: "No ifs, ands, or buts"')

    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

    if st.button("Continue to Section 6 →", key="next4"):
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
    <div class="task-card">
        <div class="task-step-tag">Section 6 of 6</div>
        <div class="task-title">Visuospatial & Executive Processing</div>
        <div class="task-desc">Answer the spatial reasoning and mental rotation tasks below.</div>
    </div>
    """, unsafe_allow_html=True)

    score = 0

    q1 = st.radio("1. Clock Representation: A clock shows 3:00. Where is the minute hand pointing?",
        ["", "12", "3", "6", "9"], index=0)

    q2 = st.radio("2. Polygon Geometry: Which shape has the most sides?",
        ["", "Triangle", "Square", "Pentagon", "Circle"], index=0)

    q3 = st.radio("3. Spatial Folding: If you fold a square piece of paper in half diagonally, you get a:",
        ["", "Rectangle", "Triangle", "Pentagon", "Circle"], index=0)

    q4 = st.radio("4. Mirror Orientation: If your right hand points left, your mirror image points:",
        ["", "Left", "Right", "Up", "Down"], index=0)

    st.markdown("<div style='margin-top: 1rem;'></div>", unsafe_allow_html=True)

    if st.button("Submit Assessment Protocol ✓", key="next5"):
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
        risk_label = "Low Clinical Concern"
        badge_cls  = "badge-success"
        bar_accent = "#16a34a"
        risk_desc  = "Cognitive performance across evaluated domains aligns within normal age-adjusted screening parameters."
    elif pct >= 60:
        risk_label = "Mild Cognitive Concern"
        badge_cls  = "badge-warning"
        bar_accent = "#d97706"
        risk_desc  = "Specific domain scores indicate mild variance from baseline. Further clinical evaluation is recommended."
    else:
        risk_label = "Elevated Risk Indication"
        badge_cls  = "badge-danger"
        bar_accent = "#dc2626"
        risk_desc  = "Scores indicate notable variance across multiple domains. Comprehensive neurological consultation advised."

    st.markdown(f"""
    <div class="summary-result-card">
        <div class="summary-score-large">{pct}<span>%</span></div>
        <div class="clinical-badge {badge_cls}">{risk_label}</div>
        <div class="summary-desc">{risk_desc}</div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("<h3>Domain-Specific Score Breakdown</h3>", unsafe_allow_html=True)
    st.markdown("<div class='clinical-card'>", unsafe_allow_html=True)

    domains = {
        "Orientation & Awareness":     (orientation, 5),
        "Attention & Concentration":   (attention, 5),
        "Delayed Memory Recall":       (recall, 4),
        "Language & Verbal Reasoning": (language, 4),
        "Visuospatial Function":       (visuospatial, 4),
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
            <div class="domain-score">{got} / {mx}</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("""
    <div class="clinical-callout">
        ⚠️ <strong>Clinical Notice:</strong> This digital assessment is designed for preliminary cognitive screening and academic workflow demonstration. It does not constitute a definitive medical diagnosis.
    </div>
    """, unsafe_allow_html=True)

    if st.button("🔄 Retake Cognitive Assessment", key="retake"):
        for key in ["stage","scores","memory_words","show_words","word_timer","distractor_done"]:
            if key in st.session_state:
                del st.session_state[key]
        st.rerun()