# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []
    for i, next in enumerate(text):
        if next in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append(Bracket(next, i+1))

        if next in ")]}":
            # Process closing bracket, write your code here
            # si il n'y a rien dans le stack, c'est qu'il manque un opening bracket
            if not opening_brackets_stack:
                return i + 1
            current_bracket = opening_brackets_stack.pop()
            if not are_matching(current_bracket.char, next):
                return i+1
    # si le stack n'est pas vide à la fin, c'est qu'il manque au moins un bracket
    if opening_brackets_stack:
        return opening_brackets_stack[0].position
    else :
        return "Success"


def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)


if __name__ == "__main__":
    main()
