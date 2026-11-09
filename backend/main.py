from fastapi import FastAPI
from pydantic import BaseModel

# Import prediction function
from backend.predict import predict_car_price

# Create FastAPI application
app = FastAPI()

class CarDetails(BaseModel):
    year: int
    km_driven: int
    fuel: str
    seller_type: str
    transmission: str
    owner: str
    brand: str

# Create a home route
@app.get("/")
def home():
    return {"message": "Used Car Price Prediction API is running!"}

# Prediction route
@app.post("/predict")
def predict_price(car: CarDetails):

    # Convert input data into dictionary
    car_data = car.model_dump()

    # Predict car price
    predicted_price = predict_car_price(car_data)

    # Return predicted price
    return {
        "predicted_price": round(float(predicted_price), 2)
    }