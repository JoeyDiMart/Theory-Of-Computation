'''
Name: Joseph DiMartino
Date: 1.25.2026
Program: Create a program to represent the Deterministic Finite Automaton that only accepts strings ending with a '1' in the
third to last position
'''


def isAccepted(s):
    ending_sequence = []
    for i in s:
        if len(ending_sequence) != 3:
            ending_sequence += i
            continue

        ending_sequence[0] = ending_sequence[1]
        ending_sequence[1] = ending_sequence[2]
        ending_sequence[2] = i
    print(ending_sequence)

    # the below can just be ending_sequence[0] = "1" but I wanted to match the diagram from the book
    if (ending_sequence == ["1", "0", "0"] or ending_sequence == ["1", "0", "1"] or ending_sequence == ["1", "1", "0"]
            or ending_sequence == ["1", "1", "1"]):
        return "Accepted"
    else:
        return "Not Accepted"


s = input("enter a binary string: ")
print(isAccepted(s))