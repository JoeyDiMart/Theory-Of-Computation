'''
create a python program that makes sure there's an equal # of ( and )
'''

input = input("Enter a string with '(' and ')': ")
stack = []

for i in input:
    if i == "(":
        if 1 in stack:
            stack.pop()
        else:
            stack.append(0)
    elif i == ")":
        if 1 in stack or not stack:
            stack.append(1)
        else:
            stack.pop()

if not stack:
    print("Program Accepts")
else:
    print("Program Rejects")