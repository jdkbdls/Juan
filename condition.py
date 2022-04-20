# Date  Open  High  Low  Close  Volume  Dividends  Stock Splits

# ===== price relative condition =====
class Technical:
    # 近m日有n日上漲
    def __init__(self, df):
        self.df = df
    def price_up(self,m,n): 
        if m >= n:
            c = 0
            for i in range(0,m):
                if self.df['Close'].iloc[-1-i] > self.df['Close'].iloc[-2-i]:
                    c = c + 1
            if c >= n:
                return True
            else:
                return False
        else:
            print("m should >= n and m, n should be integer")

    # 近m日有n日紅K
    def red_k(self,m,n): 
        if m >= n:
            c = 0
            for i in range(0,m):
                if self.df['Close'].iloc[-1-i] > self.df['Open'].iloc[-1-i]:
                    c = c + 1
            if c >= n:
                return True
            else:
                return False
        else:
            print("m should >= n and m, n should be integer")
    
    # 跳空

    # 價整理態

    # 均線上揚

    # 下跌



    # ===== volume relative condition =====
    # 近m日有n日量增
    def volume_increase(self,m,n): 
        if m >= n:
            c = 0
            for n in range(0,m):
                if self.df['Volume'].iloc[-1-n] > self.df['Volume'].iloc[-2-n]:
                    c = c + 1
            if c >= n:
                return True
            else:
                return False
        else:
            print("m should >= n and m, n should be integer")

    # 近3日平均量為近12日平均之n倍
    def volume_3days_ave_increase(self,n): 
        # print(self.df['Volume'].iloc[-3:])
        if (self.df['Volume'].iloc[-3:].mean()) > (self.df['Volume'].iloc[-12:-4].mean()*n):
            return True
        else:
            return False


    # 突然量增為前一天的n倍
    def volume_n_times_increase(self,n): 
        if (self.df['Volume'].iloc[-1]) > (self.df['Volume'].iloc[-2]*n):
            return True
        else:
            return False
