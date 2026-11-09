🚗 Used Car Price Prediction

A Machine Learning web application that predicts the estimated selling price of a used car based on its details such as brand, manufacturing year, kilometers driven, fuel type, transmission, and ownership.

🎯 Project Objective

The objective of this project is to build a machine learning model that estimates used car prices using historical car sales data.

🛠️ Technologies Used

- Python
- Pandas and NumPy
- Matplotlib and Seaborn
- Scikit-learn
- Random Forest Regressor
- Joblib
- FastAPI
- Streamlit
- Git and GitHub

📂 Project Structure

Used-Car-Price-Prediction/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── 01_EDA.ipynb
│   └── 02_Data_Preprocessing.ipynb
│
├── models/
│   └── random_forest_model.pkl
│
├── backend/
│   ├── predict.py
│   └── main.py
│
├── frontend/
│   ├── app.py
│   └── assets/
│
├── requirements.txt
├── .gitignore
└── README.md

📊 Dataset

- Source: Kaggle – Vehicle Dataset from CarDekho
- Original records: 4,340
- Records after removing duplicates: 3,577
- Target variable: "selling_price"

Features Used

- Year
- Kilometers Driven
- Fuel
- Seller Type
- Transmission
- Owner
- Brand

🔍 Exploratory Data Analysis (EDA)

Performed exploratory data analysis to understand the dataset:

- Checked missing values and duplicate records.
- Analyzed numerical and categorical features.
- Extracted car brands from car names.
- Visualized feature distributions.
- Identified outliers using the IQR method.
- Analyzed correlations between numerical features.

⚙️ Data Preprocessing

- Removed duplicate records.
- Extracted brand names from the car name column.
- Separated independent and dependent variables.
- Split the dataset into training and testing sets (80:20).
- Applied StandardScaler to numerical features.
- Applied OneHotEncoder to categorical features.
- Used ColumnTransformer and Scikit-learn Pipeline.

🤖 Machine Learning Models

Three regression models were trained and evaluated:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

Model Evaluation

Model| MAE| RMSE| R² Score
Linear Regression| 179642.89| 384722.69| 0.5405
Decision Tree| 198734.06| 473873.48| 0.3029
Random Forest| 158827.69| 367979.71| 0.5796

Random Forest Regressor performed best among the three tested models.

🌐 Application Features

- User-friendly Streamlit interface.
- Enter car details to predict its estimated price.
- FastAPI backend for prediction requests.
- Indian currency formatting.
- Input validation and error handling.

▶️ How to Run the Project

1. Clone the repository

git clone https://github.com/Amanpal003/Used-Car-price-prediction.git

2. Navigate to the project folder

cd Used-Car-Price-Prediction

3. Install dependencies

pip install -r requirements.txt

4. Start the FastAPI backend

python -m uvicorn backend.main:app --reload

API documentation:

"http://127.0.0.1:8000/docs"

5. Start the Streamlit frontend

Open another terminal and run:

python -m streamlit run frontend/app.py

Open the application:

"http://localhost:8501"

📈 Evaluation Metrics

- MAE: Measures the average absolute difference between actual and predicted prices.
- RMSE: Measures prediction error while giving more weight to larger errors.
- R² Score: Measures how much variation in the target variable is explained by the model.

⚠️ Limitations

- Predictions depend on the available historical dataset.
- The dataset contains car records from 1992 to 2020.
- Predictions are estimates and may differ from actual market prices.

👨‍💻 Author

Aman Pal

Machine Learning | Python | Data Science
