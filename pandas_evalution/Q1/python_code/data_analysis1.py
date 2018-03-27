import pandas as pd

raw_data = pd.read_csv("../../../../data1/AAPL-1Min.txt", parse_dates = [['Date', 'Time']])

work_data = pd.DataFrame(raw_data).set_index('Date_Time')
work_data.to_pickle('../output/AAPL-1Min.pickle')

ohlc_dict = {'Open':'mean', 'High':'mean', 'Low':'mean', 'Close': 'mean', 'Volume': 'mean'}
hourly_data = work_data.resample('H').apply(ohlc_dict)
daily_data = work_data.resample('D').apply(ohlc_dict)

hourly_report = hourly_data[['Open', 'High', 'Low', 'Close', 'Volume']]
hourly_report.to_pickle('../output/hourly_data.pickle')
hourly_report.describe().to_pickle('../output/hourly_summary.pickle')

daily_report = daily_data[['Open', 'High', 'Low', 'Close', 'Volume']]
daily_report.to_pickle('../output/daily_data.pickle')
daily_report.describe().to_pickle('../output/daily_summary.pickle')

twominutes_data = work_data.resample('2T').apply(ohlc_dict)
threeminutes_data = work_data.resample('3T').apply(ohlc_dict)
fiveminutes_data = work_data.resample('5T').apply(ohlc_dict)
tenminutes_data = work_data.resample('10T').apply(ohlc_dict)

twominutes_data[['Open', 'High', 'Low', 'Close', 'Volume']].to_pickle('../output/AAPL-2Min.pickle')
threeminutes_data[['Open', 'High', 'Low', 'Close', 'Volume']].to_pickle('../output/AAPL-3Min.pickle')
fiveminutes_data[['Open', 'High', 'Low', 'Close', 'Volume']].to_pickle('../output/AAPL-5Min.pickle')
tenminutes_data[['Open', 'High', 'Low', 'Close', 'Volume']].to_pickle('../output/AAPL-10Min.pickle')
