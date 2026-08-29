import streamlit as st
import pandas as pd
import numpy as np
import joblib


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Used Car Price Prediction",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ============================================================
# LOAD FINAL MODEL
# ============================================================

@st.cache_resource
def load_model():
    return joblib.load("models/final_app_model.pkl")


model = load_model()


# ============================================================
# CUSTOM PROFESSIONAL CSS
# ============================================================

st.markdown(
"""
<style>

/* Main page */
.stApp {
    background:
        radial-gradient(circle at 10% 10%, rgba(30, 64, 175, 0.12), transparent 25%),
        radial-gradient(circle at 90% 20%, rgba(14, 165, 233, 0.10), transparent 25%);
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* Main title */
h1 {
    font-size: 3rem !important;
    font-weight: 800 !important;
    letter-spacing: -1px;
}

/* Headings */
h2, h3 {
    font-weight: 700 !important;
}

/* Containers */
[data-testid="stVerticalBlockBorderWrapper"] {
    border-radius: 18px !important;
    border: 1px solid rgba(120, 120, 120, 0.22) !important;
    box-shadow: 0px 8px 26px rgba(0,0,0,0.05);
}

/* Inputs */
div[data-baseweb="input"] > div {
    border-radius: 10px !important;
}

div[data-baseweb="select"] > div {
    border-radius: 10px !important;
}

/* Primary button */
div.stButton > button[kind="primary"] {
    height: 54px;
    border-radius: 12px;
    font-weight: 750;
    font-size: 17px;
    box-shadow: 0px 8px 24px rgba(59, 130, 246, 0.18);
}

/* Normal buttons */
div.stButton > button {
    border-radius: 12px;
    font-weight: 650;
}

/* Metrics */
[data-testid="stMetric"] {
    padding: 17px;
    border-radius: 15px;
    background: rgba(120,120,120,0.06);
    border: 1px solid rgba(120,120,120,0.15);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    border-right: 1px solid rgba(120,120,120,0.15);
}

/* Success box */
div[data-testid="stAlert"] {
    border-radius: 12px;
}

/* Divider spacing */
hr {
    margin-top: 1.2rem;
    margin-bottom: 1.2rem;
}

</style>
""",
    unsafe_allow_html=True
)


# ============================================================
# SIDEBAR
# ============================================================

