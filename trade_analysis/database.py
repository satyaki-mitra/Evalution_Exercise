from sqlalchemy import Column, ForeignKey, Integer, String, Float, DateTime, Index, create_engine 
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class Trade(Base):
     __tablename__ = 'trade'
     date = Column(String(100), unique = True, index = True, nullable = False)
	 price = Column(String(100), unique = True, index = True, nullable = False)
	 amount = Column(String(100), unique = True, index = True, nullable = False)
	 amountBase = Column(String(100), unique = True, index = True, nullable = False)
	 buyer = Column(String(100), unique = True, index = True, nullable = False)
	 seller = Column(String(100), unique = True, index = True, nullable = False)
	 side = Column(String(100), unique = True, index = True, nullable = False)
	 tokenAddr = Column(String(100), unique = True, index = True, nullable = False)
	 txHash = Column(String(100), unique = True, index = True, nullable = False)
	 
	 
	 def __init__(self, date, price, amount, amountBase, buyer, seller, side, tokenAddr, txHash):
	     self.date = date
		 self.price = price
		 self.amount = amount
		 self.amountBase = amountBase
		 self.buyer = buyer
		 self.seller = seller
		 self.side = side
		 self.tokenAddr = tokenAddr
		 self.txHash = txHash
		 
	def __repr__(self):
	    return "<Trade(date = %s, price = %s, amount = %s, amountBase = %s, buyer = %s, seller = %s, side = %s, tokenAddr = %s, txHash = %s)>" %(self.amount, self.amountBase, self.buyer, self.date, self.price, self.seller, self.side, self.tokenAddr, self.txHash)            
	
	 
	 
	
class Outliers(Base):
    __tablename__ = 'outliers'
    date = Column(DateTime(100), unique = True, index = True, nullable = False)
    price = Column(Float(100), unique = True, index = True, nullable = False)
    amount = Column(Float(100), unique = True, index = True, nullable = False)
    amountBase = Column(Float(100), unique = True, index = True, nullable = False)
    buyer = Column(String(100), unique = True, index = True, nullable = False)
    seller = Column(String(100), unique = True, index = True, nullable = False)
    side = Column(String(100), unique = True, index = True, nullable = False)
    tokenAddr = Column(String(100), unique = True, index = True, nullable = False)
    txHash = Column(String(100), unique = True, index = True, nullable = False)
    
    
    def __init__(self, date, price, amount, amountBase, buyer, seller, side, tokenAddr, txHash):
	     self.date = date
		 self.price = price
		 self.amount = amount
		 self.amountBase = amountBase
		 self.buyer = buyer
		 self.seller = seller
		 self.side = side
		 self.tokenAddr = tokenAddr
		 self.txHash = txHash
		 
	def __repr__(self):
	    return "<Trade(date = %s, price = %f, amount = %f, amountBase = %f, buyer = %s, seller = %s, side = %s, tokenAddr = %s, txHash = %s)>" %(self.amount, self.amountBase, self.buyer, self.date, self.price, self.seller, self.side, self.tokenAddr, self.txHash)            
	
	 
    
    
class StudyData(Base):
    __tablename__ = 'studydata'
    date = Column(DateTime(100), unique = True, index = True, nullable = False)
    price = Column(Float(100), unique = True, index = True, nullable = False)
    amount = Column(Float(100), unique = True, index = True, nullable = False)
    amountBase = Column(Float(100), unique = True, index = True, nullable = False)
    buyer = Column(String(100), unique = True, index = True, nullable = False)
    seller = Column(String(100), unique = True, index = True, nullable = False)
    tokenAddr = Column(String(100), unique = True, index = True, nullable = False)
    txHash = Column(String(100), unique = True, index = True, nullable = False)
    
    
    
     def __init__(self, date, price, amount, amountBase, buyer, seller, side, tokenAddr, txHash):
	     self.date = date
		 self.price = price
		 self.amount = amount
		 self.amountBase = amountBase
		 self.buyer = buyer
		 self.seller = seller
		 self.side = side
		 self.tokenAddr = tokenAddr
		 self.txHash = txHash
		 
	def __repr__(self):
	    return "<Trade(date = %s, price = %f, amount = %f, amountBase = %f, buyer = %s, seller = %s, side = %s, tokenAddr = %s, txHash = %s)>" %(self.amount, self.amountBase, self.buyer, self.date, self.price, self.seller, self.side, self.tokenAddr, self.txHash)            
	
	 
