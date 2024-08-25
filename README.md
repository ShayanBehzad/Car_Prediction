
# Car Prediction Project

A cutting-edge application designed to predict the price of cars using advanced Machine Learning techniques.

## Features

- **Data Scraping**: Data is scraped from [bama.ir](https://bama.ir) and inserted into a MySQL database.
- **Data Cleaning**: The scraped data is cleaned and processed into a usable dataset using Pandas.
- **Machine Learning**: The dataset is analyzed using the `RandomForestRegressor` algorithm, which provides an approximate 90% accuracy in predicting car prices based on specifications provided by the user.

## Technologies Used

- **Python**: The core language for development.
- **scikit-learn**: For implementing the machine learning model.
- **Pandas**: For data cleaning and manipulation.
- **MySQL**: To store the scraped data.
- **Nginx**: For serving the application.
- **Gunicorn**: As the WSGI HTTP server to run the Django application.

## How It Works

1. **Data Collection**: The application scrapes data from bama.ir, focusing on various car attributes.
2. **Data Cleaning**: Pandas is used to clean and prepare the dataset.
3. **Model Training**: The cleaned data is fed into the `RandomForestRegressor` to train the model.
4. **Price Prediction**: Users can input their car's specifications, and the model will predict the approximate price with a 90% accuracy.

## Deployment

The project is deployed using Nginx and Gunicorn and can be accessed at [www.shayanbehzad.ir/car_prediction/](https://www.shayanbehzad.ir/car_prediction/).

Also explaiend Project in YouTube: https://www.youtube.com/watch?v=Iiv8YwjqKQU