with st.sidebar:

    st.title("🚗 Car Price AI")

    st.caption(
        "Intelligent used-car market value estimation"
    )

    st.divider()

    st.subheader("🤖 Final Model")

    st.success("XGBoost Regressor")

    st.write(
        "Selected after comparing multiple machine-learning algorithms."
    )

    st.divider()

    st.subheader("📊 Model Performance")

    st.metric(
        "R² Score",
        "0.9202"
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

    st.subheader("⚙️ Prediction Flow")

    st.write(
        """
        **1.** Enter vehicle details

        **2.** Inputs are standardized

        **3.** XGBoost analyzes the data

        **4.** Estimated market price is generated
        """
    )

    st.divider()

    st.caption(
        "Used Car Price Prediction • ML Project"
    )


# ============================================================
# HERO / HEADER
# ============================================================

st.title("🚗 Used Car Price Prediction")

st.subheader(
    "AI-Powered Vehicle Valuation System"
)

st.write(
    """
    Estimate the market value of a used vehicle using machine learning.
    Enter the vehicle specifications below and the system will generate
    an estimated resale price using the final selected XGBoost model.
    """
)

# Top info metrics
top1, top2, top3 = st.columns(3)

with top1:
    st.metric(
        "Final Algorithm",
        "XGBoost"
    )

with top2:
    st.metric(
        "R² Score",
        "92.02%"
    )

with top3:
    st.metric(
        "Input Features",
        "8"
    )

st.divider()


# ============================================================
# VEHICLE INFORMATION
# ============================================================

with st.container(border=True):

    st.subheader("🚘 Vehicle Information")

    st.caption(
        "Enter the basic identity and manufacturing details of the vehicle."
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        brand = st.text_input(
            "Brand",
            value="Honda",
            placeholder="Example: Honda",
            help="Enter the vehicle manufacturer."
        )

    with col2:

        model_name = st.text_input(
            "Model",
            value="City",
            placeholder="Example: City",
            help="Enter only the model name. Brand name will be handled automatically."
        )

    with col3:

        year = st.number_input(
            "Manufacturing Year",
            min_value=1990,
            max_value=2026,
            value=2018,
            step=1
        )


# ============================================================
# DRIVING DETAILS
# ============================================================

st.write("")

with st.container(border=True):

    st.subheader("⛽ Driving & Performance")

    st.caption(
        "Provide the fuel, transmission and usage information."
    )

    col4, col5, col6 = st.columns(3)

    with col4:

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

    with col5:

        transmission = st.selectbox(
            "Transmission",
            [
                "Manual",
                "Automatic"
            ]
        )

    with col6:

        kilometers = st.number_input(
            "Kilometers Driven",
            min_value=0,
            max_value=500000,
            value=60000,
            step=1000,
            help="Total kilometers driven by the vehicle."
        )


# ============================================================
# ADDITIONAL DETAILS
# ============================================================

st.write("")

with st.container(border=True):

    st.subheader("⚙️ Additional Details")

    st.caption(
        "Add vehicle seating capacity and body type."
    )

    col7, col8 = st.columns(2)

    with col7:

        seats = st.number_input(
            "Seats",
            min_value=2,
            max_value=10,
            value=5,
            step=1
        )

    with col8:

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


# ============================================================
# PREDICTION SECTION
# ============================================================

st.write("")

st.subheader("🔮 Generate Price Estimate")

st.caption(
    "Review the vehicle details and click below to calculate the estimated used-car price."
)

predict_button = st.button(
    "✨ Predict Estimated Car Price",
    use_container_width=True,
    type="primary"
)


# ============================================================
# PREDICTION LOGIC
# ============================================================

if predict_button:

    try:

        # ----------------------------------------------------
        # INPUT VALIDATION
        # ----------------------------------------------------

        if not brand.strip():
            st.error("Please enter the car brand.")
            st.stop()

        if not model_name.strip():
            st.error("Please enter the car model.")
            st.stop()


        # ----------------------------------------------------
        # CLEAN BRAND
        # Honda / HONDA / honda -> honda
        # ----------------------------------------------------

        brand_clean = brand.strip().lower()


        # ----------------------------------------------------
        # CLEAN MODEL
        # City / CITY -> city
        # ----------------------------------------------------

        model_clean = model_name.strip().lower()


        # ----------------------------------------------------
        # ADD BRAND TO MODEL IF REQUIRED
        #
        # Honda + City -> honda city
        # BMW + 3 Series -> bmw 3 series
        # ----------------------------------------------------

        if not model_clean.startswith(brand_clean):

            model_clean = (
                brand_clean
                + " "
                + model_clean
            )


        # ----------------------------------------------------
        # CLEAN OTHER CATEGORICAL INPUTS
        # ----------------------------------------------------

        fuel_clean = fuel_type.strip().lower()

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
        # CREATE MODEL INPUT
        #
        # DO NOT CHANGE THESE COLUMN NAMES
        # ----------------------------------------------------

        input_data = pd.DataFrame({

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

        })


        # ----------------------------------------------------
        # MODEL PREDICTION
        # ----------------------------------------------------

        with st.spinner(
            "Analyzing vehicle specifications..."
        ):

            log_prediction = model.predict(
                input_data
            )[0]


        # ----------------------------------------------------
        # LOG PRICE -> ACTUAL RUPEES
        # ----------------------------------------------------

        predicted_price = np.expm1(
            log_prediction
        )

        predicted_price = max(
            float(predicted_price),
            0
        )


        # ----------------------------------------------------
        # SUCCESS MESSAGE
        # ----------------------------------------------------

        st.success(
            "✅ Vehicle analysis completed successfully!"
        )


        # ----------------------------------------------------
        # BIG RESULT SECTION
        # ----------------------------------------------------

        st.subheader("💰 Estimated Market Value")

        result_col1, result_col2 = st.columns(
            [2, 1]
        )

        with result_col1:

            st.metric(
                label="Estimated Used Car Price",
                value=f"₹{predicted_price:,.2f}"
            )

            st.caption(
                "AI-powered price estimate generated using the final XGBoost regression model."
            )

        with result_col2:

            st.metric(
                label="Model Confidence Indicator",
                value="R² 92.02%"
            )

            st.caption(
                "Performance measured on the test dataset."
            )


        # ----------------------------------------------------
        # VEHICLE SUMMARY
        # ----------------------------------------------------

        st.write("")

        st.subheader("📋 Vehicle Summary")

        summary1, summary2, summary3, summary4 = st.columns(4)

        with summary1:

            st.metric(
                "Brand",
                brand.title()
            )

            st.metric(
                "Model",
                model_name.title()
            )

        with summary2:

            st.metric(
                "Year",
                str(year)
            )

            st.metric(
                "Fuel",
                fuel_type
            )

        with summary3:

            st.metric(
                "Transmission",
                transmission
            )

            st.metric(
                "Body Type",
                body_type
            )

        with summary4:

            st.metric(
                "Kilometers",
                f"{kilometers:,} km"
            )

            st.metric(
                "Seats",
                str(seats)
            )


        # ----------------------------------------------------
        # DETAILED VIEW
        # ----------------------------------------------------

        with st.expander(
            "🔍 View Complete Prediction Details"
        ):

            details = pd.DataFrame({

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

            })

            st.dataframe(
                details,
                use_container_width=True,
                hide_index=True
            )


        # ----------------------------------------------------
        # NOTE
        # ----------------------------------------------------

        st.info(
            "ℹ️ The displayed price is a machine-learning estimate. "
            "Actual resale value may vary depending on vehicle condition, "
            "location, service history and current market demand."
        )


    except Exception as error:

        st.error(
            f"Prediction Error: {error}"
        )


# ============================================================
# MODEL COMPARISON
# ============================================================

st.write("")

with st.expander(
    "📊 Why XGBoost Was Selected"
):

    st.write(
        """
        Three regression algorithms were tested using the same
        final prediction features.
        """
    )

    comparison_data = pd.DataFrame({

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

    })

    st.dataframe(
        comparison_data,
        use_container_width=True,
        hide_index=True
    )

    st.success(
        "🏆 XGBoost was selected because it achieved the highest "
        "R² score and the lowest RMSE among the tested models."
    )


# ============================================================
# ABOUT SYSTEM
# ============================================================

st.write("")

with st.expander(
    "🤖 About This System"
):

    about1, about2, about3 = st.columns(3)

    with about1:

        st.subheader("📥 Input")

        st.write(
            """
            The system uses eight important vehicle attributes including
            brand, model, year, fuel type and kilometers driven.
            """
        )

    with about2:

        st.subheader("🧠 Processing")

        st.write(
            """
            Categorical and numerical values are transformed using the
            trained preprocessing pipeline before prediction.
            """
        )

    with about3:

        st.subheader("💰 Output")

        st.write(
            """
            The final XGBoost model generates an estimated used-car
            market price in Indian Rupees.
            """
        )


# ============================================================
# FOOTER
# ============================================================

st.divider()

footer1, footer2, footer3 = st.columns(
    [1, 2, 1]
)

with footer2:

    st.caption(
        "🚗 Used Car Price Prediction System  •  "
        "Powered by XGBoost  •  Machine Learning Project"
    )