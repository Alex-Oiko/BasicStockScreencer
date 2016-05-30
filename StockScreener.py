import yahoo_finance as yf
from Stock import Stock
from IntrinioAPI import IntrinioApi
import json
if __name__=='__main__':
    tickers_input = raw_input('Please enter the tickers:')
    tickers_list=tickers_input.split(',')
    for ticker in tickers_list:
        stock = Stock(ticker,2015)
        print(stock)
    #inapi = IntrinioApi('AAPL','balance_sheet',date='2016-09-26',type='FY')
    #decoded = inapi.fetchData()
    #print('Total Assets:' +str(decoded['data'][13]))
    #rint('Total Liabilities:' + str(decoded['data'][21]))
    #print('Long term debt:' + str(decoded['data'][18]))
    #print('Short term debt:' + str(decoded['data'][14]))
    #print('Intanginble Assets:' + str(decoded['data'][10]))
    #print('Goodwill:' + str(DECODED['data'][9]))
    #print('Cash and Cash Equivelants:' + str(decoded['data'][0]))
    #inapi = IntrinioApi('AAPL', 'income_statement',fiscal_period='FY',fiscal_year='2015')
    #data = inapi.fetchData()
    #print(data)
    #print('Net Income 2015:'+str(data['data'][15]))
    #print('Basic eps:' + str(data['data'][17]))
    #print('Total revenue:' + str(data['data'][1]))
    #inapi = IntrinioApi('AAPL', 'income_statement', fiscal_period='FY', fiscal_year='2014')
    #print('Net Income 2014:'+str(data['data'][15]))
    #print('Net Income 2014:' + str(data['data'][15]))
    #inapi = IntrinioApi('AAPL', 'income_statement', fiscal_period='FY', fiscal_year='2013')
    #print('Net Income 2013:' + str(data['data'][15]))
    #stock = Stock('AAPL',2015)
    #print(stock)

