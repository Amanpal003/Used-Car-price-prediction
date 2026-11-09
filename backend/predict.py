import pandas as pd
import joblib
from pathlib import Path

# Get the project root directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Load the trained Random Forest model
MODEL_PATH = BASE_DIR / "models" / "random_forest_model.pkl"

model = joblib.load(MODEL_PATH)


# Function to predict used car price
def predict_car_price(car_details):

    # Convert user input into a DataFrame
    input_data = pd.DataFrame([car_details])

    # Predict the car selling price
    predicted_price = model.predict(input_data)[0]

    return predicted_price


# Test the prediction function
if __name__ == "__main__":

    car = {
        "year": 2020,
        "km_driven": 35000,
        "fuel": "Petrol",
        "seller_type": "Individual",
        "transmission": "Manual",
        "owner": "First Owner",
        "brand": "Hyundai"
    }

    price = predict_car_price(car)

    print(f"Predicted Car Price: ₹{price:,.0f}")