import streamlit as st
import pandas as pd
import numpy as np
import joblib


# ============================================================
# 1. LOAD FINAL MODEL
# ============================================================

model = joblib.load("models/final_app_model.pkl")


# ============================================================
# 2. PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Used Car Price Prediction",
    page_icon="🚗",
    layout="wide"
)

st.title("🚗 Used Car Price Prediction System")

st.write(
    "Enter the vehicle details below to estimate "
    "the used-car price using the XGBoost model."
)

st.divider()


# ============================================================
# 3. VEHICLE INFORMATION
# ============================================================

st.subheader("Vehicle Information")

col1, col2, col3 = st.columns(3)


# BRAND
with col1:

    brand = st.text_input(
        "Brand",
        value="Honda",
        placeholder="Example: Honda"
    )


# MODEL
with col2:

    model_name = st.text_input(
        "Model",
        value="City",
        placeholder="Example: City"
    )


# YEAR
with col3:

    year = st.number_input(
        "Manufacturing Year",
        min_value=1990,
        max_value=2026,
        value=2018,
        step=1
    )


# ============================================================
# 4. FUEL / TRANSMISSION / KM
# ============================================================

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
        step=1000
    )


# ============================================================
# 5. ADDITIONAL DETAILS
# ============================================================

st.subheader("Additional Details")

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


st.divider()


# ============================================================
# 6. PREDICTION BUTTON
# ============================================================

if st.button(
    "🔮 Predict Car Price",
    use_container_width=True
):

    try:

        # ----------------------------------------------------
        # VALIDATE INPUT
        # ----------------------------------------------------

        if not brand.strip():

            st.error(
                "Please enter the car brand."
            )

            st.stop()


        if not model_name.strip():

            st.error(
                "Please enter the car model."
            )

            st.stop()


        # ----------------------------------------------------
        # CLEAN BRAND
        # Honda / HONDA / honda -> honda
        # ----------------------------------------------------

        brand_clean = (
            brand
            .strip()
            .lower()
        )


        # ----------------------------------------------------
        # CLEAN MODEL
        # City -> city
        # CITY -> city
        # Honda City -> honda city
        # ----------------------------------------------------

        model_clean = (
            model_name
            .strip()
            .lower()
        )


        # ----------------------------------------------------
        # ADD BRAND NAME TO MODEL WHEN REQUIRED
        #
        # Brand = Honda
        # Model = City
        #
        # Final model value = honda city
        # ----------------------------------------------------

        if not model_clean.startswith(
            brand_clean
        ):

            model_clean = (
                brand_clean
                + " "
                + model_clean
            )


        # ----------------------------------------------------
        # CLEAN OTHER CATEGORICAL VALUES
        # ----------------------------------------------------

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
        # CREATE INPUT DATA
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
        # PREDICT LOG PRICE
        # ----------------------------------------------------

        log_prediction = model.predict(
            input_data
        )[0]


        # ----------------------------------------------------
        # CONVERT LOG PRICE BACK TO RUPEES
        # ----------------------------------------------------

        predicted_price = np.expm1(
            log_prediction
        )


        # Prevent negative price
        predicted_price = max(
            float(predicted_price),
            0
        )


        # ----------------------------------------------------
        # DISPLAY RESULT
        # ----------------------------------------------------

        st.success(
            "Prediction completed successfully!"
        )


        st.metric(
            "Estimated Used Car Price",
            f"₹{predicted_price:,.2f}"
        )


        st.caption(
            "Prediction generated using the "
            "final selected XGBoost model."
        )


    except Exception as error:

        st.error(
            f"Prediction Error: {error}"
        )