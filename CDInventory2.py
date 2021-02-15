#------------------------------------------#
# Title: CDInventory.py
# Desc: Starter Script for Assignment 05
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
#AHertel, 2021-Feb-14, updated file to include list of dicts, load existing data, add entry deletion
#------------------------------------------#

# Declare variables

strChoice = '' # User input
dicRow = {}  # empty dictionary
lstTbl = []  # list of lists to hold data
lstRow = []  # list of data row
strFile = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# Get user Input
print('The Magic CD Inventory\n')
while True:
    #Display menu allowing the user to choose:
    print('[a] load Inventory from file\n[b] Add CD\n[c] Display Current Inventory')
    print('[d] delete CD from Inventory\n[e] Save Inventory to file\n[exit] exit')
    strChoice = input('a, b, c, d, e or exit: ').lower()  # convert choice to lower case at time of input
    print()

    if strChoice == 'exit':
        #exit the program
        break
    
    if strChoice == 'a':
        #load existing data 
        print("Your Inventory")
        print('ID | CD Title | Artist')
        file = open("CDInventory.txt", "r")
        for line in file:
            print(line)
        file.close()
        
    elif strChoice == 'b': 
        #Add data to the table
        
        strID=int(input("Enter CD ID#"))
        strTitle=input("Enter CD Title")
        strArtist=input("Enter CD Artist")
        new_cd = [strID, strTitle, strArtist]
        lstTbl.append(new_cd)
        
    elif strChoice == 'c':
        #Display the current data
        print('ID | CD Title | Artist')
        file = open("CDInventory.txt", "r")
        for line in file:
            print(line)
        file.close()
            
    elif strChoice == 'd':
        #delete an entry
        print('ID | CD Title | Artist')
        file = open("CDInventory.txt", "r")
        for line in file:
            print(line)
        file.close()
        user_input = input("Please enter the ID for the CD you'd like to delete. ")
        if line == user_input:
            lstTbl.pop(line)
        
    elif strChoice == 'e':
        #Save the data to a text file CDInventory.txt
        strFile = open("CDInventory.txt", "a+")
        for row in lstTbl:
            strFile.write("[{} | {} | {}]\n".format(*row))
        strFile.close()
        
    else:
        print('Please choose either a, b, c, d, e, or type "exit"')

