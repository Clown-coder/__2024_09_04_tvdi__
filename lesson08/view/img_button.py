from tkinter import ttk
from PIL import Image,ImageTk


class ImageButton(ttk.Button):
    def __init__(self, master=None, **kwargs):
        self.icon_img = Image.open('refresh_16.png')
        self.icon_phto = ImageTk.PhotoImage(self.icon_img)
        super().__init__(master=master,image=self.icon_phto,**kwargs)