# ------------------------------------------------------------------------ #
# Title: Assignment 05
# Description: Working with Dictionaries and Files
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
#  RRoot,1.1.2030,Created started script
#  rblake50,7/31/21,Added code to complete assignment 5
# GitHub link: https://github.com/rblake50/IntroToProg-Python
# ------------------------------------------------------------------------ #

# -- Data -- #
# declare variables and constants
objFile = "ToDoList.txt"   # An object that represents a file
strData = ""  # A row of text data from the file
strTask = "" # First element of strData (separated by comma)
strPriority = "" # Second element of strData (separated by comma)
dicRow = {}    # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strMenu = ""   # A menu of user options
strChoice = "" # A Capture the user option selection
boolFound = False # Indicator if task is found in the list

# Initialize
strMenu = """
    Menu of Options
    1) Show current data
    2) Add a new item.
    3) Remove an existing item.
    4) Save Data to File
    5) Exit Program
    """

# -- Processing -- #
# Step 1 - When the program starts, load the any data you have
# in a text file called ToDoList.txt into a python list of dictionaries rows (like Lab 5-2)
objFileText = open(objFile,"r")
for strData in objFileText:
    # Assume comma separated values
    strTask = strData.split(",")[0].strip()
    strPriority = strData.split(",")[1].strip()
    dicRow = {"Task":strTask,"Priority":strPriority}
    lstTable.append(dicRow)
objFileText.close()

# -- Input/Output -- #
# Step 2 - Display a menu of choices to the user
while (True):
    print(strMenu)
    strChoice = str(input("Which option would you like to perform? [1 to 5] - "))
    #print()  # adding a new line for looks
    # Step 3 - Show the current items in the table
    if (strChoice.strip() == '1'):
        print("Task, Priority\n==============")
        for item in lstTable:
            print(item["Task"]+", "+item["Priority"])
        input("Press enter to return to menu.")
        continue
    # Step 4 - Add a new item to the list/Table
    elif (strChoice.strip() == '2'):
        strTask = input("What task would you like to add? ")
        strPriority = input("What priority is this task? ")
        dicRow = {"Task":strTask,"Priority":strPriority}
        lstTable.append(dicRow)
        continue
    # Step 5 - Remove a new item from the list/Table
    elif (strChoice.strip() == '3'):
        strTask = input("Which item would you like to remove? Type the \"Task\": ")
        for item in lstTable:
            if strTask == item["Task"]:
                boolFound = True
                lstTable.remove(item)
                print("Item deleted")
        if boolFound == False:
            print("The Task you entered was not found...")
        input("Press ENTER to continue")
        boolFound = False
        continue
    # Step 6 - Save tasks to the ToDoToDoList.txt file
    elif (strChoice.strip() == '4'):
        objFileText = open(objFile,"w")
        for item in lstTable:
            objFileText.write(item["Task"]+", "+item["Priority"]+"\n")
        objFileText.close()
        input("Data has been saved to file. Press ENTER to return to menu.")
        continue
    # Step 7 - Exit program
    elif (strChoice.strip() == '5'):
        input("Good-bye!")
        break  # and Exit the program
