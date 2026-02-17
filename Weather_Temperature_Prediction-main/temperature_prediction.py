import numpy as np
import pickle
from data_preprocessing import load_weather_data

model = pickle.load(open("temperature_model.pkl", "rb"))

data = load_weather_data()
last_day = len(data)

future_days = int(input("Enter number of future days to predict: "))

future = np.arange(last_day, last_day + future_days).reshape(-1, 1)
predictions = model.predict(future)

print("\nPredicted Future Temperatures:")
for i, temp in enumerate(predictions, start=1):
    print(f"Day {i}: {round(temp, 2)} °C")
