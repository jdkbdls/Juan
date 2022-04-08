import yfinance as yf
import h5py
import pandas as pd
import json
import pandas_ta as ta
from condition import Technical

# Date  Open  High  Low  Close  Volume  Dividends  Stock Splits
def CAL_MA():
    # df[SMA_5] SMA_10 SMA_20
    df.ta.sma(close='close', length=5,   append=True)
    # df.ta.sma(close='close', length=10,  append=True)
    df.ta.sma(close='close', length=20,  append=True)
    df.ta.sma(close='close', length=60,  append=True)
    # df.ta.sma(close='close', length=5,   append=True)
    # df.ta.sma(close='close', length=10,  append=True)



# ===============================
with open('list.txt', 'r') as list_file:
    list_stock_all = json.load(list_file)

# list_stock_all = ["2330.TW"]


list_picked_stock = []
for stock_id in list_stock_all:
    data = pd.read_hdf("data/"+stock_id+".h5")
    df = pd.DataFrame(data)
    CAL_MA()
    TA = Technical(df)
    # if TA.volume_3days_ave_increase(3):
    if TA.volume_n_times_increase(5):
    # if TA.price_up(4,3) & TA.red_k(4,3):
        print(stock_id)
    # if 

    del df
