# WineMaker
### Introduction
Hello. My name is Stephen Layton and this is the repository for my WineMaker software. This was created for my ECE 1895 Junior Design class. This program was created in python using the customTKinter library for the GUI.

Please direct any questions to: stl82@pitt.edu

CustomTKinter library GitHub: [CustomTKinter](https://github.com/TomSchimansky/CustomTkinter)

### Installation

1. Download the repository and extract the zip file onto your computer

2. Open the output file and run the application

This should be all you need to do. The program should run as intended and nothing more should need to be done. You can right click on the application to add a shortcut to your home screen to have it readily avalible.

### Overview
This is a software for winemakers to track the properties of wines and create a suggested schedule. This program will allow you to store different wines and the  information that goes along with them including name, tank number, volume(L), sugar, pH, stage, and SO2. Using this inputed information, the program can run various calculations such as potassium metabisulfite additions based on volume and desired SO2 ppm raised, yeast addition for fermentation, and basic unit conversions. Also, given a start date and an anticipated end date, the program will genrate a suggusted schedule to use including 1st racking, 2nd racking, bentonite addition, bentonite racking, rough filtration, sweetening, and final filtration. All data is stored in an excel sheet using the openpyxl library to create an excel file and store, adjust, and delete data in given cells. This is done so that users have easy access to all data in case of program errors.

Overall, this version of the program is similar to the original concept. I wanted to make a program that would keep track of wines and their proporties, run calculations, and generate a timeline based on a desired end date. The biggest difference this current version has from the original is in the orignal concept, I planned to have a section that keeps note on the staus of the vineyard and what is being done. This idea proved to be too big an addition given the time constraint but may be able to be implemented if future versions of this program are made.

As stated earlier, this program uses the customTKinter library and while that was incredibly useful for the GUI widgets, such as buttons and labels, all functionallity of this program was created from scratch. I choose to do this project because my parents own a winery and there aren't many good softwares for winemakers to keep track of their wines and wine properties so I decided to make this program for my dad to see if this would be helpful to him.


### Verification

Since this project was a software design, I didn't really create a prototype but I did look into the customTKinter library to ensure it would do what I hoped it would do. I choose this library because it looked much nicer then a lot of other GUI libraries with a more modern feel. It also had all the widgets I wanted including labels, buttons, and drop down menus. I used an iterative proccess to design this program, designing one section at a time to ensure each section was able to be made. 

#### Commit Iterations

Below is a picture of all the commits for this project. This shows that this program was created with an iterative process and verification was done piece by piece to ensure everything would work as intended.

![image](https://github.com/slayton03/WineMaker/blob/main/WineMaker%20images/winemaker_commits.png)

### Implementation

As stated in the overview, this program is meant to help wine makers keep track of their wines by storing different wines and their properties. This program keeps track of different wine properties including name, tank number, volume(L), sugar, pH, stage, and SO2. The program uses these metrics to run various calculation such as potassium metabisulfite additions based on volume and desired SO2 ppm raised, yeast addition for fermentation, and basic unit conversions. Finally, the program is able to create a schedule for the wine maker to use to help them plan for what needs to be done with the wine. Below I will show pictures of each screen and what can be done from each.

#### Main Screen Example Images

##### Home screen:
![image](https://github.com/slayton03/WineMaker/blob/main/WineMaker%20images/winemaker_home.png)

This is the home screen. From here you can see a general overview of all your tanks(1-11) and what wine is in each one and  it's volume. The home screen also includes a simple to-do list where you can hit the + button to add any text you'd like and save it as a to-do task. When finished you can hit the done button and it will remove that item from the list. All new items are added from the bottom.

##### Wines screen:
![image](https://github.com/slayton03/WineMaker/blob/main/WineMaker%20images/winemaker_wines.png)

This is the wine screen. From here you can see all your current wines along with what tank they are in, their volume, the stage they are in, their pH, and their SO2 in parts per million. Hitting the + gives you the ability to create a new wine where you can input all the information for it and it will be saved in the program. Hitting the buttons with the three dots(...) sends you to the information screen where you can see all the wines information. This information screen will be shown next.

##### Wine Information screen:
![image](https://github.com/slayton03/WineMaker/blob/main/WineMaker%20images/winemaker_info.PNG)

This is the wine information screen. From here you can see all the information about the wine including name, tank number, volume(L), sugar, pH, stage, and SO2. The drop down bar allows you to change what wine is being looked at. Clicking the edit button will allow you to edit all the wines information or to just delete the wine entirely. 

##### Calculations screen:
![image](https://github.com/slayton03/WineMaker/blob/main/WineMaker%20images/winemaker_calc.png)

This is the calculations screen. From here you can run various calculations including potassium metabisulfite additions based on volume and desired SO2 ppm raised, yeast addition for fermentation, and basic unit conversions. The volume section will automatically be filled in based on what wine the calculation is being done for, which can be changed with the dropdown menu at the top of the screen. The volume can also be changed manually if desired. Then you input all other fields and hit the calculate button and the program will run the calculation. Using the tabs up top you can change to a different set of calculations.

##### Schedule screen:
![image](https://github.com/slayton03/WineMaker/blob/main/WineMaker%20images/winemaker_schgen.PNG)

This is the schedule generation screen. This is the screen you see if you currently have no schedule made. From here you input your start date and desired end date and the program will generate a schedule outline for you that includes 1st racking, 2nd racking, bentonite addition, bentonite racking, rough filtration, sweetening, and final filtration for each wine. The next image will show what this looks like.

##### Generated Schedule:
![image](https://github.com/slayton03/WineMaker/blob/main/WineMaker%20images/winemaker_sch.png)

This is what the generated schedule will look like. This shows some key items in making wine and gives suggested dates for when they shold be done. From here you can also generate a new schedule for possibly new dates or new wines but this will delete the old schedule.

For this program, one of the most challenging things to accomplish was getting all the information to be stored an accessed correctly. I wanted to save all data in excel so that, if need be, the average user could just open the excel file and look at or change data as needed. This proved to be somewhat of a challenge since I have never done anything like that before. I used the library openpyxl to get functions for adding data, adjusting data, and deleting data in certian cells. While the functions made this fairly simple, it was still difficult ensure everything was where I wanted it and making sure that the data I accessed what the actual data I wanted. This was especially tough when accessing or storing data in loops. I had to make sure I had the correct starting index, the correct traversal direction, and the correct length of the loop otherwise it wouldn't work how I needed it to. Eventually through trial and error I figured out better how to work the library and get all the correct information I needed.

### Testing

As stated before, this was an iterative proccess so testing occured while the program was being built. Below I will go through each section and describe what testing occured and at least on example of a bug that occured for each.

#### Home Screen:

To test the home screen, for the to-do list I would simply try to add new to-do tasks and then attempt to delete them.

_To-do bug ex)_ When doing this, I had an issue where the loop to get the to-do tasks would try and access one extra cell that was blank. I later learned that this was because unlike all my other accessing loops up to this point, this data didn't have a header in the excel sheet so I was skipping the first cell adding and extra empty cell onto the end. Once I figured this out it was a simple fix of indexing

To test the tanks I would simply make new wines and assign them to one of the tanks then check to see if the tank was now occupied.

_Tanks bug ex)_ Similarly to the to-do bug, this one had an issue where all the tanks were assigned 1 higher then they should be. Also like the to-do the issue was I was indexing the loop starting at 0 while the tanks started at 1. This was also a simple indexing fix.

#### Wine Screen:

To test the wines I would create new wines and make sure everyhing worked ass intended and would delete wines to make sure everything that was supposed to be was deleted. I also edited each value in the wines to make sure everything changed like it should.

_Wines bug ex)_ When inputing a letter into the tank value, the program wouldn't create the new wine until I put a number in. Once I finally did put a number in I saw that there were a bunch of half done new wines with the same name as the wine I just added. This was because no error was detected until after the wine name was already stored so it still added the wine name to the excel sheel but nothing else. To fix this I implemented error checking before anything gets added to ensure nothing got added before everything was good.

#### Calculation Screen:

To test the calculations, I inputed numbers to which I knew the correct answer to ensure the equations worked as intended.

_Calculations bug ex)_ When getting the numbers from the entry boxes, I at first couldn't get the calculations to run because of some value errors. What I found out was happening was that the entry box only gets the values as strings. To fix this I had to convert the entries into float values, then run the calculations, then convert the number back to a string to set it as the label text.

#### Schedule Screen:

To test the scheduling, I would create schedules with various end and start dates to ensure the function was generating the correct schedule.

_Scheduling bug ex)_ I realized vary quickily that adding and subtracting calendar dates wouldn't be as simple as just adding the days together. To accomplish adding and subtracting dates, I created specialized functions that knew how many days were in each month, accounting for leap years, and was able to produce a new date based on how many days you were trying to add or subtract.

### Conclusion

I was able to make a program for wine makers that would store various wines and the data that goes along with them, run calculations based on the wines properties, and create a suggested schedule for wine makers to follow. Overall, I am extremly happy with how this project turned out, doing most of what I wanted it to do, and feel like I learned a lot from this experience. I learned a lot about making a stand alone program and how to format it to make it more user friendly. I also learned more about storing and accessing data and how to use that data to accomplish different tasks. I believe this project was a great success and look forward to doing similar things in the future.

### Future ideas

If future iterations of this program are done, there are a couple of things I would like to possibley change or add. First off, I would like to add more information that is stored in the wines data. I currently have name, tank number, volume(L), sugar, pH, stage, and SO2. In later iterations, I would like to add more information that is relevent to the wines, such as current alcohol. I would also like to add more calculations. I would like to give the program more ability to be useful by adding more calculations that it can run such as how much bentonite should be added for cold stablization. Finally, I would like to update the scheduling. While I am happy with what I have now, the current scheduling is very dull and basic. I would like to add more points in the wine making proccess to be scheduled and make the overall scheduling page look nicer instaed of just a list of dates.

