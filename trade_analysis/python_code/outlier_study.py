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



def ProcessPairlist(database, next_pair):
    ''' This function is taking a database and one of the top traded pairs as arguments and then calling
    another function DataManipulation to make the readymade dataframe and then calling another function 
    DetectOutliers that takes the resultant dataframe as the argument of the previous function to detect 
    the outliers in that dataframe. '''
    
    TradeData = database[next_pair]
    TradeDataframe = pd.DataFrame(TradeData)
    manipulated_data = DataManipulation(TradeDataframe)
    outliers = DetectOutlier(manipulated_data, 'price')
    outliers.to_csv('output_files/outlier_study/OutlierReport_'+ next_pair +'.csv')
    return outliers



def PrepareSummary(pair_list, outlier_files_path, database):
    ''' This function is determining the percentage of the outliers. For that it's first determining the shape
    of the actual dataframe and the dataframe of outliers, the list of pairs is passed as arguments in this. 
    Then it's determining amount of data in those two dataframes. Then it's calculating the relative percentage 
    of the outliers in the dataframe for each pair of coins and reurning a dataframe containing the summary. '''
   
    info_of_outliers = []
    for p in pair_list:
        trade_data = database[p]
        trade_dataframe = pd.DataFrame(trade_data)
        row1, col1 = trade_dataframe.shape
        outlier_data = pd.read_csv(outlier_files_path + p +'.csv')
        outlier_dataframe = pd.DataFrame(outlier_data)
        row2, col2 = outlier_dataframe.shape
        relative_percentage = (float(row2)/float(row1)) * 100
        summary1 = [p, row1, row2, relative_percentage]
        info_of_outliers.append(summary1)
    report_of_outliers = pd.DataFrame(info_of_outliers).sort_values(by = 2)
    report_of_outliers.columns = ['pair', 'total_data', 'outliers_in_data', '%_of_outliers']
    summary_report = report_of_outliers.set_index('pair')
    return summary_report



top_hourly_traded_pairs = pd.read_csv('output_files/initial_study/top_hourly_traded_pairs.csv')
PairList = list(top_hourly_traded_pairs['pair'])
for pair in PairList:
    ProcessPairlist (TradeDb, pair)
path_to_outliers = 'output_files/outlier_study/OutlierReport_'  
SummaryReport = PrepareSummary(PairList, path_to_outliers, TradeDb)
SummaryReport.to_csv('output_files/outlier_study/OutlierSummaryReport.csv')
