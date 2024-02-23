import os

folders = input(" please provide list of folders names with spaces in between:" ).split()


for folder in folders:

    try:
        files = os.listdir(folder)
    except FileNotFoundError:
        print("please provide a valid folder name , looks like folder does not exist:" + folder)
        break
    except PermissionError:
        print("no acces to this folder:" + folder)
        break

    print("==listing files for the floder - " + folder)
    
    for file in files:
        print(file)