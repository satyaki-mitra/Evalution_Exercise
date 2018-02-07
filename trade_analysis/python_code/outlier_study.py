import pandas as pd
import json
import datetime

fp = open("input_csv/ed_trade_data.json")
TradeDb = json.load(fp)



def DataManipulation(df_in):
    ''' This function is for converting object type columns to numeric type columns of the dataframe which is 
    passed as the argument here and returning the required dataframe with all numeric columns. ''' 
    
    df_in['datetime'] = pd.to_datetime(df_in['date'])
    df_in['price'] = df_in['price'].astype(float)
    df_in['amount'] = df_in['amount'].astype(float)
    df_in['amountBase'] = df_in['amountBase'].astype(float)
    required_dataframe = df_in[['datetime', 'amount', 'amountBase', 'price']].set_index('datetime')
    return required_dataframe



def DetectOutlier(input_df, col_name):
    ''' This function is taking a dataframe & one of its column as arguments and then calculating the 
    1st and 3rd quartiles. iqr is the variable where it's calculating the Inter Quartile Range and hence 
    it's calculating the upper and lower bound and checking  whether all the values of that particular
    column belongs withing that boundary. df_out is returning the values which are out of the range. '''
    
    q1 = input_df[col_name].quantile(0.25)
    q3 = input_df[col_name].quantile(0.75)
    iqr = (q3 - q1) #Interquartile range
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    df_out = input_df[(input_df[col_name] < lower_bound) | (input_df[col_name] > upper_bound)]
    return df_out



def ProcessPairlist(data, pair_name):
    ''' This function is taking a dictionary and one of the top traded pair name as arguments and then calling
    another function DataManipulation to make the readymade dataframe and then calling another function 
    DetectOutliers that takes the resultant dataframe as the argument of the previous function to detect 
    the outliers in that dataframe. '''
    
    TradeDataframe = pd.DataFrame(data)
    manipulated_data = DataManipulation(TradeDataframe)
    outliers = DetectOutlier(manipulated_data, 'price')
    outliers.to_csv('output_files/outlier_study/OutlierReport_'+ pair_name +'.csv')
    summary = [pair_name] + PrepareSummary(TradeDataframe, outliers)
    return summary



def PrepareSummary(df1, df2):
    ''' This function is determining the percentage of the outliers. For that it's first determining the shape
    of df1 and the df2 which are passed as arguments in this. Then it's determining amount of data of those two
    dataframes. Then it's calculating the relative percentage of the outliers in the dataframe for each pair of 
    coins and reurning a list of the summary. '''
   
    row1, col1 = df1.shape
    row2, col2 = df2.shape
    relative_percentage = (float(row2)/float(row1)) * 100
    summary = [row1, row2, relative_percentage]
    return summary



def ReportMaking(summary_list, old_report):
    ''' This function is taking the list of summary of outliers as argument and producting a well formated 
    Dataframe containing summary of Outliers.'''
    
    report = pd.DataFrame(summary_list).sort_values(by = 2)
    report.columns = ['pair', 'total_data', 'outliers_in_data', '%_of_outliers']
    initial_report = old_report[['pair', 'min_date', 'max_date', 'total_time', 'no_of_trades', 'avg_hourly_trades', 'volume_traded', 'total_turnover', 'avg_price_of_unit_volume']]
    summary_report = pd.merge(initial_report, report, how = 'left', left_on = 'pair', right_on = 'pair')
    final_report = summary_report.set_index('pair').sort_values(by = '%_of_outliers')
    return final_report



top_hourly_traded_pairs = pd.read_csv('output_files/initial_study/top_hourly_traded_pairs.csv')
PairList = list(top_hourly_traded_pairs['pair'])
info_outliers = []
for pair in PairList:
    TradeData = TradeDb[pair]
    SummaryOutliers = ProcessPairlist(TradeData, pair)
    info_outliers.append(SummaryOutliers)

SummaryReport = ReportMaking(info_outliers, top_hourly_traded_pairs)
SummaryReport.to_csv('output_files/outlier_study/Outlier_Summary_Report.csv')
