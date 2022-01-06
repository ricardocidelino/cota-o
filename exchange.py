import requests
from tkinter import *
from tkinter.ttk import *


def pegarCotacao():
    req = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,GBP-BRL")
    req_dic = req.json()
    cotacao_dolar = req_dic["USDBRL"]["bid"]
    cotacao_euro = req_dic["EURBRL"]["bid"]
    cotacao_btc = req_dic["BTCBRL"]["bid"]
    cotacao_libra= req_dic["GBPBRL"]["bid"]
    # data = datetime.strptime.date(datetime[:-6],"%d%m%Y %h:%m")

    # print(f"Cotação Dólar Atualizada: {cotacao_dolar} {datetime.now()}")
    texto = f'''
    Dólar: R$ {cotacao_dolar[:-2]}
    Euro: R$ {cotacao_euro[:-2]}
    Libra: R$ {cotacao_libra[:-2]}
    Bitcoin: R$ {cotacao_btc},00'''

    textoCotacoes["text"] = texto


wind = Tk()
wind.title("Cotação")
wind['bg'] = 'darkblue'
wind.geometry("250x250")
botao = Button(wind, text="Atualizar Cotações", command=pegarCotacao)
botao.grid(column=100, row=11, padx=40, pady=30)

textoCotacoes = Label(wind, text='')
textoCotacoes.grid(column=100, row=12, padx=30, pady=20)

wind.resizable(False, False)
# wind.iconbitmap('@/home/ricardo/PycharmProjects/exchange.xbm')
wind.mainloop()
