import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it will charge you 2 dollar per day")

elif type == "t2.medium":
    print ("it will charge you 4 dollar per day") 

elif type == "t2.large":
    print ("it will charge you 6 dollar per day")

elif type == "t2.xlarge":
    print ("it will charge you 8 dollar per day")

else:
    print("please provide a valid instance type")