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



def ProcessPairlist(database, pair):
    ''' This function is taking a dictionary and one of the top traded pair name as arguments and then calling
    another function DataManipulation to make the readymade dataframe and then calling another function 
    DetectOutliers that takes the resultant dataframe as the argument of the previous function to detect 
    the outliers in that dataframe. '''
    
    TradeDataframe = pd.DataFrame(TradeData)
    manipulated_data = DataManipulation(TradeDataframe)
    outliers = DetectOutlier(manipulated_data, 'price')
    outliers.to_csv('output_files/outlier_study/OutlierReport_'+ pair +'.csv')
    return outliers



def PrepareSummary(data1, outlier_dataframe):
    ''' This function is determining the percentage of the outliers. For that it's first determining the shape
    of the actual dataframe and the dataframe of outliers which areS passed as arguments in this. 
    Then it's determining amount of data of those two dataframes. Then it's calculating the relative percentage 
    of the outliers in the dataframe for each pair of coins and reurning a dataframe containing the summary. '''
   
    trade_dataframe = pd.DataFrame(data1)
    row1, col1 = trade_dataframe.shape
    row2, col2 = outlier_dataframe.shape
    relative_percentage = (float(row2)/float(row1)) * 100
    summary = [row1, row2, relative_percentage]
    return summary



def ReportMaking(summary_list):
    ''' This function is taking the list of summary of outliers as argument and producting a well formated 
    Dataframe containing summary of Outliers.'''
    
    report = pd.DataFrame(summary_list).sort_values(by = 2)
    report.columns = ['pair', 'total_data', 'outliers_in_data', '%_of_outliers']
    final_report = report.set_index('pair')
    return final_report


top_hourly_traded_pairs = pd.read_csv('output_files/initial_study/top_hourly_traded_pairs.csv')
PairList = list(top_hourly_traded_pairs['pair'])

info_outliers = []

for pair in PairList:
    TradeData = TradeDb[pair]
    OutlierDataframe = ProcessPairlist(TradeData, pair)
    SummaryOutliers = [pair] + PrepareSummary(TradeData, OutlierDataframe)
    info_outliers.append(SummaryOutliers)

SummaryReport = ReportMaking(info_outliers)
SummaryReport.to_csv('output_files/outlier_study/Outlier_Summary_report.csv')
