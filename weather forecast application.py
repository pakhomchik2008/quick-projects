import requests
from abc import ABC, abstractmethod

API_KEY = "YOUR_API_KEY_HERE"   # Better: load from .env later
BASE_URL = "https://api.openweathermap.org/data/2.5"


# ================= ABSTRACT SERVICE =================
class WeatherService(ABC):
    def __init__(self, city: str, api_key: str):
        self.city = city
        self.api_key = api_key

    @abstractmethod
    def fetch_weather_data(self):
        pass

    def _request(self, endpoint: str):
        params = {"q": self.city, "appid": self.api_key, "units": "metric"}
        response = requests.get(f"{BASE_URL}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()


# ================= CURRENT WEATHER =================
class CurrentWeather(WeatherService):
    def fetch_weather_data(self):
        data = self._request("weather")
        return {
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }


# ================= 5-DAY FORECAST =================
class ForecastWeather(WeatherService):
    def fetch_weather_data(self):
        return self._request("forecast")


# ================= FORMATTER =================
class WeatherFormatter(ABC):
    @abstractmethod
    def format(self, data, city):
        pass


class SimpleFormatter(WeatherFormatter):
    def format(self, data, city):
        print(f"{city}: {data['temp']}°C, {data['description'].capitalize()}")


# ================= MAIN PROGRAM =================
def main():
    formatter = SimpleFormatter()

    while True:
        print("\n1. Show 5-day forecast")
        print("2. Show current weather")
        print("3. Exit")

        choice = input("Choose 1/2/3: ").strip()
        if choice == "3":
            print("Bye 👋")
            break

        city = input("Enter city: ").strip()

        try:
            if choice == "1":
                service = ForecastWeather(city, API_KEY)
                data = service.fetch_weather_data()

                print(f"\n5-Day Forecast for {city}:\n")

                printed = set()
                for item in data["list"]:
                    # Print only at 12:00 each day
                    if "12:00:00" in item["dt_txt"]:
                        date = item["dt_txt"].split()[0]
                        temp = item["main"]["temp"]
                        desc = item["weather"][0]["description"]
                        print(f"{date} | {temp}°C | {desc}")

            elif choice == "2":
                service = CurrentWeather(city, API_KEY)
                data = service.fetch_weather_data()
                formatter.format(data, city)

            else:
                print("Invalid option!")

        except requests.exceptions.HTTPError:
            print(" City not found or API error.")
        except Exception as e:
            print(" Something went wrong:", e)


if __name__ == "__main__":
    main()

