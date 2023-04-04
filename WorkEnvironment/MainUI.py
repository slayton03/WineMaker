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
        self.home_btn = customtkinter.CTkButton(self.sidebar_frame, command=self.home_screen)
        self.home_btn.grid(row=1, column=0, padx=20, pady=10)
        self.home_btn.configure(text="Home")
        # Create Wines button
        self.wines_btn = customtkinter.CTkButton(self.sidebar_frame, command=self.wine_screen)
        self.wines_btn.grid(row=2, column=0, padx=20, pady=10)
        self.wines_btn.configure(text="Wines")
        # Create Calculations button
        self.calc_btn = customtkinter.CTkButton(self.sidebar_frame, command=self.calc_screen)
        self.calc_btn.grid(row=3, column=0, padx=20, pady=10)
        self.calc_btn.configure(text="Calculations")
        # Create Schedule button
        self.sch_btn = customtkinter.CTkButton(self.sidebar_frame, command=self.sch_screen)
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
        # ---------------------------------------------------------------------------------------------------------------------------

        self.home_screen()



    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)
    def sidebar_button_event(self):
        print("sidebar_button click")

    def home_screen(self):
        self.main_frame = customtkinter.CTkFrame(self, width=120, corner_radius=0)
        self.main_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")
        # self.main_frame.grid_rowconfigure(6, weight=1)

        # Home label
        self.home_label = customtkinter.CTkLabel(self.main_frame, text="Home",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.home_label.grid(row=0, column=1, padx=(0, 500), pady=(20, 400))
        # self.sidebar_frame.grid_rowconfigure(2, weight=0)

        # to-do label
        self.todo_label = customtkinter.CTkLabel(self.main_frame, text="To-Do",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.todo_label.grid(row=0, column=1, padx=(0, 500), pady=(20, 200))

    def wine_screen(self):
        # Create main frame
        self.wine_frame = customtkinter.CTkFrame(self, width=120, corner_radius=0)
        self.wine_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")

        # Calc label
        self.wine_label = customtkinter.CTkLabel(self.wine_frame, text="Wine",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.wine_label.grid(row=0, column=1, padx=(0, 500), pady=(20, 400))

    def calc_screen(self):
        # Create main frame
        self.calc_frame = customtkinter.CTkFrame(self, width=120, corner_radius=0)
        self.calc_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")

        # Calc label
        self.calc_label = customtkinter.CTkLabel(self.calc_frame, text="Calc",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.calc_label.grid(row=0, column=1, padx=(0, 500), pady=(20, 400))

        # Multiplication test
        self.entry1 = customtkinter.CTkEntry(self.calc_frame, placeholder_text="Num 1")
        self.entry1.place(x=10, y=100)
        self.entry2 = customtkinter.CTkEntry(self.calc_frame, placeholder_text="Num2")
        self.entry2.place(x=200, y=100)
        # Mult label
        self.mult_label = customtkinter.CTkLabel(self.calc_frame, text="x", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.mult_label.place(x=170, y=100)
        # equals label
        self.eq_label = customtkinter.CTkLabel(self.calc_frame, text="=",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.eq_label.place(x=360, y=100)

        # answer
        self.an_label = customtkinter.CTkLabel(self.calc_frame, text="answer",
                                               font=customtkinter.CTkFont(size=20, weight="bold"))
        self.an_label.place(x=390, y=100)

        # calculate button
        self.get_an_btn = customtkinter.CTkButton(self.calc_frame, command=self.mult)
        self.get_an_btn.place(x=490, y=100)
        self.get_an_btn.configure(text="Calculate")

    def mult(self):
        self.an_label.configure(text=(str(int(self.entry1.get()) * int(self.entry2.get()))))





    def sch_screen(self):
        self.sch_frame = customtkinter.CTkFrame(self, width=120, corner_radius=0)
        self.sch_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")
        # self.main_frame.grid_rowconfigure(6, weight=1)

        # Calc label
        self.sch_label = customtkinter.CTkLabel(self.sch_frame, text="Schedule",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.sch_label.grid(row=0, column=1, padx=(0, 500), pady=(20, 400))


if __name__ == "__main__":
    # root = customtkinter.CTk()
    main = App()
    main.mainloop()
