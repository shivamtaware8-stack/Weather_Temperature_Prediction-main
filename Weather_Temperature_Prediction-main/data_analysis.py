import matplotlib.pyplot as plt
from data_preprocessing import load_weather_data

data = load_weather_data()

plt.plot(data['date'], data['temperature'])
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.title("Historical Temperature Trend")
plt.show()
