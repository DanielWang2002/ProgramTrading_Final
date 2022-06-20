
import talib
import pandas as pd
import yF_Kbar
from get_KPI import get_KPI


def get_TA(stock_id, period="12mo"):

    df = yF_Kbar.get_data(stock_id, period)

    df.rename(columns={"Open": "開盤價",
                       "High": "最高價",
                       "Low": "最低價",
                       "Close": "收盤價",
                       "VoLume": "交易量"}, inplace=True)

    df["Buy"] = None
    df["Sell"] = None

    df["STOCH_5"] = talib.ADX(df["最高價"], df["最低價"], df["收盤價"])
    df["STOCH_5_T1"] = df["STOCH_5"].shift(1)
    df["STOCH_5_T2"] = df["STOCH_5"].shift(2)

    df["DX_5"] = talib.DX(df["最高價"], df["最低價"], df["收盤價"])
    df["DX_5_T1"] = df["DX_5"].shift(1)
    df["DX_5_T2"] = df["DX_5"].shift(2)

    df["SMA_20"] = talib.SMA(df["收盤價"], 20)
    df["SMA_20_T1"] = df["SMA_20"].shift(1)
    print(df["SMA_20"])

    df["OSC_5"] = talib.APO(df["收盤價"], 5)
    df["OSC_5_T1"] = df["OSC_5"].shift(1)
    df["OSC_5_T2"] = df["OSC_5"].shift(2)

    fastperiod = 12
    slowperiod = 26
    signalperiod = 9

    df["macd"], df["signal"], df["hist"] = talib.MACD(df["收盤價"],
                                                      fastperiod=fastperiod,
                                                      slowperiod=slowperiod,
                                                      signalperiod=signalperiod)
    return df


def trade(df):
    df["Buy"] = None
    df["Sell"] = None

    last_index = df.index[-1]
    hold = 0
    for index, row in df.copy().iterrows():
        if index == last_index:
            if hold == 1:
                df.at[index, "Sell"] = row["收盤價"]
                hold = 0
            break
        buy_condition_1 = (row["STOCH_5_T1"] <= row["STOCH_5_T2"]) and (row["STOCH_5_T1"] < row["STOCH_5"])
        buy_condition_1 = (row["DX_5_T1"] <= row["DX_5_T2"]) and (row["DX_5_T1"] < row["DX_5"])
        buy_condition_2 = row["SMA_20"] > row["SMA_20_T1"]

        sell_condition_1 = (row["OSC_5_T1"] >= row["OSC_5_T2"]) and (row["OSC_5_T1"] > row["OSC_5"])
        sell_condition_2 = row["macd"] < 0 and row["signal"] < 0

        if(buy_condition_1 and buy_condition_2) and hold == 0:
            df.at[index, "Buy"] = row["收盤價"]
            hold = 1
        elif(sell_condition_1 and sell_condition_2) and hold == 1:
            df.at[index, "Sell"] = row["收盤價"]
            hold = 0
            
    return df


def main(stock_id, period="12mo"):
    df = get_TA(stock_id, period)  # 取的資料
    df = trade(df)  # 交易
    result_txt = get_KPI(df)  # 取得KPI文字

    return df, result_txt


if __name__ == "__main__":
    df, result_txt = main(3008, "36mo")
    print(df, result_txt)
