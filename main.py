# from crypt import methods
from flask import Flask, render_template
from flask import request
import pandas as pd
from symbol import simil
from mod import Predictions
from pipeline import Crypto
from apscheduler.schedulers.background import BackgroundScheduler
from extract import postgres    
app = Flask(__name__)
from functools import reduce
import pandas as pd
df=postgres()
def ditrubition():
    c= Crypto()
    c.CoinCaP(simil)
    c.Polygon(coins)
    data=postgres()
    Predictions(data)

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/Market')
def Market():
    return render_template('trading.html')
@app.route('/Contact')
def Contact():
    return render_template('Contact.html')
@app.route('/Recommandation',methods=['GET','POST'])
def Recommand():
    return render_template('recommand.html',data1=[{'price':'>$1000'},{'price':'$100  -   $1000'},{'price':'$10   -   $100'},{'price':'$1  -  $10'},{'price':'$0.1 -  $1'},{'price':'<$0.1'}],
    data2=[{'market':'>$10 Billion'},{'market':'$1 Billion - $10 Billion'},{'market':'$100 million - $1 Billion'},{'market':'$10 Million - $100 Million'},{'market':'$1 Million - $10 Million'},{'market':'<$1 Million'}],
    data3=[{'release':'> 5 years'},{'release':'2 years - 5 years'},{'release':'1 years - 2 years'},{'release':'1 year - 6 Months'},{'release':'6 Months - 3 Months'},{'release':'< 3 Months'}],
    data4=[{'method':'Daily Trader(days-weeks)'},{'method':'Investor (months-year)'}],
    data5=[{'risk':'High Risk  - High Reward'},{'risk':'Low Risk  - Low Reward'}])
     ####################  Predict Page    ########################
@app.route("/predict1", methods=['GET', 'POST'])
def predict():
            data = list(request.form.values())
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
            ####################  Price  - Filtering    ########################
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

            ####################  24Volume - Filtering    ########################
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
                ####################  MarketCap - Filtering    ########################
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

            l=[p,m,v,b,k,rk]
            res = list(reduce(lambda i, j: i & j, (set(x) for x in l)))

            #  list1 = set(p)
            #  intersection = list1.intersection(m)
            #  list2= list(intersection)
            #  l1 = set(v)
            #  intersection1 = l1.intersection(b)
            #  l2= list(intersection1)
            #  l3 = set(l2)
            #  intersection2 = l3.intersection(list2)
            #  final= list(intersection2)
            s=[];m=[];c=[]
            for t in res:
                s.append(df['symbol'][t])
                m.append(df['open'][t])
                c.append(df['volume'][t])
            e=len(s)
            dt=pd.DataFrame({'symbol':s,'marketcap':m,'volume':c})
                    
            return render_template('rec.html',symbol=s,market=['%.3f' % float(m1) for m1 in m],change=['%.3f' % float(c1) for c1 in c],l=e,
            data1=[{'price':'>$1000'},{'price':'$100  -   $1000'},{'price':'$10   -   $100'},{'price':'$1  -  $10'},{'price':'$0.1 -  $1'},{'price':'<$0.1'}],
            data2=[{'market':'>$10 Billion'},{'market':'$1 Billion - $10 Billion'},{'market':'$100 million - $1 Billion'},{'market':'$10 Million - $100 Million'},{'market':'$1 Million - $10 Million'},{'market':'<$1 Million'}],
            data3=[{'release':'> 5 years'},{'release':'2 years - 5 years'},{'release':'1 years - 2 years'},{'release':'1 year - 6 Months'},{'release':'6 Months - 3 Months'},{'release':'< 3 Months'}],
            data4=[{'method':'Daily Trader(days-weeks)'},{'method':'Investor (months-year)'}],
            data5=[{'risk':'High Risk  - High Reward'},{'risk':'Low Risk  - Low Reward'}])
#############################################  Forcasting Page ############################################# 
@app.route('/forecast',methods=['GET','POST'])
def Forcast():
    pred=pd.read_csv('C:/Users/T14s/Desktop/Forecaster 1/Back_end/prediction.csv')
    ln=len(pred['Day'])
    return render_template('forecast.html',l=ln,
    data1=list(simil.values()),
    data2=[{'Type':'1 Day '},{'Type':'7Days'},{'Type':'15Days'}],coins=pred['Coins'],
    data3= [ '%.2f' % elem for elem in pred['Day']],
    data4=[ '%.2f' % elem for elem in pred['Week']],
    data5=[ '%.2f' % elem for elem in pred['2Weeks']])
   
@app.route('/predict2',methods=['GET','POST'])
def predict2():
    data = list(request.form.values())
    pred=pd.read_csv('C:/Users/T14s/Desktop/Forecaster 1/Back_end/prediction.csv')
    ln=len(pred['Day'])
    c=list(simil.values())
    if data[0] in c:
        coin=data[0]
        p=df['open'].loc[df['symbol']== coin]  
        m=df['marketcap'].loc[df['symbol']== coin]
        v=df['volume'].loc[df['symbol']== coin]
        day=pred['Day'].loc[pred['Coins']== coin]
        week=pred['Week'].loc[pred['Coins']== coin]
        weeks=pred['2Weeks'].loc[pred['Coins']== coin]
        return render_template('coins.html',coin=coin,market=['%.2f' % float(m1) for m1 in m][0],
        price=['%.2f' % float(p1) for p1 in p][0],volume=['%.2f' % float(v1) for v1 in v][0],
        #volume= '%.2f' % float(v),price='%.2f' % float(p),
        day='%.3f' % float(day),
        week='%.3f' % float(week),weeks='%.3f' % float(weeks),
     data1=[{'Type':'1 Day '},{'Type':'7Days'},{'Type':'15Days'}])

    else:
            return render_template('forecast.html',l=ln,dat=data,
            data1=list(simil.values()),

            data2=[{'Type':'1 Day '},{'Type':'7Days'},{'Type':'15Days'}],coins=pred['Coins'],
            data3= [ '%.2f' % elem for elem in pred['Day']],
            data4=[ '%.2f' % elem for elem in pred['Week']],
            data5=[ '%.2f' % elem for elem in pred['2Weeks']])
#############################################  CoinsPage ############################################# 
@app.route('/<coin>')
def coins(coin):
    pred=pd.read_csv('C:/Users/T14s/Desktop/Forecaster 1/Back_end/prediction.csv')
    p=df['open'].loc[df['symbol']== coin]
    m=df['marketcap'].loc[df['symbol']== coin]
    v=df['volume'].loc[df['symbol']== coin]
    day=pred['Day'].loc[pred['Coins']== coin]
    week=pred['Week'].loc[pred['Coins']== coin]
    weeks=pred['2Weeks'].loc[pred['Coins']== coin]
    print(day)
    return render_template('coins.html',coin=coin,market=['%.2f' % float(m1) for m1 in m][0],
        price=['%.2f' % float(p1) for p1 in p][0],volume=['%.2f' % float(v1) for v1 in v][0],
        day='%.3f' % float(day), week='%.3f' % float(week),weeks='%.3f' % float(weeks),

    data1=[{'Type':'1 Day '},{'Type':'7Days'},{'Type':'15Days'}])

if __name__ == "__main__":
       
    # sched = BackgroundScheduler(daemon=True)
    # sched.add_job(ditrubition,'interval',minutes=10)
    # sched.start()
    app.run(debug=True) 
    