import numpy as np
import pickle
from sklearn.linear_model import LinearRegression
from data_preprocessing import load_weather_data

data = load_weather_data()

# Convert date to numerical index
data['day'] = np.arange(len(data))

X = data[['day']]
y = data['temperature']

model = LinearRegression()
model.fit(X, y)

pickle.dump(model, open("temperature_model.pkl", "wb"))

print("Temperature prediction model trained successfully")
