# python_candlestick_chart.py
from datetime import datetime
import matplotlib.pyplot as plt
import mplfinance as fplt
import pandas as pd
import matplotlib.dates as mpl_dates

# Extracting Data for plotting
data = pd.read_csv('5min_sample.csv')
data['DateTime'] = pd.to_datetime(data['Date'] + " " + data['Time'], format="%m/%d/%Y %H:%M")
print(data['DateTime'])

fplt.plot(data,
          type='candle',
          title='5 min sample',
          ylabel='Price ($)')

sleep(20)
