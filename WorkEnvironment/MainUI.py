import tkinter
import tkinter.messagebox
import customtkinter
import os.path
import pandas as pd
from openpyxl import Workbook, load_workbook

if os.path.exists("WineMakerData.xlsx"):
    book = load_workbook("WineMakerData.xlsx")
    current = book.active

else:
    book = Workbook()
    current = book.active
    current.title = "WineData"
    current["A1"] = "Index"
    current["B1"] = "Wine"
    current["C1"] = "Tank"
    current["D1"] = "Sugar"
    current["E1"] = "pH"
    book.save("WineMakerData.xlsx")
    # ws1 = wb.create_sheet("Wine Data")




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

        # for i in range(3):
        #     current["A" + str(i+2)] = 1
        #     # print("A" + str(i+2))
        #
        # for i in range(self.get_maximum_rows(sheet_object=current)-1):
        #     current["B" + str(i + 2)] = 2
        #     current["C" + str(i + 2)] = 3
        #     current["D" + str(i + 2)] = 4
        #
        # book.save("WineMakerData.xlsx")

        # current["C9"] = 66


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

        # To-do---------------------------------------------------------------------------------------
        # to-do label
        self.todo_label = customtkinter.CTkLabel(self.main_frame, text="To-Do",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.todo_label.grid(row=0, column=1, padx=(0, 500), pady=(20, 200))
        # to-do list
        self.scrollable_todo = customtkinter.CTkScrollableFrame(self.main_frame, width=450, height=400)
        self.scrollable_todo.place(x=0, y=160)

        for i in range(4):
            # wine
            todo = customtkinter.CTkLabel(master=self.scrollable_todo, text=str(i+1)+") Whatever to-do",
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
            todo.grid(row=i*2, column=0, padx=10, pady=(0, 20))

            complete = customtkinter.CTkButton(self.scrollable_todo, text="Completed")
            complete.grid(row=(i*2)+1, column=0, padx=10, pady=(0, 20))


    def wine_screen(self):
        # Create main frame
        self.wine_frame = customtkinter.CTkFrame(self, width=120, corner_radius=0)
        self.wine_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")

        # Wine label
        self.wines_label = customtkinter.CTkLabel(self.wine_frame, text="Wines",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.wines_label.place(x=20, y=20)

        # Create wine tabs-------------------------------------------------------------------------
        # wine
        self.wine_label = customtkinter.CTkLabel(self.wine_frame, text="Wine",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.wine_label.place(x=40, y=100)
        # tank
        self.tank_label = customtkinter.CTkLabel(self.wine_frame, text="Tank(s)",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.tank_label.place(x=110, y=100)
        # sugar
        self.sugar_label = customtkinter.CTkLabel(self.wine_frame, text="Sugar",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.sugar_label.place(x=200, y=100)
        # pH
        self.ph_label = customtkinter.CTkLabel(self.wine_frame, text="pH",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.ph_label.place(x=270, y=100)
        #Add button
        self.addWine = customtkinter.CTkButton(self.wine_frame, text="+", width=20, height=20)
        self.addWine.place(x=700, y=110)
        # Bottom Line
        self.wine_line = customtkinter.CTkLabel(self.wine_frame, text="----------------------------------------------------------------------------------",
                                               font=customtkinter.CTkFont(size=20, weight="bold"))
        self.wine_line.place(x=20, y=130)
        # ---------------------------------------------------------------------------------------------------------

        # Add scrollable frame
        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.wine_frame, width=850, height=400)
        self.scrollable_frame.place(x=20, y=150)

        # Loop for adding wines and values
        for i in range(self.get_maximum_rows(sheet_object=current)-1):
            # wine
            wine = customtkinter.CTkLabel(master=self.scrollable_frame, text=current["B" + str(i+2)].value,
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
            wine.grid(row=i, column=0, padx=10, pady=(0, 20))
            # tank
            tank = customtkinter.CTkLabel(master=self.scrollable_frame, text=current["C" + str(i+2)].value,
                                                     font=customtkinter.CTkFont(size=20, weight="bold"))
            tank.grid(row=i, column=1, padx=10, pady=(0, 20))
            # sugar
            sugar = customtkinter.CTkLabel(master=self.scrollable_frame, text=current["D" + str(i+2)].value,
                                                      font=customtkinter.CTkFont(size=20, weight="bold"))
            sugar.grid(row=i, column=2, padx=10, pady=(0, 20))
            # pH
            ph = customtkinter.CTkLabel(master=self.scrollable_frame, text=current["E" + str(i+2)].value,
                                                   font=customtkinter.CTkFont(size=20, weight="bold"))
            ph.grid(row=i, column=3, padx=10, pady=(0, 20))

            # edit button
            self.scrollable_frame.columnconfigure(4, weight=1)
            edit = customtkinter.CTkButton(self.scrollable_frame, text="...", width=20, height=15)
            edit.grid(row=i, column=5, padx=10, pady=(0, 20))


    def calc_screen(self):
        # Create main frame
        self.calc_frame = customtkinter.CTkFrame(self, width=120, corner_radius=0)
        self.calc_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")

        #Create tabs
        self.calctabs = customtkinter.CTkTabview(self.calc_frame, width=850, height=500)
        self.calctabs.place(x=20, y=50)
        self.calctabs.add("Basic")
        self.calctabs.add("Main")
        self.calctabs.add("Test")

        # Calc label
        self.calc_label = customtkinter.CTkLabel(self.calc_frame, text="Calculations",
                                                 font=customtkinter.CTkFont(size=30, weight="bold"))
        self.calc_label.place(x=20, y=20)

        # Multiplication test
        self.entry1 = customtkinter.CTkEntry(self.calctabs.tab("Basic"), placeholder_text="Num 1")
        self.entry1.place(x=10, y=0)
        self.entry2 = customtkinter.CTkEntry(self.calctabs.tab("Basic"), placeholder_text="Num2")
        self.entry2.place(x=200, y=0)
        # Mult label
        self.mult_label = customtkinter.CTkLabel(self.calctabs.tab("Basic"), text="x", font=customtkinter.CTkFont(size=20, weight="bold"))
        self.mult_label.place(x=170, y=0)
        # equals label
        self.eq_label = customtkinter.CTkLabel(self.calctabs.tab("Basic"), text="=",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.eq_label.place(x=360, y=0)

        # answer
        self.an_label = customtkinter.CTkLabel(self.calctabs.tab("Basic"), text="answer",
                                               font=customtkinter.CTkFont(size=20, weight="bold"))
        self.an_label.place(x=390, y=0)

        # calculate button
        self.get_an_btn = customtkinter.CTkButton(self.calctabs.tab("Basic"), width=80, command=self.mult)
        self.get_an_btn.place(x=490, y=0)
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

    def get_maximum_rows(self, sheet_object):
        rows = 0
        for max_row, row in enumerate(sheet_object, 1):
            if not all(col.value is None for col in row):
                rows += 1
        return rows


if __name__ == "__main__":
    # root = customtkinter.CTk()
    main = App()
    main.mainloop()
