# prove a DFA that is divisible by 3


def isAccepted(s):
    works = False
    counter = 0
    for i in s:
        counter += 1
        works = False
        if counter % 3 == 0:
            works = True

    return "Accepted" if works else "Not Accepted"


s = input("enter a binary string: ")
print(isAccepted(s))