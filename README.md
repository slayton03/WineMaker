# WineMaker
### Introduction
Hello. My name is Stephen Layton and this is the repository for my WineMaker software. This was created for my ECE 1895 Junior Design class. This program was created in python using the customTKinter library for the GUI.

Please direct any questions to: stl82@pitt.edu

CustomTKinter library GitHub: [CustomTKinter](https://github.com/TomSchimansky/CustomTkinter)
### Overview
This is a software for winemakers to track wines properties and track predicted schedule. This program will allow you to store different wines and the  information that goes along with them including name, tank number, volume(L), sugar, pH, stage, and SO2. Using this inputed information, the program can run various calculations such as potassium metabisulfite additions based on volume and desired SO2 ppm raised, yeast addition for fermentation, and basic unit conversions. Also, given a start date and an anticipated end date, the program will genrate a suggusted schedule to use including 1st racking, 2nd racking, bentonite addition, bentonite racking, rough filtration, sweetening, and final filtration. All data is stored in an excel sheet using the openpyxl library to create an excel file and store, adjust, and delete data in given cells. This is done so that users have easy access to all data in case of program errors.

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

__To-do bug ex)__

#### Wine Screen:

#### Calculation Screen:

#### Schedule Screen:

### Conclusion



### Future ideas

If future iterations of this program are done, there are a couple of things I would like to possibley change or add. First off, I would like to add more information that is stored in the wines data. I currently have name, tank number, volume(L), sugar, pH, stage, and SO2. In later iterations, I would like to add more information that is relevent to the wines, such as current alcohol.


Personal writing reference, delete later
# Heading level 1
## Heading level 2
### Heading level 3
#### Heading level 4
##### Heading level 5
###### Heading level 6
*one star on each side*
_This text is also italic_
**two stars on each side**
__This text is also bold__
***This text is italic and bold.***
___This text is also italic and bold.___
~~strikethrough~~
[This text links to gfg](https://write.geeksforgeeks.org/).

-Just add a dash first and then write a text.

-If you add another dash in the following line, you will have another item in the list.
    - If you add four spaces or use a tab key, you will create an indented list.
        - If you need sert an indenta list within an intended one, just press a tab key again.

Sometimes you want bullet points:

*Start a line with a star 
*Profit!

1. Just type a number follow by a dot.
2. If you want to add a second item, just type in another number followed by a dot.
1. If you make a mistake when typing numbers, fear not, Markdown will correct for you. 
    1. If you press a tab key or type four spaces, you will get an indented list and the numbering will start from scratch.
        1. If you want to insert an indented numbered list within an existing indented numbered one, just press the tab key again. 
            -If need be, you can also add an indented unordered list within an indented numbered one, by pressing a tab key and typing adash.
            
![image](https://media.geeksforgeeks.org/wp-content/cdn-uploads/20210914130327/100-Days-of-Code-with-GFG-Get-Committed-to-a-Challenge.png)
