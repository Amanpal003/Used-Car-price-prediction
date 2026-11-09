
# Used Car Price Prediction

## Project Overview
This project aims to predict the estimated selling price of used cars using Machine Learning.

## Problem Type
Supervised Machine Learning - Regression

## Machine Learning Algorithms
1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Jupyter Notebook
- FastAPI
- Streamlit

 ## Dataset
Dataset Name: Vehicle Dataset from CarDekho
Source: Kaggle
Dataset File: CAR DETAILS FROM CAR DEKHO.csv
Location: data/raw/

## Dataset Link: https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho

The dataset contains information about used cars, including manufacturing year, selling price, kilometers driven, fuel type, transmission, owner, and seller type.

## Project Workflow
1. Dataset Collection
2. Exploratory Data Analysis (EDA)
3. Data Preprocessing
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. API Development
8. Frontend Development
9. Deployment

## Machine Learning Models

The following regression algorithms were trained and evaluated:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

## Model Evaluation

Models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R2 Score

### Model Comparison

| Model | MAE | RMSE | R2 Score |
|---|---:|---:|---:|
| Linear Regression | 179642.89 | 384722.69 | 0.5405 |
| Decision Tree | 198734.06 | 473873.48 | 0.3029 |
| Random Forest | 158827.69 | 367979.71 | 0.5796 |

**Best Performing Model:** Random Forest Regressor

## Saved Model

The trained Random Forest pipeline is saved in:

`models/random_forest_model.pkl`

The pipeline includes preprocessing and the trained regression model.

## Project Status

EDA, data preprocessing, feature engineering,
model training, and model evaluation completed.

Currently working on user input-based price prediction.

