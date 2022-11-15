import sys
import pickle
import pandas as pd
import numpy as np
from symbol import coins
from Backend.Functions import Analyse
sys.path.append('C:/Users/T14s/Desktop/Forecaster 1/Back_end')
import Backend.extract as e
data=e.postgres()
def Predictions(data):
                dt=pd.DataFrame({'pair':data['pair'],'symbol':data['symbol'],'Open':data['open'],'High':data['high'],'Low':data['low'],'Close':data['close'],'Volume':data['volume'],'Adj Close':data['close']})
                new=[]
                cn= [d.replace("-USD","") for d in  dt.pair]
                cn=[d.replace(" ","") for d in  cn]
                for i,coin in enumerate(dt['symbol']):
                        print(coin)
                        globals()[dt['symbol'][i]]=Analyse(dt.loc[i])
                        new.append(globals()[dt['symbol'][i]])
                day,week,weeks=[],[],[]
                for i,coin in enumerate(cn):
                    day.append(coin+'_day')
                    week.append(coin+'_week')
                    weeks.append(coin+'_2weeks')
                Day,Week,Weeks=[],[],[]

                for i in range(len(cn)):
                            globals()[day[i]]=pickle.load(open('Back_end/pretrained/1Day_model_'+cn[i]+'.pkl', 'rb'))
                            Day.append(globals()[day[i]])
                            globals()[week[i]]=pickle.load(open('Back_end/pretrained/7Day_model_'+cn[i]+'.pkl', 'rb'))
                            Week.append(globals()[week[i]])
                            globals()[weeks[i]]=pickle.load(open('Back_end/pretrained/15Day_model_'+cn[i]+'.pkl', 'rb'))
                            Weeks.append(globals()[weeks[i]])
                s=[Day,Week,Weeks]
                prediction=[]
                for i,coin in enumerate(cn):
                    prediction.append(coin+'_predict')
                pred=[]
                for i in range(len(prediction)):
                    globals()[prediction[i]]=[s[0][i].predict(new[i][2:].values.reshape(1, -1)),s[1][i].predict(new[i][2:].values.reshape(1, -1)),s[2][i].predict(new[i][2:].values.reshape(1, -1))]
                    pred.append(globals()[prediction[i]])
                names=data['symbol']
                d,w,w2=[],[],[]
                for p in pred:
                    d.append(p[0][0])     
                    w.append(p[1][0])
                    w2.append(p[2][0])
                predictions=pd.DataFrame({'Coins':names,'Day':d,'Week':w,'2Weeks':w2})
                predictions.to_csv('Back_end/prediction.csv',index=False)
                return 'prediction Done ...'
