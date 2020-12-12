import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import mplfinance as fplt
import pandas as pd
from datetime import datetime as dt
import matplotlib.dates as mpdates

plt.ion()
dts = [ ]
cdf = pd.read_csv('chart1.csv')
#cdf = pd.read_csv('market_1H_grey.csv')
for row in cdf.itertuples():
    rdt = row.Date + ' ' + row.Time
    dtm = dt.strptime(rdt, "%m/%d/%Y %H:%M")
    dts.append(dtm)

cols = ['Open','High','Low','Close']
df = cdf[cols]

dti = pd.DatetimeIndex(dts)
df.set_index(dti, inplace=True) 

print(df)

for bar in range(5, len(df)):
    wdf = df[bar-5:bar]
    highest_low = max(wdf['Low'])
    lowest_high = min(wdf['High'])
    if (highest_low > lowest_high):
        continue

    fplt.plot(wdf, type='candle', style='charles',
              title='Ovelapping Labelling',
              ylabel='Price ($)')

    plt.show(block=False)
    plt.pause(0.001)
    input("Overlapping?");
    plt.close('all')
