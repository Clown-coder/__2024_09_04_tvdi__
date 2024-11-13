import tkinter as tk
from tkinter.simpledialog import Dialog
from tkinter import ttk
from PIL import Image, ImageTk


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
        main_frame = ttk.Frame(master,borderwidth=1,relief='groove')
        ttk.Label(main_frame,text=self.status).pack()

        canvas_left = tk.Canvas(main_frame,width=200,height=200)
        canvas_left.create_rectangle(10,10,190,190,outline='#9E7A7A',fill='#B19639',width=2)
        # canvas_left.create_oval(15, 15, 185, 185, outline="#f11",
        #     fill="#1f1", width=2)
        canvas_left.create_text(100,60,text='AQI',font=('Helvetica',24,'bold'),fill='blue')
        canvas_left.create_text(100,110,text=self.aqi,font=('Helvetica',24,'bold'),fill='green')
        img = Image.open(r'C:\\Users\\user\\Documents\\GitHub\\__2024_09_04_tvdi__\\lesson09\\green_light.png')
        self.resize_image= img.resize((60,60))
        self.green = ImageTk.PhotoImage(self.resize_image)
        canvas_left.create_image(100,150,anchor='center',image=self.green)
        canvas_left.pack(side='left')


        canvas_right = tk.Canvas(main_frame,width=200,height=200)
        canvas_right.create_rectangle(10,10,190,190,outline='#AB3B3A',fill='#724938',width=2)
        # canvas_right.create_oval(15, 15, 185, 185, outline="#f11",
        #     fill="#1f1", width=2)
        canvas_right.create_text(100,60,text='PM2.5',font=('Helvetica',24,'bold'),fill='blue')
        canvas_right.create_text(100,110,text=self.aqi,font=('Helvetica',24,'bold'),fill='green')
        canvas_right.pack(side='right')

        
        
        main_frame.pack(fill='x', expand=True)

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


        