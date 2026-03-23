import customtkinter as ctk

# Set the appearance mode (System, Light, or Dark)
ctk.set_appearance_mode("System")  
ctk.set_default_color_theme("blue") 

class MyFirstApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("E-GrassProjectManager")
        self.geometry("800x600")

        # ConfigureGrid(2 colums, 1 row)
