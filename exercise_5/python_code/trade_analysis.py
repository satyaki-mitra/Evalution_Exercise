import json
import pandas as pd
from pprint import pprint
data = open("input_csv/ed_trade_data.json")
data = json.load(data)
l = list(data.keys())
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
    shape = df_i.shape
    maxdate = df.index.max()
    mindate = df.index.min()
    total_days = (maxdate - mindate).days
    grouped = df.groupby(lambda x : x.month)
    grouped.index = 'month'
    a = grouped.count()
    grouped = df.groupby(lambda x: x.month)
    grouped.index = 'month'
    no_of_trades = (grouped['amount'].count())
    a = grouped['amount'].sum()
    b = grouped['amountBase'].sum()
    c = (b / a)
    if (total_days != 0):
        daily_trades_average = sum(no_of_trades) / (total_days)
    else:
        daily_trades_average = 0
    result = [pair, shape, mindate, maxdate, total_days, sum(no_of_trades), sum(a), sum(b), (sum(c)/len(c)), daily_trades_average]
    l2.append(result)
output = pd.DataFrame(l2)
output.columns = ['pair', 'shape', 'min_date', 'max_date', 'total_days', 'no_of_trades', 'volume_traded', 'total_turnover', 'avg_price_of_unit_volume', 'avg_daily_trades']
resultant = output.set_index('pair')
resultant.to_csv('output_csv/initial_analysis.csv')
resultant.to_html('output_csv/initial_analysis.html')

