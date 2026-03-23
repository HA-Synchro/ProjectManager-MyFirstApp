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
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # SIDEBAR
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")

        self.logo_label = ctk.CTkLabel(self.sidebar, text="E-Grass", font=("Arial", 24, "bold"))
        self.logo_label.pack(pady=20)

        # MAIN VIEW
        self.main_view = ctk.CTkFrame(self, fg_color="transparent")
        self.main_view.grid(row=0, column=1, sticky="nsew")

        self.header = ctk.CTkLabel(self.main_view, text="3D Cooking Tycoon tasks", font=("Arial", 20))
        self.header.pack(anchor="w")
        # Input Area
        self.entry = ctk.CTkEntry(self.main_view, placeholder_text="New Tast(e.g., Model)")
        self.entry.pack(fill="x", pady=10)

        self.add_button = ctk.CTkButton(self.main_view, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        # TASK LIST
        self.task_list_frame = ctk.CTkScrollableFrame(self.main_view, label_text = "Active Tasks")
        self.task_list_frame.pack(fill="both", expand=True, padx=10)

    def add_task(self):
        task_text= self.entry.get()
        if task_text:
            new_task = ctk.CTkLabel(self.task_list_frame, text=task_text)
            new_task.pack(anchor="w", pady=2)
            self.entry.delete(0, 'end')




if __name__ == "__main__":
    app = MyFirstApp()
    app.mainloop()