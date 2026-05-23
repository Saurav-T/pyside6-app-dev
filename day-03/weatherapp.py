import sys
import requests
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout,
    QLineEdit, QPushButton, QLabel
)

API_KEY = "YOUR_API_KEY"
BASE_URL = "http://api.weatherapi.com/v1/current.json"


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App (WeatherAPI)")
        self.resize(320, 200)

        # UI
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city (e.g., Kathmandu)")

        self.button = QPushButton("Get Weather")

        self.output = QLabel("Weather info will appear here")

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.city_input)
        layout.addWidget(self.button)
        layout.addWidget(self.output)
        self.setLayout(layout)

        # signal
        self.button.clicked.connect(self.fetch_weather)

    def fetch_weather(self):
        city = self.city_input.text().strip()

        if not city:
            self.output.setText("Please enter a city name")
            return

        try:
            params = {
                "key": API_KEY,
                "q": city,
                "aqi": "no"
            }

            response = requests.get(BASE_URL, params=params)
            data = response.json()

            if "error" in data:
                self.output.setText("City not found / API error")
                return

            location = data["location"]["name"]
            country = data["location"]["country"]

            temp = data["current"]["temp_c"]
            condition = data["current"]["condition"]["text"]
            humidity = data["current"]["humidity"]
            wind = data["current"]["wind_kph"]

            self.output.setText(
                f"{location}, {country}\n"
                f"Temp: {temp}°C\n"
                f"Condition: {condition}\n"
                f"Humidity: {humidity}%\n"
                f"Wind: {wind} km/h"
            )

        except Exception as e:
            self.output.setText(f"Error: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec())