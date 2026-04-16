'''
Programmer: Joseph DiMartino
Date: 4.16.2026
Program: Create a Universal Turing Machine (from Section 8.3 in the textbook)
'''
from collections import defaultdict  # used Claude to get info about this, made error handling easy


# created a main class for the UTM with the rules, define start/halt, etc. that a UTM has
class UTM:
    BLANK = "_"
    LEFT = "L"
    RIGHT = "R"
    STAY = "S"

    def __init__(self, start: str, halts: set[str], rules: dict[tuple, tuple], tape: list[str]):
        self.start = start
        self.halts = halts
        self.rules = rules  # Store rules by state, read_symbol

        self.tape = defaultdict(lambda: self.BLANK)
        for i, sym in enumerate(tape):
            self.tape[i] = sym

        self.state = start
        self.pos = 0
        self.steps = 0

    def instantaneous_description(self):  # prints out the current description of hte machine (current state, where on the tape)
        if not self.tape:
            return f"[{self.state}|{self.BLANK}]"

        lo = min(self.tape.keys())
        hi = max(self.tape.keys())
        lo = min(lo, self.pos)
        hi = max(hi, self.pos)

        parts = []
        for i in range(lo, hi + 1):
            sym = self.tape[i]
            if i == self.pos:
                parts.append(f"[{self.state}|{sym}]")
            else:
                parts.append(sym)
        return "".join(parts)   # print out the link for the description of the machine

    def step(self):  # execure one step
        if self.state in self.halts:
            return False  # fail

        key = (self.state, self.tape[self.pos])
        if key not in self.rules:
            return False  # fail

        new_state, write_sym, direction = self.rules[key]

        self.tape[self.pos] = write_sym
        self.state = new_state

        # move head
        if direction == self.RIGHT:
            self.pos += 1
        elif direction == self.LEFT:
            self.pos -= 1
        elif direction == self.STAY:
            pass  # head does not move

        self.steps += 1
        return True

    def run(self, max_steps: int = 1000, verbose: bool = True):

        self.state = self.start
        self.pos = 0

        # repeat forever, based off pseudocode from textbook but also a way to stop infinite loops thank you Claude (even though the example inputs wouldn't go on infinitely)
        for i in range(max_steps):
            if verbose:
                print(self.instantaneous_description())   # print(id)

            if self.state in self.halts:
                break

            if not self.step():  # no applicable rule so halt
                if verbose:
                    print(self.instantaneous_description())
                    print(f"\n[No rule for ({self.state}, "
                          f"'{self.tape[self.pos]}') == implicit halt]")
                break
        else:
            if verbose:
                print(f"\n[Reached step limit of {max_steps}]")

        if verbose:
            tape_str = self._tape_contents()
            print(f"\n--- Halted in state '{self.state}' after {self.steps} step(s) ---")
            print(f"Final tape: {tape_str}")

        return self.state

    def _tape_contents(self):
        if not self.tape:
            return self.BLANK
        lo = min(self.tape.keys())
        hi = max(self.tape.keys())
        return "".join(self.tape[i] for i in range(lo, hi + 1))


def parse_utm_description(description: str, tape_input: str) -> UTM:

    lines = [l.strip() for l in description.strip().splitlines() if l.strip()]
    start = lines[0]
    halts = set(lines[1].split())
    rules = {}

    for line in lines[2:]:

        parts = [p.strip() for p in line.replace(",", " ").split()]
        if len(parts) != 5:
            raise ValueError(f"Bad rule (expected 5 fields): '{line}'")
        q, read, new_q, write, direction = parts
        rules[(q, read)] = (new_q, write, direction.upper())

    tape = list(tape_input) if tape_input else [UTM.BLANK]
    return UTM(start=start, halts=halts, rules=rules, tape=tape)

def demo_binary_increment():
    """
    TM that increments a binary number written on the tape.
    e.g.  1011  →  1100
    """
    print("=" * 60)
    print("DEMO 1: Binary increment  (1011 → 1100)")
    print("=" * 60)

    # define description from example in textbook
    description = """\
q0
qh
q0,0,q0,0,R
q0,1,q0,1,R
q0,_,q1,_,L
q1,1,q1,0,L
q1,0,qh,1,S
q1,_,qh,1,S"""

    utm = parse_utm_description(description, "1011")
    utm.run()
    print()


def demo_palindrome_checker():
    """
    TM that accepts binary palindromes.
    Accepts:  0, 1, 00, 11, 010, 101, 0110, ...
    Rejects:  01, 10, 001, ...

    Strategy: repeatedly compare leftmost and rightmost unread symbols.
    Blank them if they match; reject if they differ.
    Accept if tape is empty (or single symbol remains).
    """
    print("=" * 60)
    print("DEMO 2: Palindrome checker (accepts '1001')")
    print("=" * 60)

    description = """\
q0
qa qr
q0,_,qa,_,S
q0,0,q1,X,R
q0,1,q4,X,R
q0,X,q0,X,R
q1,0,q1,0,R
q1,1,q1,1,R
q1,X,q1,X,R
q1,_,q2,_,L
q2,0,q3,X,L
q2,X,qa,X,S
q2,_,qa,_,S
q2,1,qr,1,S
q3,0,q3,0,L
q3,1,q3,1,L
q3,X,q3,X,L
q3,_,q0,_,R
q4,0,q4,0,R
q4,1,q4,1,R
q4,X,q4,X,R
q4,_,q5,_,L
q5,1,q3,X,L
q5,X,qa,X,S
q5,_,qa,_,S
q5,0,qr,0,S"""

    utm = parse_utm_description(description, "1001")
    final = utm.run()
    print(f"Result: {'ACCEPT' if final == 'qa' else 'REJECT'}\n")


def demo_unary_addition():
    print("=" * 60)
    print("DEMO 3: Unary addition  (111+11 → 11111)")
    print("=" * 60)

    description = """\
q0
qh
q0,1,q0,1,R
q0,0,q1,1,R
q1,1,q1,1,R
q1,_,q2,_,L
q2,1,qh,_,S"""

    utm = parse_utm_description(description, "111011")
    utm.run()
    print()


if __name__ == "__main__":
    # the three examples from the book all in their own funcs
    demo_binary_increment()
    demo_palindrome_checker()
    demo_unary_addition()
