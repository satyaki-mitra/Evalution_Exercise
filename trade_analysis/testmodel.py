import pandas as pd
import json
import datetime
import numpy as np
from model import Pair, Trade
fp = open("input_csv/ed_trade_data.json")
jsondata = json.load(fp)
pairlist = jsondata.keys()

total_info = []
for i in pairlist:
    pair_name = Pair().get_name(i)
    pair_data = jsondata[str(pair_name)]
    for j in pair_data:
        trade = Trade(j)
        trade_info = (pair_name, trade)
        total_info.append(trade_info)
print total_info
    
