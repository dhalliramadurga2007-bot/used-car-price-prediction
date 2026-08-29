import streamlit as st
import pandas as pd
import numpy as np
import joblib


# ============================================================
# 1. PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="AutoValue AI - Used Car Price Predictor",
    page_icon="🚘",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# 2. LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("final_app_model.pkl")


try:
    model = load_model()

except Exception as error:

    st.error(
        f"❌ Model loading failed: {error}"
    )

    st.info(
        "Check whether models/final_app_model.pkl exists."
    )

    st.stop()


# ============================================================
# 3. PROFESSIONAL CSS
# ============================================================

st.markdown(
    """
<style>

/* ------------------------------------------------------------
   APP BACKGROUND
------------------------------------------------------------ */

.stApp {

    background:
        linear-gradient(
            rgba(2, 6, 23, 0.80),
            rgba(2, 6, 23, 0.94)
        ),
        url("https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=2000&q=90");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}


/* ------------------------------------------------------------
   ANIMATED CAR BACKGROUND
------------------------------------------------------------ */

.stApp::before {

    content: "";

    position: fixed;

    top: 0;
    left: 0;

    width: 100%;
    height: 100%;

    pointer-events: none;

    z-index: 0;

    opacity: 0.22;

    background-size: cover;
    background-position: center;

    animation: carAnimation 30s infinite ease-in-out;
}


@keyframes carAnimation {

    0% {

        background-image:
            url("https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=2000&q=90");

        transform: scale(1.02);
    }

    25% {

        background-image:
            url("https://images.unsplash.com/photo-1504215680853-026ed2a45def?auto=format&fit=crop&w=2000&q=90");

        transform: scale(1.08);
    }

    50% {

        background-image:
            url("https://images.unsplash.com/photo-1494976388531-d1058494cdd8?auto=format&fit=crop&w=2000&q=90");

        transform: scale(1.04);
    }

    75% {

        background-image:
            url("https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=2000&q=90");

        transform: scale(1.08);
    }

    100% {

        background-image:
            url("https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=2000&q=90");

        transform: scale(1.02);
    }
}


/* ------------------------------------------------------------
   MAIN CONTENT
------------------------------------------------------------ */

.block-container {

    position: relative;

    z-index: 5;

    max-width: 1250px;

    padding-top: 2rem;

    padding-bottom: 4rem;
}


/* ------------------------------------------------------------
   STREAMLIT HEADER
------------------------------------------------------------ */

header[data-testid="stHeader"] {

    background: rgba(2, 6, 23, 0.35);

    backdrop-filter: blur(16px);
}


/* ------------------------------------------------------------
   MAIN TITLES
------------------------------------------------------------ */

h1 {

    font-size: 3.6rem !important;

    font-weight: 900 !important;

    letter-spacing: -2px !important;

    background:
        linear-gradient(
            90deg,
            #ffffff,
            #38bdf8,
            #818cf8,
            #e879f9
        );

    -webkit-background-clip: text;

    -webkit-text-fill-color: transparent;
}


h2 {

    color: #f8fafc !important;

    font-weight: 800 !important;
}


h3 {

    color: #f8fafc !important;

    font-weight: 750 !important;
}


p {

    color: #cbd5e1;
}


/* ------------------------------------------------------------
   CAPTION
------------------------------------------------------------ */

[data-testid="stCaptionContainer"] {

    color: #94a3b8 !important;
}


/* ------------------------------------------------------------
   GLASS CONTAINERS
------------------------------------------------------------ */

[data-testid="stVerticalBlockBorderWrapper"] {

    background:
        linear-gradient(
            145deg,
            rgba(15, 23, 42, 0.88),
            rgba(2, 6, 23, 0.72)
        );

    border:
        1px solid rgba(148, 163, 184, 0.18)
        !important;

    border-radius:
        22px
        !important;

    backdrop-filter:
        blur(22px);

    box-shadow:
        0 18px 55px rgba(0, 0, 0, 0.30);

    transition:
        all 0.30s ease;
}


[data-testid="stVerticalBlockBorderWrapper"]:hover {

    transform:
        translateY(-3px);

    border:
        1px solid rgba(56, 189, 248, 0.35)
        !important;

    box-shadow:
        0 22px 65px rgba(0, 0, 0, 0.38);
}


/* ------------------------------------------------------------
   METRIC CARDS
------------------------------------------------------------ */

[data-testid="stMetric"] {

    background:
        linear-gradient(
            135deg,
            rgba(14, 165, 233, 0.12),
            rgba(99, 102, 241, 0.10),
            rgba(168, 85, 247, 0.10)
        );

    border:
        1px solid rgba(125, 211, 252, 0.20);

    border-radius:
        18px;

    padding:
        19px;

    box-shadow:
        0 12px 35px rgba(0, 0, 0, 0.25);

    transition:
        all 0.25s ease;
}


[data-testid="stMetric"]:hover {

    transform:
        translateY(-4px);

    border-color:
        rgba(56, 189, 248, 0.45);
}


[data-testid="stMetricLabel"] {

    color:
        #cbd5e1 !important;

    font-weight:
        600 !important;
}


[data-testid="stMetricValue"] {

    color:
        #67e8f9 !important;

    font-weight:
        850 !important;

    font-size:
        28px !important;
}


/* ------------------------------------------------------------
   TEXT INPUT
------------------------------------------------------------ */

div[data-baseweb="input"] > div {

    background:
        rgba(15, 23, 42, 0.88)
        !important;

    border:
        1px solid rgba(148, 163, 184, 0.24)
        !important;

    border-radius:
        13px !important;

    min-height:
        47px;
}


div[data-baseweb="input"] > div:focus-within {

    border:
        1px solid #38bdf8
        !important;

    box-shadow:
        0 0 0 3px rgba(56, 189, 248, 0.10);
}


div[data-baseweb="input"] input {

    color:
        white !important;
}


/* ------------------------------------------------------------
   SELECT BOX
------------------------------------------------------------ */

div[data-baseweb="select"] > div {

    background:
        rgba(15, 23, 42, 0.88)
        !important;

    border:
        1px solid rgba(148, 163, 184, 0.24)
        !important;

    border-radius:
        13px !important;

    min-height:
        47px;
}


div[data-baseweb="select"] span {

    color:
        white !important;
}


/* ------------------------------------------------------------
   LABELS
------------------------------------------------------------ */

label {

    color:
        #e2e8f0 !important;

    font-weight:
        650 !important;
}


/* ------------------------------------------------------------
   PREDICT BUTTON
------------------------------------------------------------ */

div.stButton > button[kind="primary"],
div[data-testid="stFormSubmitButton"] > button {

    min-height:
        62px;

    width:
        100%;

    border:
        none !important;

    border-radius:
        16px !important;

    color:
        white !important;

    font-size:
        18px !important;

    font-weight:
        850 !important;

    background:
        linear-gradient(
            90deg,
            #0284c7,
            #2563eb,
            #7c3aed,
            #db2777
        ) !important;

    background-size:
        300% 100%
        !important;

    box-shadow:
        0 15px 40px rgba(37, 99, 235, 0.38);

    animation:
        buttonGradient 5s infinite alternate;

    transition:
        all 0.25s ease;
}


@keyframes buttonGradient {

    0% {

        background-position:
            0% 50%;
    }

    100% {

        background-position:
            100% 50%;
    }
}


div.stButton > button[kind="primary"]:hover,
div[data-testid="stFormSubmitButton"] > button:hover {

    transform:
        translateY(-3px)
        scale(1.005);

    box-shadow:
        0 20px 55px rgba(99, 102, 241, 0.55);
}


/* ------------------------------------------------------------
   SIDEBAR
------------------------------------------------------------ */

section[data-testid="stSidebar"] {

    background:
        linear-gradient(
            180deg,
            rgba(2, 6, 23, 0.97),
            rgba(15, 23, 42, 0.97)
        );

    backdrop-filter:
        blur(25px);

    border-right:
        1px solid rgba(148, 163, 184, 0.15);
}


/* ------------------------------------------------------------
   SUCCESS / ERROR / INFO
------------------------------------------------------------ */

div[data-testid="stAlert"] {

    border-radius:
        15px;

    backdrop-filter:
        blur(20px);
}


/* ------------------------------------------------------------
   EXPANDERS
------------------------------------------------------------ */

[data-testid="stExpander"] {

    background:
        rgba(15, 23, 42, 0.80);

    border:
        1px solid rgba(148, 163, 184, 0.18);

    border-radius:
        16px;

    backdrop-filter:
        blur(18px);
}


/* ------------------------------------------------------------
   DIVIDERS
------------------------------------------------------------ */

hr {

    border:
        none;

    height:
        1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(56, 189, 248, 0.45),
            rgba(168, 85, 247, 0.45),
            transparent
        );

    margin:
        28px 0;
}


/* ------------------------------------------------------------
   SCROLLBAR
------------------------------------------------------------ */

::-webkit-scrollbar {

    width:
        8px;
}


::-webkit-scrollbar-track {

    background:
        #020617;
}


::-webkit-scrollbar-thumb {

    background:
        linear-gradient(
            #0284c7,
            #7c3aed
        );

    border-radius:
        10px;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# 4. SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🚘 AutoValue AI")

    st.caption(
        "Smart Used-Car Valuation Platform"
    )

    st.divider()

    st.subheader("🧠 AI Model")

    st.success(
        "XGBoost Regressor"
    )

    st.write(
        "Our machine-learning model analyzes vehicle "
        "specifications and historical market patterns "
        "to estimate a used car's value."
    )

    st.divider()

    st.subheader("📊 Performance")

    st.metric(
        "R² Score",
        "92.02%"
    )

    st.metric(
        "MAE",
        "₹1,04,085"
    )

    st.metric(
        "RMSE",
        "₹1,86,844"
    )

    st.divider()

    st.subheader("⚡ Prediction Flow")

    st.write(
        "① Enter vehicle details"
    )

    st.write(
        "② AI processes the information"
    )

    st.write(
        "③ XGBoost analyzes learned patterns"
    )

    st.write(
        "④ Estimated market value is generated"
    )

    st.divider()

    st.info(
        "💡 Use realistic vehicle details for a better estimate."
    )

    st.caption(
        "AutoValue AI • ML Project"
    )


# ============================================================
# 5. HERO SECTION
# ============================================================

st.caption(
    "✦ AI-POWERED VEHICLE INTELLIGENCE"
)

st.title(
    "Predict Your Car's Real Market Value 🚘"
)

st.subheader(
    "Advanced Machine Learning for Smarter Vehicle Valuation"
)

st.write(
    "Enter your vehicle specifications and let AutoValue AI "
    "analyze the key factors that influence used-car prices. "
    "Get an instant data-driven market estimate in seconds."
)

st.caption(
    "⚡ Fast Prediction  •  📊 Data Driven  •  🧠 Machine Learning  •  🇮🇳 Price in INR"
)

st.divider()


# ============================================================
# 6. TOP INFORMATION CARDS
# ============================================================

top1, top2, top3, top4 = st.columns(4)


with top1:

    st.metric(
        "🧠 Algorithm",
        "XGBoost"
    )


with top2:

    st.metric(
        "🎯 R² Accuracy",
        "92.02%"
    )


with top3:

    st.metric(
        "🚗 Features",
        "8 Inputs"
    )


with top4:

    st.metric(
        "⚡ Result",
        "Instant"
    )


st.write("")


# ============================================================
# 7. INPUT FORM
# ============================================================

with st.form(
    "vehicle_prediction_form"
):

    # --------------------------------------------------------
    # VEHICLE IDENTITY
    # --------------------------------------------------------

    with st.container(
        border=True
    ):

        st.subheader(
            "🚘 Vehicle Identity"
        )

        st.caption(
            "Enter the manufacturer, model and manufacturing year."
        )


        identity1, identity2, identity3 = st.columns(3)


        with identity1:

            brand = st.text_input(
                "Brand",
                value="Honda",
                placeholder="Example: Honda",
                help="Enter the vehicle manufacturer."
            )


        with identity2:

            model_name = st.text_input(
                "Model",
                value="City",
                placeholder="Example: City",
                help="Enter only the model name."
            )


        with identity3:

            year = st.number_input(
                "Manufacturing Year",
                min_value=1990,
                max_value=2026,
                value=2018,
                step=1
            )


    st.write("")


    # --------------------------------------------------------
    # DRIVING INFORMATION
    # --------------------------------------------------------

    with st.container(
        border=True
    ):

        st.subheader(
            "⛽ Driving & Performance"
        )

        st.caption(
            "Provide fuel, transmission and usage information."
        )


        drive1, drive2, drive3 = st.columns(3)


        with drive1:

            fuel_type = st.selectbox(
                "Fuel Type",
                [
                    "Petrol",
                    "Diesel",
                    "CNG",
                    "LPG",
                    "Electric"
                ]
            )


        with drive2:

            transmission = st.selectbox(
                "Transmission",
                [
                    "Manual",
                    "Automatic"
                ]
            )


        with drive3:

            kilometers = st.number_input(
                "Kilometers Driven",
                min_value=0,
                max_value=500000,
                value=60000,
                step=1000,
                help="Total kilometers driven by the vehicle."
            )


    st.write("")


    # --------------------------------------------------------
    # CONFIGURATION
    # --------------------------------------------------------

    with st.container(
        border=True
    ):

        st.subheader(
            "🛞 Vehicle Configuration"
        )

        st.caption(
            "Choose seating capacity and vehicle body type."
        )


        config1, config2 = st.columns(2)


        with config1:

            seats = st.number_input(
                "Seating Capacity",
                min_value=2,
                max_value=10,
                value=5,
                step=1
            )


        with config2:

            body_type = st.selectbox(
                "Body Type",
                [
                    "Hatchback",
                    "Sedan",
                    "SUV",
                    "MUV",
                    "Minivan",
                    "Pickup Truck"
                ]
            )


    st.write("")


    # --------------------------------------------------------
    # PREDICT BUTTON
    # --------------------------------------------------------

    predict_button = st.form_submit_button(
        "🚘 PREDICT ESTIMATED CAR PRICE",
        type="primary",
        use_container_width=True
    )


# ============================================================
# 8. PREDICTION
# ============================================================

if predict_button:

    try:

        # ----------------------------------------------------
        # VALIDATION
        # ----------------------------------------------------

        if not brand.strip():

            st.error(
                "❌ Please enter the vehicle brand."
            )

            st.stop()


        if not model_name.strip():

            st.error(
                "❌ Please enter the vehicle model."
            )

            st.stop()


        # ----------------------------------------------------
        # CLEAN INPUTS
        # ----------------------------------------------------

        brand_clean = (
            brand
            .strip()
            .lower()
        )


        model_clean = (
            model_name
            .strip()
            .lower()
        )


        if not model_clean.startswith(
            brand_clean
        ):

            model_clean = (
                brand_clean
                + " "
                + model_clean
            )


        fuel_clean = (
            fuel_type
            .strip()
            .lower()
        )


        transmission_clean = (
            transmission
            .strip()
            .lower()
        )


        body_clean = (
            body_type
            .strip()
            .lower()
        )


        # ----------------------------------------------------
        # CREATE MODEL DATAFRAME
        # ----------------------------------------------------

        input_data = pd.DataFrame(
            {

                "oem": [
                    brand_clean
                ],

                "model": [
                    model_clean
                ],

                "myear": [
                    year
                ],

                "body": [
                    body_clean
                ],

                "transmission": [
                    transmission_clean
                ],

                "fuel": [
                    fuel_clean
                ],

                "km": [
                    kilometers
                ],

                "Seats": [
                    seats
                ]

            }
        )


        # ----------------------------------------------------
        # PREDICT
        # ----------------------------------------------------

        with st.spinner(
            "🧠 AutoValue AI is analyzing your vehicle..."
        ):

            log_prediction = model.predict(
                input_data
            )[0]


        # ----------------------------------------------------
        # CONVERT LOG PRICE
        # ----------------------------------------------------

        predicted_price = np.expm1(
            log_prediction
        )


        predicted_price = max(
            float(predicted_price),
            0
        )


        # ----------------------------------------------------
        # SUCCESS
        # ----------------------------------------------------

        st.success(
            "✅ Vehicle analysis completed successfully!"
        )


        st.write("")


        # ----------------------------------------------------
        # MAIN PRICE RESULT
        # ----------------------------------------------------

        with st.container(
            border=True
        ):

            st.subheader(
                "💰 AI Estimated Market Value"
            )

            result1, result2 = st.columns(
                [2, 1]
            )


            with result1:

                st.metric(
                    "Estimated Used-Car Price",
                    f"₹{predicted_price:,.0f}"
                )

                st.caption(
                    f"Estimated market value for "
                    f"{brand.title()} {model_name.title()}."
                )


            with result2:

                st.metric(
                    "Model R² Score",
                    "92.02%"
                )

                st.caption(
                    "Performance measured on the final test dataset."
                )


        st.write("")


        # ----------------------------------------------------
        # VEHICLE SUMMARY
        # ----------------------------------------------------

        st.subheader(
            "📋 Vehicle Snapshot"
        )


        summary1, summary2, summary3, summary4 = st.columns(4)


        with summary1:

            st.metric(
                "🚘 Brand",
                brand.title()
            )

            st.metric(
                "Model",
                model_name.title()
            )


        with summary2:

            st.metric(
                "📅 Year",
                str(year)
            )

            st.metric(
                "⛽ Fuel",
                fuel_type
            )


        with summary3:

            st.metric(
                "⚙️ Transmission",
                transmission
            )

            st.metric(
                "🚙 Body",
                body_type
            )


        with summary4:

            st.metric(
                "🛣️ Kilometers",
                f"{kilometers:,} km"
            )

            st.metric(
                "💺 Seats",
                str(seats)
            )


        # ----------------------------------------------------
        # DETAILS
        # ----------------------------------------------------

        with st.expander(
            "🔍 View Complete Prediction Details"
        ):

            details = pd.DataFrame(
                {

                    "Vehicle Parameter": [
                        "Brand",
                        "Model",
                        "Manufacturing Year",
                        "Fuel Type",
                        "Transmission",
                        "Kilometers Driven",
                        "Seats",
                        "Body Type",
                        "Prediction Algorithm"
                    ],

                    "Selected Value": [
                        brand.title(),
                        model_name.title(),
                        year,
                        fuel_type,
                        transmission,
                        f"{kilometers:,} km",
                        seats,
                        body_type,
                        "XGBoost Regressor"
                    ]

                }
            )


            st.dataframe(
                details,
                use_container_width=True,
                hide_index=True
            )


        st.info(
            "ℹ️ The displayed value is a machine-learning estimate. "
            "Actual resale price can change depending on vehicle condition, "
            "location, accident history, service records and market demand."
        )


    except Exception as error:

        st.error(
            f"❌ Prediction Error: {error}"
        )


# ============================================================
# 9. MODEL COMPARISON
# ============================================================

st.write("")


with st.expander(
    "📊 Why XGBoost Was Selected"
):

    st.write(
        "Three machine-learning regression algorithms were evaluated "
        "using the final prediction features."
    )


    comparison_data = pd.DataFrame(
        {

            "Algorithm": [
                "XGBoost",
                "Random Forest",
                "Linear Regression"
            ],

            "MAE": [
                "₹1,04,085",
                "₹1,02,645",
                "₹1,11,722"
            ],

            "RMSE": [
                "₹1,86,844",
                "₹1,87,085",
                "₹2,05,761"
            ],

            "R² Score": [
                "0.9202",
                "0.9200",
                "0.9032"
            ]

        }
    )


    st.dataframe(
        comparison_data,
        use_container_width=True,
        hide_index=True
    )


    st.success(
        "🏆 XGBoost was selected because it achieved "
        "the highest R² score and the lowest RMSE."
    )


# ============================================================
# 10. HOW SYSTEM WORKS
# ============================================================

st.write("")


with st.expander(
    "🧠 How AutoValue AI Works"
):

    about1, about2, about3 = st.columns(3)


    with about1:

        st.subheader(
            "📥 Input"
        )

        st.write(
            "Eight important vehicle specifications are collected, "
            "including brand, model, year, fuel type and kilometers driven."
        )


    with about2:

        st.subheader(
            "⚙️ Processing"
        )

        st.write(
            "Categorical and numerical information is transformed "
            "using the preprocessing pipeline learned during training."
        )


    with about3:

        st.subheader(
            "💰 Prediction"
        )

        st.write(
            "The trained XGBoost model analyzes learned market patterns "
            "and generates an estimated used-car value."
        )


# ============================================================
# 11. FOOTER
# ============================================================

st.divider()

st.caption(
    "🚘 AutoValue AI  •  Used Car Price Prediction System  •  "
    "Powered by XGBoost & Machine Learning"
)

st.caption(
    "Drive Smart • Predict Smarter"
)
