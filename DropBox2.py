import tkinter as tk
from tkinter import ttk


class DropBox2:
    def __init__(self):
        self.value = None

    # def callbackFunc(event):
    #     print("New Element Selected")

    def draw(self):

        def callback():
            self.value = n.get()
            app.destroy()

        # def changeMonth():
        #     comboExample["values"] = ["July",
        #                               "August",
        #                               "September",
        #                               "October"]


        app = tk.Tk()
        app.geometry('300x100')

        labelTop = tk.Label(app,
                            text = "Choose your key commands")
        labelTop.grid(column=0, row=0)
        n = tk.StringVar()
        comboExample = ttk.Combobox(app,
                                    values=[
                                        ' Q A',
                                        ' E D',
                                        ' O L',
                                        ' UP DOWN'], textvariable=n)

        comboExample.grid(column=0, row=1)
        button = ttk.Button(app, text="Submit", command=callback)
        button.grid(column=1, row=1)

        app.mainloop()
