import yahoo_finance as yf
from IntrinioAPI import IntrinioApi

class Stock(object):


    def __init__(self,ticker,last_year):
        data = 'data'
        value = 'value'

        self.ticker = ticker
        share = yf.Share(ticker)
        self.price = share.get_price()
        self.eps = share.get_earnings_share()
        self.pe = share.get_price_earnings_ratio()
        self.pb = share.get_price_book()
        self.mktcap = share.get_market_cap()
        income_statement_data_last_year = self.getIncomeStatementData(str(last_year))
        income_statement_data_two_years = self.getIncomeStatementData(str(last_year-1))
        income_statement_data_three_years = self.getIncomeStatementData(str(last_year - 2))
        balance_sheet_data = self.getBalanceSheetData(last_year)
        try:
            self.last_year_net_income = income_statement_data_last_year[data][self.findIndex(income_statement_data_last_year[data],'netincome')][value]
        except Exception:
            self.last_year_net_income = 'N/A'
        try:
            self.two_years_year_net_income = income_statement_data_two_years[data][self.findIndex(income_statement_data_two_years[data],'netincome')][value]
        except Exception:
            self.two_years_year_net_income = 'N/A'
        try:
            self.three_years_net_income = income_statement_data_three_years[data][self.findIndex(income_statement_data_three_years[data],'netincome')][value]
        except Exception:
            self.three_years_net_income = 'N/A'
        try:
            self.basiceps_last_year = income_statement_data_last_year[data][self.findIndex(income_statement_data_last_year[data],'basiceps')][value]
        except Exception:
            self.basiceps_last_year = 'N/A'
        try:
            self.basiceps_two_years = income_statement_data_two_years[data][self.findIndex(income_statement_data_two_years[data],'basiceps')][value]
        except Exception:
            self.basiceps_two_years = 'N/A'
        try:
            self.basiceps_three_years = income_statement_data_three_years[data][self.findIndex(income_statement_data_three_years[data],'basiceps')][value]
        except Exception:
            self.basiceps_three_years = 'N/A'
        try:
            self.cashtodebt = balance_sheet_data[data][self.findIndex(balance_sheet_data[data],'cashandequivalents')][value]/balance_sheet_data[data][self.findIndex(balance_sheet_data[data],'longtermdebt')][value]+balance_sheet_data[data][self.findIndex(balance_sheet_data[data],'shorttermdebt')][value]
        except Exception:
            self.cashtodebt = 'N/A'
        try:
            self.profitmargin = self.last_year_net_income/income_statement_data_last_year[data][self.findIndex(income_statement_data_last_year[data],'totalrevenue')][value]
        except Exception:
            self.profitmargin = 'N/A'
        try:
            self.assettodebt = balance_sheet_data[data][self.findIndex(balance_sheet_data[data],'totalassets')][value]/balance_sheet_data[data][self.findIndex(balance_sheet_data[data],'longtermdebt')][value]+balance_sheet_data[data][self.findIndex(balance_sheet_data[data],'shorttermdebt')][value]
        except Exception:
            self.assettodebt = 'N/A'
        try:
            self.booktomkt = (balance_sheet_data[data][self.findIndex(balance_sheet_data[data],'totalassets')][value]-balance_sheet_data[data][self.findIndex(balance_sheet_data[data],'intangibleassets')][value]+balance_sheet_data[data][self.findIndex(balance_sheet_data[data],'goodwill')][value]-balance_sheet_data[data][self.findIndex(balance_sheet_data[data],'totalliabilities')][value])/float(self.convertMktCap(self.mktcap))
        except Exception:
            self.booktomkt = 'N/A'

    def __str__(self):
        return self.ticker + '\nPrice: ' + str(self.price) + ' EPS:' + str(self.eps) + ' P/E:' + str(self.pe) + ' P/B:' + str(self.pb) + ' Mkt. cap:' + str(self.mktcap) + ' \n'+'Net income 2015:'+str(self.last_year_net_income)+' Net income 2014:'+str(self.two_years_year_net_income)+' Net income 2013:'+str(self.three_years_net_income)+'\n'+'Basic eps 2015:'+str(self.basiceps_last_year)+' Basic eps 2014:'+str(self.basiceps_two_years)+' Basic eps 2013:'+str(self.basiceps_three_years)+'\nCash/debt:'+str(self.cashtodebt)+' Profit margin: '+str(self.profitmargin)+' asset/debt:'+str(self.assettodebt)+' Book/Mkt:'+str(self.booktomkt)+'\n\n'

    def getIncomeStatementData(self,year):
        inapi = IntrinioApi(self.ticker, 'income_statement', fiscal_period='FY', fiscal_year=year)
        return inapi.fetchData()

    def getBalanceSheetData(self,year):
        inapi = IntrinioApi(self.ticker, 'balance_sheet', fiscal_period='FY', fiscal_year=year)
        return inapi.fetchData()

    def convertMktCap(self,strmktcap):
        if(strmktcap.endswith('B')):
            return float(strmktcap.split('B')[0])*10**9
        elif(strmktcap.endswith('M')):
            return float(strmktcap.split('M')[0])*10**6

    def findIndex(self,data,tagName):
        tag = 'tag'
        for idx,dic in enumerate(data):
            if(dic[tag]==tagName):
                return idx

