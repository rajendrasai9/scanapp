from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
# from kivy.uix.textinput import TextInput
from binance.client import Client
from kivy.core.window import Window
from time import sleep
# from kivy.network.urlrequest import UrlRequest
from kivy.uix.screenmanager import ScreenManager, Screen

api_key = "IMQaYnycqb2zEnVWoLxP7M0l5drTf4Y2UPcJybkHtIVBY71jWuqGiinZGxxkLWpj"
api_secret = "S7cT4lJsC2QoJFcbjapwvrusEcbqNmL6LSn1tJzwJPUvnyVZvpiWrIJkJnLokuz5"
try:
    client = Client(api_key, api_secret)
except:
    print("Please check your internet connection!")

# print("connection established")
# k_lines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC")
# print(k_lines[0])
tickers = ['BTCUSDT', 'ETHUSDT', 'BNBUSDT', 'NEOUSDT', 'LTCUSDT', 'QTUMUSDT', 'ADAUSDT', 'XRPUSDT','EOSUSDT', 'TUSDUSDT',
         'IOTAUSDT', 'XLMUSDT', 'ONTUSDT', 'TRXUSDT', 'ETCUSDT', 'ICXUSDT','NULSUSDT', 'VETUSDT', 'LINKUSDT', 'WAVESUSDT',
         'BTTUSDT', 'ONGUSDT', 'HOTUSDT', 'ZILUSDT', 'ZRXUSDT', 'FETUSDT','BATUSDT', 'XMRUSDT', 'ZECUSDT',
         'IOSTUSDT', 'CELRUSDT', 'DASHUSDT', 'NANOUSDT', 'OMGUSDT', 'THETAUSDT', 'ENJUSDT', 'MITHUSDT', 'MATICUSDT',
         'ATOMUSDT', 'TFUELUSDT', 'ONEUSDT', 'FTMUSDT', 'ALGOUSDT', 'GTOUSDT', 'DOGEUSDT',
         'DUSKUSDT', 'ANKRUSDT', 'WINUSDT', 'COSUSDT', 'COCOSUSDT', 'MTLUSDT', 'TOMOUSDT', 'PERLUSDT',
         'DENTUSDT', 'MFTUSDT', 'KEYUSDT', 'DOCKUSDT', 'WANUSDT', 'FUNUSDT', 'CVCUSDT', 'CHZUSDT',
         'BANDUSDT','BEAMUSDT', 'XTZUSDT', 'RENUSDT', 'RVNUSDT', 'HBARUSDT', 'NKNUSDT',
         'STXUSDT', 'KAVAUSDT', 'ARPAUSDT', 'IOTXUSDT', 'RLCUSDT', 'CTXCUSDT', 'BCHUSDT', 'TROYUSDT',
         'VITEUSDT', 'FTTUSDT', 'EURUSDT', 'OGNUSDT', 'DREPUSDT', 'TCTUSDT', 'WRXUSDT',
         'BTSUSDT', 'LSKUSDT', 'BNTUSDT', 'LTOUSDT','AIONUSDT', 'MBLUSDT',
         'COTIUSDT', 'STPTUSDT', 'WTCUSDT', 'DATAUSDT' , 'SOLUSDT',
         'CTSIUSDT', 'HIVEUSDT', 'CHRUSDT', 'GXSUSDT', 'ARDRUSDT', 'MDTUSDT',
         'STMXUSDT', 'KNCUSDT', 'LRCUSDT', 'PNTUSDT', 'COMPUSDT', 'SCUSDT',
         'ZENUSDT', 'SNXUSDT', 'VTHOUSDT', 'DGBUSDT', 'GBPUSDT', 'SXPUSDT', 'MKRUSDT', 'DCRUSDT',
         'STORJUSDT' , 'MANAUSDT', 'AUDUSDT', 'YFIUSDT', 'BALUSDT', 'BLZUSDT',
         'IRISUSDT', 'KMDUSDT' , 'JSTUSDT', 'SRMUSDT', 'ANTUSDT', 'CRVUSDT', 'SANDUSDT', 'OCEANUSDT', 'NMRUSDT',
         'DOTUSDT', 'LUNAUSDT', 'RSRUSDT', 'PAXGUSDT', 'WNXMUSDT', 'TRBUSDT', 'BZRXUSDT', 'SUSHIUSDT', 'YFIIUSDT',
         'KSMUSDT', 'EGLDUSDT', 'DIAUSDT', 'RUNEUSDT', 'FIOUSDT', 'UMAUSDT', 'BELUSDT', 'WINGUSDT', 'UNIUSDT', 'NBSUSDT',
         'OXTUSDT', 'SUNUSDT', 'AVAXUSDT', 'HNTUSDT', 'FLMUSDT', 'ORNUSDT', 'UTKUSDT', 'XVSUSDT', 'ALPHAUSDT',
         'AAVEUSDT', 'NEARUSDT','FILUSDT', 'INJUSDT','AUDIOUSDT', 'CTKUSDT', 'AKROUSDT', 'AXSUSDT', 'HARDUSDT', 'DNTUSDT',
         'STRAXUSDT','UNFIUSDT', 'ROSEUSDT', 'AVAUSDT', 'XEMUSDT', 'SKLUSDT', 'SUSDUSDT', 'GRTUSDT', 'JUVUSDT', 'PSGUSDT',
         '1INCHUSDT','REEFUSDT','OGUSDT', 'ATMUSDT', 'ASRUSDT', 'CELOUSDT', 'RIFUSDT', 'BTCSTUSDT', 'TRUUSDT', 'CKBUSDT',
         'LITUSDT', 'SFPUSDT', 'DODOUSDT', 'CAKEUSDT', 'ACMUSDT', 'BADGERUSDT', 'FISUSDT', 'OMUSDT', 'PONDUSDT', 'DEGOUSDT',
         'ALICEUSDT', 'LINAUSDT', 'PERPUSDT', 'RAMPUSDT', 'SUPERUSDT', 'CFXUSDT', 'EPSUSDT', 'AUTOUSDT', 'TKOUSDT',
         'PUNDIXUSDT', 'TLMUSDT','BTGUSDT', 'MIRUSDT', 'BARUSDT', 'FORTHUSDT', 'BAKEUSDT','TWTUSDT', 'FIROUSDT',
         'BURGERUSDT', 'SLPUSDT', 'SHIBUSDT', 'ICPUSDT', 'ARUSDT', 'POLSUSDT', 'MDXUSDT', 'MASKUSDT', 'LPTUSDT',
         'NUUSDT', 'XVGUSDT', 'ATAUSDT', 'GTCUSDT', 'TORNUSDT', 'KEEPUSDT', 'ERNUSDT', 'KLAYUSDT', 'PHAUSDT', 'BONDUSDT',
         'MLNUSDT', 'DEXEUSDT', 'C98USDT', 'CLVUSDT', 'QNTUSDT', 'FLOWUSDT', 'TVKUSDT', 'MINAUSDT', 'RAYUSDT', 'FARMUSDT',
         'ALPACAUSDT', 'QUICKUSDT', 'MBOXUSDT', 'FORUSDT', 'REQUSDT', 'GHSTUSDT', 'WAXPUSDT', 'TRIBEUSDT', 'GNOUSDT',
         'XECUSDT', 'ELFUSDT', 'DYDXUSDT', 'POLYUSDT', 'IDEXUSDT', 'VIDTUSDT', 'USDPUSDT', 'GALAUSDT', 'ILVUSDT', 'YGGUSDT',
         'SYSUSDT', 'DFUSDT', 'FIDAUSDT', 'FRONTUSDT', 'CVPUSDT', 'AGLDUSDT', 'RADUSDT', 'BETAUSDT', 'RAREUSDT']
