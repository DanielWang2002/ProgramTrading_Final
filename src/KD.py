import talib
import pandas as pd
import yF_Kbar
import get_KPI


def get_TA(stock_id, period="12mo", interval='1d'):
    # get Data
    df = yF_Kbar.get_data(stock_id, period, interval)

    df.rename(columns={
        "Open": "開盤價",
        "High": "最高價",
        "Low": "最低價",
        "Close": "收盤價",
        "Volume": "交易量"
    }, inplace=True)

    df["Buy"] = None
    df["Sell"] = None

    # KD args: 5, 3, 3
    df['K'], df['D'] = talib.STOCH(df['最高價'], df['最低價'], df['收盤價'], fastk_period=5, slowk_period=3, slowd_period=3)
    df['K_T1'] = df['K'].shift(1)
    df['D_T1'] = df['D'].shift(1)

    fastPeriod = 12
    slowPeriod = 26
    signalPeriod = 9

    df["macd"], df["signal"], df["hist"], = talib.MACD(df["收盤價"],
                                                       fastperiod=fastPeriod,
                                                       slowperiod=slowPeriod,
                                                       signalperiod=signalPeriod)

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

        ##########----------買進條件----------##########
        # KD黃金交叉
        buy_condition_1 = (row['K'] > row['K_T1']) and (row['D'] < row['D_T1']) and (row['K'] >= row['D'])
        buy_condition_2 = (row['K'] <= 22.5) or (row['D'] <= 22.5)
        ##########----------買進條件----------##########

        ##########----------賣出條件----------##########
        # KD死亡交叉
        sell_condition_1 = (row['K'] < row['K_T1']) and (row['D'] > row['D_T1']) and (row['K'] <= row['D'])
        sell_condition_2 = (row['K'] >= 77.5) or (row['D'] >= 77.5)
        ##########----------賣出條件----------##########

        if (buy_condition_1 and buy_condition_2) and hold == 0:
            df.at[index, "Buy"] = row["收盤價"]
            hold = 1
        elif (sell_condition_1 and sell_condition_2) and hold == 1:
            df.at[index, "Sell"] = row["收盤價"]
            hold = 0

    return df


def main(stock_id, period="12mo", interval='1d'):
    df = get_TA(stock_id, period, interval)
    df = trade(df)

    # 取得KPI文字
    KPI_df = get_KPI.get_KPI(df)

    return df, KPI_df

if __name__ == "__main__":
    df, result_text = main('3532', "36mo", '1d')
    print(df, result_text)