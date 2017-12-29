import pandas as pd

data = pd.read_csv('input_csv/bitcoin-cross-new.csv', sep = ',')
df = data.set_index('#')

## Largest exchnages in the given data ##

df1 = df[['Source', 'Pair', 'Volume (24h)']]  
# df1 is a slice of the main dataframe(df) containing only 'Source', 'Pair' and 'Volume(24h)' columns.
df2 = df1.groupby(['Source']).sum()           
# df2 is another dataframe which is grouped by 'Source' and contains the total for a group object.
df3 = df2.sort_values(by = ['Volume (24h)'], ascending = False).head(25)
# df3 is another dataframe which contains sorted 25 values of 'Volume (24h)' in descending order.
df3.to_csv('output_csv/top25_exchanges.csv')



## Most traded pairs wrt Exchanges in the given data ##

df7 = pd.DataFrame(df.Pair.value_counts())
# df7 is a dataframe which contains the 'Pair' and the frequency of the pairs.
df8 = df7.rename(columns = {'Pair' : 'No_of_traded_pair'})
df8.index.name = 'Pair'
# df8 is another dataframe where we change the names of the index column to 'Pair' and 'Pair column to 'No_of_traded_pairs'.
df8.head(10).to_csv('output_csv/most_traded_pairs.csv')



## Cheapest pairs in the given data ##

df4 = df[['Pair', 'Price']]  
# df4 is a slice of the main dataframe(df) containing only 'Pair' and 'Price' columns.
df5 = df4.groupby(['Pair']).sum()           
# df5 is another dataframe which is grouped by 'Pair' and contains the total for a group object.
df6 = df5.sort_values(by = ['Price'], ascending = True).head(25)
# df6 is another dataframe which contains sorted 25 values of 'Price' in ascending order.
df6.to_csv('output_csv/cheapest_25_pairs.csv')



## Most traded pairs wrt Turnover in the given data ##

df9 = df[['Pair', 'Volume (24h)']]
# df9 is a Dataframe that contains only 'Pair' & 'Volume (24h)' columns.

df10 = df9.groupby('Pair').sum()
# df10 is another Dataframe that makes the groups according to the 'Pair' and then takes sum of the 'Volume (24h)' of the corresponding groups. 

df11 = df10.sort_values(by = ['Volume (24h)'], ascending = False).head(10)
# df11 is a Dataframe that sort the 'Volume (24h)' column in descending order.

df11.to_csv('output_csv/most_traded_pairs_wrt_turnover.csv')
df11
