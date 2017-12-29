import pandas as pd

data = pd.read_csv('input_csv/bitcoin-cross-new.csv', sep = ',')
df = data.set_index('#')

## Largest  & Smallest Exchnages wrt turnover in the given data ##

df1 = df[['Source', 'Pair', 'Volume (24h)']]  
# df1 is a slice of the main dataframe(df) containing only 'Source', 'Pair' and 'Volume(24h)' columns.
df2 = df1.groupby(['Source']).sum()           
# df2 is another dataframe which is grouped by 'Source' and contains the total for a group object.
df3 = df2.sort_values(by = ['Volume (24h)'], ascending = False).head(20)
df4 = df2.sort_values(by = ['Volume (24h)'], ascending = True).head(20)
# df3 & df4 are is dataframes which contains Top 20 and bottom values of 'Volume (24h)'.
df3.to_csv('output_csv/top20_exchanges_wrt_turnover.csv')
df4.to_csv('output_csv/bottom20_exchanges_wrt_turnover.csv')



## Largest  & Smallest Exchnages wrt traded pairs in the given data ##

df15 = pd.DataFrame(df.Source.value_counts())
# df15 is a dataframe which contains the 'Pair' and the frequency of the pairs.
df16 = df15.rename(columns = {'Source' : 'No_of_traded_pair'})
df16.index.name = 'Source'
# df16 is another dataframe where we change the names of the index column to 'Pair' and 'Pair column to 'No_of_traded_pairs'.
df16.head(20).to_csv('output_csv/top20_exchanges_wrt_traded_pairs.csv')
df16.tail(20).to_csv('output_csv/bottom20_exchanges_wrt_traded_pairs.csv')



## Cheapest & Expensive pairs in the given data ##

df5 = df[['Pair', 'Price']]  
# df5 is a slice of the main dataframe(df) containing only 'Pair' and 'Price' columns.
df6 = df5.groupby(['Pair']).mean()           
# df6 is another dataframe which is grouped by 'Pair' and contains the total for a group object.
df7 = df6.sort_values(by = ['Price'], ascending = True).head(20)
df8 = df6.sort_values(by = ['Price'], ascending = False).head(20)
# df7 and df8 are dataframes which contains top 20  and bottom 20 values of 'Price'.
df7.to_csv('output_csv/cheapest_20_pairs.csv')
df8.to_csv('output_csv/expensive_20_pairs.csv')




## Most traded pairs  and Least traded pairs wrt Exchanges in the given data ##

df9 = pd.DataFrame(df.Pair.value_counts())
# df9 is a dataframe which contains the 'Pair' and the frequency of the pairs.
df10 = df9.rename(columns = {'Pair' : 'No_of_traded_pair'})
df10.index.name = 'Pair'
# df10 is another dataframe where we change the names of the index column to 'Pair' and 'Pair column to 'No_of_traded_pairs'.
df10.head(10).to_csv('output_csv/most_traded_pairs_wrt_exchanges.csv')
df10.tail(10).to_csv('output_csv/least_traded_pairs_wrt_exchanges.csv')



## Most traded and least traded pairs wrt turnover in the given data ##

df11 = df[['Pair', 'Volume (24h)']]
# df11 is a Dataframe that contains only 'Pair' & 'Volume (24h)' columns.
df12 = df11.groupby('Pair').sum()
# df12 is another Dataframe that makes the groups according to the 'Pair' and then takes sum of the 'Volume (24h)' of the corresponding groups. 
df13 = df12.sort_values(by = ['Volume (24h)'], ascending = False).head(10)
df14 = df12.sort_values(by = ['Volume (24h)'], ascending = True).head(10)
# df12 & df14 are Dataframes that contains the top10 and bottom10 of the sorted 'Volume (24h)' column.
df13.to_csv('output_csv/most_traded_pairs_wrt_turnover.csv')
df14.to_csv('output_csv/least_traded_pairs_wrt_turnover.csv')
