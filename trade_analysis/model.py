import json
import pandas as pd
import numpy as np
import datetime


class Pair(object):
	
	def __init__(self, pair_name):
	
	    self.pair_name = pair_name
	    
	def GetPairs(self, data):
	    
	    trade_data = json.load(open(data))
	    pairlist = list(trade_data.keys())
	    return pairlist


class Trade(Pair):

    def __init__(self, date, price, amount, amountBase, buyer, seller, side, tokenAddr, txHash):
		
		self.date = date
		self.datetime = datetime
		self.price = price
		self.amount = amount
		self.amountBase = amountBase
		self.buyer = buyer
		self.seller = seller
		self.side = side
		self.tokenAddr = tokenAddr
		self.txHash = txHash
	    
	    
	    
    def GetTradeData(self, rawdata):
	    
	    PairList = Pair.GetPairs(rawdata)
		for pair in PairList:
   		    data = TradeData[pair]
    		dataframe =  pd.DataFrame(data)
    		dataframe['datetime'] = pd.to_datetime(dataframe['date'])
    		dataframe['price'] = dataframe['price'].astype(float)
    		dataframe['amount'] = dataframe['amount'].astype(float)
    		dataframe['amountBase'] = dataframe['amountBase'].astype(float)
    	    final_dataframe = dataframe.set_index('datetime')
	    return final_dataframe
	    
	    	      
	def GetOutliers(self, TradeData, col_name):
	    
    	q1 = TradeData[col_name].quantile(0.25)
        q3 = TradeData[col_name].quantile(0.75)
        iqr = (q3 - q1) #Interquartile range
        lower_bound = q1 - (1.5 * iqr)
        upper_bound = q3 + (1.5 * iqr)
        outlier_df = TradeData[(TradeData[col_name] < lower_bound) | (TradeData[col_name] > upper_bound)]
        return outlier_df
	
	
	def GetStudyData(TradeData, col1, col2, col3):
    
    	q1 = TradeData[col1].quantile(0.25)
    	q3 = TradeData[col1].quantile(0.75)
    	if (TradeData[col1] < q1):
        	TradeData[col1] = q1
        	TradeData[col3] = TradeData[col2] * q1
    	elif (TradeData.price > q3):
        	TradeData[col1] = q3
        	TradeData[col3] = TradeData[col2] * q3
    	return TradeData
