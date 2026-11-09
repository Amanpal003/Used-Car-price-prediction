import streamlit as st
import requests
from pathlib import Path

# -------------------------------------------------
# Page configuration
# -------------------------------------------------
st.set_page_config(
    page_title="CarPrice AI | Used Car Price Predictor",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="collapsed"
)

BASE_DIR = Path(__file__).resolve().parent
ASSETS_DIR = BASE_DIR / "assets"
HERO_IMAGE = ASSETS_DIR / "hero_car.png"
ABOUT_IMAGE = ASSETS_DIR / "about_car.png"
API_URL = "http://127.0.0.1:8000/predict"


# -------------------------------------------------
# Helper: Indian currency formatting
# Example: 470780 -> 4,70,780
# -------------------------------------------------
def format_indian_currency(value):
    number = str(int(round(float(value))))

    if len(number) <= 3:
        return number

    last_three = number[-3:]
    remaining = number[:-3]
    groups = []

    while remaining:
        groups.insert(0, remaining[-2:])
        remaining = remaining[:-2]

    return ",".join(groups) + "," + last_three


# -------------------------------------------------
# Custom styling
# -------------------------------------------------
st.markdown("""


<style>
:root {
    --navy: #071a36;
    --red: #d7192d;
    --red-dark: #a90d20;
    --blue: #174b83;
    --text: #10264b;
}

.stApp {
    background: linear-gradient(180deg, #f8faff 0%, #edf3ff 100%);
    color: var(--text);
}

.block-container {
    max-width: 1500px;
    padding: 0.7rem 1.2rem 1.5rem 1.2rem;
}

#MainMenu, footer, header {
    visibility: hidden;
}

div[data-testid="stForm"] {
    background: #ffffff;
    border: 1px solid #dce5f3;
    border-radius: 18px;
    padding: 1.1rem 1.15rem 0.9rem 1.15rem;
    box-shadow: 0 7px 22px rgba(17, 45, 88, 0.10);
}

div[data-testid="stForm"] label {
    color: #10264b !important;
    font-weight: 650 !important;
}

div[data-baseweb="input"] > div,
div[data-baseweb="select"] > div {
    border-radius: 10px !important;
    border-color: #cbd8ea !important;
    background: #fbfdff !important;
}

div[data-testid="stFormSubmitButton"] button {
    width: 100%;
    min-height: 48px;
    border: 0;
    border-radius: 12px;
    color: white;
    font-weight: 750;
    font-size: 1rem;
    background: linear-gradient(90deg, #f0182e, #b90d22);
    box-shadow: 0 4px 12px rgba(190, 13, 34, 0.18);
}

div[data-testid="stFormSubmitButton"] button:hover {
    color: white;
    border: 1px solid #8f0a1b;
    background: linear-gradient(90deg, #d71128, #97091b);
}

div.stButton > button {
    border-radius: 12px;
    font-weight: 700;
}

.brand {
    color: #071a36;
    font-size: 1.8rem;
    font-weight: 850;
    letter-spacing: -1px;
    padding: 0.25rem 0 0.55rem 0;
}

.brand span {
    color: #d7192d;
}

.tagline {
    text-align: right;
    color: #263a5b;
    font-size: 0.92rem;
    font-style: italic;
    padding-top: 0.65rem;
}

.hero-copy {
    min-height: 235px;
    border-radius: 18px;
    padding: 1.4rem 1.5rem;
    color: white;
    background: linear-gradient(115deg, #06162f 0%, #102f59 68%, #173e70 100%);
    display: flex;
    flex-direction: column;
    justify-content: center;
    box-shadow: 0 8px 20px rgba(5, 25, 55, 0.15);
}

.hero-copy h1 {
    font-size: clamp(2.1rem, 4vw, 3.8rem);
    line-height: 1.0;
    margin: 0;
    color: white;
    font-weight: 850;
}

.hero-copy h1 span {
    color: #f0182e;
}

.hero-copy h2 {
    font-size: clamp(1.2rem, 2.2vw, 2rem);
    margin: 0.45rem 0 0.4rem 0;
    color: #ffffff;
}

.hero-copy p {
    color: #e4edfa;
    font-size: 1rem;
    margin-bottom: 0.8rem;
}

.hero-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 0.5rem;
}

.hero-pills span {
    border: 1px solid #7386a5;
    background: rgba(255,255,255,0.08);
    padding: 0.35rem 0.65rem;
    border-radius: 30px;
    font-size: 0.83rem;
}

.hero-image img {
    width: 100%;
    height: 235px;
    object-fit: cover;
    border-radius: 18px;
    box-shadow: 0 8px 20px rgba(5, 25, 55, 0.15);
}

.section-heading {
    color: #10264b;
    font-size: 1.35rem;
    font-weight: 800;
    margin: 0.25rem 0 0.2rem 0;
}

.section-subtitle {
    color: #51627c;
    font-size: 0.9rem;
    margin-bottom: 0.8rem;
}

.form-heading {
    background: linear-gradient(100deg, #d7192d, #09264c 45%, #174b83);
    color: white;
    border-radius: 14px 14px 0 0;
    padding: 0.75rem 1rem;
    margin: -0.1rem -0.1rem 0.8rem -0.1rem;
}

.form-heading h3 {
    color: white;
    margin: 0;
    font-size: 1.25rem;
}

.form-heading p {
    color: #e7effa;
    margin: 0.15rem 0 0 0;
    font-size: 0.83rem;
}

.panel {
    background: #ffffff;
    border: 1px solid #dce5f3;
    border-radius: 18px;
    padding: 1.15rem;
    min-height: 100%;
    box-shadow: 0 7px 22px rgba(17, 45, 88, 0.10);
}

.empty-result {
    min-height: 290px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    text-align: center;
    background: linear-gradient(145deg, #f5f9ff, #ffffff);
    border: 1px dashed #b9c9df;
    border-radius: 15px;
    padding: 1.5rem;
}

.empty-result h3 {
    color: #10264b;
    margin-bottom: 0.4rem;
}

.empty-result p {
    color: #61718a;
}

.success-heading {
    text-align: center;
    color: #168342;
    font-size: 1.25rem;
    font-weight: 800;
    margin-top: 0.15rem;
}

.success-sub {
    text-align: center;
    color: #53647b;
    font-size: 0.88rem;
}

.price-box {
    margin: 1rem 0;
    padding: 1rem 0.6rem;
    border-radius: 14px;
    text-align: center;
    background: linear-gradient(100deg, #fff1f3, #eef6ff);
    border: 1px solid #d8dfed;
}

.price-label {
    color: #10264b;
    font-weight: 750;
    font-size: 1.1rem;
}

.price-value {
    color: #cf142b;
    font-size: clamp(2rem, 4vw, 3.1rem);
    font-weight: 900;
    line-height: 1.15;
}

.note-box {
    background: #fff4d8;
    border: 1px solid #f4dfa2;
    color: #5b4817;
    padding: 0.8rem;
    border-radius: 12px;
    font-size: 0.88rem;
    text-align: center;
}

.feature-card {
    background: white;
    border: 1px solid #dce5f3;
    border-radius: 15px;
    padding: 1rem 0.7rem;
    text-align: center;
    min-height: 145px;
    box-shadow: 0 5px 15px rgba(17, 45, 88, 0.07);
}

.feature-icon {
    font-size: 1.8rem;
}

.feature-card h4 {
    color: #10264b;
    font-size: 0.98rem;
    margin: 0.35rem 0 0.2rem 0;
}

.feature-card p {
    color: #53647b;
    font-size: 0.8rem;
    margin: 0;
}

.about-card {
    background: white;
    border: 1px solid #dce5f3;
    border-radius: 15px;
    padding: 1rem;
    min-height: 145px;
    box-shadow: 0 5px 15px rgba(17, 45, 88, 0.07);
}

.about-card h3 {
    color: #10264b;
    margin-top: 0;
}

.footer {
    background: #071a36;
    color: #f2f6ff;
    border-radius: 14px;
    text-align: center;
    padding: 1rem;
    margin-top: 1rem;
}

.footer p {
    margin: 0.15rem 0;
    color: #dbe5f4;
    font-size: 0.85rem;
}

@media (max-width: 800px) {
    .block-container {
        padding-left: 0.7rem;
        padding-right: 0.7rem;
    }
    .hero-copy {
        min-height: auto;
    }
    .hero-image img {
        height: 190px;
    }
    .tagline {
        text-align: left;
        padding-top: 0;
    }
}
.navigation {
    display: flex;
    justify-content: center;
    gap: 10px;
    padding-top: 5px;
}

.nav-btn {
    text-decoration: none !important;
    padding: 10px 22px;
    border-radius: 30px;
    font-weight: 700;
    color: #10264b !important;
    background: #e8efff;
    border: 1px solid #d5e0f3;
}

.home-btn {
    color: white !important;
    background: linear-gradient(90deg, #f0182e, #b90d22);
}

.nav-btn:hover {
    opacity: 0.8;
}

</style>
""", unsafe_allow_html=True)



