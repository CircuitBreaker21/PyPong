import tkinter as tk
from tkinter import ttk


class DropBox():

    def draw(self):
        # Creating tkinter window
        window = tk.Tk()
        window.geometry('350x250')
        # Label
        ttk.Label(window, text="Select your controls :",
                  font=("Times New Roman", 10)).grid(column=0,
                                                     row=15, padx=10, pady=25), postcommand = retrunVal,

        n = tk.StringVar()
        controlsList = ttk.Combobox(window, width=27,
                                    textvariable=n)

        # Adding combobox drop down list
        controlsList['values'] = (' Q A',
                                  ' E D',
                                  ' O L',
                                  ' UP DOWN')

        controlsList.grid(column=1, row=15)

        # Shows february as a default value
        controlsList.current()
        print(controlsList.get())
        window.mainloop()

    def retrunVal():
        print(val)
