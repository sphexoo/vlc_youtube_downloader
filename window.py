import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x200")
        label_textfield = tk.Label(self, text="URL: ")
        label_textfield.grid(row=0, column=0)
        entry_textfield = tk.Entry(self, width=75)
        entry_textfield.grid(row=0, column=1)
        entry_textfield.focus()
        button_download = tk.Button(text="Download", command=self.onClick_download)
        button_download.grid(row=1, column=0, columnspan=2)

    def onClick_download(self):
        print("test")

