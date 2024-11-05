from tkinter import ttk
import tkinter as tk

class SitenameFrame(ttk.Frame):
    """
    SitenameFrame 主要是提供一個自訂的Frame,當使用者選取城市時，必須要建立對應的SitenameFrame

    SitenameFrame 內會使用checkbox_widget,提供給使用者勾選站點
    
    """
    def __init__(self,master=None,sitenames:list[str]=None,**kwargs):
        super().__init__(master=master, **kwargs)
        #欄寬度的權重
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1,weight=1)
        self.selected_radio = tk.StringVar() #負責取得使用者選取資料
        for idx,value in enumerate(sitenames):
            column = idx %2
            index = int(idx/2)
            ttk.Radiobutton(self, text=value, value=value, variable=self.selected_radio,command=self.radio_button_selected).grid(column=column,row=index,sticky='w')
    

    def radio_button_selected(self):
        print(self.selected_radio.get())