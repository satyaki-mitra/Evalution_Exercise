import pandas as pd
class Pair(object):
    def get_name(self, name):
        self._name = name
        return self._name

class Trade(Pair):
    
    def __init__(self, _dict):
        ''' This function takes the trade informations from the dictionary '''
        self._date = pd.to_datetime(_dict['date'])
        self._price = float(_dict['price'])
        self._amount = float(_dict['amount'])
        self._amountBase = float(_dict['amountBase'])
        self._buyer = str(_dict['buyer'])
        self._seller = str(_dict['seller'])
        self._side = str(_dict['side'])
        self._tokenAddr = str(_dict['tokenAddr'])
        self._txHash = str(_dict['txHash'])
        
    def __repr__(self):
        '''This function returns the representation of the Trade class'''
        return "Trade( %s | %f | %f | %f | %s | %s | %s | %s | %s )" %(self._date, self._amount, self._amountBase, self._price, self._buyer, self._seller, self._side, self._tokenAddr, self._txHash)         
    

