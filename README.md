# Weather Forecast App

The Weather Forecast App is a command-line tool that allows users to retrieve current weather data and 5-day forecast information for a specific location using the Meteomatics API. The app provides temperature data in Celsius for the specified location and time range. It also uses the Google Maps Geocoding API to retrieve latitude and longitude coordinates based on the city name provided by the user.

## Features

- Get current weather data for a specific location.
- Get a 5-day forecast for a specific location and time range.
- Display average, minimum, and maximum temperatures for each day in the 5-day forecast.

## Prerequisites

Before using the app, make sure you have the following:

- Python 3.x installed.
- A valid Meteomatics API username and password.
- A valid Google Maps API key.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/weather_forecast_app.git
   cd weather_forecast_app
   
2. Install required packages using pip:
   ```bash
    pip install requests

  ## Usage

1. Run the app:

   ```bash
   python main.py

Follow the on-screen instructions to choose an option:

1. Get Current Weather: Retrieve the current weather data for a specific city.
2. Get Forecast Data for a Time Range: Retrieve the 5-day forecast data for a specific city and time range.
Provide the requested information when prompted, such as the city name.

## APIs Used

- **Meteomatics API:** The app uses the Meteomatics API to retrieve weather forecast data. It queries the API for both current weather and 5-day forecast information based on the location and time range provided by the user.

- **Google Maps Geocoding API:** The app uses the Google Maps Geocoding API to convert a city name to latitude and longitude coordinates. This allows the app to accurately query weather data based on the user-provided city name.


The app will display temperature data based on your selection.
