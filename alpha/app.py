from flask import Flask,jsonify,request 
import requests as req
import json
from modules.db import  StockImport
app = Flask(__name__)  
stock_prices=[
    {
        "id":1,
        "name":'dow jones'
    },
        {
        "id":2,
        "name":'coke cola'
    }
]



# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key

r = json.loads(req.get(url='https://www.alphavantage.co/'+'query', 
                                  params={'symbol': 'IBM',
                                          'function': 'TIME_SERIES_DAILY',
                                          'apikey': 'FOE5IX5FB8JJ2V91'}).text)['Time Series (Daily)']

for day, values in r.items():
    print(day,values.get('4. close'))
    StockImport.save_or_update_stock_imports(date=day, close=float(values.get('4. close')),open=float(values.get('1. open')) ,high=float(values.get('2. high')) ,low=float(values.get('3. low')) ,volume=float(values.get('5. volume')) ,stock='IBM')
@app.route('/stock',methods=['GET','POST']) 

def stocks():
    if request.method=='GET':
        if len(data)>0:
            return json.loads(req.get(url='https://www.alphavantage.co/'+'query', 
                                  params={'symbol': 'IBM',
                                          'function': 'TIME_SERIES_DAILY',
                                          'apikey': 'FOE5IX5FB8JJ2V91'}).text)['Time Series (Daily)']
       
  
if __name__ == '__main__' :
  app.run()