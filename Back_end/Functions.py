import numpy as np
import pandas as pd
from functools import reduce
from flask import request
from extract import postgres    
####################################################_______________________________________________________Main Function_____________________________________________________________3#########################################################
def Predict(data):
            df=postgres()
            rk=[]
            k=[]
            r1=df['Risk1'].tolist()
            if data[4]=='Daily Trader(days-weeks)':
                r=df['daily']
                for i in range(len(r)):
                    if df.iloc[i]['daily']>=4:
                        k.append(r1[i])
            elif data[4]=='Investor (months-year)':
                r=df['investor']
                for i in range(len(r)):
                    if df.iloc[i]['investor']<=4:
                        k.append(r1[i])
            else:
                r=df['all']
            if data[5]=='High Risk  - High Reward':
                for i in range(len(r)):   
                  if r1[i]>5:
                    rk.append(i)
            elif data[5]=='Low Risk  - Low Reward':
                for i in range(len(r)):   
                  if r1[i]<5:
                    rk.append(i)
            else:
                for i in range(len(r)): 
                    rk.append(i)
####################  Price  - Filtering ########################################
            p=[]
            price=df['open']
            if data[0]=='>$1000':
                for i in range(len(price)):
                    if price[i]>1000:
                        p.append(i)
            elif data[0]=='$100  -   $1000':
                for i in range(len(price)):
                    if 1000>price[i]>100:
                        p.append(i)
            elif data[0]=='$10   -   $100':
                for i in range(len(price)):
                    if 100>price[i]>10:
                        p.append(i)
            elif data[0]=='$1  -  $10':
                for i in range(len(price)):
                    if 10>price[i]>1:
                        p.append(i)
            elif data[0]=='$0.1 -  $1':
                for i in range(len(price)):
                    if 1>price[i]>0.1:
                        p.append(i)
            elif data[0]=='<$0.1':
                for i in range(len(price)):
                    if price[i]<0.1:
                        p.append(i)
            else:
                for i in range(len(price)):
                    p.append(i)
            ####################  24Volume - Filtering    ########################################
            v=[]
            volume=df['volume']
            if data[2]=='>$10 Billion':
                for i in range(len(volume)):
                    if volume[i]>10000:
                        v.append(i)
            elif data[2]=='$1 Billion - $10 Billion':
                for i in range(len(volume)):
                    if 10000>volume[i]>1000:
                        v.append(i)
            elif data[2]=='$100 million - $1 Billion':
                for i in range(len(volume)):
                    if 1000>volume[i]>100:
                        v.append(i)
            elif data[2]=='$10 Million - $100 Million':
                for i in range(len(volume)):
                    if 100>volume[i]>10:
                        v.append(i)
            elif data[2]=='$1 Million - $10 Million':
                for i in range(len(volume)):
                    if 10>volume[i]>1:
                        v.append(i)
            elif data[2]=='<$1 Million':
                for i in range(len(volume)):
                    if 1>volume[i]:
                        v.append(i)
            else:
                for i in range(len(volume)):
                    v.append(i)
                ####################  MarketCap - Filtering    #################################
            m=[]
            market=df['marketcap']
            if data[1]=='>$10 Billion':
                for i in range(len(volume)):
                    if market[i]>10000:
                        m.append(i)
            elif data[1]=='$1 Billion - $10 Billion':
                for i in range(len(volume)):
                    if 10000>market[i]>1000:
                        m.append(i)
            elif data[1]=='$100 million - $1 Billion':
                for i in range(len(volume)):
                    if 1000>market[i]>100:
                        m.append(i)
            elif data[1]=='$10 Million - $100 Million':
                for i in range(len(volume)):
                    if 100>market[i]>10:
                        m.append(i)
            elif data[1]=='$1 Million - $10 Million':
                for i in range(len(volume)):
                    if 10>market[i]>1:
                        m.append(i)
            elif data[1]=='<$1 Million':
                for i in range(len(volume)):
                    if 1>market[i]:
                        m.append(i)
            else:
                for i in range(len(volume)):
                    m.append(i)
        ##########################   Release Date - Filtering  #############################
            b=[]
            release=df['date']
            if data[3]=='> 5 years':
                for i in range(len(volume)):
                    if release[i]=='+5':
                        b.append(i)
            elif data[3]=='2 years - 5 years':
                for i in range(len(volume)):
                    if release[i]=='-5' or release[i]=='+2':
                        b.append(i)
            elif data[3]=='1 years - 2 years':
                for i in range(len(volume)):
                    if release[i]=='+1':
                        b.append(i)
            elif data[3]=='1 year - 6 Months':
                for i in range(len(volume)):
                    if release[i]=='-1' :
                        b.append(i)
            elif data[3]=='6 Months - 3 Months':
                for i in range(len(volume)):
                    if release[i]=='-6' or release[i]=='-0.6':
                        b.append(i)
            elif data[3]=='< 3 Months':
                for i in range(len(volume)):
                    if release[i]=='-3' :
                        b.append(i)
            elif data[3]=='Coming Soon':
                for i in range(len(volume)):
                    if release[i]=='ICO(Initial Coin Offerings)':
                        b.append(i)
            else:
                for i in range(len(volume)):
                    b.append(i)

        ##########################  ensemble Date - Filtering  #############################

            l=[p,m,v,b,rk]
            res = list(reduce(lambda i, j: i & j, (set(x) for x in l)))
            s=[];m=[];c=[]
            for t in res:
                s.append(df['symbol'][t])
                m.append(df['open'][t])
                c.append(df['volume'][t])
            e=len(s)
            dt=pd.DataFrame({'symbol':s,'marketcap':m,'volume':c})
            return s,m,c,e
#########################################3_______________________________________________________Data Preprocessing_____________________________________________________________3###############################################
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
