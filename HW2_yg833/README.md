# Homework 3

This was week 3 of the course but the second homeowrk assignment submitted via GitHub.
There were multiple assignments as part of Homework 3. I collaborated with a number of classmates on the homework assignments as follow:
 * Collaborated with Sam Falk (sjf374) on assignment 1 and 2. Where we went through the steps to create a file and deleted the file, and choose a sample data set from NYC OPEN Data. We did some data exploration and determined the steps to be taken for the assignment. 
 * Worked collaboratively with Klo'e (kyn227), Rachel(rms818), Qin Yu(qg412) and Vaidehi(vvt221) on assignment 3 and 4. The collaboration was mostly in thought partnership and how to approach the problem. 

## Assignment 1: perform the instruction in deleteData.md: delete data and its history from a GitHub repo
Steps:
1) Created a test.csv file in my repo locally and pushed it to github
![test_file1](../HW2_yg833/screenshots/testcsv.PNG)
![test_file1_history](../HW2_yg833/screenshots/testcsv_history.PNG)

2) Creates a test2.csv file via the text editor on Github and pulled the changes
![test_file2](../HW2_yg833/screenshots/test2csv.PNG)
![test_file2_history](../HW2_yg833/screenshots/test2csv_history.PNG)

3) deleted the files and its history
![test_delete_history](../HW2_yg833/screenshots/postDeleingTestcsv.PNG)

4) forced the changes to the origin

## Assignment 2: Choose a file in CSV format from NYC Open Data and use pandas to read the file and mangle the data within it.

## Assignment 3: Write a script to stream real-time bus data from MTA through the MTA Bus Time interface. 
Created a script named "show_bus_locations.py" which takes 3 arguments:
<py script name> <API Key> <Bus_Line>
show_bus_locations_yg833.py xxxxx-xxxxx-xxxxx-xxxxx-xxxxx B52

## Assignment 4: Write scripts to stream real-time bus data from MTA through the MTA Bus Time interface. 
Created a script named "get_bus_info_yg833.py" which takes 4 arguments:
<py script name> <API Key> <Bus_Line> <Bus_line.csv>
show_bus_locations_yg833.py xxxxx-xxxxx-xxxxx-xxxxx-xxxxx B52 B52.csv

The csv file is a file out. Tested this with B52 and B65 bus line.
