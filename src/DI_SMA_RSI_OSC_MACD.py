import talib
import pandas as pd
import yF_Kbar
from get_KPI import get_KPI

# 取得技術分析(Technical Analysis)指標
def get_TA(stock_id, period = "12mo"):
    # 取得資料
    df = yF_Kbar.get_data(stock_id, period)

    # 配合程式更改欄位名稱
    df.rename(columns = {"Open" : "開盤價", 
               "High" : "最高價",
               "Low" : "最低價",
               "Close" : "收盤價",
               "Volume" : "交易量"}
              , inplace = True)
    
    df["Buy"] = None
    df["Sell"] = None

    df["RSI_5"] = talib.RSI(df["收盤價"], 5) # 計算RSI
    df["RSI_5_T1"] = df["RSI_5"].shift(1) # 前一日的RSI
    df["RSI_5_T2"] = df["RSI_5"].shift(2) # 前兩日的RSI
    
    df["SMA_20"] = talib.SMA(df["收盤價"], 20) # 計算 SMA20
    df["SMA_20_T1"] = df["SMA_20"].shift(1) # 前一日的 SMA20
    
    df["+DI"] = talib.PLUS_DI(df["最高價"], df["最低價"], df["收盤價"])
    df["+DI_T1"] = df["+DI"].shift(1)
    df["+DI_T2"] = df["+DI"].shift(2)
    
    # 設定 MACD 的參數
    fastperiod = 12
    slowperiod = 26
    signalperiod = 9
    
    # 參考：https://fxlittw.com/what-is-macd-indicator/
    # macd = EMA_12 - EMA_26，即DIF值，也稱為快線
    # signal = DIF值取EMA_9，也稱為慢線
    # hist = 柱狀圖，快線 - 慢線
    df["macd"], df["signal"], df["hist"] = talib.MACD(df["收盤價"], 
                                    fastperiod=fastperiod, 
                                    slowperiod=slowperiod, 
                                    signalperiod=signalperiod)
    
    # 此處的OSC為快線 - 慢線
    df["OSC"] = df["macd"] - df["signal"]
    df["OSC_T1"] = df["OSC"].shift(1) # 前一日的OSC
    df["OSC_T2"] = df["OSC"].shift(2) # 前兩日的OSC
    
    #df = df.dropna() # 去除空值
   
    return df

def trade(df):
    
    df["Buy"] = None
    df["Sell"] = None
    
    last_index = df.index[-1]
    hold = 0 # 是否持有
    for index, row in df.copy().iterrows():
        # 最後一天不交易，並將部位平倉
        if index == last_index: 
            if hold == 1: # 若持有部位，平倉
                df.at[index, "Sell"] = row["收盤價"] # 紀錄賣價
                hold = 0
            break # 跳出迴圈
        
        # 買進條件
        # 買進條件1 前一日RSI5<=前二日RSI5 and 前一日RSI5<今日RSI5
        # 買進條件2 今日SMA20>前一日SMA20
        buy_condition_1 = (row["+DI_T1"] <= row["+DI_T2"]) and (row["+DI_T1"] < row["+DI"])
        buy_condition_2 = row["SMA_20"] > row["SMA_20_T1"]
        buy_condition_3 = (row["RSI_5_T1"] <= row["RSI_5_T2"]) and (row["RSI_5_T1"] < row["RSI_5"])
        
        # 賣出條件
        # 賣出條件1 前一日SMA5>=前二日SMA5 and 前一日SMA5>今日SMA5
        # 賣出條件2 今日DIF<0 and今日MACD<0 
        sell_condition_1 = (row["OSC"] >= row["OSC_T2"]) and (row["OSC_T1"] > row["OSC"])
        sell_condition_2 = row["SMA_20"] < 0 and row["SMA20_T1"] < 0
        sell_condition_3 = row["macd"] < 0 and row["signal"] < 0
        
        # 符合兩個買進條件，沒有持有股票，符合以上條件買入
        if ((buy_condition_1 or buy_condition_2) and buy_condition_3) and hold == 0:
            df.at[index, "Buy"] = row["收盤價"] # 記錄買價
            hold = 1
        # 符合兩個賣出條件，有持有股票，符合以上條件賣出
        elif ((sell_condition_1 or sell_condition_2) and sell_condition_3) and hold == 1:
            df.at[index, "Sell"] = row["收盤價"] # 紀錄賣價
            hold = 0
    
    return df

def main(stock_id, period = "12mo"):
    df = get_TA(stock_id, period) # 取得資料
    df = trade(df) # 交易
    KPI_df = get_KPI(df) # 取得KPI文字
    
    return df, KPI_df

if __name__ == "__main__":
    df, KPI_df = main('2357', "36mo")
    print(df, KPI_df)