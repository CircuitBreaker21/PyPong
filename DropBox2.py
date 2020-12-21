import tkinter as tk
from tkinter import ttk


class DropBox2:
    
    
      

    def callbackFunc(event):
        print("New Element Selected")
        

    def draw(self):
        def changeMonth(val):
            return val
            comboExample["values"] = ["July",
                                    "August",
                                    "September",
                                    "October"
                                        ]

        app = tk.Tk()
        app.geometry('200x100')

        labelTop = tk.Label(app,
                            text = "Choose your favourite month")
        labelTop.grid(column=0, row=0)

        comboExample = ttk.Combobox(app, 
                                    values=[
                                            "January", 
                                            "February",
                                            "March",
                                            "April"],
                                    postcommand=changeMonth(val))


        comboExample.grid(column=0, row=1)

        app.mainloop()
