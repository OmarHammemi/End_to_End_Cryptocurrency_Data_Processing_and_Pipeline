from requests import Session
import json
import time
import psycopg2
import websocket, json
from requests import Session
import psycopg2
from symbol import simil
from symbol import coins
class Crypto:
            def CoinCaP(self,simil):
                    def getInfo (): # Function to get the info
                            url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest' # Coinmarketcap API url
                            # coins= "BTCUSD,ETHUSD,XLMUSD,LTCUSD,SHIBUSD,ETCUSD,XRPUSD,XMRUSD,XVGUSD,EOSUSD"
                            s=simil.values()
                            cs=list(s)
                            cs=cs
                            car=""
                            for coin in cs:
                                car+=coin+","
                            coins= car[:-1]
                            coins=coins.lower()
                            coins=coins.replace(" ", "-")
                            parameters = { 'slug': coins, 'convert': 'USD' } # API parameters to pass in for retrieving specific cryptocurrency data
                            # key1='4041310f-6b20-4c98-85c4-8244f356b32f'
                            key2='4041310f-6b20-4c98-85c4-8244f356b32f'
                            headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': key2} # Replace 'YOUR_API_KEY' with the API key you have recieved in the previous step
                            session = Session()
                            session.headers.update(headers)
                            response = session.get(url, params=parameters)
                            info = json.loads(response.text)
                            return info
                    data=getInfo()
                    # data.keys()
                    date,vl,mcap,sym,sm= [],[],[],[],[]
                    for i in data['data'].keys():
                                # data=getInfo()
                                df=data['data'][i]
                                sym.append(df['name'])
                                sm.append(df['symbol']+'-USD')
                                date.append(df['date_added'][:4])
                                vl.append(df['quote']['USD']['volume_24h'])
                                mcap.append(df['quote']['USD']['market_cap'])
                    #Establishing the connection
                    conn = psycopg2.connect(
                    database="postgres", user='postgres', password='omar1998', host='127.0.0.1', port= '5433'
                    )
                    #Creating a cursor object using the cursor() method

                    cursor = conn.cursor()
                    cursor.execute("DROP TABLE IF EXISTS coincap")
                    sql='''Create Table coincap(
                    Symbol varchar(40) not null,
                    date VARCHAR(5) not null,
                    vl_24 float not null,
                    MarketCap float not null
                    )
                    '''
                    cursor.execute(sql)

                    for i in range(len(date)):
                        cursor.execute('INSERT INTO coincap ( Symbol,date, vl_24 , MarketCap ) VALUES(%s,%s,%s,%s)',(sym[i],date[i],vl[i],mcap[i]))
                    conn.commit()
                    conn.close()
                    print('Coincap done')
            def Polygon(self,coins):
                    key=""
                    for d in coins:
                        key+="XA."+d +"-USD,"
                    key=key[:-1]
                    # coins=['Bitcoin',  'Ethereum','Stellar','Litecoin', 'Shiba Inu', 'Ethereum Classic', 'XRP', 'Monero',  'Verge',  'EOS']
                    def on_open(ws):
                        auth_data = {
                            "action": "auth",
                            "params": 'n8pb4Jngx0gmpLLvz0aYb0flDhIs9JfO'
                        }
                        ws.send(json.dumps(auth_data))
                        channel_data = {
                            "action": "subscribe",
                            "params": key
                            }
                        ws.send(json.dumps(channel_data))
                    def on_error(ws, error):
                        print(error)
                    sym,pair,open,close,low,high,volw,vol,e,s= [],[],[],[],[],[],[],[],[],[]
                    def on_close(ws):
                                print( "### closed ###")
                    def on_message(ws, message):
                        data={}
                        msg=json.loads(message)
                        m=msg[0]
                        if m['ev']=='XA':
                            if len(pair)!=100 and m['pair'] not in pair:
                                pair.append(m['pair'])
                                sym.append(simil[m['pair']])
                                open.append(m['o'])
                                close.append(m['c'])
                                low.append(m['l'])
                                high.append(m['h'])
                                volw.append(m['vw'])
                                vol.append(m['v'])
                                e.append(m['e'])
                                s.append(m['s'])
                            else:
                                ws.close()



                    data={'symbol':sym,'pair':pair,'open':open,'close':close,'low':low,'high':high,'vol_week':volw,'volume':volw}

                    def Stream():
                        websocket.enableTrace(True)

                        crypto = "wss://socket.polygon.io/crypto"
                        ws = websocket.WebSocketApp(crypto,
                                                on_open=on_open,
                                                on_message=on_message,
                                                on_error=on_error,
                                                on_close=on_close,keep_running=False)

                        ws.run_forever() # Set dispatcher to automatic reconnection
                        return data
                    data=Stream()
                    # for k in data.keys():
                    #     locals()[k]=data[k]
                    # dt={'symbol':symbol,'pair':pair,'open':open,'close':close,'low':low,'high':high,'vol_week':vol_week,'volume':volume}
                    def postgres(data):
                            conn = psycopg2.connect( database="postgres", user='postgres', password='omar1998', host='127.0.0.1', port= '5433')
                            cursor = conn.cursor()
                            #Doping EMPLOYEE table if already exists.
                            cursor.execute("DROP TABLE IF EXISTS crypto")
                            #Creating table as per requirement
                            sql ='''CREATE TABLE crypto(
                                pair CHAR(100) NOT NULL ,
                                Symbol CHAR(80) NOT NULL,
                                Price Float NOT NULL,
                                open Float NOT NULL,
                                close Float NOT NULL,
                                low Float NOT NULL,
                                high Float NOT NULL,
                                volume Float NOT NULL
                            )  '''
                            cursor.execute(sql)

                            for i in range(len(data['pair'])):
                                # try:
                                cursor.execute('insert into crypto values(%s,%s,%s,%s,%s,%s,%s,%s)',(data['pair'][i],data['symbol'][i],data['open'][i],data['open'][i],data['close'][i],data['low'][i],data['high'][i],data['volume'][i]))           
                                print(i)
                                # except:
                                #     print('ok')
                                #     pass

                            conn.commit()
                            cursor.close()
                            return "Table created successfully........"
                    postgres(data)
                    return data
