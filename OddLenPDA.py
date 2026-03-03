'''
Create A python program to model a Pushdown Automata that only accepts strings of off lengths (rejects even lengths)
'''

stack = []

input = input("enter a string: ")
length = len(input)
stack.append(0)

for i in range(0, length):
    if stack:  # if something in stack pop
        stack.pop()
    else:  # if nothing in stack append something
        stack.append(0)

if not stack:
    print("Program Accepts")
else:
    print("Program Rejects")