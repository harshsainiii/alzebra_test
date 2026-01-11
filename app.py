import streamlit as st

# Set page configuration
st.set_page_config(page_title="Class 8 Algebra Quiz", layout="centered")

# CSS for styling
st.markdown("""
<style>
    .stRadio > label {font-size: 1.1rem; font-weight: 500;}
    .success-msg {color: #10b981; font-weight: bold;}
    .error-msg {color: #ef4444; font-weight: bold;}
    .stat-box {
        text-align: center; 
        padding: 15px; 
        background: #f0f2f6; 
        border-radius: 10px; 
        margin: 5px;
    }
</style>
""", unsafe_allow_html=True)

# Define the Questions Data
quiz_data = [
    {"q": "Solve for x: 3x - 5 = 10", "options": ["x = 3", "x = 5", "x = 15", "x = -5"], "correct": "x = 5"},
    {"q": "If x = 2, find value of 3x² - 4x", "options": ["4", "2", "8", "6"], "correct": "4"},
    {"q": "Expand: (2x + 3y)²", "options": ["4x² + 9y²", "4x² + 6xy + 9y²", "4x² + 12xy + 9y²", "2x² + 3y²"], "correct": "4x² + 12xy + 9y²"},
    {"q": "Factorize: x² + 5x + 6", "options": ["(x+2)(x+3)", "(x+1)(x+6)", "(x-2)(x-3)", "(x+5)(x+1)"], "correct": "(x+2)(x+3)"},
    {"q": "Coefficient of x in 4x² - 7x + 2", "options": ["4", "7", "-7", "2"], "correct": "-7"},
    {"q": "Value of (3²)³", "options": ["3⁵", "3⁶", "3⁸", "9³"], "correct": "3⁶"},
    {"q": "Solve: x/3 + 1 = 7/15", "options": ["-8/5", "-5/8", "8/5", "2/5"], "correct": "-8/5"},
    {"q": "A number multiplied by 5 and increased by 10 is 60. Find number.", "options": ["8", "12", "10", "50"], "correct": "10"},
    {"q": "Expand: (a - b)²", "options": ["a² + b² - 2ab", "a² - b²", "a² + b² + 2ab", "a² - b² - 2ab"], "correct": "a² + b² - 2ab"},
    {"q": "Calculate: (2x) × (3x²) × (-4y)", "options": ["24x³y", "-24x³y", "-24x²y", "12x³y"], "correct": "-24x³y"},
    {"q": "Solve for y: 2y + 9 = 4", "options": ["2.5", "-2.5", "5", "-5"], "correct": "-2.5"},
    {"q": "Standard form of 0.000035", "options": ["3.5 × 10⁻⁵", "3.5 × 10⁻⁴", "35 × 10⁻⁶", "3.5 × 10⁵"], "correct": "3.5 × 10⁻⁵"},
    {"q": "Common factor of 12x and 36", "options": ["12x", "12", "6x", "36"], "correct": "12"},
    {"q": "Evaluate: 50² - 40²", "options": ["100", "900", "10", "200"], "correct": "900"},
    {"q": "Simplify: 2x(3x + 5) - 3x(2x - 4)", "options": ["22x", "2x", "-2x", "22x²"], "correct": "22x"},
    {"q": "Degree of polynomial 7x³ - 5x² + 2", "options": ["2", "3", "1", "7"], "correct": "3"},
    {"q": "Multiplicative inverse of 10⁻⁵", "options": ["10⁵", "10⁻⁵", "-10⁵", "1"], "correct": "10⁵"},
    {"q": "Solve: 5(x - 2) + 3(x + 1) = 25", "options": ["x = 3", "x = 4", "x = 2", "x = 5"], "correct": "x = 4"},
    {"q": "Divide 15x³y² by 3x²y", "options": ["5xy", "5x", "5y", "12xy"], "correct": "5xy"},
    {"q": "If perimeter of square is 4x + 12, length of one side is:", "options": ["x + 3", "4x + 3", "x + 12", "2x + 6"], "correct": "x + 3"}
]

# Initialize Session State
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# Header
st.title("📚 Class 8 Algebra Proficiency Test")
st.markdown("---")

if not st.session_state.submitted:
    # --- QUIZ FORM ---
    with st.form("quiz_form"):
        user_answers = {}
        
        for i, item in enumerate(quiz_data):
            st.subheader(f"Q{i+1}: {item['q']}")
            # Unique key for each radio button prevents conflicts
            user_answers[i] = st.radio(
                "Select an option:", 
                item['options'], 
                index=None, 
                key=f"q_{i}", 
                label_visibility="collapsed"
            )
            st.divider()
        
        submitted = st.form_submit_button("Submit Test", type="primary")
        
        if submitted:
            st.session_state.submitted = True
            st.session_state.user_answers = user_answers
            st.rerun()

else:
    # --- DASHBOARD & ANALYSIS ---
    st.success("Test Submitted Successfully!")
    
    # Calculate Score
    score = 0
    total = len(quiz_data)
    results = []
    
    for i, item in enumerate(quiz_data):
        user_choice = st.session_state.user_answers.get(i)
        is_correct = (user_choice == item['correct'])
        if is_correct:
            score += 1
        results.append({
            "question": item['q'],
            "user_choice": user_choice,
            "correct_answer": item['correct'],
            "is_correct": is_correct
        })

    # 1. Score Cards
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.markdown(f"<div class='stat-box'><h3>Total Score</h3><h1>{score}/{total}</h1></div>", unsafe_allow_html=True)
    with col2:
        percentage = (score / total) * 100
        st.markdown(f"<div class='stat-box'><h3>Percentage</h3><h1>{percentage:.0f}%</h1></div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='stat-box'><h3>Correct</h3><h1 style='color:#10b981'>{score}</h1></div>", unsafe_allow_html=True)
    with col4:
        st.markdown(f"<div class='stat-box'><h3>Wrong</h3><h1 style='color:#ef4444'>{total - score}</h1></div>", unsafe_allow_html=True)

    st.markdown("---")
    
    # 2. Detailed Analysis
    st.header("📝 Detailed Analysis")
    
    for i, res in enumerate(results):
        with st.expander(f"Q{i+1}: {res['question']} - {'✅ Correct' if res['is_correct'] else '❌ Incorrect'}", expanded=not res['is_correct']):
            if res['is_correct']:
                st.markdown(f"**Your Answer:** <span class='success-msg'>{res['user_choice']}</span>", unsafe_allow_html=True)
            else:
                st.markdown(f"**Your Answer:** <span class='error-msg'>{res['user_choice'] if res['user_choice'] else 'Skipped'}</span>", unsafe_allow_html=True)
                st.markdown(f"**Correct Answer:** <span class='success-msg'>{res['correct_answer']}</span>", unsafe_allow_html=True)

    # Retry Button
    if st.button("Retake Test"):
        st.session_state.submitted = False
        st.session_state.user_answers = {}
        st.rerun()