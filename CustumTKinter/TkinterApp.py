import customtkinter as ctk
import json
import os

class EGrassApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. Window Configuration
        self.title("Task Manager")
        self.geometry("900x600")
        
        # Grid Layout (Sidebar: Col 0, Content: Col 1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # --- SIDEBAR ---
        self.sidebar = ctk.CTkFrame(self, width=200, corner_radius=0)
        self.sidebar.grid(row=0, column=0, sticky="nsew")
        
        self.logo = ctk.CTkLabel(self.sidebar, text="E-GRASS", font=("Arial", 26, "bold"))
        self.logo.pack(pady=30)

        self.del_button = ctk.CTkButton(self.sidebar, text="Clear Current Tab", 
                                        fg_color="#912a2a", hover_color="#5e1919",
                                        command=self.delete_all_tasks)
        self.del_button.pack(side="bottom", pady=20)

        # --- MAIN TABVIEW ---
        self.tabview = ctk.CTkTabview(self)
        self.tabview.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        
        # Creating Tabs for your active projects
        self.tabview.add("Tab 1")
        self.tabview.add("Tab 2")
        self.tabview.add("Tab 3")

        # --- INPUT SECTION (Universal for all tabs) ---
        self.entry_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.entry_frame.grid(row=1, column=1, padx=20, pady=(0, 20), sticky="ew")
        
        self.entry = ctk.CTkEntry(self.entry_frame, placeholder_text="Enter new task...", height=40)
        self.entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        
        self.entry_tab = ctk.CTkEntry(self.entry_frame,placeholder_text="Enter new tab name", height=40)
        self.entry_tab.pack(side="left", fill="x", expand=True, padx=(0, 10))
        # Bind the ENTER key to add task automatically
        self.entry.bind("<Return>", lambda event: self.add_task())

        self.add_button = ctk.CTkButton(self.entry_frame, text="Add Task", width=100, height=40, command=self.add_task)
        self.add_button.pack(side="right")

        self.add_button = ctk.CTkButton(self.entry_frame, text="Add tab", width=100, height=40, command=self.add_tab)
        self.add_button.pack(side="right", padx=(0, 10))
        # --- INITIAL LOAD ---
        self.load_tasks()

    def get_current_frame(self):
        """Helper to get the frame of the currently selected tab"""
        tab_name = self.tabview.get()
        return self.tabview.tab(tab_name)
    

    def add_tab(self):
        new_tab_name = self.entry_tab.get()
        if new_tab_name:
            self.tabview.add(new_tab_name)
            self.tabview.select(new_tab_name)  # Automatically switch to the new tab
            self.save_tasks()  # Save to update the new tab structure
            self.entry_tab.delete(0, 'end')

    def add_task(self, task_text=None):
        # If task_text isn't passed (from load), get it from entry field
        if task_text is None:
            task_text = self.entry.get()

        if task_text:
            current_tab_frame = self.get_current_frame()
            
            # Create checkbox inside the active tab
            new_task = ctk.CTkCheckBox(current_tab_frame, text=task_text)
            new_task.pack(anchor="w", pady=5, padx=10)
            
            self.entry.delete(0, 'end')
            self.save_tasks()

    def delete_all_tasks(self):
        current_tab_frame = self.get_current_frame()
        for widget in current_tab_frame.winfo_children():
            widget.destroy()
        self.save_tasks()

    def save_tasks(self):
        """Saves tasks for ALL tabs into a structured JSON dictionary"""
        data = {}
        for tab_name in self.tabview._tab_dict:
            tab_frame = self.tabview.tab(tab_name)
            tasks = [child.cget("text") for child in tab_frame.winfo_children() if isinstance(child, ctk.CTkCheckBox)]
            data[tab_name] = tasks
        
        with open("egrass_data.json", "w") as f:
            json.dump(data, f)


    def load_tasks(self):
        if os.path.exists("egrass_data.json"):
            with open("egrass_data.json", "r") as f:
                data = json.load(f)
                for tab_name, tasks in data.items():
                    try:
                        tab_frame = self.tabview.tab(tab_name)
                    except ValueError:
                        self.tabview.add(tab_name)
                        tab_frame = self.tabview.tab(tab_name)
                    for t in tasks:
                        cb = ctk.CTkCheckBox(tab_frame, text=t)
                        cb.pack(anchor="w", pady=5, padx=10)

if __name__ == "__main__":
    app = EGrassApp()
    app.mainloop()