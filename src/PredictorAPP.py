import streamlit as st
import joblib
import pandas as pd
import numpy as np

# Loading the pre-trained model
model_file_path = "C:\Users\17174\OneDrive\Desktop\606_Project_Final\Code files and Dataset\best_model.pkl"
model = joblib.load(model_file_path)

# Defining feature names
feature_names = ['Store', 'Dept', 'Year', 'Month', 'Day', 'IsHoliday', 'Temperature', 'Fuel_Price', 'Unemployment', 'Size', 'Type_A', 'Type_B', 'Type_C']

# Input validation
def validate_input(input_data):
    errors = []

    if not (1990 <= input_data["Year"] <= 2050):
        errors.append("Year must be between 1990 and 2050")

    if not (1 <= input_data["Month"] <= 12):
        errors.append("Month must be between 1 and 12")

    max_days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    # Ensuring number of days in February in Leap years are accepted upto 29 days
    if input_data["Year"] % 4 == 0 and (input_data["Year"] % 100 != 0 or input_data["Year"] % 400 == 0):
        max_days_in_month[2] = 29

    if not (1 <= input_data["Day"] <= max_days_in_month[input_data["Month"]]):
        errors.append("Invalid day for the selected month")

    if input_data["Size"] < 1:
        errors.append("Invalid value for Store Size")

    return errors

# Creating Streamlit app
st.title("Sales Predictor App")

# Input fields for feature values
feature_input = {}
feature_input["Store"] = st.selectbox("Select Store", list(range(1, 46)))
feature_input["Dept"] = st.selectbox("Select Dept", list(range(1, 99)))
feature_input["Year"] = st.number_input("Year (1990-2050)", min_value=1990, max_value=2050)
feature_input["Month"] = st.selectbox("Month (1-12)", list(range(1, 13)))
feature_input["Day"] = st.number_input("Day (1-31)", min_value=1, max_value=31)
feature_input["IsHoliday"] = 1 if st.checkbox("Is Holiday") else 0 
feature_input["Temperature"] = st.number_input("Temperature")
feature_input["Fuel_Price"] = st.number_input("Fuel Price")
feature_input["Unemployment"] = st.number_input("Unemployment")
feature_input["Size"] = st.number_input("Size (min 1)", min_value=1)

store_type = st.selectbox("Select Store Type", ["Type_A", "Type_B", "Type_C"])
feature_input["Type_A"] = 1 if store_type == "Type_A" else 0
feature_input["Type_B"] = 1 if store_type == "Type_B" else 0
feature_input["Type_C"] = 1 if store_type == "Type_C" else 0

# Prediction button
if st.button("Predict"):
    validation_errors = validate_input(feature_input)
    
    if validation_errors:
        st.error("\n".join(validation_errors))
    else:
        input_data = pd.DataFrame([feature_input], columns=feature_names)
        prediction = model.predict(input_data)
        # Applying inverse log transformation to get the actual sales value
        actual_sales = np.exp(prediction[0])
        st.success(f"Predicted Sales: {actual_sales:.2f}")
