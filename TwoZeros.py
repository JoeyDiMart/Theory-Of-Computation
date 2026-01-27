# Create a proof (by writing a program) that creates a Deterministic Finite Automata that accepts
# all strings within the alphabet {0,1} and contains at least two zeros


def isAccepted(s, i=0, c=0):
    if s[0] == "0" and c == 0:
        i += 1
        c = 1
        isAccepted(s[i:], i, c)
    elif s[0] == "0" and c == 1:
        return "Accepted"
    else:
        if s[-1] == s[0]:
            return "Not Accepted"
    i += 1
    isAccepted(s[i:], i, c)


s = input("enter a string of 1's and 0's: ")
print(isAccepted(s))