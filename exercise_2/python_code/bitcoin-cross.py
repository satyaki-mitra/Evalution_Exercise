import pandas as pd

data = pd.read_csv('input_csv/bitcoin-cross-new.csv', sep = ',')
df = data.set_index('#')

df1 = df.sort_values(by = ['Volume (24h)'], ascending = False)
large_exchanges = df1[['Source', 'Volume (24h)']].head(10)
large_exchanges.to_csv('output_csv/ten_largest_exchanges.csv')

df3 = df.sort_values(by = ['Price'], ascending = True)
cheapest_pairs = df3[['Pair', 'Price']].head(10)
cheapest_pairs.to_csv('output_csv/ten_cheapest_pairs.csv')
