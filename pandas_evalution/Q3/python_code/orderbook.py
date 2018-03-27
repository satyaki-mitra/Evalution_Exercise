import pandas as pd
import json
import glob

def Volume(df):
    row, col = df.shape
    if (row % 2 == 0):
        volumes = df['amount'][row/2:]
        tot_vol = volumes.sum()
        return tot_vol
    else:
        volumes = df['amount'][((row/2)+1):]
        tot_vol = volumes.sum()
        return tot_vol
        
file1 = "../../../../data3/t00/ed__ETH_KIN_depth_20180314000001.json"
fp1 = open(file1)
order1 = json.load(fp1)
seller1 = pd.DataFrame(order1['sells'])
seller1.price = seller1.price.astype(float)
seller1.amount = seller1.amount.astype(float)
buyer1 = pd.DataFrame(order1['buys'])
buyer1.price = buyer1.price.astype(float)
buyer1.amount = buyer1.amount.astype(float)
buyer1.sort_values(by = ['price'], ascending = False)['amount']
seller1.sort_values(by = ['price'], ascending = False)['amount']
volume11 = Volume(buyer1)
volume12 = Volume(seller1)
bid1 = max(buyer1.price)
ask1 = min(seller1.price)
spread1 = (ask1 - bid1)
l1 = file1.split('_')
l2 = l1[5].split('.')
time1 = pd.to_datetime(l2[0])
measures1 = {'Ask' : ask1, 'Bid' : bid1, 'Spread' : spread1, 'Volume_sell' : volume12, 'Volume_buy' : volume11}

file2 = "../../../../data3/t00/ed__ETH_KIN_depth_20180314000023.json"
fp2 = open(file2)
order2 = json.load(fp2)
seller2 = pd.DataFrame(order2['sells'])
seller2.price = seller2.price.astype(float)
seller2.amount = seller2.amount.astype(float)
buyer2 = pd.DataFrame(order2['buys'])
buyer2.price = buyer2.price.astype(float)
buyer2.amount = buyer2.amount.astype(float)
buyer2.sort_values(by = ['price'], ascending = False)['amount']
seller2.sort_values(by = ['price'], ascending = False)['amount']
volume21 = Volume(buyer2)
volume22 = Volume(seller2)
bid2= max(buyer2.price)
ask2= min(seller2.price)
spread2 = (ask2 - bid2)
l3 = file2.split('_')
l4 = l3[5].split('.')
time2 = pd.to_datetime(l4[0])
measures2 = {'Ask' : ask2, 'Bid' : bid2, 'Spread' : spread2, 'Volume_sell' : volume22, 'Volume_buy' : volume21}

def comparison(measures1, measures2):
    list1 = []
    list1.append(measures1)
    if measures1 != measures2:
        ask = ask2
        bid = bid2
        spread = spread2
        time = time2
        volume_sell = volume22
        volume_buy = volume21
        entry = {'Ask' : ask, 'Bid' : bid, 'Spread' : spread, 'Timestamp' : time, 'Volume_sell' : volume_sell, 'Volume_buy' : volume_buy}
        list1.append(entry)
    else:    
		ask = ask1
		bid = bid1
		spread = spread1
		time = time1
		volume_sell = volume12
		volume_buy = volume11
    
    pd.DataFrame(list1)


