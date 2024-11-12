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

        #=========RightFrame END===========

        #===========TopFrame=============








        #=========TOPFrame END===========
    








def main():
    window= Window(theme='arc')
    window.mainloop()


if __name__ == '__main__':
    main()





