# machine in this example only accepts strings ending in "1"
# the "A" state has a loop back at 0 and a 1 pointing to "B"
# B state has a loopback at 1 and a 0 pointing to "A"
def machine(s):
    state = "A"
    '''
    for i in s:
        if state == "A" and i == "1":
            state = "B"
        if state == "B" and i == "0":
            state = "A"
    '''
    for i in s:
        match state, i:
            case "A", "1":
                state = "B"
            case "B", "0":
                state = "A"


    return "accepted" if state == "B" else "Denied"

print(machine("000101001001"))