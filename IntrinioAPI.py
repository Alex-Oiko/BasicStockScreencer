import requests
import base64

class IntrinioApi():

    def __init__(self,ticker=None,statement=None,**kwargs):
        self.ticker = ticker
        self.statement = statement
        self.username = 'feca9c5d6e1afa3a570c2f4d847f43ef'
        self.password = 'afd09f8b0a8ecddcb575395161f65983'
        self.query = 'https://www.intrinio.com/api/financials/standardized?ticker='+self.ticker+'&statement='+self.statement
        if kwargs:
            for key,value in kwargs.iteritems():
                self.query = self.query+'&'+key+'='+str(value)

    def fetchData(self):
        headers = {'Authorization':'Basic '+base64.b64encode(self.username+':'+self.password)}
        return requests.get(self.query,headers=headers).json()
