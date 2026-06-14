"""
Weather Forecast Application
=============================
A command-line weather app that fetches live data from the OpenWeatherMap API.

Architecture:
  - WeatherService (ABC)  — abstract base; defines the fetch contract
      ├── CurrentWeather  — fetches current conditions
      └── ForecastWeather — fetches 5-day forecast
  - WeatherFormatter (ABC) — abstract base; defines the format contract
      └── SimpleFormatter — prints weather in a human-readable format
  - main()                — drives the interactive loop

Design patterns demonstrated:
  - Abstract Base Classes (interface enforcement)
  - Template Method pattern (WeatherService._request() shared by all services)
  - Strategy pattern (swap formatters without changing the rest of the code)

Setup:
  1. Get a free API key from https://openweathermap.org/api
  2. Replace YOUR_API_KEY_HERE below, or set the environment variable:
         export OPENWEATHER_API_KEY="your_key_here"
  3. Install dependency: pip install requests
  4. Run: python weather_app.py
"""

import os
import requests
from abc import ABC, abstractmethod


API_KEY: str = os.getenv("OPENWEATHER_API_KEY", "YOUR_API_KEY_HERE")
BASE_URL: str = "https://api.openweathermap.org/data/2.5"


# ── Abstract service layer ─────────────────────────────────────────────────────

class WeatherService(ABC):
    """
    Abstract base class for weather data services.

    The _request() method is a shared template used by all concrete services.
    Subclasses only need to implement fetch_weather_data() using that template.
    """

    def __init__(self, city: str, api_key: str) -> None:
        self.city = city
        self.api_key = api_key

    @abstractmethod
    def fetch_weather_data(self) -> dict:
        """Fetch and return raw weather data as a dictionary."""

    def _request(self, endpoint: str) -> dict:
        """
        Send a GET request to the OpenWeatherMap API.
        Shared by all subclasses — avoids repeating connection logic.

        Raises:
            requests.exceptions.HTTPError: On 4xx/5xx responses.
        """
        params = {
            "q": self.city,
            "appid": self.api_key,
            "units": "metric",
        }
        response = requests.get(f"{BASE_URL}/{endpoint}", params=params, timeout=10)
        response.raise_for_status()
        return response.json()


class CurrentWeather(WeatherService):
    """Fetches current weather conditions for a city."""

    def fetch_weather_data(self) -> dict:
        data = self._request("weather")
        return {
            "temp": data["main"]["temp"],
            "feels_like": data["main"]["feels_like"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
            "wind_speed": data["wind"]["speed"],
        }


class ForecastWeather(WeatherService):
    """Fetches the 5-day (3-hour interval) forecast for a city."""

    def fetch_weather_data(self) -> dict:
        return self._request("forecast")


# ── Abstract formatter layer ───────────────────────────────────────────────────

class WeatherFormatter(ABC):
    """
    Abstract base class for weather output formatters.
    Swap implementations to change how data is displayed
    without touching the rest of the program.
    """

    @abstractmethod
    def format_current(self, data: dict, city: str) -> None:
        """Display current weather data."""

    @abstractmethod
    def format_forecast(self, data: dict, city: str) -> None:
        """Display 5-day forecast data."""


class SimpleFormatter(WeatherFormatter):
    """Plain-text formatter for the terminal."""

    def format_current(self, data: dict, city: str) -> None:
        print(f"\n  Current weather in {city}:")
        print(f"    Temperature : {data['temp']}°C (feels like {data['feels_like']}°C)")
        print(f"    Humidity    : {data['humidity']}%")
        print(f"    Wind speed  : {data['wind_speed']} m/s")
        print(f"    Description : {data['description'].capitalize()}")

    def format_forecast(self, data: dict, city: str) -> None:
        print(f"\n  5-Day Forecast for {city}:\n")
        print(f"  {'Date':<12} {'Temp':>8} {'Description'}")
        print("  " + "-" * 40)
        for item in data["list"]:
            if "12:00:00" in item["dt_txt"]:   # One reading per day at noon
                date = item["dt_txt"].split()[0]
                temp = item["main"]["temp"]
                desc = item["weather"][0]["description"].capitalize()
                print(f"  {date:<12} {temp:>5.1f}°C  {desc}")


# ── Main program ───────────────────────────────────────────────────────────────

def main() -> None:
    formatter = SimpleFormatter()

    print("\n  Weather Forecast Application")
    print("  " + "=" * 30)

    while True:
        print("\n  1. Current weather")
        print("  2. 5-day forecast")
        print("  3. Exit")

        choice = input("\n  Choose an option (1/2/3): ").strip()

        if choice == "3":
            print("\n  Goodbye!")
            break

        if choice not in ("1", "2"):
            print("  Invalid option. Please choose 1, 2, or 3.")
            continue

        city = input("  Enter city name: ").strip()
        if not city:
            print("  City name cannot be empty.")
            continue

        try:
            if choice == "1":
                service = CurrentWeather(city, API_KEY)
                data = service.fetch_weather_data()
                formatter.format_current(data, city)

            elif choice == "2":
                service = ForecastWeather(city, API_KEY)
                data = service.fetch_weather_data()
                formatter.format_forecast(data, city)

        except requests.exceptions.HTTPError as e:
            if e.response is not None and e.response.status_code == 404:
                print(f"  City '{city}' not found. Please check the spelling.")
            elif e.response is not None and e.response.status_code == 401:
                print("  Invalid API key. Please check your OPENWEATHER_API_KEY.")
            else:
                print(f"  HTTP error: {e}")
        except requests.exceptions.ConnectionError:
            print("  No internet connection. Please check your network.")
        except requests.exceptions.Timeout:
            print("  Request timed out. Try again later.")
        except Exception as e:
            print(f"  Unexpected error: {e}")


if __name__ == "__main__":
    main()
