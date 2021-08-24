# ---------------------------------------------- #
# Title: Pickling and Error Handling
# Dev: rblake50
# ChangeLog:
#  rblake50, 08.17.2021, created script
#  rblake50, 08.24.2021, removed "Edit Player"
#            option (can be developed in the
#            future)
# ---------------------------------------------- #
# DESCRIPTION:
# This script reads a pickled object from a user-
# specified file and allows users to add player
# statistics (home runs and games) to a list
# of dictionary objects. The user can calculate
# the average number of home runs per 162 game
# season. All data can be saved (pickled) back
# to the same user-specified file.
# ---------------------------------------------- #
# ASSUMPTIONS:
# This script assumes that the pickled object
# being read is in the appropriate dictionary
# format (Name,hrs,gms). Reading an existing
# pickled object in a different format will
# present unhandled errors.

import pickle

# -- Declare data types -- #
lstData = []
dicPlayers = {}

class FileIO:
    """This class defines functions for file input and output"""
    def readFile(strFileName):
        """Reads a serialized file"""
        with open(strFileName, 'rb') as fileIncoming:
            lstData = pickle.load(fileIncoming)
        return lstData

    def overwriteFile(strFileName,lstData):
        """
        This function pickles a list and overwrites it to a file.
        :param strFileName (string) of file to save
        :param lstData (list) to pickle and save
        :return (string) of success message
        """
        with open(strFileName, 'wb') as file:
            pickle.dump(lstData, file)
        return "Success"

class Present:
    """This class presents information as text."""

    @staticmethod
    def printMenu():
        """
        This method displays the user menu.
        """
        print("""
        =========================================
        1. Add player
        2. Calculate average home runs per season
        3. Exit program (with save option)
        """)

    def printList(lstName):
        """
        Prints formatted elements of a list
        :param lstName (list) with items
        """
        msg = "Here are the players in your list:\n"+"="*32+"\n"
        for item in lstName:
            msg = msg + item["Name"] + "\n"
        print(msg)

class Calculate:
    """This class performs calculations of statistics."""

    def avgHR(name,lst):
        """
        Calculates the average number of home runs per 162 game season.
        :param name (string) of player in the list
        :return (float) average HRs per 162 game season
        """
        for player in lst:
            if name.lower() == player["Name"].lower():
                index = lst.index(player)

        # HRs per game
        numHRs = lst[index]["hrs"] / lst[index]["gms"]

        # HRs per season
        numHRs = numHRs * 162

        return numHRs

# -- Input -- #
strFileName = input("What file would you like to open? (Hint: try data.pickle) ")

# -- Deserializing data -- #
try:
    lstData = FileIO.readFile(strFileName)
except FileNotFoundError:
    print("Ugh! Your file was not found in the immediate directory.")
    input("You'll be starting from scratch. Otherwise, exit and start over using data.pickle.")

# -- Operations -- #
while True:
    # Show current players in list
    Present.printList(lstData)

    # Display menu
    Present.printMenu()
    choice = input("What is your selection? ")

    # Add player
    if choice == "1":
        player = input("Who do you want to add? ")
        try:
            homeRuns = float(input("How many home runs? "))
            games = float(input("In how many games? "))
        except ValueError:
            input("D'oh! You need to put a number for both. Let's start over.")
            continue
        else:
            dicPlayer = {"Name":player.title(),"hrs":homeRuns,"gms":games}
            lstData.append(dicPlayer)

    # Calculate average
    elif choice == "2":
        try:
            choiceCalc = input("Who do you want to calculate? ")
            HRperSeason = Calculate.avgHR(choiceCalc, lstData)
            print(choiceCalc.title() + " hit %.2f home runs per season." % HRperSeason)
            input("Press ENTER to return to menu.")
        except UnboundLocalError:
            print("Name not found on list. Try again!")
            input("Press ENTER")

    # Exit (and save if desired)
    elif choice == "3":
        choiceSave = input("Do you want to save? [y]es or [n]o\n" ).lower()
        if choiceSave == "y" or choiceSave == "yes":
            try:
                FileIO.overwriteFile(strFileName, lstData)
            except:
                print("Where's the file??")
            else:
                input("Data successfully pickled to " + strFileName + ". Press ENTER to exit.")
            break
        elif choiceSave == "n" or choiceSave == "no":
            input("Good-bye! Press ENTER to exit.")
            break
        else:
            input("You entered nonsense... Let's go back to the menu.")
            continue

    # Invalid selection
    else:
        input("Invalid choice. Press ENTER to return to the menu.")
