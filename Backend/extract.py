import psycopg2
import pandas as pd
import numpy as np
def postgres():
        pair,symbol,price,open,close,high,low,volume,marketcap,date=[],[],[],[],[],[],[],[],[],[]
        connection = psycopg2.connect(database="postgres", user='postgres', password='omar1998', host='127.0.0.1', port= '5433')
        cursor = connection.cursor()
        postgreSQL_select_Query = "SELECT X.*,Y.* FROM crypto X INNER JOIN coincap Y ON X.symbol = Y.symbol;"
        cursor.execute(postgreSQL_select_Query)
        print("Selecting rows from mobile table using cursor.fetchall")
        mobile_records = cursor.fetchall()

        for row in mobile_records:
                p=row[0];s=row[1]; pr=row[2];o=row[3]; c=row[4]; l=row[5];h=row[6];v=row[10];d=row[9];mc=row[11]
                p.replace(' ','')
                s=s.rstrip()
                pair.append(p);symbol.append(s);price.append(pr);open.append(o);close.append(c);low.append(l);high.append(h);volume.append(v),date.append(d);marketcap.append(mc)
                
                    
        cursor.close()
        connection.close()
        date =[2022-int(d) for d in date]
        for i in range(len(date)):
            if date[i]>5:
                date[i]='+5'
            elif date[i]>2:
                date[i]='+2'
            elif date[i]>1:
                date[i]='+1'
            else:
                date[i]='-1'
        daily,investor,all,risk=np.zeros(len(date)),np.zeros(len(date)),np.zeros(len(date)),np.zeros(len(date))
        for i in range(len(marketcap)):
            marketcap[i]=marketcap[i]/1000000 
            volume[i]=volume[i]/1000000
            df=pd.DataFrame({'pair':pair,'symbol':symbol,'price':price,'marketcap':marketcap,'open':open,'close':close,'high':high,'low':low,'volume':volume,'date':date})
            if marketcap[i]>10000: t=4
            elif 10000>=marketcap[i]>1000:t=2
            elif 1000>=marketcap[i]>100: t=1
            elif 100>=marketcap[i]>10: t=0.5
            else: t=0
            if date[i]=='+5': d=4
            elif date[i]=='+2': d=2
            elif date[i]=='+1': d=1
            elif date[i]=='-1': d=0.5
            else: d=0
            daily[i]=10-(d+t)
            investor[i]=d+t
            all[i]=10
            risk[i]=10-(d+t)
            # df.to_csv('extration.csv',index=False)
        pair=[p.replace(' ','') for p in pair]
        # print(pair)
        df=pd.DataFrame({'pair':pair,'symbol':symbol,'price':price,'marketcap':marketcap,'open':open,'close':close,'high':high,'low':low,'volume':volume,'date':date,'daily':daily,'investor':investor,'all':all,'Risk1':risk})
        return df
