# Create a proof (by writing a program) that creates a Deterministic Finite Automata that accepts
# all strings within the alphabet {0,1} and contains at least two zeros


def isAccepted(s, c=0):
    if s[0] == "0" and c == 0:
        c = 1
        return isAccepted(s[1:], c)
    elif s[0] == "0" and c == 1:
        return "Accepted"
    elif len(s) == 1:
        return "Not Accepted"
    else:
        return isAccepted(s[1:], c)


s = input("enter a string of 1's and 0's: ")
print(isAccepted(s))