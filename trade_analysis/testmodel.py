import pandas as pd
import json
import datetime
from model import Pair, Trade
fp = open("input_csv/ed_trade_data.json")
jsondata = json.load(fp)
pairlist = jsondata.keys()

total_data = []
for i in pairlist:
    pair = Pair(i)
    pair_data = jsondata[str(pair)]
    trades = []
    for j in pair_data:
        trade = Trade(j)
        trades.append(trade)
    info_trade = (pair, trades)
    total_data.append(info_trade)  
