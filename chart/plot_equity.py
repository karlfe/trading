from numpy import isnan
from pandas import read_excel
from pandas import DataFrame as df
from datetime import datetime as dt
import plotly.express as px

report = 'equity_curve_1H_grey.xlsx'
trades = 'Trades List'
cols = [ 0, 1, 2, 7 ];

# read trading data into a DataFrame
tdf = read_excel(report, sheet_name=trades, header=2, usecols=cols);
tdf.drop(0, axis=0);
print(tdf)

last_cpl = 0
rows = [ ]
for row in tdf.itertuples():
    rowdict = { }
    if row.Index == 0:
        continue

    if row.Type == 'Buy':
        posid = row[1] # '#' column
        trade_pl = row[4] # 'Cumulative P/L' column
        if isnan(trade_pl):
            break
        rowdict['Position Id'] = int(posid) # '#' column
        rowdict['Date/Time'] = row[3] # 'Date/Time' column
        rowdict['Order Type'] = row.Type
        rowdict['Profit/Loss'] = 0
        rowdict['Cumulative P/L'] = last_cpl
        
    if row.Type == 'Sell':
        last_cpl = row[4] # 'Cumulative P/L' column
        if isnan(last_cpl):
            break
        rowdict['Position Id'] = int(posid)
        rowdict['Date/Time'] = row[3] # 'Date/Time' column
        rowdict['Order Type'] = row.Type
        rowdict['Profit/Loss'] = trade_pl
        rowdict['Cumulative P/L'] = last_cpl

    rows.append(rowdict);

# create an empyt equity curve DataFrame
ecols = ['Position Id', 'Date/Time', 'Order Type',
         'Profit/Loss', 'Cumulative P/L']
edf = df(rows)

fig = px.line(edf, x='Date/Time', y='Cumulative P/L', title="Equity Curve");
fig.show()
