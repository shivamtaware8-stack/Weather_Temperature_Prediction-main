import pandas as pd

def load_weather_data():
    data = pd.read_csv("dataset/weather.csv")
    data['date'] = pd.to_datetime(data['date'])
    data = data.sort_values('date')
    return data
