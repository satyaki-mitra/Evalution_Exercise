import pandas as pd
import json
import datetime



def data_manipulation(df_in):
    trade_data1 = data2[df_in]
    trade_data = pd.DataFrame(trade_data1)
    trade_data['datetime'] = pd.to_datetime(trade_data['date'])
    trade_data['price'] = trade_data['price'].astype(float)
    trade_data['amount'] = trade_data['amount'].astype(float)
    trade_data['amountBase'] = trade_data['amountBase'].astype(float)
    dataframe = trade_data[['datetime', 'amount', 'amountBase', 'price']].set_index('datetime')
    return dataframe



def detect_outlier(input_df, col_name):
    q1 = input_df[col_name].quantile(0.25)
    q3 = input_df[col_name].quantile(0.75)
    iqr = q3 - q1 #Interquartile range
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    df_out = input_df[(input_df[col_name] < lower_bound) | (input_df[col_name] > upper_bound)]
    row1, col1 = df_out.shape
    total_data = row1
    return df_out



l = []
def proportion_outlier(input_data):
    row1, col1 = data.shape
    total_data = row1
    row2, col2 = outliers.shape
    outliers_in_data = row2
    percentage_of_outliers = (float(row2)/float(row1))*100
    output = [i, total_data, outliers_in_data, percentage_of_outliers]
    l.append(output)
    return l



data1 = pd.read_csv('output_files/initial_study/top__daily_traded_pairs.csv')
pairs = list(data1['pair'])
pair_iter = iter(pairs)
for i in pairs:
    fp = open("input_csv/ed_trade_data.json")
    data2 = json.load(fp)
    data = data_manipulation(i)
    outliers = detect_outlier(data, 'price')
    outliers.to_csv('output_files/outlier_study/outliers_'+i+'.csv')
    output_data = proportion_outlier(outliers)



report = pd.DataFrame(output_data)
report.columns = ['pair', 'total_data', 'outliers_in_data', '%_of_outliers']
outlier_report = report.sort_values(by = ['%_of_outliers'], ascending = True).set_index('pair')
outlier_report.to_csv('output_files/outlier_study/outlier_report.csv')
