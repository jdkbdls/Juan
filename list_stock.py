import yfinance as yf
import json
def check_tw(stock_no):
    # result = True
    df = yf.download(str(stock_no)+".TW",start="2022-03-20")
    if (df.empty):
        result = False
    else:
        result = True
    return result
    del df

def check_two(stock_no):
    df = yf.download(str(stock_no)+".TWO",start="2022-03-20")
    if (df.empty):
        result = False
    else:
        result = True
    return result
    del df


list = []
for i in range(1101, 9999):
    if check_tw(i):
        list.append(str(i)+".TW")
    elif check_two(i):
            list.append(str(i)+".TWO")

with open("list.txt","w") as f:
    json.dump(list,f)
