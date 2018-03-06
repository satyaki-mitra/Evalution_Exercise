import pandas as pd


class Pair(object):
    def __init__(self, name):
        self._name = name
    def __repr__(self):
        return "%s" % self._name

    
class Trade(object):
    
    def __init__(self, name, _dict):
        ''' This function takes the trade informations from the dictionary '''
        self.pair = Pair(name)
        try:
            self._date = pd.to_datetime(_dict['date'])
        except:
            self._date = None
        try:   
            self._price = float(_dict['price']) 
        except:
            self._price = None
        try:
            self._amount = float(_dict['amount'])
        except:
            self._amount = None
        try:
            self._amountBase = float(_dict['amountBase'])
        except:
            self._amountBase = None
        try:
            self._buyer = str(_dict['buyer'])
        except:
            self._buyer = None
        try:
            self._seller = str(_dict['seller'])
        except:
            self._seller = None
        try:
            self._side = str(_dict['side'])
        except:
            self._side = None
        try:
            self._tokenAddr = str(_dict['tokenAddr'])
        except:
            self._tokenAddr = None
        try:
            self._txHash = str(_dict['txHash'])
        except :
            self._txHash = None
                 
    def __repr__(self):
        '''This function returns the representation of the Trade class'''
        return "(%s | %s | %s | %s | %s | %s | %s | %s | %s | %s)" %(self.pair, self._date, self._amount, self._amountBase, self._price, self._buyer, self._seller, self._side, self._tokenAddr, self._txHash) 

