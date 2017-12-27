"""
NAME : Quandl exercise.
====================================
Description : To calculate rolling AVERAGE & STANDARD DEVIATION of the various columns
(e.g : close,wap,volume,etc) for all the stocks which is given.
================================================================================================
Input : A csv file of stock list,containing  quandl code with company name 
=======================================================================================
Output : A csv file containing stock code, company name & calculating values
========================================================================================
"""

import pandas as pd
import numpy as np
import quandl

#please fill up the rest of the code.

def answer_one():
    API_Key = 'yAaYLTzP5XcW5jQvueqJ'
    stock_list = pd.read_csv('stock_list.csv')
    l = []
    for i,j in zip(stock_list['Quandl_Code'], stock_list['Company_Name']):    
        data = quandl.get(i, authtoken = API_Key, start_date = '2017-11-10')
        data[['Rolling_avg_Close', 'Rolling_avg_WAP', 'Rolling_avg_Vol']] = data[['Close', 'WAP', 'No. of Shares']].rolling(window = 22).mean() 
        data[['Rolling_std_Close', 'Rolling_std_WAP', 'Rolling_std_Vol']] = data[['Close', 'WAP', 'No. of Shares']].rolling(window = 22).std()
        s = i, j, (data['Rolling_avg_Close'][-1]), (data['Rolling_avg_WAP'][-1]), (data['Rolling_avg_Vol'][-1]), (data['Rolling_std_Close'][-1]), (data['Rolling_std_WAP'][-1]), (data['Rolling_std_Vol'][-1])
        l.append(s)
    labels = ['Quandl_Code', 'Company_Name', 'Rolling_avg_Close', 'Rolling_avg_WAP', 'Rolling_avg_Vol', 'Rolling_std_Close', 'Rolling_std_WAP', 'Rolling_std_Vol']
    df = pd.DataFrame.from_records(l, columns = labels)
    df.to_csv('answer_to_test1.csv')
    print df
answer_one()
