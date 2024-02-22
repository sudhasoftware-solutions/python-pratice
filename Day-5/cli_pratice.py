import sys

def add (num1, num2):
    add = num1 +num2
    return add

def sub(num1,num2):
    s = num1 - num2
    return s

def div(num1 , num2):
    d = num1 /num2
    return d

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "add":
    output = add(num1 , num2)
    print(output)


if operation == "-":
    output = sub(num1 , num2)
    print(output) 

if operation == "/":
    output = div(num1 , num2)
    print(output)    