import pandas as pd

# reading the given csv file in pandas DataFrame format

data = pd.read_csv('input_csv/ping-api-etherdelta-com.csv', sep = ' ' )
data = pd.DataFrame(data)

# making the given data to the desired format

data['time(ms)'] = data['of'].str.split('=').str[1]
data['icmp_seq'] = data['56(84)'].str.split('=').str[1]
df1 = data[['time(ms)','icmp_seq']]
df = df1.set_index('icmp_seq')

# calculating the rolling mean & std for time periods 5, 10 & 20

df['5_pt_moving_avg'] = df['time(ms)'].rolling(window = 5).mean()
df['5_pt_moving_std'] = df['time(ms)'].rolling(window = 5).std()
df['10_pt_moving_avg'] = df['time(ms)'].rolling(window = 10).mean()
df['10_pt_moving_std'] = df['time(ms)'].rolling(window = 10).std()
df['20_pt_moving_avg'] = df['time(ms)'].rolling(window = 20).mean()
df['20_pt_moving_std'] = df['time(ms)'].rolling(window = 20).std()

# converting the desired output to a csv file
df.to_csv('output_csv/exercise_3.csv')

print df
