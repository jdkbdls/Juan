import yfinance as yf
import h5py
import pandas as pd
import json

with open('list.txt', 'r') as list_file:
    list = json.load(list_file)

for stock_id in list:
    data = pd.read_hdf("data/"+stock_id+".h5")
    df = pd.DataFrame(data)
    last_date = df.index[-1]
    # print(last_date)

    # get new data from yahoo finance
    stock = yf.Ticker(stock_id)
    df2 = pd.DataFrame()
    stock_history = stock.history(start=last_date,rounding=True)
    df2 = pd.concat([df2, stock_history])
    df2 = df2.iloc[1:]  # remove 1st (iloc[0]) data
    df = df.append(df2)
    df = df.tail(800)  # save up to 1000 days
    df.to_hdf("data/"+stock_id+".h5",key="s")
    del df
    del df2