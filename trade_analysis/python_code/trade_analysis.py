import json
import pandas as pd
import numpy as np
from pprint import pprint
import datetime
RawData = open("input_csv/ed_trade_data.json")
TradeData_daily = json.load(RawData)
l = list(TradeData_daily.keys())
l2 = []
for i in l:
    x_i = data[i]
    df_i =  pd.DataFrame(x_i)
    df_i['datetime'] = pd.to_datetime(df_i['date'])
    df_i['price'] = df_i['price'].astype(float)
    df_i['amount'] = df_i['amount'].astype(float)
    df_i['amountBase'] = df_i['amountBase'].astype(float)
    df = df_i[['datetime', 'amount', 'amountBase', 'price']].set_index('datetime')
    pair = i
    row, col = df_i.shape
    maxdate = df.index.max()
    mindate = df.index.min()
    total_days = (maxdate - mindate).days
    total_seconds = (np.datetime64(maxdate) - np.datetime64(mindate)).item().total_seconds()
    total_hours = (total_seconds / 3600)
    no_of_trades = (grouped['amount'].count())
    a = grouped['amount'].sum()
    b = grouped['amountBase'].sum()
    c = (b / a)
    if (total_days != 0):
        daily_trades_average = sum(no_of_trades) / (total_days)
    else:
        daily_trades_average = 0
    avg_hourly_trades = (sum(no_of_trades) / total_hours)
    result = [pair, row, sum(no_of_trades), str(datetime.timedelta(seconds=total_seconds)), avg_hourly_trades, mindate, maxdate, sum(a), sum(b), (sum(c)/len(c)), total_days]
    l2.append(result)
output = pd.DataFrame(l2)
output.columns = ['pair', 'no_of_rows', 'no_of_trades', 'total_time', 'avg_hourly_trades', 'min_date', 'max_date', 'volume_traded', 'total_turnover', 'avg_price_of_unit_volume', 'total_days']
resultant = output.set_index('pair')
s = resultant.sort_values(by = ['no_of_rows'], ascending = False)
s1 = s.query('no_of_trades >= 500')
s2 = s1.query('total_days <= 4')
top_daily_traded_pairs = s2.sort_values(by = ['avg_hourly_trades'], ascending = False)
top_daily_traded_pairs.to_csv('output_files/initial_study/top_hourly_traded_pairs.csv')
top_daily_traded_pairs.to_html('output_files/initial_study/top_hourly_traded_pairs.html')
