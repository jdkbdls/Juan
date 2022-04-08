import yfinance as yf
import h5py
import pandas as pd
import json

with open('list.txt', 'r') as list_file:
    list = json.load(list_file)

# Date  Open  High  Low  Close  Volume  Dividends  Stock Splits
# list = ["2330.TW"]
for stock_id in list:
    stock = yf.Ticker(stock_id)
    df = pd.DataFrame()
    stock_history = stock.history(period="3y",rounding=True)
    df = pd.concat([df, stock_history])
    df.to_hdf("data/"+stock_id+".h5",key="s")
    print(stock_id)
    del df