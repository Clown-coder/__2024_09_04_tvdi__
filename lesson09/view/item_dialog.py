import tkinter as tk
from tkinter.simpledialog import Dialog

class MyCustomDialog(Dialog):
    def __init__(self, parent,record:list ,title = None):
        print(f'傳過來的資料: {record}')
        self.date = record[0]
        self.county =record[1]
        self.sitename = record[2]
        self.aqi = record[3]
        self.pm25 = record[4]
        self.status = record[5]
        self.lat = float(record[6])
        self.lon = float(record[7])
        #super().__init__ 這行執行完，就會跳出去執行別行
        #所以有其他東西要執行，就要在這行之前
        super().__init__(parent=parent,title=title)

    def body(self, master):
        # 創建對話框主體。返回應具有初始焦點的控件。
        pass

    def apply(self):
        # 當用戶按下確定時處理數據
        pass
        
    def buttonbox(self):
        # Add custom buttons (overriding the default buttonbox)
        box = tk.Frame(self)
        self.ok_button = tk.Button(box, text="OK", width=10, command=self.ok, default=tk.ACTIVE)
        self.ok_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.cancel_button = tk.Button(box, text="Cancel", width=10, command=self.cancel)
        self.cancel_button.pack(side=tk.LEFT, padx=5, pady=5)
        self.bind("<Return>", self.ok)
        self.bind("<Escape>", self.cancel)
        box.pack()

    def ok(self, event=None):
        # Override the ok method
        print("OK button was clicked!")
        super().ok()

    def cancel(self,event=None):
        print('Cancel button was clicked!')
        super().cancel()


        