def sma(series,timeperiod):
    sum=0
    for i in range(timeperiod):
        sum=sum + float(series[-i-2])
    return sum /timeperiod
Window.size = (700, 400)
volume = []
pairs = []

def breakoutcheck(symbol):
    k_lines = client.get_historical_klines(symbol, Client.KLINE_INTERVAL_1HOUR, "1 day ago UTC")
    # k_lines = client.get_historical_klines(symbol,Client.KLINE_INTERVAL_15MINUTE , "1 day ago UTC")
    i = 0
    while i < 24:
        volume.append(k_lines[i][5])
        i = i+1
    # print(" volume list :   ", volume)
    avg_volume = sma(volume, timeperiod=20)

    if float(volume[-1]) > (10.0*avg_volume):
        # print(symbol, end="  ")
        # pairs.append(symbol)
        return 1
        # print(" avg volume :   ", avg_volume)# print(volume[-3])  # print(volume[-2]) # print("yes!!! volume breakout")
    else:
        # print("n", end=" ")
        return 0
    # return pairs

# sm = ScreenManager()
# screen1 = Screen(name="api_details")
# sm.add_widget(screen1)
# screen2 = Screen(name="congratulations")
# sm.add_widget(screen2)
# sm.add_widget(build(name='kbuild'))

# def build(self):
# class apidetails():
#     def apidetails(self):
#         self.window1 = GridLayout()
#         self.window1.cols = 2
#         self.window1.size_hint = (0.6, 0.7)
#         self.window1.pos_hint = {"center_x": 0.5, "center_y":0.5}
#
#         self.apik= Label(text= "enter api key",font_size= 18,  color= '#00FFCE' )
#         self.window1.add_widget(self.apik)
#
#         self.apis= Label(text= "enter secret api key",font_size= 18,  color= '#00FFCE' )
#         self.window1.add_widget(self.apis)
#
#         self.apikey= TextInput(multiline= False,padding_y=(20,20), size_hint=(1, 0.5)  )
#         self.window1.add_widget(self.apikey)
#
#         self.apisecret= TextInput(multiline= False,padding_y=(20,20), size_hint=(1, 0.5)  )
#         self.window1.add_widget(self.apisecret)
#
#         self.button1= Button(text="OK",size_hint= (1,0.5),bold=True,background_color ='#00FFCE',)
#         self.button1.bind(on_press= sm.switch_to(screen2))
#         self.window1.add_widget(self.button1)
#
#         return self.window1
#
# class connectclient():
#     def connectclient(self):
#         # self.client = Client(self.   apikey, self.apisecret)
#         self.window2 = GridLayout()
#         self.msg = Label(text="Connection established", font_size=18, color='#00FFCE')
#         self.window2.add_widget(self.msg)
#
#         return self.window2

