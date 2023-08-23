from datetime import datetime

def display_forecast_data(csv_data, is_current=True):
    csv_lines = csv_data.decode('utf-8').split('\n')

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
