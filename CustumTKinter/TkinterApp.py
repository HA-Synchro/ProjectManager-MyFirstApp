import customtkinter as ctk
import json
import os

class EGrassApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("E-Grass Project Manager")
        self.geometry("800x500")

        # Configure Grid (2 columns, 1 row)
        self.grid_columnconfigure(1, weight=1) # Main view expands
        self.grid_rowconfigure(0, weight=1)

        # --- SIDEBAR ---
        self.sidebar = ctk.CTkFrame(self, width=50, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.logo_label = ctk.CTkLabel(self.sidebar, text="E-GRASS", font=("Arial", 24, "bold"))
        self.logo_label.pack(pady=20, padx=20)

        # --- MAIN VIEW ---
        self.main_view = ctk.CTkFrame(self, fg_color="transparent")
        self.main_view.grid(row=0, column=1, sticky="nsew", padx=20, pady=20)

        self.header = ctk.CTkLabel(self.main_view, text="3D Cooking Tycoon Tasks", font=("Arial", 20))
        self.header.pack(anchor="w")

        # --- INPUT AREA ---
        self.entry = ctk.CTkEntry(self.main_view, placeholder_text="New Task (e.g., Model Chef Character)")
        self.entry.pack(fill="x", pady=10)

        self.add_button = ctk.CTkButton(self.main_view, text="Add Task", command=self.add_task)
        self.add_button.pack(pady=5)

        self.add_button = ctk.CTkButton(self.main_view, text="Delete All Taks", command=self.delete_all_tasks)
        self.add_button.pack(pady=5)

        # --- TASK LIST (The "Container") ---
        self.task_list_frame = ctk.CTkScrollableFrame(self.main_view, label_text="Active Tasks")
        self.task_list_frame.pack(fill="both", expand=True, pady=10)

        self.load_tasks() # Load tasks from file on startup

    def add_task(self):
        task_text = self.entry.get()
        self.save_tasks() # Save current tasks before adding new one
        if task_text:
            # Create a Checkbox for the new task
            new_task = ctk.CTkCheckBox(self.task_list_frame, text=task_text)
            new_task.pack(anchor="w", pady=5)
            self.save_tasks() # Save tasks after adding new one
            self.entry.delete(0, 'end') # Clear input field
    
    
    def save_tasks(self):
        tasks = []
        for widget in self.task_list_frame.winfo_children():
            if isinstance(widget, ctk.CTkCheckBox):
                tasks.append(widget.cget("text"))
        with open("tasks.json", "w") as f:
            json.dump(tasks, f)
    def load_tasks(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as f:
                tasks = json.load(f)
                for task_text in tasks:
                    self.create_task_widget(task_text)
    
    def delete_all_tasks(self):
        for widget in self.task_list_frame.winfo_children():
            widget.destroy()
        self.save_tasks() # Save empty task list to file

    def create_task_widget(self, text):
        new_task = ctk.CTkCheckBox(self.task_list_frame, text=text)
        new_task.pack(anchor="w", pady=5)
if __name__ == "__main__":
    app = EGrassApp()
    app.mainloop()