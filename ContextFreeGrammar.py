'''
Name: Joseph DiMartino
Class: CSC 320: Theory of Computation
Program: Create an arbitrary Context-Free Grammar that will take in User Input
'''
import random

def takeInput():
    counter = int(input("Enter number of strings you'd like to print: "))  # counter = # of times to print some string
    cfg_input = input("enter the Context-Free Grammar in the format X aXa; X bXb; X *   : ").split(";")
    cfg = {}  # cfg = Context-Free Grammar dict

    for i in cfg_input:
        i = i.split()
        try:
            cfg[i[0]].append(i[1])
        except Exception:
            cfg[i[0]] = [i[1]]

    return cfg, counter


def makeStrings(cfg, counter):
    print(cfg, "\n")
    cfg_before = []
    cfg_after = []
    cfg_stack = []
    cfg_strings = []
    i = 0
    while i < counter:
        cfg_stack.append(list(cfg.keys())[0])

        while cfg_stack:
            curr_state = cfg_stack.pop()
            curr_item = cfg[curr_state][random.randint(0, len(cfg[curr_state])-1)]
            if curr_item == "*":
                cfg_strings.append(cfg_before + cfg_after)
                break
            for j in curr_item:
                hit_state = False


                if (hit_state is False) and (j.islower()):
                    cfg_before += j
                elif j.isupper():
                    hit_state = True
                    cfg_stack.append(j)
                elif (hit_state is True) and (j.islower()):
                    cfg_after += j

        i += 1

    return cfg_strings


def printStrings(cfg_strings):  # 
    for i in cfg_strings:
        print(''.join(i))
    return


def main():
    cfg, counter = takeInput()
    cfg_strings = makeStrings(cfg, counter)
    printStrings(cfg_strings)


if __name__ == "__main__":
    main()
