import pandas as pd

data = pd.read_csv('input_csv/bitcoin-cross-new.csv', sep = ',')
df = data.set_index('#')

df1 = df[['Source', 'Pair', 'Volume (24h)']]  
# df1 is a slice of the main dataframe(df) containing only 'Source', 'Pair' and 'Volume(24h)' columns.
df2 = df1.groupby(['Source']).sum()           
# df2 is another dataframe which is grouped by 'Source' and contains the total for a group object.
df3 = df2.sort_values(by = ['Volume (24h)'], ascending = False).head(25)
# df3 is another dataframe which contains sorted 25 values of 'Volume (24h)' in descending order.
df3.to_csv('output_csv/top25_exchanges.csv')



