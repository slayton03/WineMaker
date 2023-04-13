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
    current["F1"] = "Volume"
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
        # Run loop to fill array with indexes, this is for indexing purposes
        self.index_array = []
        for i in range(self.get_maximum_rows(sheet_object=current) - 1):
            self.index_array.append(2+i)



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
        # tabs should include
        # wine name
        # Tank number
        # Volume
        # Stage
        # ph
        # SO2
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
        self.addWine = customtkinter.CTkButton(self.wine_frame, text="+", width=20, height=20, command=self.add_wine)
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
            edit = customtkinter.CTkButton(self.scrollable_frame, text="...", width=20, height=15, command=lambda: self.wine_info(int(current["A" + str(i+2)].value) + 1))
            edit.grid(row=i, column=5, padx=10, pady=(0, 20))

    def add_wine(self):
        # Create main frame
        self.add_wine_frame = customtkinter.CTkFrame(self, width=120, corner_radius=0)
        self.add_wine_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")

        # Wine label
        self.add_wines_label = customtkinter.CTkLabel(self.add_wine_frame, text="New Wines",
                                                  font=customtkinter.CTkFont(size=30, weight="bold"))
        self.add_wines_label.place(x=20, y=20)

        # Input Wine name
        self.new_name = customtkinter.CTkLabel(self.add_wine_frame, text="Name:",
                                                  font=customtkinter.CTkFont(size=20, weight="bold"))
        self.new_name.place(x=20, y=100)

        self.name_entry = customtkinter.CTkEntry(self.add_wine_frame, placeholder_text="Name")
        self.name_entry.place(x=120, y=100)

        # Input tank number
        self.new_tank = customtkinter.CTkLabel(self.add_wine_frame, text="Tank:",
                                               font=customtkinter.CTkFont(size=20, weight="bold"))
        self.new_tank.place(x=20, y=150)

        self.tank_entry = customtkinter.CTkEntry(self.add_wine_frame, placeholder_text="Tank Number")
        self.tank_entry.place(x=120, y=150)

        # Input Volume
        self.new_vol = customtkinter.CTkLabel(self.add_wine_frame, text="Volume:",
                                                font=customtkinter.CTkFont(size=20, weight="bold"))
        self.new_vol.place(x=20, y=200)

        self.vol_entry = customtkinter.CTkEntry(self.add_wine_frame, placeholder_text="Volume")
        self.vol_entry.place(x=120, y=200)

        # Input Sugar
        self.new_sugar = customtkinter.CTkLabel(self.add_wine_frame, text="Sugar:",
                                               font=customtkinter.CTkFont(size=20, weight="bold"))
        self.new_sugar.place(x=20, y=250)

        self.sugar_entry = customtkinter.CTkEntry(self.add_wine_frame, placeholder_text="Sugar")
        self.sugar_entry.place(x=120, y=250)

        # Input Wine pH
        self.new_ph = customtkinter.CTkLabel(self.add_wine_frame, text="pH:",
                                               font=customtkinter.CTkFont(size=20, weight="bold"))
        self.new_ph.place(x=20, y=300)

        self.ph_entry = customtkinter.CTkEntry(self.add_wine_frame, placeholder_text="pH")
        self.ph_entry.place(x=120, y=300)
        #Confirm Button
        self.confirm_btn = customtkinter.CTkButton(self.add_wine_frame, text="Confirm", command=self.confirm_add)
        self.confirm_btn.place(x=20, y=350)
    def wine_info(self, index: int):
        # Create main frame
        self.wine_info_frame = customtkinter.CTkFrame(self, width=120, corner_radius=0)
        self.wine_info_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")

        # Info label
        self.wines_info_label = customtkinter.CTkLabel(self.wine_info_frame, text="Wine Information",
                                                      font=customtkinter.CTkFont(size=30, weight="bold"))
        self.wines_info_label.place(x=20, y=20)
        #Wine dropdown bar
        self.wine_drop = customtkinter.CTkComboBox(self.wine_info_frame, values=[current["B" + str(i+2)].value for i in range(self.get_maximum_rows(sheet_object=current) - 1)], command=self.wine_info)
        self.wine_drop.place(x=320, y=25)
        for i in range(self.get_maximum_rows(sheet_object=current) - 1):   # in progress loop for combp box index
            if self.wine_drop.get() == current["B" + str(i+2)].value:
                info_index = str(i+2)


        # Input Wine name
        self.wine_name = customtkinter.CTkLabel(self.wine_info_frame, text="Name:",
                                               font=customtkinter.CTkFont(size=20, weight="bold"))
        self.wine_name.place(x=20, y=100)

        self.current_wine = customtkinter.CTkLabel(self.wine_info_frame, text=current["B" + info_index].value)
        self.current_wine.place(x=120, y=100)

        # Input tank number
        self.tank_num = customtkinter.CTkLabel(self.wine_info_frame, text="Tank:",
                                               font=customtkinter.CTkFont(size=20, weight="bold"))
        self.tank_num.place(x=20, y=150)

        self.current_tank = customtkinter.CTkLabel(self.wine_info_frame, text=current["C" + info_index].value)
        self.current_tank.place(x=120, y=150)

        # Input Volume
        self.vol_num = customtkinter.CTkLabel(self.wine_info_frame, text="Volume:",
                                              font=customtkinter.CTkFont(size=20, weight="bold"))
        self.vol_num.place(x=20, y=200)

        self.current_vol = customtkinter.CTkLabel(self.wine_info_frame, text=current["F" + info_index].value)
        self.current_vol.place(x=120, y=200)

        # Input Sugar
        self.sugar_num = customtkinter.CTkLabel(self.wine_info_frame, text="Sugar:",
                                                font=customtkinter.CTkFont(size=20, weight="bold"))
        self.sugar_num.place(x=20, y=250)

        self.current_sugar = customtkinter.CTkLabel(self.wine_info_frame,text=current["D" + info_index].value)
        self.current_sugar.place(x=120, y=250)

        # Input Wine pH
        self.ph_num = customtkinter.CTkLabel(self.wine_info_frame, text="pH:",
                                             font=customtkinter.CTkFont(size=20, weight="bold"))
        self.ph_num.place(x=20, y=300)

        self.current_ph = customtkinter.CTkLabel(self.wine_info_frame, text=current["E" + info_index].value)
        self.current_ph.place(x=120, y=300)


    def confirm_add(self):
        ind = self.get_maximum_rows(sheet_object=current)+1

        current["A" + str(ind)] = ind-1
        current["B" + str(ind)] = self.name_entry.get()
        current["C" + str(ind)] = int(self.tank_entry.get())
        current["D" + str(ind)] = int(self.sugar_entry.get())
        current["E" + str(ind)] = float(self.ph_entry.get())
        current["F" + str(ind)] = int(self.vol_entry.get())
        book.save("WineMakerData.xlsx")
        self.wine_screen()

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
        # self.entry1.insert(0, current["C2"].value)
        self.entry2 = customtkinter.CTkEntry(self.calctabs.tab("Basic"), placeholder_text="Num2")
        self.entry2.place(x=200, y=0)
        # self.entry2.insert(0, current["C3"].value)
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
