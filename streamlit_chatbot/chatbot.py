

import streamlit as st
import google.generativeai as genai

# Setup Gemini API (load from secrets for safety)
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

# -------- Helper Functions -------- #
def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []

def get_gemini_response(prompt):
    system_prompt = (
        "You are a skincare expert AI assistant. Answer questions kindly and clearly. "
        "Recommend products only if asked. Give advice based on skin types: oily, dry, sensitive, combination."
    )
    full_prompt = system_prompt + "\n\nUser: " + prompt
    response = model.generate_content(full_prompt)
    return response.text

def skin_type_quiz():
    st.subheader("🧪 Find Your Skin Type")

    oiliness = st.radio("How oily does your skin feel by the afternoon?", ["Not oily", "Slightly oily", "Very oily"])
    sensitivity = st.radio("Does your skin react to new products?", ["No", "Sometimes", "Yes"])
    dryness = st.radio("Does your skin feel tight or dry?", ["Often", "Sometimes", "Never"])
    
    if st.button("Get My Skin Type"):
        if oiliness == "Very oily":
            st.success("You likely have **Oily Skin**.")
        elif dryness == "Often":
            st.success("You likely have **Dry Skin**.")
        elif sensitivity == "Yes":
            st.success("You likely have **Sensitive Skin**.")
        else:
            st.success("You may have **Combination Skin**.")

def product_recommendations():
    st.subheader("🧴 Product Recommendations")
    skin_type = st.selectbox("Select your skin type:", ["Oily", "Dry", "Sensitive", "Combination"])
    
    st.write("### Recommended Products:")
    if skin_type == "Oily":
        st.markdown("- Gel cleanser\n- Oil-free moisturizer\n- Salicylic acid serum")
    elif skin_type == "Dry":
        st.markdown("- Cream cleanser\n- Hyaluronic acid serum\n- Rich moisturizer")
    elif skin_type == "Sensitive":
        st.markdown("- Fragrance-free products\n- Gentle toner\n- Soothing creams with ceramides")
    else:
        st.markdown("- Balanced cleanser\n- Light moisturizer\n- Niacinamide serum")

def daily_routine_tracker():
    st.subheader("📋 Daily Skincare Routine Tracker")

    st.write("### Morning Routine")
    cleanser = st.checkbox("Cleanser")
    serum = st.checkbox("Serum")
    moisturizer = st.checkbox("Moisturizer")
    sunscreen = st.checkbox("Sunscreen")

    st.write("### Night Routine")
    makeup = st.checkbox("Makeup Remover")
    night_serum = st.checkbox("Night Serum")
    night_cream = st.checkbox("Night Cream")

    if st.button("Save Routine"):
        st.success("Routine saved for today! ✅")

def ingredient_checker():
    st.subheader("🔍 Ingredient Checker")
    ingredient = st.text_input("Enter an ingredient (e.g., Niacinamide, Retinol, Salicylic Acid):")
    
    if ingredient:
        # Simulated simple lookup (you could expand this with a real database)
        info = {
            "Niacinamide": "Great for reducing inflammation and controlling oil. Safe for most skin types.",
            "Retinol": "Powerful anti-aging. Can cause dryness or irritation. Use at night.",
            "Salicylic Acid": "Best for acne-prone skin. Helps unclog pores and reduce oil."
        }
        result = info.get(ingredient.title(), "Sorry, I don't have information on that ingredient.")
        st.info(result)

def dermatologist_advice():
    st.subheader("👩‍⚕️ Dermatologist Advice")

    st.markdown("""
    - For persistent acne, see a dermatologist to avoid scarring.
    - Dry, flaky skin may be eczema. Consider a gentle routine and moisturizer.
    - If over-the-counter treatments don’t help, get a professional diagnosis.
    """)

def skincare_tips():
    st.subheader("📰 Skincare Tips & Articles")

    st.markdown("""
    - **Use sunscreen daily**, even if you're indoors.
    - Don't over-exfoliate — 2–3 times a week is enough.
    - Layer products from thinnest to thickest consistency.
    - Stay hydrated! Water helps your skin from the inside out.
    """)

def ai_chatbot():
    st.subheader("💬 AI Skincare Assistant (Gemini)")

    initialize_session_state()

    with st.expander("💡 Example Questions", expanded=False):
        st.markdown("""
        - What's the best routine for sensitive skin?
        - Can I mix niacinamide and retinol?
        - Recommend a product for oily skin with acne.
        """)

    # Show chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.write(msg["content"])

    # Chat input
    if prompt := st.chat_input("Ask a skincare question..."):
        with st.chat_message("user"):
            st.write(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})
        reply = get_gemini_response(prompt)

        with st.chat_message("assistant"):
            st.write(reply)

        st.session_state.messages.append({"role": "assistant", "content": reply})

# -------- Streamlit App Layout -------- #
st.set_page_config(page_title="Skincare Assistant", page_icon="🧴", layout="centered")

st.sidebar.title("🧴 Skincare Website")
page = st.sidebar.radio("Navigate", [
    "Skin Type Quiz",
    "Product Recommendations",
    "Routine Tracker",
    "Ingredient Checker",
    "Dermatologist Advice",
    "Skincare Tips",
    "AI Chat Assistant"
])

if page == "Skin Type Quiz":
    skin_type_quiz()
elif page == "Product Recommendations":
    product_recommendations()
elif page == "Routine Tracker":
    daily_routine_tracker()
elif page == "Ingredient Checker":
    ingredient_checker()
elif page == "Dermatologist Advice":
    dermatologist_advice()
elif page == "Skincare Tips":
    skincare_tips()
elif page == "AI Chat Assistant":
    ai_chatbot()

    GOOGLE_API_KEY = "AIzaSyBBXMiYkzVuNpg4sdVE-k1lUC-r7FKanT8"

