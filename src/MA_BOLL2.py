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

    # 今日、前一日、前二日 MA5
    df['MA5'] = talib.MA(df['收盤價'], 5)
    df['MA5_T1'] = df['MA5'].shift(1)
    df['MA5_T2'] = df['MA5'].shift(2)

    # 布林通道 args: close 20 0
    df['upper'], df['middle'], df['lower'] = talib.BBANDS(df['收盤價'], timeperiod=10, nbdevup=2, nbdevdn=2, matype=0)

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
        # 收在中軌上方且為紅K
        buy_condition_1 = (row['收盤價'] > row['middle']) and (row['開盤價'] < row['收盤價'])

        # MA5呈上漲
        buy_condition_2 = row['MA5'] > row['MA5_T1'] > row['MA5_T2']
        ##########----------買進條件----------##########

        ##########----------賣出條件----------##########
        # 收在上軌上方且為紅K
        sell_condition_1 = (row['收盤價'] > row['upper']) and (row['開盤價'] < row['收盤價'])
        ##########----------賣出條件----------##########

        if buy_condition_1 and buy_condition_2 and hold == 0:
            df.at[index, "Buy"] = row["收盤價"]
            print(f'Buy {index}')
            hold = 1
        elif sell_condition_1 and hold == 1:
            df.at[index, "Sell"] = row["收盤價"]
            print(f'Sell {index}')
            hold = 0

    return df

def main(stock_id, period="12mo", interval='1d'):
    df = get_TA(stock_id, period, interval)
    df = trade(df)

    # 取得KPI文字
    KPI_df = get_KPI.get_KPI(df)

    return df, KPI_df


if __name__ == "__main__":
    # 1m, 2m, 5m, 15m, 30m, 60m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo
    df, result_text = main('2377', '36mo', '1d')
    print(df)
    print(result_text)