import requests

API_KEY = "0341b3db2a90744fc2aa6438ec2c0b77"


def get_data(place, forecast_days=None, kind=None):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    print(url)
    response = requests.get(url)
    data = response.json()

    filtered_data = data["list"]
    city_data = data["city"]
    print(city_data)
    nr_values = 8 * forecast_days
    filtered_data = filtered_data[:nr_values]

    if kind == "Temperature":
        filtered_data = [item["main"]["temp"] for item in filtered_data]
    if kind == "Sky":
        filtered_data = [item["weather"][0]["main"] for item in filtered_data]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="Tokyo", forecast_days=3, kind="Temperature"))