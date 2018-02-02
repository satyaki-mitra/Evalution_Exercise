import pandas as pd
import json
import datetime



def data_manipulation(df_in):
    df_in['datetime'] = pd.to_datetime(df_in['date'])
    df_in['price'] = df_in['price'].astype(float)
    df_in['amount'] = df_in['amount'].astype(float)
    df_in['amountBase'] = df_in['amountBase'].astype(float)
    required_dataframe = df_in[['datetime', 'amount', 'amountBase', 'price']].set_index('datetime')
    return required_dataframe



def detect_outlier(input_df, col_name):
    q1 = input_df[col_name].quantile(0.25)
    q3 = input_df[col_name].quantile(0.75)
    iqr = (q3 - q1) #Interquartile range
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    df_out = input_df[(input_df[col_name] < lower_bound) | (input_df[col_name] > upper_bound)]
    return df_out



summary = []
def summary_of_outliers(input_data1, input_data2):
    row1, col1 = input_data1.shape
    total_data = row1
    row2, col2 = input_data2.shape
    outliers_in_data = row2
    percentage_of_outliers = (float(row2)/float(row1))*100
    output = [i, total_data, outliers_in_data, percentage_of_outliers]
    summary.append(output)
    return summary



top_hourly_traded_pairs = pd.read_csv('output_files/initial_study/top_hourly_traded_pairs.csv')
pair_list = list(top_hourly_traded_pairs['pair'])
for i in pair_list:
    fp = open("input_csv/ed_trade_data.json")
    trade_db = json.load(fp)
    current_trade_data = trade_db[i]
    current_dataframe = pd.DataFrame(current_trade_data)
    manipulated_data = data_manipulation(current_dataframe)
    outliers = detect_outlier(manipulated_data, 'price')
    outliers.to_csv('output_files/outlier_study/OutlierReport_'+i+'.csv')
    outlier_summary = summary_of_outliers(manipulated_data, outliers)

report = pd.DataFrame(outlier_summary)
report.columns = ['pair', 'total_data', 'outliers_in_data', '%_of_outliers']
outlier_summary_report = report.sort_values(by = ['%_of_outliers'], ascending = True).set_index('pair')
outlier_summary_report.to_csv('output_files/outlier_study/outlier_summary_report.csv')





