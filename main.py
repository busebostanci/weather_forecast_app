import requests
from datetime import datetime, timedelta

def get_coordinates(city_name, api_key):
    # API URL to retrieve coordinates based on city name
    url = f'https://maps.googleapis.com/maps/api/geocode/json?address={city_name}&key={api_key}'
    response = requests.get(url)
    data = response.json()

    if 'results' in data and data['results']:
        lat = data['results'][0]['geometry']['location']['lat']
        lng = data['results'][0]['geometry']['location']['lng']
        return lat, lng
    else:
        return None, None

def get_current_weather(api_username, api_password, valid_date_time, parameter, location):
    url = f"https://api.meteomatics.com/{valid_date_time}/{parameter}/{location}/csv?model=mix"
    response = requests.get(url, auth=(api_username, api_password))
    return response.content

# Function to get forecast data for a specific time range and interval
def get_forecast_data(api_username, api_password, valid_date_time_range, parameter, location):
    url = f"https://api.meteomatics.com/{valid_date_time_range}/{parameter}/{location}/csv?model=mix"
    response = requests.get(url, auth=(api_username, api_password))
    return response.content

def display_forecast_data(csv_data, is_current=True):
    csv_lines = csv_data.decode('utf-8').split('\n')

    header = csv_lines[0]
    print("\nForecast Data:")

    if is_current:
        line = csv_lines[1]
        timestamp, temperature = line.split(';')
        timestamp_formatted = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ')
        temperature_celsius = float(temperature)
        print(f"Timestamp: {timestamp_formatted} | Temperature: {temperature_celsius:.2f}°C")
    else:
        forecast_per_day = {}

        for line in csv_lines[1:]:
            if line:
                timestamp, temperature = line.split(';')
                date = datetime.strptime(timestamp, '%Y-%m-%dT%H:%M:%SZ').date()
                temperature_celsius = float(temperature)

                if date not in forecast_per_day:
                    forecast_per_day[date] = [temperature_celsius, temperature_celsius, temperature_celsius, 1]
                else:
                    forecast_per_day[date][0] += temperature_celsius
                    forecast_per_day[date][1] = min(forecast_per_day[date][1], temperature_celsius)
                    forecast_per_day[date][2] = max(forecast_per_day[date][2], temperature_celsius)
                    forecast_per_day[date][3] += 1

        print("\n5-Day Forecast:")
        for date in forecast_per_day:
            avg_temperature = forecast_per_day[date][0] / forecast_per_day[date][3]
            min_temperature = forecast_per_day[date][1]
            max_temperature = forecast_per_day[date][2]
            print(f"Date: {date} | Average Temperature: {avg_temperature:.2f}°C | "
                  f"Min Temperature: {min_temperature:.2f}°C | Max Temperature: {max_temperature:.2f}°C")

def main():
    print("Welcome to the Weather Forecast App!")
    api_username = "****"  # Replace with your actual Meteomatics API username
    api_password = "****"  # Replace with your actual Meteomatics API password
    google_api_key = "****"

    while True:
        print("\n1. Get Current Weather")
        print("2. Get Forecast Data for Next 5 Days")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            city_name = input("Enter the city name: ")
            parameter = "t_2m:C"
            latitude, longitude = get_coordinates(city_name, google_api_key)

            if latitude is None or longitude is None:
                print(f"Could not find coordinates for {city_name}.")
            else:
                location = f"{latitude},{longitude}"
                current_datetime = datetime.utcnow()
                valid_date_time = current_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')
                current_weather_data = get_current_weather(api_username, api_password, valid_date_time, parameter, location)
                display_forecast_data(current_weather_data)

        elif choice == "2":
            city_name = input("Enter the city name: ")
            latitude, longitude = get_coordinates(city_name, google_api_key)

            if latitude is None or longitude is None:
                print(f"Could not find coordinates for {city_name}.")
            else:
                location = f"{latitude},{longitude}"
                current_datetime = datetime.utcnow()
                end_date_time = (current_datetime + timedelta(days=5)).strftime('%Y-%m-%dT%H:%M:%SZ')
                valid_date_time_range = f"{current_datetime.strftime('%Y-%m-%dT%H:%M:%SZ')}--{end_date_time}"
                parameter = "t_2m:C"  # Adjust parameter as needed
                forecast_data = get_forecast_data(api_username, api_password, valid_date_time_range, parameter, location)
                display_forecast_data(forecast_data, is_current=False)

        elif choice == "3":
            print("Thank you for using the Weather Forecast App. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
