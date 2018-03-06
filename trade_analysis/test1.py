import pandas as pd
import json
import datetime
from model import Pair, Trade
fp = open("input_csv/ed_trade_data.json")
jsondata = json.load(fp)
pairlist = jsondata.keys()

y = {u'amount': u'510',
 u'amountBase': u'0.01377',
 u'buyer': u'0x13e2c5f84bce6ff7b9068313b21729dc8fd55d5a',
 u'seller': u'0x96e1e7ba823796772bbda5c2abe81c8556b5e937',
 u'tokenAddr': u'0x814964b1bceaf24e26296d031eadf134a2ca4105',
 u'txHash': u'0x122b9d6932b50d748d7848aae071cf41f7df8baa1400472dbcc4182bf3287478'}
 
b = Trade('ETH_NEWB', y)
print b
