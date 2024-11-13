import pandas as pd
import numpy as np
import requests
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter import ttk
import datasource


class Window(ThemedTk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("Stock Analysis")
        #==========STYLE===========
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=('Helvetica',20))
        #==========END style============
        
        #===========RightFrame=============
        rightFrame= ttk.Frame(self)
        ttk.Label(rightFrame,text='走勢分析',style='TopFrame.TLabel').pack()
        rightFrame.pack(side='right')
        #=========RightFrame END===========

        #===========TopFrame=============
        topFrame = ttk.Frame(self)
        ttk.Label(topFrame,text='台積電股票預測',style='TopFrame.TLabel',borderwidth=2,relief='groove').pack()
        ttk.Label(topFrame,text='起始數據: 2020-01-01',style='TopFrame.TLabel',borderwidth=2,relief='groove').pack()

           #=== 分析方法===
        analysisFrame = ttk.Frame(topFrame)
        linear_btn = ttk.Button(analysisFrame,text='線性回歸分析')
        linear_btn.grid(row=0,column=0,padx=5,pady=5)
        linear_btn = ttk.Button(analysisFrame,text='RSI')
        linear_btn.grid(row=0,column=1,padx=5,pady=5)
        linear_btn = ttk.Button(analysisFrame,text='MACD')
        linear_btn.grid(row=1,column=0,padx=5,pady=5)
        linear_btn = ttk.Button(analysisFrame,text='MA')
        linear_btn.grid(row=1,column=1,padx=5,pady=5)

        analysisFrame.pack()

           #=== 分析方法end===
            #===預測分析=====
        resultFrame = ttk.Frame(topFrame)
        ttk.Label(resultFrame,text='預測分析',borderwidth=2,relief='groove').grid()
        ttk.Label(resultFrame,text='明日股價',borderwidth=2,relief='groove').grid(row=0,column=0,padx=5,pady=5)
        result_entry = ttk.Entry(resultFrame)
        
        result_entry.grid(row=0,column=1,padx=5,pady=5)
        resultFrame.pack()
                #=== 預測分析 end===

           


        topFrame.pack(side='left')


        #=========TOPFrame END===========


        #=========bottomFrame ===========
       
        #=========bottomFrame END===========








def main():
    window= Window(theme='arc')
    window.mainloop()


if __name__ == '__main__':
    main()





