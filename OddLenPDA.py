'''
Create A python program to model a Pushdown Automata that only accepts strings of off lengths (rejects even lengths)
'''

stack = []

input = input("enter a string: ")
stack.append(0)

for i, j in enumerate(input):
    if stack:
        stack.pop()
    else:
        stack.append(0)

if not stack:
    print("Program Accepts")
else:
    print("Program Rejects")