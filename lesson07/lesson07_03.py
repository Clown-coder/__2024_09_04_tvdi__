import datasouce
from tkinter import ttk
import tkinter as tk
from ttkthemes import ThemedTk
from tkinter.messagebox import showinfo
import sqlite3

class Window(ThemedTk):
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title('登入')
        self.resizable(False,False)
        #==============style===============
        style = ttk.Style(self)
        style.configure('TopFrame.TLabel',font=('Helvetica',20))
        #============end style===============
        
        #==============top Frame===============

        topFrame = ttk.Frame(self)
        ttk.Label(topFrame,text='空氣品質指標(AQI)(歷史資料)',style='TopFrame.TLabel').pack()
        topFrame.pack(padx=20,pady=20)
        
        #==============end topFrame===============

        #==============bottomFrame===============
        bottomFrame = ttk.Frame(self)
            #==============selectedFrame===============
        selectedFrame=ttk.Frame(self,padding=[10,10,10,10])
        sitenames = datasouce.get_sitename()
        self.selected_site = tk.StringVar()
        sitenames_cb = ttk.Combobox(selectedFrame, textvariable=self.selected_site,values=sitenames,state='readonly')
        self.selected_site.set('請選擇站點')
        sitenames_cb.bind('<<ComboboxSelected>>', self.sitename_selected)
        sitenames_cb.pack(expand=True,anchor='n')        
        
        selectedFrame.pack(side='left',expand=True,fill='y',padx=(20,0))
            #==============end selectedFrame===============  

        # define columns
        columns = ('date', 'county', 'AQI','PM25','status','lat','lon')

        self.tree = ttk.Treeview(bottomFrame, columns=columns, show='headings')

        # define headings
        self.tree.heading('date', text='日期')
        self.tree.heading('county', text='縣市')
        self.tree.heading('AQI', text='AQI')
        self.tree.heading('PM25', text='PM25')
        self.tree.heading('status', text='狀態')
        self.tree.heading('lat', text='緯度')
        self.tree.heading('lon', text='經度')

        #set the width for each column
        self.tree.column('date',width=150,anchor='center')
        self.tree.column('county', width=80,anchor='center')
        self.tree.column('AQI', width=50,anchor='center')
        self.tree.column('PM25', width=50,anchor='center')
        self.tree.column('status', width=50,anchor='center')
        self.tree.column('lat', width=150,anchor='center')
        self.tree.column('lon', width=150,anchor='center')

        #單筆輸入
        # self.tree.insert('',tk.END,values=('2024-10-28 09:00','屏東縣',17,6.5,'良好',22.260899,120.651472))


        # generate sample data
        # contacts = []
        # for n in range(1, 100):
        #     contacts.append((f'first {n}', f'last {n}', f'email{n}@example.com'))

        # add data to the treeview
        # for contact in contacts:
        #     tree.insert('', tk.END, values=contact)
        
        self.tree.pack(side='right')
        
        bottomFrame.pack(expand=True,fill='x',padx=20,pady=(0,20),ipadx=10,ipady=10)
        #==============end bottomFrame===============
    
    
    def sitename_selected(self,e):
        for child in self.tree.get_children():
            self.tree.delete(child)
        selected = self.selected_site.get()
        
        selected_data = datasouce.get_selected_data(selected)
        # print(selected_data)
        for record in selected_data:
            self.tree.insert('',tk.END,values=record)


        



def main():
    datasouce.download_data() #下載至資料庫
    window = Window(theme="arc")
    window.mainloop()


if __name__ == '__main__':
    main()





"""
set 跟 current的差異是
        set 可以隨便設定 不一定 要在 list  或者數據裡面
        current 則一定要出現在表單裡面
        
        注意
        區域變數，且為資料時，因為不可以pack 所以要使用 self. 來開頭 讓資料保存

        我的寫法 也可以執行
        bottomFrame = ttk.Frame(self)
        self.selected_sitenames = tk.StringVar()
        sitenames = datasouce.get_sitename()
        sitenames.insert(0,'--請選擇地點--')

        sitenames_cb= ttk.Combobox(bottomFrame,textvariable=self.selected_sitenames)

        sitenames_cb.configure(values=sitenames,state ='readonly')
        sitenames_cb.pack()
        
        sitenames_cb.set(sitenames[0])
        #sitenames_cb.current(0)

"""