global masa_sayisi
import tkinter
import pandas as pd
from datetime import date
import numpy as np
from tkinter.messagebox import askyesno
from tkinter import *
from PIL import Image, ImageTk
import os
import time
from docx import Document
path = './dosyalar'
try:
    os.mkdir(path)
except:
    pass
masa_sayisi = 0
masas = {}
try:
    menuDf = pd.read_csv('./dosyalar\\menu.csv')
except:
    menuDf = pd.DataFrame(columns=['Ürün', 'Fiyat'])
tk = tkinter.Tk()
ico = Image.open('./dosyalar\\banner.png')
photo = ImageTk.PhotoImage(ico)
tk.wm_iconphoto(False, photo)
menu = []
alınan_odemeler = []
tk.title('Restoran Takip Uygulaması | Made by Turan')
image = Image.open("./dosyalar\\banner.png")
resize_image = image.resize((250, 250))
img = ImageTk.PhotoImage(resize_image)
img_label = tkinter.Label(tk, image=img).place(x=0, y=1500)

class masalar:

    def __init__(self):
        self.orders = pd.DataFrame(columns=['Ürün', 'Fiyat'])

    def aktar_order(self, siparisler, masanum):
        self.orders = siparisler
        masas[masanum].orders.drop(masas[masanum].orders.index, inplace=True)
        onay = tkinter.messagebox.showinfo(title='Masa Aktarımı', message='Masa Aktarımı başarılı!')
        masalar()

    def add_order_bir(self, ürün_numarası, masanum):
        self.orders.loc[len(self.orders)] = menuDf.loc[int(ürün_numarası)]
        masa_menusu_bir(masanum)

    def add_order_eks(self, ürün_numarası, masanum):
        self.orders.loc[len(self.orders)] = menuDf.loc[int(ürün_numarası)]
        masa_menusu_eks(masanum)

    def add_order_goz(self, ürün_numarası, masanum):
        self.orders.loc[len(self.orders)] = menuDf.loc[int(ürün_numarası)]
        masa_menusu_goz(masanum)

    def add_order_tost(self, ürün_numarası, masanum):
        self.orders.loc[len(self.orders)] = menuDf.loc[int(ürün_numarası)]
        masa_menusu_tost(masanum)

    def add_order_sicak(self, ürün_numarası, masanum):
        self.orders.loc[len(self.orders)] = menuDf.loc[int(ürün_numarası)]
        masa_menusu_sicak(masanum)

    def add_order_soguk(self, ürün_numarası, masanum):
        self.orders.loc[len(self.orders)] = menuDf.loc[int(ürün_numarası)]
        masa_menusu_soguk(masanum)

    def show_orders(self):
        return self.orders

    def paying(self):
        for i in range(len(self.orders)):
            alınan_odemeler.append(self.orders.loc[i])
        self.orders.drop(self.orders.index, inplace=True)

    def delete_order(self, urunum):
        self.orders.drop([urunum], inplace=True)
        self.orders.reset_index(drop=True, inplace=True)

def masa_olustur():
    global masa_sayisi
    masa_sayisi = masa_sayisi + 1
    a = f'masa{masa_sayisi}'
    masas[a] = masalar()

def masa_listesi():
    for masa in masas:
        print(f'{masa}')
for i in range(26):
    masa_olustur()
dict_masa = {'masa1': 'Dışarı Sol1', 'masa2': 'Dışarı Sol2', 'masa3': 'Dışarı Sol3', 'masa4': 'Dışarı Orta1', 'masa5': 'Dışarı Orta2', 'masa6': 'Dışarı Orta3', 'masa7': 'Dışarı Sag1', 'masa8': 'Dışarı Sag2', 'masa9': 'Dışarı Sag3', 'masa10': 'İçeri1', 'masa11': 'İçeri2', 'masa12': 'İçeri3', 'masa13': 'İçeri4', 'masa14': 'Loca Cam', 'masa15': 'Loca Bar', 'masa16': 'Üst1', 'masa17': 'Üst2', 'masa18': 'Üst3', 'masa19': 'Üst4', 'masa20': 'Üst5', 'masa21': 'Üst6', 'masa22': 'Üst7', 'masa23': 'Üst8', 'masa24': 'Üst9', 'masa25': 'Üst10', 'masa26': 'Üst11'}

