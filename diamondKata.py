import string
import sys
from printer import Printer

def return_alphabet_section(character):
    character = character.upper()
    alphabet = list(string.ascii_uppercase)
    new_alph = alphabet[:alphabet.index(character) + 1]
    return new_alph


def make_diamond(section):
    top_of_diamond = []

    for index, letter in enumerate(section):
        if index == 0:
            space = " " * (len(section) - 1)
            top_of_diamond.append(space + letter)
        else:
            first_space = " " * (len(section) - (index + 1))
            second_space = " " * (index + (index - 1))
            top_of_diamond.append(first_space + letter + second_space + letter)

    bottom_of_diamond = list(reversed(top_of_diamond))
    del bottom_of_diamond[0]
    diamond_list = top_of_diamond + bottom_of_diamond
    diamond = "\n".join(diamond_list)

    return diamond


def run_functions(args, printer):
    if not validate_args(args):
        printer.display("Please provide one argument")
    else:
        usr_input = args[1]
        all_letters = list(string.ascii_letters)

        if usr_input not in all_letters:
            printer.display("AAAGHHHH")
        else:
            section = return_alphabet_section(usr_input)
            diamond = make_diamond(section)
            printer.display(diamond)

def validate_args(args):
    if len(args) != 2:
        return False
    else:
        return True


def main():
    printer = Printer()
    run_functions(sys.argv, printer)



if __name__ == "__main__":
    main()