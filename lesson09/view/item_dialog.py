import tkinter as tk
from tkinter.simpledialog import Dialog

class MyCustomDialog(Dialog):
    def __init__(self, parent, title = None):
        super().__init__(parent=parent,title=title)