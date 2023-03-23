import os
import sys
import customtkinter
import tkinter


class vehicle_App(customtkinter.CTk):


    #constructor
    def __init__(self):
        super().__init__()
        self.title("Vehicle Information")
        self.geometry("1100x580")
        self.grid_rowconfigure(0, weight=1)  
        self.grid_columnconfigure(0, weight=1)
        
        self.textbox = customtkinter.CTkTextbox(master=self, width=500, height=400, text_color="black", corner_radius=0)
        self.textbox.grid(row=0, column=0, sticky="nsew")
        self.textbox.insert("0.0", " Marque : \n\n Modèle : \n\n Année : \n\n Couleur :  ")
        self.textbox.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

        self.button = customtkinter.CTkButton(self, command=self.button_click, text="valider", width=100, height=50,text_color="black")
        self.button.grid(row=0, column=0, padx=20, pady=10)
        

    def button_click(self):
        print("button click")

    def clean_up(self):
        os.system('cls')

    def start(self):
        print("Interface is starting ...")

    def quit(self):
        sys.exit()

app = vehicle_App()
app.mainloop()
