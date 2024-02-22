import sys

type = sys.argv[1]

if type == "t2.micro":
    print("okay, we will create instance")
else:
    print("your input is not t2.micro , so we cannot create instance")