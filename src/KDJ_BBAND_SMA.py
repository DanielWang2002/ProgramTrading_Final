# -*- coding: utf-8 -*-
"""
Created on Thu Jun 16 00:17:12 2022

@author: USER
"""
#策略六

import talib
import yF_Kbar
from get_KPI import get_KPI

def get_TA(stock_id,period = "12mo"):
    
    df = yF_Kbar.get_data(stock_id,period)

    # 配合程式更改欄位名稱
    df.rename(columns = {"Open" : "開盤價", 
               "High" : "最高價",
               "Low" : "最低價",
               "Close" : "收盤價",
               "Volume" : "交易量"}
              , inplace = True)
    
    df["Buy"] = None
    df["Sell"] = None
    

    df["SMA_20"] = talib.SMA(df["收盤價"],20) # 計算 SMA20
    df["SMA_20_T1"] =df["SMA_20"].shift(1) #計算前一日 SMA


    df["Bupper"],df["Bmiddle"],df["Blower"] = talib.BBANDS(df["收盤價"],5)
    
    df["B%B"]=  (df["收盤價"]-df["Blower"])/(df["Bupper"]-df["Blower"])*100
    df["B%B_T1"] =df["B%B"].shift(1)
    df["B%B_T2"] =df["B%B"].shift(2)
        
    fastk_period=9
    slowk_period=3
    slowk_matype=0
    slowd_period=3
    slowd_matype=0
    
    df['K'] , df["D"]= talib.STOCH(df['最高價'], df['最低價'], df['收盤價'],
                                   fastk_period=fastk_period,
                                   slowk_period=slowk_period,
                                   slowk_matype=slowk_matype,
                                   slowd_period=slowd_period,
                                   slowd_matype=slowd_matype)
    df["K_T1"] = df["K"].shift(1)
    df["K_T2"] = df["K"].shift(2)
    
    df["D_T1"] = df["D"].shift(1)
    df["D_T2"] = df["D"].shift(2)
        
    df["J"] = (3*df["K"])-(2*df["D"])
    
    df["J_T1"] = df["J"].shift(1)
    df["J_T2"] = df["J"].shift(2)
    
    
    print(df)
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
        
        buy_condition_1 = (row["K_T1"]and row["D_T1"] and row["J_T1"] <= row["K_T2"]and row["D_T2"] and row["J_T2"]) and (row["K_T1"]and row["D_T1"] and row["J_T1"] < row["K"] and row["D"] and row["J"])

        buy_condition_2 = row["SMA_20"] > row["SMA_20_T1"]
        
        
        sell_condition_1 = (row["B%B"] > row["B%B_T2"]) and (row["B%B_T1"]>row["B%B"])

        sell_condition_2 = row["SMA_20"] < row["SMA_20_T1"]
            
        if (buy_condition_1 and buy_condition_2 ) and hold ==0:
            df.at[index,"Buy"] = row["收盤價"]
            hold = 1
            
        elif (sell_condition_1 and sell_condition_2 ) and hold ==1:
            df.at[index,"Sell"] = row["收盤價"]
            
            hold = 0
    print(df)
    return df

def main(stock_id,period = "12mo"):
    df = get_TA(stock_id,period) # 取的資料
    df = trade(df) # 交易
    result_txt = get_KPI(df) # 取得KPI文字
    
    return df, result_txt

if __name__ == "__main__":
    df, result_txt = main(1101,"max")
    print(df, result_txt)
