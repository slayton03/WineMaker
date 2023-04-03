import tkinter
import tkinter.messagebox
import customtkinter

customtkinter.set_appearance_mode("Dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("green")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # configure window
        self.title("WineMaker")
        self.geometry(f"{1100}x{580}")

        # configure grid layout (4x4)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((2, 3), weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        # create sidebar frame with widgets-----------------------------------------------------------------------------
        # Create Sidebar frame
        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(6, weight=1)
        # Create main label
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="WineMaker", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))
        # Create Home button
        self.home_btn = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.home_btn.grid(row=1, column=0, padx=20, pady=10)
        self.home_btn.configure(text="Home")
        # Create Wines button
        self.wines_btn = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.wines_btn.grid(row=2, column=0, padx=20, pady=10)
        self.wines_btn.configure(text="Wines")
        # Create Calculations button
        self.calc_btn = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.calc_btn.grid(row=3, column=0, padx=20, pady=10)
        self.calc_btn.configure(text="Calculations")
        # Create Schedule button
        self.sch_btn = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.sch_btn.grid(row=4, column=0, padx=20, pady=10)
        self.sch_btn.configure(text="Schedule")
        # Create Notes button
        self.note_btn = customtkinter.CTkButton(self.sidebar_frame, command=self.sidebar_button_event)
        self.note_btn.grid(row=5, column=0, padx=20, pady=10)
        self.note_btn.configure(text="Notes")
        # Create apperance label
        self.appearance_mode_label = customtkinter.CTkLabel(self.sidebar_frame, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        # Create apperance dropdown
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.sidebar_frame, values=["Light", "Dark", "System"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 10))



        # Home label
        self.home_label = customtkinter.CTkLabel(self, text="Home",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.home_label.grid(row=0, column=1, padx=(20,0), pady=(20, 10))
        self.sidebar_frame.grid_rowconfigure(2, weight=1)

        # to-do label
        self.todo_label = customtkinter.CTkLabel(self, text="To-Do",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.todo_label.grid(row=0, column=3, padx=(20, 0), pady=(20, 10))

        # to-do label
        self.todo2_label = customtkinter.CTkLabel(self, text="To-Do",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.todo2_label.grid(row=0, column=4, padx=(20, 0), pady=(20, 10))


    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def sidebar_button_event(self):
        print("sidebar_button click")

if __name__ == "__main__":
    app = App()
    app.mainloop()
