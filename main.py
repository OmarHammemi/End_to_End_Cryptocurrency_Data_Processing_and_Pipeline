# from crypt import methods
from flask import Flask, render_template
from flask import request
import pandas as pd
from symbol import simil,dt1,dt2,dt3,dt4,dt5
# from mod import Predictions
from pipeline import Crypto
from apscheduler.schedulers.background import BackgroundScheduler
from extract import postgres    
app = Flask(__name__)
from Functions import Predict
from functools import reduce
import pandas as pd
df=postgres()
##################################_______________________________________________________Home Page_____________________________________________________________###############################################


@app.route('/')
def home():
    return render_template('home.html')


##################################_______________________________________________________Market Page_____________________________________________________________###############################################


@app.route('/Market')
def Market():
    return render_template('trading.html')

##################################_______________________________________________________Contact Page_____________________________________________________________###############################################


@app.route('/Contact')
def Contact():
    return render_template('Contact.html')

##################################_______________________________________________________Recommendation Page_____________________________________________________________###############################################


@app.route('/Recommandation',methods=['GET','POST'])
def Recommand():
    return render_template('recommand.html',data1=dt1,data2=dt2, data3=dt3,data4=dt4, data5=dt5)

##################################_______________________________________________________Recommendation Prediction Page_____________________________________________________________###############################################



@app.route("/predict1", methods=['GET', 'POST'])
def predict():
            data = list(request.form.values())
            s,m,c,e=Predict(data)
            return render_template('rec.html',symbol=s,market=['%.3f' % float(m1) for m1 in m],change=['%.3f' % float(c1) for c1 in c],l=e,data1=dt1,data2=dt2, data3=dt3,data4=dt4, data5=dt5)
#return render_template('recommand.html',data1=dt1,data2=dt2, data3=dt3,data4=dt4, data5=dt5)


##################################_______________________________________________________Forecasting Page_____________________________________________________________###############################################



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
#return render_template('rec.html',symbol=s,market=['%.3f' % float(m1) for m1 in m],change=['%.3f' % float(c1) for c1 in c],l=e,data1=dt1,data2=dt2, data3=dt3,data4=dt4, data5=dt5)



##################################_______________________________________________________Forecasting Prediction Page_____________________________________________________________###############################################



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



##################################_______________________________________________________Coin Page_____________________________________________________________###############################################



@app.route('/<coin>')
def coins(coin):
    pred=pd.read_csv('C:/Users/T14s/Desktop/Forecaster 1/Back_end/prediction.csv')
    p=df['open'].loc[df['symbol']== coin]
    m=df['marketcap'].loc[df['symbol']== coin]
    v=df['volume'].loc[df['symbol']== coin]
    day=pred['Day'].loc[pred['Coins']== coin]
    week=pred['Week'].loc[pred['Coins']== coin]
    weeks=pred['2Weeks'].loc[pred['Coins']== coin]
    return render_template('coins.html',coin=coin,market=['%.2f' % float(m1) for m1 in m][0],
        price=['%.2f' % float(p1) for p1 in p][0],volume=['%.2f' % float(v1) for v1 in v][0],
        day='%.3f' % float(day), week='%.3f' % float(week),weeks='%.3f' % float(weeks),

    data1=[{'Type':'1 Day '},{'Type':'7Days'},{'Type':'15Days'}])

if __name__ == "__main__":
       
    app.run(debug=True) 
    