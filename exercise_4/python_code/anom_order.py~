import pandas as pd
data = pd.read_csv('input_file/anom_order.out', sep = '_', header = None, names = ['ed', '-', 'ETH', 'Source', 'anom', 'DateTime'])
data['DateTime'] = data['DateTime'].str.replace('.csv', '')
data = data[['Source','DateTime']]
data['DateTime'] = pd.to_datetime(data['DateTime'], unit='ns')
data['Date'] = [i.date() for i in data['DateTime']]
data['Time'] = [j.time() for j in data['DateTime']]
df = data[['Source', 'Date', 'Time']]



## Calculating Frequency of the Sources ##

df1 = pd.DataFrame(df.Source.value_counts())
# df1 is a dataframe which contains the 'Source' and the total count of each Sources.
df1 = df1.rename(columns = {'Source' : 'Count_of_the_source'})
df1.index.name = 'Source'
df1.to_csv('output_files/frequency_of_sources.csv')



## Calculating Datewise Frequency of received files ##

df2 = pd.DataFrame(df.Date.value_counts())
# df1 is a dataframe which contains the 'Source' and the total count of each Sources.
df2 = df2.rename(columns = {'Date' : 'Files_received_on_particular_date'})
df2.index.name = 'Date'
df2.to_csv('output_files/no_of_files_on_particular_date.csv')