def masalar():
    global d_sol1
    for widget in tk.winfo_children():
        widget.destroy()
    btnback = tkinter.Button(tk, text='Geri', command=main)
    labelmasa = tkinter.Label(tk, text='Masalar').grid(column=1, row=0)
    if len(masas['masa1'].show_orders()) > 0:
        d_sol1 = tkinter.Button(tk, text='Dışarı Sol1', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa1'), bg='#39FF14').grid(column=0, row=1, sticky='N')
    else:
        d_sol1 = tkinter.Button(tk, text='Dışarı Sol1', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa1')).grid(column=0, row=1, sticky='N')
    if len(masas['masa2'].show_orders()) > 0:
        d_sol2 = tkinter.Button(tk, text='Dışarı Sol2', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa2'), bg='#39FF14').grid(column=1, row=1, sticky='N')
    else:
        d_sol2 = tkinter.Button(tk, text='Dışarı Sol2', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa2')).grid(column=1, row=1, sticky='N')
    if len(masas['masa3'].show_orders()) > 0:
        d_sol3 = tkinter.Button(tk, text='Dışarı Sol3', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa3'), bg='#39FF14').grid(column=2, row=1, sticky='N')
    else:
        d_sol3 = tkinter.Button(tk, text='Dışarı Sol3', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa3')).grid(column=2, row=1, sticky='N')
    if len(masas['masa4'].show_orders()) > 0:
        d_orta1 = tkinter.Button(tk, text='Dışarı Orta1', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa4'), bg='#39FF14').grid(column=3, row=1, sticky='N')
    else:
        d_orta1 = tkinter.Button(tk, text='Dışarı Orta1', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa4')).grid(column=3, row=1, sticky='N')
    if len(masas['masa5'].show_orders()) > 0:
        d_orta2 = tkinter.Button(tk, text='Dışarı Orta2', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa5'), bg='#39FF14').grid(column=4, row=1, sticky='N')
    else:
        d_orta2 = tkinter.Button(tk, text='Dışarı Orta2', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa5')).grid(column=4, row=1, sticky='N')
    if len(masas['masa6'].show_orders()) > 0:
        d_orta3 = tkinter.Button(tk, text='Dışarı Orta3', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa6'), bg='#39FF14').grid(column=5, row=1, sticky='N')
    else:
        d_orta3 = tkinter.Button(tk, text='Dışarı Orta3', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa6')).grid(column=5, row=1, sticky='N')
    if len(masas['masa7'].show_orders()) > 0:
        d_sag1 = tkinter.Button(tk, text='Dışarı Sag1', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa7'), bg='#39FF14').grid(column=6, row=1, sticky='N')
    else:
        d_sag1 = tkinter.Button(tk, text='Dışarı Sag1', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa7')).grid(column=6, row=1, sticky='N')
    if len(masas['masa8'].show_orders()) > 0:
        d_sag2 = tkinter.Button(tk, text='Dışarı Sag2', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa8'), bg='#39FF14').grid(column=7, row=1, sticky='N')
    else:
        d_sag2 = tkinter.Button(tk, text='Dışarı Sag2', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa8')).grid(column=7, row=1, sticky='N')
    if len(masas['masa9'].show_orders()) > 0:
        d_sag3 = tkinter.Button(tk, text='Dışarı Sag3', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa9'), bg='#39FF14').grid(column=8, row=1, sticky='N')
    else:
        d_sag3 = tkinter.Button(tk, text='Dışarı Sag3', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa9')).grid(column=8, row=1, sticky='N')
    if len(masas['masa10'].show_orders()) > 0:
        I1 = tkinter.Button(tk, text='İçeri1', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa10'), bg='#39FF14').grid(column=0, row=2, sticky='N')
    else:
        I1 = tkinter.Button(tk, text='İçeri1', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa10')).grid(column=0, row=2, sticky='N')
    if len(masas['masa11'].show_orders()) > 0:
        I2 = tkinter.Button(tk, text='İçeri2', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa11'), bg='#39FF14').grid(column=1, row=2, sticky='N')
    else:
        I2 = tkinter.Button(tk, text='İçeri2', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa11')).grid(column=1, row=2, sticky='N')
    if len(masas['masa12'].show_orders()) > 0:
        I3 = tkinter.Button(tk, text='İçeri3', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa12'), bg='#39FF14').grid(column=2, row=2, sticky='N')
    else:
        I3 = tkinter.Button(tk, text='İçeri3', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa12')).grid(column=2, row=2, sticky='N')
    if len(masas['masa13'].show_orders()) > 0:
        I4 = tkinter.Button(tk, text='İçeri4', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa13'), bg='#39FF14').grid(column=3, row=2, sticky='N')
    else:
        I4 = tkinter.Button(tk, text='İçeri4', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa13')).grid(column=3, row=2, sticky='N')
    if len(masas['masa14'].show_orders()) > 0:
        I_locacam = tkinter.Button(tk, text='Loca Cam', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa14'), bg='#39FF14').grid(column=4, row=2, sticky='N')
    else:
        I_locacam = tkinter.Button(tk, text='Loca Cam', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa14')).grid(column=4, row=2, sticky='N')
    if len(masas['masa15'].show_orders()) > 0:
        I_locabar = tkinter.Button(tk, text='Loca Bar', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa15'), bg='#39FF14').grid(column=5, row=2, sticky='N')
    else:
        I_locabar = tkinter.Button(tk, text='Loca Bar', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa15')).grid(column=5, row=2, sticky='N')
    if len(masas['masa16'].show_orders()) > 0:
        U1 = tkinter.Button(tk, text='Üst1', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa16'), bg='#39FF14').grid(column=0, row=3, sticky='N')
    else:
        U1 = tkinter.Button(tk, text='Üst1', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa16')).grid(column=0, row=3, sticky='N')
    if len(masas['masa17'].show_orders()) > 0:
        U2 = tkinter.Button(tk, text='Üst2', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa17'), bg='#39FF14').grid(column=1, row=3, sticky='N')
    else:
        U2 = tkinter.Button(tk, text='Üst2', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa17')).grid(column=1, row=3, sticky='N')
    if len(masas['masa18'].show_orders()) > 0:
        U3 = tkinter.Button(tk, text='Üst3', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa18'), bg='#39FF14').grid(column=2, row=3, sticky='N')
    else:
        U3 = tkinter.Button(tk, text='Üst3', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa18')).grid(column=2, row=3, sticky='N')
    if len(masas['masa19'].show_orders()) > 0:
        U4 = tkinter.Button(tk, text='Üst4', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa19'), bg='#39FF14').grid(column=3, row=3, sticky='N')
    else:
        U4 = tkinter.Button(tk, text='Üst4', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa19')).grid(column=3, row=3, sticky='N')
    if len(masas['masa20'].show_orders()) > 0:
        U5 = tkinter.Button(tk, text='Üst5', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa20'), bg='#39FF14').grid(column=4, row=3, sticky='N')
    else:
        U5 = tkinter.Button(tk, text='Üst5', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa20')).grid(column=4, row=3, sticky='N')
    if len(masas['masa21'].show_orders()) > 0:
        U6 = tkinter.Button(tk, text='Üst6', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa21'), bg='#39FF14').grid(column=5, row=3, sticky='N')
    else:
        U6 = tkinter.Button(tk, text='Üst6', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa21')).grid(column=5, row=3, sticky='N')
    if len(masas['masa22'].show_orders()) > 0:
        U7 = tkinter.Button(tk, text='Üst7', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa22'), bg='#39FF14').grid(column=6, row=3, sticky='N')
    else:
        U7 = tkinter.Button(tk, text='Üst7', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa22')).grid(column=6, row=3, sticky='N')
    if len(masas['masa23'].show_orders()) > 0:
        U8 = tkinter.Button(tk, text='Üst8', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa23'), bg='#39FF14').grid(column=7, row=3, sticky='N')
    else:
        U8 = tkinter.Button(tk, text='Üst8', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa23')).grid(column=7, row=3, sticky='N')
    if len(masas['masa24'].show_orders()) > 0:
        U9 = tkinter.Button(tk, text='Üst9', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa24'), bg='#39FF14').grid(column=8, row=3, sticky='N')
    else:
        U9 = tkinter.Button(tk, text='Üst9', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa24')).grid(column=8, row=3, sticky='N')
    if len(masas['masa25'].show_orders()) > 0:
        U10 = tkinter.Button(tk, text='Üst10', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa25'), bg='#39FF14').grid(column=9, row=3, sticky='N')
    else:
        U10 = tkinter.Button(tk, text='Üst10', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa25')).grid(column=9, row=3, sticky='N')
    if len(masas['masa26'].show_orders()) > 0:
        U11 = tkinter.Button(tk, text='Üst11', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa26'), bg='#39FF14').grid(column=10, row=3, sticky='N')
    else:
        U11 = tkinter.Button(tk, text='Üst11', cursor='hand2', height=10, width=15, command=lambda: masa_menusu_bir('masa26')).grid(column=10, row=3, sticky='N')
    btnback.grid()

def masa_dolu():
    masa_dolu = tkinter.messagebox.showinfo(title='Masa Aktarımı', message='Seçilen Masa Dolu Aktarma Yapılamaz!')
    masalar()

def sil_update(masanum, x):
    masas[masanum].delete_order(int(x[0]))
    masa_menusu_bir(masanum)

def aktar(masanum):
    aktarılacak_sip = masas[masanum].show_orders().copy()
    for widget in tk.winfo_children():
        widget.destroy()
    btnback = tkinter.Button(tk, text='Geri', command=main)
    labelmasa = tkinter.Label(tk, text='VKS Masalar').grid(column=1, row=0)
    if len(masas['masa1'].show_orders()) > 0:
        d_sol1 = tkinter.Button(tk, text='Dışarı Sol1', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=0, row=1, sticky='N')
    else:
        d_sol1 = tkinter.Button(tk, text='Dışarı Sol1', cursor='hand2', height=10, width=15, command=lambda: masas['masa1'].aktar_order(aktarılacak_sip, masanum)).grid(column=0, row=1, sticky='N')
    if len(masas['masa2'].show_orders()) > 0:
        d_sol2 = tkinter.Button(tk, text='Dışarı Sol2', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=1, row=1, sticky='N')
    else:
        d_sol2 = tkinter.Button(tk, text='Dışarı Sol2', cursor='hand2', height=10, width=15, command=lambda: masas['masa2'].aktar_order(aktarılacak_sip, masanum)).grid(column=1, row=1, sticky='N')
    if len(masas['masa3'].show_orders()) > 0:
        d_sol3 = tkinter.Button(tk, text='Dışarı Sol3', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=2, row=1, sticky='N')
    else:
        d_sol3 = tkinter.Button(tk, text='Dışarı Sol3', cursor='hand2', height=10, width=15, command=lambda: masas['masa3'].aktar_order(aktarılacak_sip, masanum)).grid(column=2, row=1, sticky='N')
    if len(masas['masa4'].show_orders()) > 0:
        d_orta1 = tkinter.Button(tk, text='Dışarı Orta1', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=3, row=1, sticky='N')
    else:
        d_orta1 = tkinter.Button(tk, text='Dışarı Orta1', cursor='hand2', height=10, width=15, command=lambda: masas['masa4'].aktar_order(aktarılacak_sip, masanum)).grid(column=3, row=1, sticky='N')
    if len(masas['masa5'].show_orders()) > 0:
        d_orta2 = tkinter.Button(tk, text='Dışarı Orta2', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=4, row=1, sticky='N')
    else:
        d_orta2 = tkinter.Button(tk, text='Dışarı Orta2', cursor='hand2', height=10, width=15, command=lambda: masas['masa5'].aktar_order(aktarılacak_sip, masanum)).grid(column=4, row=1, sticky='N')
    if len(masas['masa6'].show_orders()) > 0:
        d_orta3 = tkinter.Button(tk, text='Dışarı Orta3', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=5, row=1, sticky='N')
    else:
        d_orta3 = tkinter.Button(tk, text='Dışarı Orta3', cursor='hand2', height=10, width=15, command=lambda: masas['masa6'].aktar_order(aktarılacak_sip, masanum)).grid(column=5, row=1, sticky='N')
    if len(masas['masa7'].show_orders()) > 0:
        d_sag1 = tkinter.Button(tk, text='Dışarı Sag1', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=6, row=1, sticky='N')
    else:
        d_sag1 = tkinter.Button(tk, text='Dışarı Sag1', cursor='hand2', height=10, width=15, command=lambda: masas['masa7'].aktar_order(aktarılacak_sip, masanum)).grid(column=6, row=1, sticky='N')
    if len(masas['masa8'].show_orders()) > 0:
        d_sag2 = tkinter.Button(tk, text='Dışarı Sag2', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=7, row=1, sticky='N')
    else:
        d_sag2 = tkinter.Button(tk, text='Dışarı Sag2', cursor='hand2', height=10, width=15, command=lambda: masas['masa8'].aktar_order(aktarılacak_sip, masanum)).grid(column=7, row=1, sticky='N')
    if len(masas['masa9'].show_orders()) > 0:
        d_sag3 = tkinter.Button(tk, text='Dışarı Sag3', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=8, row=1, sticky='N')
    else:
        d_sag3 = tkinter.Button(tk, text='Dışarı Sag3', cursor='hand2', height=10, width=15, command=lambda: masas['masa9'].aktar_order(aktarılacak_sip, masanum)).grid(column=8, row=1, sticky='N')
    if len(masas['masa10'].show_orders()) > 0:
        I1 = tkinter.Button(tk, text='İçeri1', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=0, row=2, sticky='N')
    else:
        I1 = tkinter.Button(tk, text='İçeri1', cursor='hand2', height=10, width=15, command=lambda: masas['masa10'].aktar_order(aktarılacak_sip, masanum)).grid(column=0, row=2, sticky='N')
    if len(masas['masa11'].show_orders()) > 0:
        I2 = tkinter.Button(tk, text='İçeri2', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=1, row=2, sticky='N')
    else:
        I2 = tkinter.Button(tk, text='İçeri2', cursor='hand2', height=10, width=15, command=lambda: masas['masa11'].aktar_order(aktarılacak_sip, masanum)).grid(column=1, row=2, sticky='N')
    if len(masas['masa12'].show_orders()) > 0:
        I3 = tkinter.Button(tk, text='İçeri3', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=2, row=2, sticky='N')
    else:
        I3 = tkinter.Button(tk, text='İçeri3', cursor='hand2', height=10, width=15, command=lambda: masas['masa12'].aktar_order(aktarılacak_sip, masanum)).grid(column=2, row=2, sticky='N')
    if len(masas['masa13'].show_orders()) > 0:
        I4 = tkinter.Button(tk, text='İçeri4', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=3, row=2, sticky='N')
    else:
        I4 = tkinter.Button(tk, text='İçeri4', cursor='hand2', height=10, width=15, command=lambda: masas['masa13'].aktar_order(aktarılacak_sip, masanum)).grid(column=3, row=2, sticky='N')
    if len(masas['masa14'].show_orders()) > 0:
        I_locacam = tkinter.Button(tk, text='Loca Cam', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=4, row=2, sticky='N')
    else:
        I_locacam = tkinter.Button(tk, text='Loca Cam', cursor='hand2', height=10, width=15, command=lambda: masas['masa14'].aktar_order(aktarılacak_sip, masanum)).grid(column=4, row=2, sticky='N')
    if len(masas['masa15'].show_orders()) > 0:
        I_locabar = tkinter.Button(tk, text='Loca Bar', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=5, row=2, sticky='N')
    else:
        I_locabar = tkinter.Button(tk, text='Loca Bar', cursor='hand2', height=10, width=15, command=lambda: masas['masa15'].aktar_order(aktarılacak_sip, masanum)).grid(column=5, row=2, sticky='N')
    if len(masas['masa16'].show_orders()) > 0:
        U1 = tkinter.Button(tk, text='Üst1', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=0, row=3, sticky='N')
    else:
        U1 = tkinter.Button(tk, text='Üst1', cursor='hand2', height=10, width=15, command=lambda: masas['masa16'].aktar_order(aktarılacak_sip, masanum)).grid(column=0, row=3, sticky='N')
    if len(masas['masa17'].show_orders()) > 0:
        U2 = tkinter.Button(tk, text='Üst2', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=1, row=3, sticky='N')
    else:
        U2 = tkinter.Button(tk, text='Üst2', cursor='hand2', height=10, width=15, command=lambda: masas['masa17'].aktar_order(aktarılacak_sip, masanum)).grid(column=1, row=3, sticky='N')
    if len(masas['masa18'].show_orders()) > 0:
        U3 = tkinter.Button(tk, text='Üst3', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=2, row=3, sticky='N')
    else:
        U3 = tkinter.Button(tk, text='Üst3', cursor='hand2', height=10, width=15, command=lambda: masas['masa18'].aktar_order(aktarılacak_sip, masanum)).grid(column=2, row=3, sticky='N')
    if len(masas['masa19'].show_orders()) > 0:
        U4 = tkinter.Button(tk, text='Üst4', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=3, row=3, sticky='N')
    else:
        U4 = tkinter.Button(tk, text='Üst4', cursor='hand2', height=10, width=15, command=lambda: masas['masa19'].aktar_order(aktarılacak_sip, masanum)).grid(column=3, row=3, sticky='N')
    if len(masas['masa20'].show_orders()) > 0:
        U5 = tkinter.Button(tk, text='Üst5', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=4, row=3, sticky='N')
    else:
        U5 = tkinter.Button(tk, text='Üst5', cursor='hand2', height=10, width=15, command=lambda: masas['masa20'].aktar_order(aktarılacak_sip, masanum)).grid(column=4, row=3, sticky='N')
    if len(masas['masa21'].show_orders()) > 0:
        U6 = tkinter.Button(tk, text='Üst6', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=5, row=3, sticky='N')
    else:
        U6 = tkinter.Button(tk, text='Üst6', cursor='hand2', height=10, width=15, command=lambda: masas['masa21'].aktar_order(aktarılacak_sip, masanum)).grid(column=5, row=3, sticky='N')
    if len(masas['masa22'].show_orders()) > 0:
        U7 = tkinter.Button(tk, text='Üst7', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=6, row=3, sticky='N')
    else:
        U7 = tkinter.Button(tk, text='Üst7', cursor='hand2', height=10, width=15, command=lambda: masas['masa22'].aktar_order(aktarılacak_sip, masanum)).grid(column=6, row=3, sticky='N')
    if len(masas['masa23'].show_orders()) > 0:
        U8 = tkinter.Button(tk, text='Üst8', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=7, row=3, sticky='N')
    else:
        U8 = tkinter.Button(tk, text='Üst8', cursor='hand2', height=10, width=15, command=lambda: masas['masa23'].aktar_order(aktarılacak_sip, masanum)).grid(column=7, row=3, sticky='N')
    if len(masas['masa24'].show_orders()) > 0:
        U9 = tkinter.Button(tk, text='Üst9', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=8, row=3, sticky='N')
    else:
        U9 = tkinter.Button(tk, text='Üst9', cursor='hand2', height=10, width=15, command=lambda: masas['masa24'].aktar_order(aktarılacak_sip, masanum)).grid(column=8, row=3, sticky='N')
    if len(masas['masa25'].show_orders()) > 0:
        U10 = tkinter.Button(tk, text='Üst10', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=9, row=3, sticky='N')
    else:
        U10 = tkinter.Button(tk, text='Üst10', cursor='hand2', height=10, width=15, command=lambda: masas['masa25'].aktar_order(aktarılacak_sip, masanum)).grid(column=9, row=3, sticky='N')
    if len(masas['masa26'].show_orders()) > 0:
        U11 = tkinter.Button(tk, text='Üst11', cursor='hand2', height=10, width=15, command=lambda: masa_dolu(), bg='#39FF14').grid(column=10, row=3, sticky='N')
    else:
        U11 = tkinter.Button(tk, text='Üst11', cursor='hand2', height=10, width=15, command=lambda: masas['masa26'].aktar_order(aktarılacak_sip, masanum)).grid(column=10, row=3, sticky='N')
    btnback.grid()

def yazdır(masanum, toplamtutar):
    df_yaz = masas[masanum].show_orders().copy()
    df_yaz.loc[len(df_yaz)] = ['Toplam:', f'{toplamtutar}TL']
    df_yaz.loc[len(df_yaz)] = [dict_masa[masanum], ' ']
    df_str = df_yaz.to_string(header=False, index=False)
    document = Document()
    document.add_paragraph(df_str)
    document.save('./dosyalar\\siparis.docx')
    os.startfile('./dosyalar\\siparis.docx', 'print')
    time.sleep(5)
    os.remove('./dosyalar\\siparis.docx')

def masa_menusu_bir(masanum):
    global siparislist
    for widget in tk.winfo_children():
        widget.destroy()
    #img_label = tkinter.Label(tk, image=img).place(x=0, y=0)
    btnback = tkinter.Button(tk, text='Geri', command=masalar).grid(column=2, row=10)
    labelmasa = tkinter.Label(tk, text=f'{dict_masa[masanum]}').grid(column=0, row=0)
    btn_kahvaltılar = tkinter.Button(tk, text='Kahvaltılar', command=lambda: masa_menusu_bir(masanum), height=3, width=20).grid(column=0, row=1, padx=10, sticky='S')
    btn_Ekstralar = tkinter.Button(tk, text='Ekstralar', command=lambda: masa_menusu_eks(masanum), height=3, width=20).grid(column=0, row=2, padx=10)
    btn_Gozlemeler = tkinter.Button(tk, text='Gözlemeler', command=lambda: masa_menusu_goz(masanum), height=3, width=20).grid(column=0, row=3, padx=10)
    btn_Tost = tkinter.Button(tk, text='Tostlar', command=lambda: masa_menusu_tost(masanum), height=3, width=20).grid(column=0, row=4, padx=10)
    btn_sicak = tkinter.Button(tk, text='Sıcak İçecekler', command=lambda: masa_menusu_sicak(masanum), height=3, width=20).grid(column=0, row=5, padx=10)
    btn_soguk = tkinter.Button(tk, text='Soğuk İçecekler', command=lambda: masa_menusu_soguk(masanum), height=3, width=20).grid(column=0, row=6, padx=10)
    btn_bir = tkinter.Button(tk, text='Spesiyal Kahvaltı', command=lambda: masas[masanum].add_order_bir(menuDf.index[0], masanum), height=3, width=20).grid(column=2, row=1, sticky='S')
    btn_iki = tkinter.Button(tk, text='Vip Kahvlatı', command=lambda: masas[masanum].add_order_bir(menuDf.index[1], masanum), height=3, width=20).grid(column=2, row=2)
    btn_uc = tkinter.Button(tk, text='Van Kahvaltısı', command=lambda: masas[masanum].add_order_bir(menuDf.index[2], masanum), height=3, width=20).grid(column=2, row=3)
    btn_dort = tkinter.Button(tk, text='Köy Kahvaltısı', command=lambda: masas[masanum].add_order_bir(menuDf.index[3], masanum), height=3, width=20).grid(column=2, row=4)
    btn_bes = tkinter.Button(tk, text='Karadeniz Kahvaltısı', command=lambda: masas[masanum].add_order_bir(menuDf.index[4], masanum), height=3, width=20).grid(column=2, row=5)
    btn_alti = tkinter.Button(tk, text='Akdeniz Kahvaltısı', command=lambda: masas[masanum].add_order_bir(menuDf.index[5], masanum), height=3, width=20).grid(column=2, row=6)
    btn_yedi = tkinter.Button(tk, text='Kahvaltı Tabağı', command=lambda: masas[masanum].add_order_bir(menuDf.index[6], masanum), height=3, width=20).grid(column=2, row=7)
    btn_yedi = tkinter.Button(tk, text='Ek Servis', command=lambda: masas[masanum].add_order_bir(menuDf.index[51], masanum), height=3, width=20).grid(column=2, row=8)
    siparislist = tkinter.Listbox(height=10, width=35)
    siparisler = pd.DataFrame(columns=['Ürün', 'Fiyat'])
    siparisler = masas[masanum].show_orders()
    a = 0
    for i in range(len(siparisler)):
        eleman = f'{a}-{siparisler.iloc[a, 0]} : {siparisler.iloc[a, 1]}'
        siparislist.insert(a, eleman)
        a += 1
    labelsiparisler = tkinter.Label(text='Masanın Siparişleri:').grid(column=3, row=0)
    siparislist.grid(column=3, row=1, sticky='E', padx=10)
    toplamtutar = 0
    for i in range(len(siparisler)):
        toplamtutar = toplamtutar + siparisler.iloc[i, 1]
    tutar_label = tkinter.Label(tk, text=f'Toplam Tutar: {toplamtutar}TL').grid(column=3, row=2, sticky='N')
    odeme = tkinter.Button(tk, text='Ödeme', cursor='hand2', command=lambda: odeme_al(masanum, toplamtutar), height=3, width=20).grid(column=3, row=4)
    siparistensil = tkinter.Button(tk, text='Sil', command=lambda: sil_update(masanum, siparislist.curselection()), height=3, width=20).grid(column=3, row=3)
    btnYazdır = tkinter.Button(tk, text='Siparişi Yazdır', command=lambda: yazdır(masanum, toplamtutar), height=3, width=20).grid(column=3, row=5)
    btn_aktar = tkinter.Button(tk, text='Masa Aktar', command=lambda: aktar(masanum), height=3, width=20).grid(column=3, row=6)

def masa_menusu_eks(masanum):
    global siparislist
    for widget in tk.winfo_children():
        widget.destroy()
    #img_label = tkinter.Label(tk, image=img).place(x=0, y=0)
    btnback = tkinter.Button(tk, text='Geri', command=masalar).grid(column=2, row=10)
    labelmasa = tkinter.Label(tk, text=f'{dict_masa[masanum]}').grid(column=0, row=0)
    btn_kahvaltılar = tkinter.Button(tk, text='Kahvaltılar', command=lambda: masa_menusu_bir(masanum), height=3, width=20).grid(column=0, row=1, padx=10, sticky='S')
    btn_Ekstralar = tkinter.Button(tk, text='Ekstralar', command=lambda: masa_menusu_eks(masanum), height=3, width=20).grid(column=0, row=2, padx=10)
    btn_Gozlemeler = tkinter.Button(tk, text='Gözlemeler', command=lambda: masa_menusu_goz(masanum), height=3, width=20).grid(column=0, row=3, padx=10)
    btn_Tost = tkinter.Button(tk, text='Tostlar', command=lambda: masa_menusu_tost(masanum), height=3, width=20).grid(column=0, row=4, padx=10)
    btn_sicak = tkinter.Button(tk, text='Sıcak İçecekler', command=lambda: masa_menusu_sicak(masanum), height=3, width=20).grid(column=0, row=5, padx=10)
    btn_soguk = tkinter.Button(tk, text='Soğuk İçecekler', command=lambda: masa_menusu_soguk(masanum), height=3, width=20).grid(column=0, row=6, padx=10)
    btn_bir = tkinter.Button(tk, text='Kuymak', command=lambda: masas[masanum].add_order_eks(menuDf.index[7], masanum), height=3, width=20).grid(column=2, row=1, sticky='S')
    btn_iki = tkinter.Button(tk, text='Kavurmalı Yumurta', command=lambda: masas[masanum].add_order_eks(menuDf.index[8], masanum), height=3, width=20).grid(column=2, row=2)
    btn_uc = tkinter.Button(tk, text='Sucuklu Yumurta', command=lambda: masas[masanum].add_order_eks(menuDf.index[9], masanum), height=3, width=20).grid(column=2, row=3)
    btn_dort = tkinter.Button(tk, text='Sucuk Kızartma', command=lambda: masas[masanum].add_order_eks(menuDf.index[10], masanum), height=3, width=20).grid(column=2, row=4)
    btn_bes = tkinter.Button(tk, text='Sucuk İçi', command=lambda: masas[masanum].add_order_eks(menuDf.index[11], masanum), height=3, width=20).grid(column=2, row=5)
    btn_alti = tkinter.Button(tk, text='Salça Soslu Sosis', command=lambda: masas[masanum].add_order_eks(menuDf.index[12], masanum), height=3, width=20).grid(column=2, row=6)
    btn_yedi = tkinter.Button(tk, text='Peynirli Yumurta', command=lambda: masas[masanum].add_order_eks(menuDf.index[13], masanum), height=3, width=20).grid(column=2, row=7)
    btn_sekiz = tkinter.Button(tk, text='Kaşarlı Menemen', command=lambda: masas[masanum].add_order_eks(menuDf.index[14], masanum), height=3, width=20).grid(column=2, row=8)
    btn_Dokuz = tkinter.Button(tk, text='Yumurta Kapama', command=lambda: masas[masanum].add_order_eks(menuDf.index[15], masanum), height=3, width=20).grid(column=2, row=9)
    btn_Dokuz = tkinter.Button(tk, text='Omlet', command=lambda: masas[masanum].add_order_eks(menuDf.index[16], masanum), height=3, width=20).grid(column=3, row=1, sticky='S')
    btn_Dokuz = tkinter.Button(tk, text='Sebzeli Omlet', command=lambda: masas[masanum].add_order_eks(menuDf.index[17], masanum), height=3, width=20).grid(column=3, row=2)
    btn_Dokuz = tkinter.Button(tk, text='Sahanda Yumurta', command=lambda: masas[masanum].add_order_eks(menuDf.index[18], masanum), height=3, width=20).grid(column=3, row=3)
    btn_Dokuz = tkinter.Button(tk, text='Sigara Böreği', command=lambda: masas[masanum].add_order_eks(menuDf.index[19], masanum), height=3, width=20).grid(column=3, row=4)
    btn_Dokuz = tkinter.Button(tk, text='Paçanga Böreği', command=lambda: masas[masanum].add_order_eks(menuDf.index[20], masanum), height=3, width=20).grid(column=3, row=5)
    btn_Dokuz = tkinter.Button(tk, text='Kavurmalı Kaş. Gözleme Ex', command=lambda: masas[masanum].add_order_eks(menuDf.index[21], masanum), height=3, width=20).grid(column=3, row=6)
    btn_Dokuz = tkinter.Button(tk, text='Sucuk Kaş. Gözleme Ex', command=lambda: masas[masanum].add_order_eks(menuDf.index[22], masanum), height=3, width=20).grid(column=3, row=7)
    btn_Dokuz = tkinter.Button(tk, text='Peynirli Gözleme Ex', command=lambda: masas[masanum].add_order_eks(menuDf.index[23], masanum), height=3, width=20).grid(column=3, row=8)
    btn_Dokuz = tkinter.Button(tk, text='Sebzeli Gözleme Ex', command=lambda: masas[masanum].add_order_eks(menuDf.index[24], masanum), height=3, width=20).grid(column=3, row=9)
    btn_Dokuz = tkinter.Button(tk, text='Patatesli Gözleme Ex', command=lambda: masas[masanum].add_order_eks(menuDf.index[25], masanum), height=3, width=20).grid(column=4, row=1, sticky='S')
    btn_Dokuz = tkinter.Button(tk, text='Kavurma Kaş. Tost Ex', command=lambda: masas[masanum].add_order_eks(menuDf.index[26], masanum), height=3, width=20).grid(column=4, row=2)
    btn_Dokuz = tkinter.Button(tk, text='Sucuk Kaş. Tost Ex', command=lambda: masas[masanum].add_order_eks(menuDf.index[27], masanum), height=3, width=20).grid(column=4, row=3)
    btn_Dokuz = tkinter.Button(tk, text='Kaşarlı Tost Ex', command=lambda: masas[masanum].add_order_eks(menuDf.index[28], masanum), height=3, width=20).grid(column=4, row=4)
    btn_Dokuz = tkinter.Button(tk, text='Kızartma Tabağı', command=lambda: masas[masanum].add_order_eks(menuDf.index[29], masanum), height=3, width=20).grid(column=4, row=5)
    btn_Dokuz = tkinter.Button(tk, text='Domates Soslu Kızartma', command=lambda: masas[masanum].add_order_eks(menuDf.index[30], masanum), height=3, width=20).grid(column=4, row=6)
    btn_Dokuz = tkinter.Button(tk, text='Menemen', command=lambda: masas[masanum].add_order_eks(menuDf.index[50], masanum), height=3, width=20).grid(column=4, row=7)
    siparislist = tkinter.Listbox(height=10, width=35)
    siparisler = pd.DataFrame(columns=['Ürün', 'Fiyat'])
    siparisler = masas[masanum].show_orders()
    a = 0
    for i in range(len(siparisler)):
        eleman = f'{a}-{siparisler.iloc[a, 0]} : {siparisler.iloc[a, 1]}'
        siparislist.insert(a, eleman)
        a += 1
    labelsiparisler = tkinter.Label(text='Masanın Siparişleri:').grid(column=5, row=0)
    siparislist.grid(column=5, row=1, sticky='N', padx=10)
    toplamtutar = 0
    for i in range(len(siparisler)):
        toplamtutar = toplamtutar + siparisler.iloc[i, 1]
    tutar_label = tkinter.Label(tk, text=f'Toplam Tutar: {toplamtutar}TL').grid(column=5, row=2, sticky='N')
    odeme = tkinter.Button(tk, text='Ödeme', cursor='hand2', command=lambda: odeme_al(masanum, toplamtutar), height=3, width=20).grid(column=5, row=4)
    siparistensil = tkinter.Button(tk, text='Sil', command=lambda: sil_update(masanum, siparislist.curselection()), height=3, width=20).grid(column=5, row=3)
    btnYazdır = tkinter.Button(tk, text='Siparişi Yazdır', command=lambda: yazdır(masanum, toplamtutar), height=3, width=20).grid(column=5, row=5)

def masa_menusu_goz(masanum):
    global siparislist
    for widget in tk.winfo_children():
        widget.destroy()
    #img_label = tkinter.Label(tk, image=img).place(x=0, y=0)
    btnback = tkinter.Button(tk, text='Geri', command=masalar).grid(column=2, row=10)
    labelmasa = tkinter.Label(tk, text=f'{dict_masa[masanum]}').grid(column=0, row=0)
    btn_kahvaltılar = tkinter.Button(tk, text='Kahvaltılar', command=lambda: masa_menusu_bir(masanum), height=3, width=20).grid(column=0, row=1, padx=10, sticky='S')
    btn_Ekstralar = tkinter.Button(tk, text='Ekstralar', command=lambda: masa_menusu_eks(masanum), height=3, width=20).grid(column=0, row=2, padx=10)
    btn_Gozlemeler = tkinter.Button(tk, text='Gözlemeler', command=lambda: masa_menusu_goz(masanum), height=3, width=20).grid(column=0, row=3, padx=10)
    btn_Tost = tkinter.Button(tk, text='Tostlar', command=lambda: masa_menusu_tost(masanum), height=3, width=20).grid(column=0, row=4, padx=10)
    btn_sicak = tkinter.Button(tk, text='Sıcak İçecekler', command=lambda: masa_menusu_sicak(masanum), height=3, width=20).grid(column=0, row=5, padx=10)
    btn_soguk = tkinter.Button(tk, text='Soğuk İçecekler', command=lambda: masa_menusu_soguk(masanum), height=3, width=20).grid(column=0, row=6, padx=10)
    btn_bir = tkinter.Button(tk, text='Kavurmalı Kaş. Gözleme Menü', command=lambda: masas[masanum].add_order_goz(menuDf.index[31], masanum), height=3, width=25).grid(column=2, row=1, sticky='S')
    btn_iki = tkinter.Button(tk, text='Sucuklu Kaş. Gözleme Menü', command=lambda: masas[masanum].add_order_goz(menuDf.index[32], masanum), height=3, width=25).grid(column=2, row=2)
    btn_uc = tkinter.Button(tk, text='Peynirli Gözleme Menü', command=lambda: masas[masanum].add_order_goz(menuDf.index[33], masanum), height=3, width=25).grid(column=2, row=3)
    btn_dort = tkinter.Button(tk, text='Sebzeli Kaş. Gözleme Menü', command=lambda: masas[masanum].add_order_goz(menuDf.index[34], masanum), height=3, width=25).grid(column=2, row=4)
    btn_bes = tkinter.Button(tk, text='Patatesli Gözleme Menü', command=lambda: masas[masanum].add_order_goz(menuDf.index[35], masanum), height=3, width=25).grid(column=2, row=5)
    siparislist = tkinter.Listbox(height=10, width=35)
    siparisler = pd.DataFrame(columns=['Ürün', 'Fiyat'])
    siparisler = masas[masanum].show_orders()
    a = 0
    for i in range(len(siparisler)):
        eleman = f'{a}-{siparisler.iloc[a, 0]} : {siparisler.iloc[a, 1]}'
        siparislist.insert(a, eleman)
        a += 1
    labelsiparisler = tkinter.Label(text='Masanın Siparişleri:').grid(column=3, row=0)
    siparislist.grid(column=3, row=1, sticky='N', padx=10)
    toplamtutar = 0
    for i in range(len(siparisler)):
        toplamtutar = toplamtutar + siparisler.iloc[i, 1]
    tutar_label = tkinter.Label(tk, text=f'Toplam Tutar: {toplamtutar}TL').grid(column=3, row=2, sticky='N')
    odeme = tkinter.Button(tk, text='Ödeme', cursor='hand2', command=lambda: odeme_al(masanum, toplamtutar), height=3, width=20).grid(column=3, row=4)
    siparistensil = tkinter.Button(tk, text='Sil', command=lambda: sil_update(masanum, siparislist.curselection()), height=3, width=20).grid(column=3, row=3)
    btnYazdır = tkinter.Button(tk, text='Siparişi Yazdır', command=lambda: yazdır(masanum, toplamtutar), height=3, width=20).grid(column=3, row=5)

def masa_menusu_tost(masanum):
    global siparislist
    for widget in tk.winfo_children():
        widget.destroy()
    #img_label = tkinter.Label(tk, image=img).place(x=0, y=0)
    btnback = tkinter.Button(tk, text='Geri', command=masalar).grid(column=2, row=10)
    labelmasa = tkinter.Label(tk, text=f'{dict_masa[masanum]}').grid(column=0, row=0)
    btn_kahvaltılar = tkinter.Button(tk, text='Kahvaltılar', command=lambda: masa_menusu_bir(masanum), height=3, width=20).grid(column=0, row=1, padx=10, sticky='S')
    btn_Ekstralar = tkinter.Button(tk, text='Ekstralar', command=lambda: masa_menusu_eks(masanum), height=3, width=20).grid(column=0, row=2, padx=10)
    btn_Gozlemeler = tkinter.Button(tk, text='Gözlemeler', command=lambda: masa_menusu_goz(masanum), height=3, width=20).grid(column=0, row=3, padx=10)
    btn_Tost = tkinter.Button(tk, text='Tostlar', command=lambda: masa_menusu_tost(masanum), height=3, width=20).grid(column=0, row=4, padx=10)
    btn_sicak = tkinter.Button(tk, text='Sıcak İçecekler', command=lambda: masa_menusu_sicak(masanum), height=3, width=20).grid(column=0, row=5, padx=10)
    btn_soguk = tkinter.Button(tk, text='Soğuk İçecekler', command=lambda: masa_menusu_soguk(masanum), height=3, width=20).grid(column=0, row=6, padx=10)
    btn_bir = tkinter.Button(tk, text='Kavurmalı Kaş. Tost Menü', command=lambda: masas[masanum].add_order_tost(menuDf.index[36], masanum), height=3, width=20).grid(column=2, row=1, sticky='S')
    btn_iki = tkinter.Button(tk, text='Sucuklu Kaş. Tost Menü', command=lambda: masas[masanum].add_order_tost(menuDf.index[37], masanum), height=3, width=20).grid(column=2, row=2)
    btn_uc = tkinter.Button(tk, text='Sebzeli Tost Menü', command=lambda: masas[masanum].add_order_tost(menuDf.index[38], masanum), height=3, width=20).grid(column=2, row=3)
    btn_dort = tkinter.Button(tk, text='Kaşarlı Tost Menü', command=lambda: masas[masanum].add_order_tost(menuDf.index[39], masanum), height=3, width=20).grid(column=2, row=4)
    siparislist = tkinter.Listbox(height=10, width=35)
    siparisler = pd.DataFrame(columns=['Ürün', 'Fiyat'])
    siparisler = masas[masanum].show_orders()
    a = 0
    for i in range(len(siparisler)):
        eleman = f'{a}-{siparisler.iloc[a, 0]} : {siparisler.iloc[a, 1]}'
        siparislist.insert(a, eleman)
        a += 1
    labelsiparisler = tkinter.Label(text='Masanın Siparişleri:').grid(column=3, row=0)
    siparislist.grid(column=3, row=1, sticky='N', padx=10)
    toplamtutar = 0
    for i in range(len(siparisler)):
        toplamtutar = toplamtutar + siparisler.iloc[i, 1]
    tutar_label = tkinter.Label(tk, text=f'Toplam Tutar: {toplamtutar}TL').grid(column=3, row=2, sticky='N')
    odeme = tkinter.Button(tk, text='Ödeme', cursor='hand2', command=lambda: odeme_al(masanum, toplamtutar), height=3, width=20).grid(column=3, row=4)
    siparistensil = tkinter.Button(tk, text='Sil', command=lambda: sil_update(masanum, siparislist.curselection()), height=3, width=20).grid(column=3, row=3)
    btnYazdır = tkinter.Button(tk, text='Siparişi Yazdır', command=lambda: yazdır(masanum, toplamtutar), height=3, width=20).grid(column=3, row=5)

def masa_menusu_sicak(masanum):
    global siparislist
    for widget in tk.winfo_children():
        widget.destroy()
    #img_label = tkinter.Label(tk, image=img).place(x=0, y=0)
    btnback = tkinter.Button(tk, text='Geri', command=masalar).grid(column=2, row=10)
    labelmasa = tkinter.Label(tk, text=f'{dict_masa[masanum]}').grid(column=0, row=0)
    btn_kahvaltılar = tkinter.Button(tk, text='Kahvaltılar', command=lambda: masa_menusu_bir(masanum), height=3, width=20).grid(column=0, row=1, padx=10, sticky='S')
    btn_Ekstralar = tkinter.Button(tk, text='Ekstralar', command=lambda: masa_menusu_eks(masanum), height=3, width=20).grid(column=0, row=2, padx=10)
    btn_Gozlemeler = tkinter.Button(tk, text='Gözlemeler', command=lambda: masa_menusu_goz(masanum), height=3, width=20).grid(column=0, row=3, padx=10)
    btn_Tost = tkinter.Button(tk, text='Tostlar', command=lambda: masa_menusu_tost(masanum), height=3, width=20).grid(column=0, row=4, padx=10)
    btn_sicak = tkinter.Button(tk, text='Sıcak İçecekler', command=lambda: masa_menusu_sicak(masanum), height=3, width=20).grid(column=0, row=5, padx=10)
    btn_soguk = tkinter.Button(tk, text='Soğuk İçecekler', command=lambda: masa_menusu_soguk(masanum), height=3, width=20).grid(column=0, row=6, padx=10)
    btn_bir = tkinter.Button(tk, text='Çay', command=lambda: masas[masanum].add_order_sicak(menuDf.index[40], masanum), height=3, width=20).grid(column=2, row=1, sticky='S')
    btn_iki = tkinter.Button(tk, text='Bitki Çayı', command=lambda: masas[masanum].add_order_sicak(menuDf.index[41], masanum), height=3, width=20).grid(column=2, row=2)
    btn_uc = tkinter.Button(tk, text='Sahlep-Sıcak Çikolata', command=lambda: masas[masanum].add_order_sicak(menuDf.index[42], masanum), height=3, width=20).grid(column=2, row=3)
    btn_dort = tkinter.Button(tk, text='Termos Çay', command=lambda: masas[masanum].add_order_sicak(menuDf.index[43], masanum), height=3, width=20).grid(column=2, row=4)
    btn_dort = tkinter.Button(tk, text='Kahve Çeşitleri', command=lambda: masas[masanum].add_order_sicak(menuDf.index[44], masanum), height=3, width=20).grid(column=2, row=4)
    siparislist = tkinter.Listbox(height=10, width=35)
    siparisler = pd.DataFrame(columns=['Ürün', 'Fiyat'])
    siparisler = masas[masanum].show_orders()
    a = 0
    for i in range(len(siparisler)):
        eleman = f'{a}-{siparisler.iloc[a, 0]} : {siparisler.iloc[a, 1]}'
        siparislist.insert(a, eleman)
        a += 1
    labelsiparisler = tkinter.Label(text='Masanın Siparişleri:').grid(column=3, row=0)
    siparislist.grid(column=3, row=1, sticky='N', padx=10)
    toplamtutar = 0
    for i in range(len(siparisler)):
        toplamtutar = toplamtutar + siparisler.iloc[i, 1]
    tutar_label = tkinter.Label(tk, text=f'Toplam Tutar: {toplamtutar}TL').grid(column=3, row=2, sticky='N')
    odeme = tkinter.Button(tk, text='Ödeme', cursor='hand2', command=lambda: odeme_al(masanum, toplamtutar), height=3, width=20).grid(column=3, row=4)
    siparistensil = tkinter.Button(tk, text='Sil', command=lambda: sil_update(masanum, siparislist.curselection()), height=3, width=20).grid(column=3, row=3)
    btnYazdır = tkinter.Button(tk, text='Siparişi Yazdır', command=lambda: yazdır(masanum, toplamtutar), height=3, width=20).grid(column=3, row=5)

def masa_menusu_soguk(masanum):
    global siparislist
    for widget in tk.winfo_children():
        widget.destroy()
    #img_label = tkinter.Label(tk, image=img).place(x=0, y=0)
    btnback = tkinter.Button(tk, text='Geri', command=masalar).grid(column=2, row=10)
    labelmasa = tkinter.Label(tk, text=f'{dict_masa[masanum]}').grid(column=0, row=0)
    btn_kahvaltılar = tkinter.Button(tk, text='Kahvaltılar', command=lambda: masa_menusu_bir(masanum), height=3, width=20).grid(column=0, row=1, padx=10, sticky='S')
    btn_Ekstralar = tkinter.Button(tk, text='Ekstralar', command=lambda: masa_menusu_eks(masanum), height=3, width=20).grid(column=0, row=2, padx=10)
    btn_Gozlemeler = tkinter.Button(tk, text='Gözlemeler', command=lambda: masa_menusu_goz(masanum), height=3, width=20).grid(column=0, row=3, padx=10)
    btn_Tost = tkinter.Button(tk, text='Tostlar', command=lambda: masa_menusu_tost(masanum), height=3, width=20).grid(column=0, row=4, padx=10)
    btn_sicak = tkinter.Button(tk, text='Sıcak İçecekler', command=lambda: masa_menusu_sicak(masanum), height=3, width=20).grid(column=0, row=5, padx=10)
    btn_soguk = tkinter.Button(tk, text='Soğuk İçecekler', command=lambda: masa_menusu_soguk(masanum), height=3, width=20).grid(column=0, row=6, padx=10)
    btn_bir = tkinter.Button(tk, text='Su', command=lambda: masas[masanum].add_order_soguk(menuDf.index[45], masanum), height=3, width=20).grid(column=2, row=1, sticky='S')
    btn_iki = tkinter.Button(tk, text='Maden Suyu', command=lambda: masas[masanum].add_order_soguk(menuDf.index[46], masanum), height=3, width=20).grid(column=2, row=2)
    btn_uc = tkinter.Button(tk, text='Meyve S.-Soğuk Çay', command=lambda: masas[masanum].add_order_soguk(menuDf.index[47], masanum), height=3, width=20).grid(column=2, row=3)
    btn_dort = tkinter.Button(tk, text='Portakal Suyu-Vb.', command=lambda: masas[masanum].add_order_soguk(menuDf.index[48], masanum), height=3, width=20).grid(column=2, row=4)
    siparislist = tkinter.Listbox(height=10, width=35)
    siparisler = pd.DataFrame(columns=['Ürün', 'Fiyat'])
    siparisler = masas[masanum].show_orders()
    a = 0
    for i in range(len(siparisler)):
        eleman = f'{a}-{siparisler.iloc[a, 0]} : {siparisler.iloc[a, 1]}'
        siparislist.insert(a, eleman)
        a += 1
    labelsiparisler = tkinter.Label(text='Masanın Siparişleri:').grid(column=3, row=0)
    siparislist.grid(column=3, row=1, sticky='N', padx=10)
    toplamtutar = 0
    for i in range(len(siparisler)):
        toplamtutar = toplamtutar + siparisler.iloc[i, 1]
    tutar_label = tkinter.Label(tk, text=f'Toplam Tutar: {toplamtutar}TL').grid(column=3, row=2, sticky='N')
    odeme = tkinter.Button(tk, text='Ödeme', cursor='hand2', command=lambda: odeme_al(masanum, toplamtutar), height=3, width=20).grid(column=3, row=4)
    siparistensil = tkinter.Button(tk, text='Sil', command=lambda: sil_update(masanum, siparislist.curselection()), height=3, width=20).grid(column=3, row=3)
    btnYazdır = tkinter.Button(tk, text='Siparişi Yazdır', command=lambda: yazdır(masanum, toplamtutar), height=3, width=20).grid(column=3, row=5)

def odeme_al(masanum, toplam):
    onay = askyesno(title='Ödeme Onayı', message='Ödeme alındı mı ?')
    if onay:
        masas[masanum].paying()
        siparislist.delete(0, END)
        date1 = str(date.today())
        df = pd.DataFrame(data=alınan_odemeler)
        df_pivot = df.pivot_table(index=['Ürün'], aggfunc='size')
        df_pivot.loc[len(df)] = sum(df['Fiyat'])
        df_pivot.to_excel(f'./dosyalar\\VKS_kazanc_{date1}.xlsx')
    masa_menusu_bir(masanum)

def menu():
    for widget in tk.winfo_children():
        widget.destroy()
    img_label = tkinter.Label(tk, image=img).place(x=0, y=0)
    btnback = tkinter.Button(tk, text='Geri', command=main)
    menulist = tkinter.Listbox(height=40, width=35)
    urunler = menuDf['Ürün'].values
    fiyatlar = menuDf['Fiyat'].values
    a = 0
    for i in range(len(menuDf)):
        eleman = f'{a}-{urunler[a]} : {fiyatlar[a]}'
        menulist.insert(a, eleman)
        a += 1
    menulist.pack()
    btnback.pack(in_=tk, anchor='center')

def kazanc():
    for widget in tk.winfo_children():
        widget.destroy()
    df = pd.DataFrame(data=alınan_odemeler)
    img_label = tkinter.Label(tk, image=img).place(x=0, y=0)
    btnback = tkinter.Button(tk, text='Geri', command=main).pack(in_=tk, anchor='center')
    kazanc_label = tkinter.Label(tk, text=f"Günlük Kazanç :\n {sum(df['Fiyat'])}TL").pack()

def kapat():
    onay = askyesno(title='Uyarı!!!', message='Gün Sonu Gelmeden Kapatmayın!!\n Not:Gün sonu gelmeden kapatmak veri kaybına yol açar!!!\nKapatmak istiyor musunuz ?')
    if onay:
        tk.destroy()

def main():
    w, h = (tk.winfo_screenwidth(), tk.winfo_screenheight())
    tk.geometry('%dx%d+0+0' % (w, h))
    for widget in tk.winfo_children():
        widget.destroy()
    img_label = tkinter.Label(tk, image=img).place(x=0, y=0)
    labelgiris = tkinter.Label(tk, text='X Restoranı Sipariş Takip').grid(column=1, row=0, sticky='NS', padx=750)
    btn2 = tkinter.Button(tk, text='Menüyü Göster', cursor='hand2', height=3, width=20, command=menu).grid(column=1, row=2)
    btnkapat = tkinter.Button(tk, text='Kapat', command=kapat)
    btn4 = tkinter.Button(tk, text='Masalar', cursor='hand2', height=3, width=20, command=masalar).grid(column=1, row=4)
    btn5 = tkinter.Button(tk, text='Günlük Kazanç', height=3, width=20, cursor='hand2', command=kazanc).grid(column=1, row=5)
    btnkapat.grid(column=1, row=6)
main()
tk.mainloop()