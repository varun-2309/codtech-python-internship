import requests
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime

# Your OpenWeatherMap API Key
API_KEY = 'b56665f42acf9b88023aef419f006db5'
CITY = 'Delhi'
URL = f'https://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetch weather forecast data
response = requests.get(URL)
data = response.json()

# Check if data fetch was successful
if data.get("cod") != "200":
    print("Failed to fetch data:", data.get("message", "Unknown error"))
    exit()

# Extract datetime, temperature, and humidity
dates = []
temps = []
humidity = []

for item in data['list']:
    dt = datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S')
    dates.append(dt)
    temps.append(item['main']['temp'])
    humidity.append(item['main']['humidity'])

# Create visualizations
plt.figure(figsize=(14, 6))

# Temperature Plot
plt.subplot(1, 2, 1)
sns.lineplot(x=dates, y=temps, marker='o', color='blue')
plt.title(f'Temperature Forecast for {CITY}')
plt.xlabel('Date & Time')
plt.ylabel('Temperature (°C)')
plt.xticks(rotation=45)

# Humidity Plot
plt.subplot(1, 2, 2)
sns.lineplot(x=dates, y=humidity, marker='o', color='green')
plt.title(f'Humidity Forecast for {CITY}')
plt.xlabel('Date & Time')
plt.ylabel('Humidity (%)')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()