class SayHello(App):
    def build(self):
        #returns a window object with all it's widgets
        # global series
        self.window = GridLayout()
        self.window.cols = 1
        self.window.size_hint = (0.6, 0.7)
        self.window.pos_hint = {"center_x": 0.5, "center_y":0.5}

        # self.pair= Label(text= "Which pair do you want to scan?",font_size= 18,  color= '#00FFCE' )
        # self.window.add_widget(self.pair)

        # self.tf = Label(text="enter the timeframe")
        # self.window.add_widget(self.tf)
        #
        # self.pairname= TextInput(multiline= False,padding_y=(20,20), size_hint=(1, 0.5)  )
        # self.window.add_widget(self.pairname)

        # self.timeframe= TextInput(multiline= False,padding_y=(20,20))
        # self.window.add_widget(self.timeframe)

        self.tf = Label(text="Press SCAN to start scan")
        self.window.add_widget(self.tf)

        self.button2 = Button(text="SCAN",size_hint= (1,0.5),bold=True,background_color ='#00FFCE',)
        # self.button2.bind(on_press= self.callback3())
        self.button2.bind(on_press=lambda x:self.callbackk())
        self.button2.bind(on_release=lambda x:self.callback3())
        # return self.window
        # self.button2.bind(on_press=lambda x:self.callback3())
        self.window.add_widget(self.button2)

        # self.button= Button(text="OK",size_hint= (1,0.5),bold=True,background_color ='#00FFCE',)
        # self.button.bind(on_press=self.callback2)
        # self.window.add_widget(self.button)
        return self.window

        #
        # def callback2(self, instance):
        #     self.tf.text = "sma value is : " + str(sma(series=series,timeperiod=int(self.timeframe.text)))

    def callbackk(self):
        self.tf.text = "scan running......"
        # self.callback3()

    # def callback3(self):
    #     try:
    #         self.tf.text = "breakout status : " + str(breakoutcheck("BTCUSDT"))
    #     except:
    #         self.tf.text ="Invalid symbol"
    #     return 0

    def callback3(self):
        self.button2.disabled= True
        # self.window2 = GridLayout()
        print("scan running......")
        # if 1:
        #     self.tf.text = "scan running ......"
        # except:
        #     pass
        # text = ["scan running"]
        # self.button2.text = str(text)
        # self.status = Label(text="scan running ...")
        # self.window2.add_widget(self.status)

        j = 0
        for j in range(250):
            try:
                if breakoutcheck(tickers[j]) == 1:
                    pairs.append(tickers[j])
                else:
                    pass
            except:
                self.tf.text = "please check your internet connection"
                j = 1
                break

        # self.tf.text = "scan completed......"
        # print("scan completed......\a\a\a")
        # sleep(3)

        # try:
        #     self.tf.text = "scan completed ......"
        # except:
        #     pass

        list_to_str = ''.join(map(str, pairs))

        if pairs == []:
            print("nothing found")
            self.tf.text = "nothing found"
        elif j == 1:
            print("Please check your internet connection")
            self.tf.text = "Please check your internet connection"
        else:
            print(pairs)
            self.tf.text = list_to_str

        self.button2.disabled = False


if __name__ == "__main__":
    SayHello().run()
