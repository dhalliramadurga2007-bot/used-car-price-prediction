# 🚗 AI-Powered Used Car Price Prediction System

An intelligent Machine Learning application designed to estimate the **market value of used cars** based on important vehicle specifications.

The project compares multiple regression algorithms and selects the best-performing model for real-time price prediction through an interactive **Streamlit web application**.

---

## 🌐 Live Demo

🚀 Try the deployed application here:

[Open Used Car Price Prediction App](https://used-car-price-prediction-lrtvy8so4ctyjajhqzft5a.streamlit.app/)

---

## 🌟 Project Overview

Buying or selling a used car can be difficult because the price depends on multiple factors such as:

* Brand
* Model
* Manufacturing year
* Fuel type
* Transmission
* Kilometers driven
* Seating capacity
* Body type

This project uses **Machine Learning** to analyze these factors and estimate the market value of a used car.

The final Streamlit application allows users to enter vehicle details and instantly receive a predicted price.

---

## ✨ Key Features

* 🚘 Used-car price estimation
* 🤖 Machine Learning-based prediction
* 📊 Comparison of multiple regression algorithms
* 🏆 Selection of the best-performing model
* ⚡ Real-time price prediction
* 💻 Interactive Streamlit interface
* 🔤 Input cleaning and normalization
* 📋 Vehicle summary after prediction
* 📈 Model performance evaluation
* 💰 Price output displayed in Indian Rupees (₹)

---

## 🧠 Machine Learning Algorithms

The following regression algorithms were evaluated:

1. **Linear Regression**
2. **Random Forest Regressor**
3. **XGBoost Regressor**

---

## 📊 Model Comparison

| Algorithm                |           MAE |          RMSE |   R² Score |
| ------------------------ | ------------: | ------------: | ---------: |
| Linear Regression        |     ₹1,11,722 |     ₹2,05,761 |     0.9032 |
| Random Forest Regressor  | **₹1,02,645** |     ₹1,87,085 |     0.9200 |
| **XGBoost Regressor 🏆** |     ₹1,04,085 | **₹1,86,844** | **0.9202** |

### 🏆 Final Selected Model

**XGBoost Regressor**

XGBoost was selected as the final model because it achieved the **highest R² score** and the **lowest RMSE** among the evaluated algorithms.

Random Forest achieved the lowest MAE, while XGBoost provided the strongest overall performance based on RMSE and R² score.

**Final R² Score: `0.9202`**

---

## 🚘 Input Features

The prediction system uses the following vehicle information:

| Feature               | Description                      |
| --------------------- | -------------------------------- |
| 🏷️ Brand             | Vehicle manufacturer             |
| 🚗 Model              | Vehicle model                    |
| 📅 Manufacturing Year | Year of manufacture              |
| ⛽ Fuel Type           | Petrol, Diesel, CNG, LPG, etc.   |
| ⚙️ Transmission       | Manual or Automatic              |
| 🛣️ Kilometers Driven | Total distance travelled         |
| 💺 Seats              | Seating capacity                 |
| 🚙 Body Type          | Hatchback, Sedan, SUV, MUV, etc. |

---

## ⚙️ How It Works

```text
User Vehicle Details
        ↓
Input Cleaning & Normalization
        ↓
Feature Preprocessing
        ↓
XGBoost Regression Model
        ↓
Price Prediction
        ↓
Estimated Used-Car Market Value
```

The target price is handled using a log transformation during model training. The predicted value is converted back to the original price scale before being displayed to the user.

---

## 🛠️ Technologies Used

### 👨‍💻 Programming

* Python

### 🤖 Machine Learning

* Scikit-learn
* XGBoost
* NumPy
* Pandas

### 🌐 Web Application

* Streamlit

### 💾 Model Storage

* Joblib

### 🔧 Development & Deployment

* VS Code
* GitHub
* Streamlit Community Cloud

---

## 📁 Project Structure

```text
used-car-price-prediction/
│
├── app.py
├── compare_models.py
├── train_final_model.py
├── final_app_model.pkl
├── final_app_model_info.pkl
├── final_model_comparison.csv
├── requirements.txt
└── README.md
```

---

## 💻 Run the Project Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/dhalliramadurga2007-bot/used-car-price-prediction.git
```

### 2️⃣ Open the Project Folder

```bash
cd used-car-price-prediction
```

### 3️⃣ Install Required Packages

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Streamlit Application

```bash
streamlit run app.py
```

The application will normally open at:

```text
http://localhost:8501
```

---

## 🧪 Example Prediction

Example vehicle details:

```text
Brand              : Honda
Model              : City
Manufacturing Year : 2018
Fuel Type           : Petrol
Transmission        : Automatic
Kilometers Driven  : 60,000
Seats               : 5
Body Type           : Sedan
```

The application processes these details and displays the estimated used-car price in **₹ INR**.

---

## 📌 Model Evaluation Metrics

The models were evaluated using:

* **MAE — Mean Absolute Error:** Lower is better
* **RMSE — Root Mean Squared Error:** Lower is better
* **R² Score:** Higher is better

The final XGBoost model achieved an **R² score of approximately 0.9202** on the test data.

---

## 🚀 Future Enhancements

* 📍 Location-based price prediction
* 📸 Vehicle image-based condition analysis
* 🔎 Dynamic brand and model selection
* 📊 Advanced price analytics
* ☁️ Enhanced cloud deployment
* 📱 Improved mobile-friendly interface
* 🔄 Model retraining with newer market data

---

## ⚠️ Disclaimer

The predicted price is a **Machine Learning estimate** based on the available dataset and selected vehicle attributes.

Actual resale prices may vary depending on factors such as:

* Vehicle condition
* Location
* Service history
* Ownership history
* Market demand
* Other real-world factors

---

## ❤️ Project Goal

The goal of this project is to demonstrate how **Machine Learning can simplify used-car valuation** by providing users with a fast, data-driven, and easy-to-use price estimation system.

**🚗 Smart Valuation • 🤖 Machine Learning • 📊 Data-Driven Prediction**
