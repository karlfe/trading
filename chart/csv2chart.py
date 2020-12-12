import pandas as pd
from datetime import datetime

#df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv')
df = pd.read_csv('chart1.csv')
#df['DateTime'] = df['Date'] + " " + df['Time']
print(df)
df['DateTime'] = datetime.strptime(df['Date'] + " " + df['Time'], "%m/%d/%Y %H:%M")

import plotly.graph_objects as go
fig = go.Figure(data=[go.Candlestick(x=df['DateTime'],
                open=df['Open'],
                high=df['High'],
                low=df['Low'],
                close=df['Close'])])

fig.show()
