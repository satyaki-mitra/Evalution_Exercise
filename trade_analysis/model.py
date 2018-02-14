class Pair(object):
    
    class Pair(object):
    	def __init__(self):
        	self.pairs = None
    	def get_list(self, data):
    	    '''This function returns the list of pairs which are the keys of the dictionary supplied in json file'''
        	self.pairs = data.keys()
       		return self.pairs


class Trade(object):
    
    def __init__(self):
        '''This function initialize the variables of the data as "None" type'''
		self.date = None
		self.price = None
		self.amount = None
		self.amountBase = None
		self.buyer = None
		self.seller = None
		self.side = None
		self.tokenAddr = None
		self.txHash = None
		
	def __init__(self, trade):
	    ''' This function initiates the class trades, updates the trade informations one by one'''
	    self.__dict__.update(trade)
	            
	           
	 def __repr__(self):
        '''This function returns representation of the Trade class'''
        return "Trade(%s, %s, %s, %s, %s, %s, %s, %s, %s)" %(self.amount, self.amountBase, self.buyer, self.date, self.price, self.seller, self.side, self.tokenAddr, self.txHash)            
	
	    
	    
		
	
	    
	    
	    
    
