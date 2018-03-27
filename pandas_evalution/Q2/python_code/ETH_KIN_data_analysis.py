import pandas as pd

raw_data = pd.read_csv("../../../../data2/ETH_KIN_trade_db.csv", parse_dates = ['date']).set_index('date')

def DetectOutlier(df_in):
    ''' This function is taking a dataframe as argument and then calculating the 1st and 3rd quartiles of the column "price" 
    and hence the Inter Quartile Range. Then using iqr it's calculating it's calculating the upper and lower bound and checking  
    whether all the values of that particular column belongs within that boundary. df_out is returning the values which are out 
    of the range. '''
    
    q1 = df_in['price'].quantile(0.25)
    q3 = df_in['price'].quantile(0.75)
    iqr = (q3 - q1) #Interquartile range
    lower_bound = q1 - (1.5 * iqr)
    upper_bound = q3 + (1.5 * iqr)
    df_out = df_in[(df_in['price'] < lower_bound) | (df_in['price'] > upper_bound)]
    return df_out
    
outlier = []
split_data = raw_data.resample('D')
for i in split_data['price']:
    df = pd.DataFrame({'price':i[1]})
    output = DetectOutlier(df)
    dict = {'price':'count'}
    a = output.resample('D').apply(dict)
    outlier.append(a)
    
dict1 = {'price':'first'}
dict2 = {'price':'last'}
dict3 = {'price':'max'}
dict4 = {'price':'min'}
dict5 = {'amount':'sum'}
dict6 = {'price':'mean'}
dict7 = {'price':'std'}
dict8 = {'price':'median'}
dict9 = {'amountBase':'sum'}
dict12 = {'price':'skew'}


df1 = raw_data.resample('D').apply(dict1)
df2 = raw_data.resample('D').apply(dict2)
df3 = raw_data.resample('D').apply(dict3)
df4 = raw_data.resample('D').apply(dict4)
df5 = raw_data.resample('D').apply(dict5)
df6 = raw_data.resample('D').apply(dict6)
df7 = raw_data.resample('D').apply(dict7)
df8 = raw_data.resample('D').apply(dict8)
df9 = raw_data.resample('D').apply(dict9)
df10 = pd.DataFrame(raw_data['price'].resample('D').apply(lambda price : price.quantile(0.25)))
df11 = pd.DataFrame(raw_data['price'].resample('D').apply(lambda price : price.quantile(0.75)))
df12 = raw_data.resample('D').apply(dict12)
df13 = pd.DataFrame(raw_data['price'].resample('D').apply(lambda price : price.kurtosis()))
df14 = pd.concat(outlier)

df1.columns = ['Open']
df2.columns = ['Close']
df3.columns = ['High']
df4.columns = ['Low']
df5.columns = ['Volume']
df6.columns = ['Mean']
df7.columns = ['Std']
df8.columns = ['Median']
df9.columns = ['Turnover']
df10.columns = ['Q1']
df11.columns = ['Q3']
df12.columns = ['Skewness']
df13.columns = ['Kurtosis']
df14.columns = ['No_of_Outliers']

daily_data = pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(pd.merge(df1, df2, how = 'right', left_index = True, right_index = True), df3, how = 'right', left_index = True, right_index = True), df4, how = 'right', left_index = True, right_index = True),df5, how = 'right', left_index = True, right_index = True), df6, how = 'right', left_index = True, right_index = True), df7, how = 'right', left_index = True, right_index = True), df8, how = 'right', left_index = True, right_index = True), df9, how = 'right', left_index = True, right_index = True), df10, how = 'right', left_index = True, right_index = True), df11, how = 'right', left_index = True, right_index = True), df12, how = 'right', left_index = True, right_index = True), df13, how = 'right', left_index = True, right_index = True), df14, how = 'right', left_index = True, right_index = True)

daily_data['Range'] = daily_data['High']-daily_data['Low']
daily_data['IQR'] = daily_data['Q3']-daily_data['Q1']

final_data = daily_data[['Open','High','Low','Close','Mean','Std','Range','Q1','Median','Q3','IQR','Skewness','Kurtosis','No_of_Outliers','Volume','Turnover']]

final_data.to_csv('../output/daily_freq_data.csv')