# Navigation header
nav_left, nav_middle, nav_right = st.columns([2.2, 1.5, 2.0])

with nav_left:
    st.markdown(
        '<div class="brand">🚘 CarPrice <span>AI</span></div>',
        unsafe_allow_html=True
    )

with nav_middle:
    st.markdown("""
    <div class="navigation">
        <a href="#home" class="nav-btn home-btn">🏠 Home</a>
        <a href="#about" class="nav-btn about-btn">ℹ️ About</a>
    </div>
    """, unsafe_allow_html=True)

with nav_right:
    st.markdown(
        '<div class="tagline">Smart Prediction. Better Decisions. 📈</div>',
        unsafe_allow_html=True
    )

st.divider()

# Home Anchor

st.markdown('<div id="home"></div>', unsafe_allow_html=True)


# Hero section

hero_text, hero_visual = st.columns([1.05, 1.25], gap="small")

with hero_text:
    st.markdown("""
    <div class="hero-copy">
        <h1>CarPrice <span>AI</span></h1>
        <h2>Used Car Price Predictor</h2>
        <p>Get the estimated selling price of your used car
        using the power of Machine Learning.</p>
        <div class="hero-pills">
            <span>⚡ Instant Results</span>
            <span>🧠 ML Powered</span>
            <span>🛡️ Model Based Estimate</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

with hero_visual:
    if HERO_IMAGE.exists():
        st.markdown('<div class="hero-image">', unsafe_allow_html=True)
        st.image(str(HERO_IMAGE), use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    else:
        st.warning("Hero image missing. Add hero_car.png inside frontend/assets/.")


st.write("")


# -------------------------------------------------
# Main form and result panels
# -------------------------------------------------
form_col, result_col = st.columns([1, 1], gap="medium")

with form_col:
    st.markdown("""
    <div class="form-heading">
        <h3>🚘 Enter Your Car Details</h3>
        <p>Fill in the details below to get an estimated selling price.</p>
    </div>
    """, unsafe_allow_html=True)

    with st.form("car_prediction_form"):
        left_fields, right_fields = st.columns(2)

        with left_fields:
            brand = st.text_input(
                "🚗 Car Brand",
                value="Hyundai",
                placeholder="Example: Hyundai"
            )

            year = st.number_input(
                "📅 Manufacturing Year",
                min_value=1992,
                max_value=2020,
                value=2020,
                step=1
            )

            km_driven = st.number_input(
                "🛣️ Kilometers Driven",
                min_value=0,
                value=35000,
                step=1000
            )

            fuel = st.selectbox(
                "⛽ Fuel Type",
                ["Petrol", "Diesel", "CNG", "LPG", "Electric"]
            )

        with right_fields:
            seller_type = st.selectbox(
                "👥 Seller Type",
                ["Individual", "Dealer", "Trustmark Dealer"]
            )

            transmission = st.selectbox(
                "⚙️ Transmission",
                ["Manual", "Automatic"]
            )

            owner = st.selectbox(
                "👤 Owner",
                [
                    "First Owner",
                    "Second Owner",
                    "Third Owner",
                    "Fourth & Above Owner",
                    "Test Drive Car"
                ]
            )

        submitted = st.form_submit_button("🧮  Predict Car Price   ➜")


    # Call backend only after form submission
    if submitted:
        if not brand.strip():
            st.session_state.pop("car_prediction_result", None)
            st.error("Please enter a car brand.")
        else:
            car_data = {
                "year": int(year),
                "km_driven": int(km_driven),
                "fuel": fuel,
                "seller_type": seller_type,
                "transmission": transmission,
                "owner": owner,
                "brand": brand.strip().title()
            }

            try:
                with st.spinner("Analysing car details and predicting price..."):
                    response = requests.post(
                        API_URL,
                        json=car_data,
                        timeout=15
                    )
                    response.raise_for_status()
                    result = response.json()

                if "predicted_price" not in result:
                    st.error("The API response did not contain a predicted price.")
                    st.session_state.pop("car_prediction_result", None)
                else:
                    st.session_state["car_prediction_result"] = {
                        "price": float(result["predicted_price"]),
                        "car": car_data
                    }

            except requests.exceptions.ConnectionError:
                st.error("Backend is not running. Start FastAPI in another terminal.")
            except requests.exceptions.Timeout:
                st.error("The prediction request timed out. Please try again.")
            except requests.exceptions.HTTPError as error:
                st.error(f"Backend returned an error: {error}")
            except (requests.exceptions.RequestException, ValueError, TypeError) as error:
                st.error(f"Could not complete prediction: {error}")


with result_col:
    saved_result = st.session_state.get("car_prediction_result")

    if saved_result:
        price = saved_result["price"]
        car = saved_result["car"]

        st.markdown("""
        <div class="panel">
            <div style="text-align:center; font-size:2.4rem;">🟢</div>
            <div class="success-heading">Car price predicted successfully!</div>
            <div class="success-sub">Based on the trained Machine Learning model</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="price-box">
            <div class="price-label">Estimated Selling Price</div>
            <div class="price-value">₹ {format_indian_currency(price)}</div>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="note-box">
            💡 <b>Note:</b> This is an estimated price and may vary in the real market.
        </div>
        """, unsafe_allow_html=True)

        st.write("")
        st.markdown("**Your submitted car details**")
        detail_a, detail_b, detail_c = st.columns(3)
        detail_a.metric("Brand", car["brand"])
        detail_b.metric("Year", car["year"])
        detail_c.metric("KM Driven", f'{car["km_driven"]:,}')

        if st.button("🔄 Predict Another Car", use_container_width=True):
            st.session_state.pop("car_prediction_result", None)
            st.rerun()

    else:
        st.markdown("""
        <div class="panel empty-result">
            <div style="font-size:3rem;">🚘</div>
            <h3>Your prediction will appear here</h3>
            <p>Enter the car details on the left and click
            <b>Predict Car Price</b> to see the estimated selling price.</p>
            <div style="font-size:1.7rem;">📊　🤖　💰</div>
        </div>
        """, unsafe_allow_html=True)


# -------------------------------------------------
# Why choose section
# -------------------------------------------------
st.write("")
st.markdown('<div class="section-heading">🔴 Why Choose CarPrice AI?</div>',
            unsafe_allow_html=True)

feature_cols = st.columns(4)

features = [
    ("🎯", "Data-Based Estimate", "Prediction from a trained ML model"),
    ("⚡", "Fast & Easy", "Get results in a few seconds"),
    ("🛡️", "Model Driven", "Consistent, data-driven estimation"),
    ("🚗", "Smart Decision", "Make informed buying or selling decisions")
]

for col, feature in zip(feature_cols, features):
    icon, title, description = feature
    with col:
        st.markdown(f"""
        <div class="feature-card">
            <div class="feature-icon">{icon}</div>
            <h4>{title}</h4>
            <p>{description}</p>
        </div>
        """, unsafe_allow_html=True)

# About Section 

st.markdown('<div id="about"></div>', unsafe_allow_html=True)

# -------------------------------------------------
# About section
# -------------------------------------------------
st.write("")
about_text, about_visual = st.columns([1.4, 1], gap="medium")

with about_text:
    st.markdown("""
    <div class="about-card">
        <h3>🔴 About CarPrice AI</h3>
        <p>
            CarPrice AI is a Machine Learning based application that
            estimates the resale price of used cars using vehicle details
            such as brand, manufacturing year, kilometers driven,
            fuel type, seller type, transmission and ownership.
        </p>
        <p>
             Designed to estimate used car selling prices instantly, taking the guesswork out of automotive valuation
        </p>
    </div>
    """, unsafe_allow_html=True)

with about_visual:
    if ABOUT_IMAGE.exists():
        st.image(str(ABOUT_IMAGE), use_container_width=True)
    else:
        st.info("Add about_car.png inside frontend/assets/ for the About visual.")


# -------------------------------------------------
# Footer
# -------------------------------------------------
st.markdown("""
<div class="footer">
    <h3>🚘 CarPrice <span style="color:#ff3349;">AI</span></h3>
    <p>Smart Prediction. Better Decisions.</p>
    <p>Smart Car Pricing • Instant Valuations • Better Resale Decisions</p>
    <p>Drive Smart. Sell Better.</p>
</div>
""", unsafe_allow_html=True)
