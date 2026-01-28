'''
Name: Joseph DiMartino
Date: 1.25.2026
Program: Create a program to represent the Deterministic Finite Automaton that only accepts strings ending with a '1' in the
third to last position
'''


def isAccepted(s):
    #states = ['0', '1', '10', '11', '100', '101', '110', '111']
    accepted_endings = ['100', '101', '110', '111']  # matches the 4 final states
    transitions = {  # all 8 states + the location it'll go to if a 1 or a 0
        '0': {'0': '0', '1': '1'},
        '1': {'0': '10', '1': '11'},
        '10': {'0': '100', '1': '101'},
        '11': {'0': '110', '1': '111'},
        '100': {'0': '0', '1': '1'},
        '101': {'0': '10', '1': '11'},
        '110': {'0': '100', '1': '101'},
        '111': {'0': '110', '1': '111'}
    }
    current_state = '0'  # start at 0

    for i in s:
        if i not in ['0', '1']:
            return "Not valid input"
        current_state = transitions[current_state][i]

    return current_state in accepted_endings


s = input("enter a binary string: ").strip()
print(isAccepted(s))