import pandas as pd
import json
import datetime
data1 = pd.read_csv('output_files/initial_study/top__daily_traded_pairs.csv')
pairs = list(data1['pair'])
pair_iter = iter(pairs)
l = []
for i in pairs:
    fp = open("input_csv/ed_trade_data.json")
    data2 = json.load(fp)
    trade_data1 = data2[i]
    trade_data = pd.DataFrame(trade_data1)
    trade_data['datetime'] = pd.to_datetime(trade_data['date'])
    trade_data['price'] = trade_data['price'].astype(float)
    trade_data['amount'] = trade_data['amount'].astype(float)
    trade_data['amountBase'] = trade_data['amountBase'].astype(float)
    df = trade_data[['datetime', 'amount', 'amountBase', 'price']].set_index('datetime')
    q1 = df['price'].quantile(0.25)
    q3 = df['price'].quantile(0.75)
    iqr = q3 - q1
    lb = (q1 - (1.5 * iqr))
    ub = (q3 + (1.5 * iqr))
    df1 = df[(df['price'] < lb) | (df['price'] > ub)]
    df1.to_csv('output_files/outlier_study/outliers_'+i+'.csv')
    row1, col1 = df.shape
    total_data = row1
    row2, col2 = df1.shape
    outliers_in_data = row2
    percentage_of_outliers = (float(row2)/float(row1))*100
    df2 = [i, total_data, outliers_in_data, percentage_of_outliers]
    l.append(df2)
report = pd.DataFrame(l)
report.columns = ['pair', 'total_data', 'outliers_in_data', 'percentage_of_outliers']
outlier_report = report.sort_values(by = ['percentage_of_outliers'], ascending = False).set_index('pair')
outlier_report
