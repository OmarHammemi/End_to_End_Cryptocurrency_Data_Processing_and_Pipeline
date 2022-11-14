import numpy as np
def rsiFunc(prices, n=14):
    deltas = np.diff(prices)
    seed = deltas[:n+1]
    up = seed[seed>=0].sum()/n
    down = -seed[seed<0].sum()/n
    rs = up/down
    rsi = np.zeros_like(prices)
    rsi[:n] = 100. - 100./(1.+rs)

    for i in range(n, len(prices)):
        delta = deltas[i-1] # cause the diff is 1 shorter

        if delta>0:
            upval = delta
            downval = 0.
        else:
            upval = 0.
            downval = -delta

        up = (up*(n-1) + upval)/n
        down = (down*(n-1) + downval)/n

        rs = up/down
        rsi[i] = 100. - 100./(1.+rs)

    return rsi
def upper_shadow(df):
    return df['High'] - np.maximum(df['Close'], df['Open'])

def lower_shadow(df):
    return np.minimum(df['Close'], df['Open']) - df['Low']
def A_fac(df):
    return ((df['High']+df['Low']+df['Close'])/3)
def Analyse(dt):
        dt["high_div_low"] = dt["High"] / dt["Low"]
        dt['trade'] = dt['Close'] - dt['Open']
        dt['upper_shadow']=upper_shadow(dt)
        dt['lower_shadow']=lower_shadow(dt)
        dt['A_fac']=A_fac(dt)
        return dt
