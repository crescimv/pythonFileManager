import os

username = input("enter your username: ")
print("Welcome " + username + "\nWhat would you like to do?\n1. Read file\n2. Append file\n3. Write (overwrite) file\n4. Create file\n5. Delete file\n6. Quit program")

programMenu = input("Choose an option: ")
while not programMenu == "6":
    if programMenu == "1":
        readFile = input("Enter the name of the file: ")
        f = open(readFile)
        print(f.read())
        for line in f:
            print(line)
        f.close()
    elif programMenu == "2":
        appendFile = input("Enter the name of the file: ")
        f = open(appendFile, "a")
        userAppend = input("Write what you would like to add to " + appendFile + ": ")
        f.write(userAppend)
        f.close()

        f = open(appendFile)
        print(f.read())
        for line in f:
            print(line)
        f.close()
    elif programMenu == "3":
        writeFile = input("Enter the name of the file: ")
        f = open(writeFile, "w")
        userWrite = input("Write what you would like to add to " + writeFile + ": ")
        f.write(userWrite)
        f.close()
    elif programMenu == "4":
        createFile = input("Enter the name of the file to be created: ")
        if not os.path.exists(createFile):
            f = open(createFile, "x")
            f.close()
        else:
            print("This file already exist.")
    elif programMenu == "5":
        deleteFile = input("Enter the name of the file to be deleted: ")
        if os.path.exists(deleteFile):
            os.remove(deleteFile)
        else:
            print("This file does not exist.")
    else:
        print("Input by user was not valid, please enter a number from 1-6 to choose from the menu: ")
print("Goodbye.")
