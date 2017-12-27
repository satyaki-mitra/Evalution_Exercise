import pandas as pd

def DataAnalysis():

    data = pd.read_csv('input_csv/company-data.csv')
    
    df = data.rename(columns = {'Co_Code' : 'co_code', 'Co_Name' : 'co_name', 'Stock Exchange' : 'exchange_code', 'Industry' : 'industry_name', 'Sector' : 'sector_name', 'Year End' : 'year_end', 'Equity Paid Up' : 'equity_paid_up', 'Net Sales' : 'net_sales', 'PAT' : 'pat', 'PBIDT' : 'pbidt', 'Debt-Equity Ratio[Latest]' : 'debt_equity_ratio_latest', 'PBIDTM (%)[Latest]' : 'pbidtm_percentage_latest'})

    #company
    df1 = df[['co_code', 'co_name']].groupby('co_code').first()
    df1.to_csv('output_csv/company.csv')

    #exchange
    df2 = df[['exchange_code']].groupby('exchange_code').first()
    df2['exchange_name'] = ['National Stock Exchange', 'National Stock Exchange - Small & Medium Enterprises']
    df2.to_csv('output_csv/exchange.csv')
    
    # sector
    df3 = pd.unique(df['sector_name'])
    df3 = pd.DataFrame(df3)
    df3['sector_code'] = df3.index
    df4 = df3.set_index('sector_code')
    df5 = df4.rename(columns = {0 : 'sector_name'})
    df5.to_csv('output_csv/sector.csv')
    
    
    #industry
    df6 = pd.unique(df['industry_name'])
    df6 = pd.DataFrame(df6)
    df6['industry_code'] = df6.index
    df7 = df6.set_index('industry_code')
    df8 = df7.rename(columns = {0 : 'industry_name'})
    df8.to_csv('output_csv/industry.csv')

    #company_financials    
    df9 = df[['co_code', 'year_end', 'equity_paid_up', 'net_sales', 'pat', 'pbidt', 'debt_equity_ratio_latest', 'pbidtm_percentage_latest' ]].set_index(['co_code', 'year_end'])
    df9.to_csv('output_csv/company_financials.csv')
    
    
DataAnalysis()

