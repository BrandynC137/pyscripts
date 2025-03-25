import pgeocode # type: ignore
import requests # type: ignore

def get_lat_long_from_zip(zip_code, country_code="US"):
    nomi = pgeocode.Nominatim(country_code)
    location = nomi.query_postal_code(zip_code)
    return location.latitude, location.longitude

def get_local_weather(lat, long):
    r = requests.get(f"https://api.weather.gov/points/{lat},{long}")
    forecast = r.json()["properties"]["forecast"]
    now = requests.get(forecast)
    return now.json()["properties"]["periods"][0]["detailedForecast"]

def main():
    zip_code = input("Enter your zip code: ")
    latitude, longitude = get_lat_long_from_zip(zip_code)
    
    print(f"Lat: {latitude}, Long: {longitude}")
    local_weather = get_local_weather(latitude, longitude)
    print(local_weather)


# This ensures that the main function only runs when the script is executed directly
if __name__ == "__main__":
    main()