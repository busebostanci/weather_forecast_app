import requests

def get_coordinates(city_name, api_key):
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
    response = requests.get(url, auth=(api_username,
