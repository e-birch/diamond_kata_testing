import unittest
from diamondKata import *

# class PrinterMock:
#     text = ""
#     def display(self, text):
#         return text

class PrinterMock:
    text = ""

    def display(self, text):
        self.text += str(text)


class TestDiamond(unittest.TestCase):

    def test_return_alphabet_section(self):
        input_char = "E"
        section = return_alphabet_section(input_char)
        self.assertListEqual(section, ["A", "B", "C", "D", "E"])

    def test_return_alphabet_section_lower(self):
        input_char = "e"
        section = return_alphabet_section(input_char)
        self.assertListEqual(section, ["A", "B", "C", "D", "E"])


    def test_make_diamond_e(self):
        section = ["A", "B", "C", "D", "E"]
        diamond = make_diamond(section)
        exp_diamond = ""
        exp_diamond += "    A\n"
        exp_diamond += "   B B\n"
        exp_diamond += "  C   C\n"
        exp_diamond += " D     D\n"
        exp_diamond += "E       E\n"
        exp_diamond += " D     D\n"
        exp_diamond += "  C   C\n"
        exp_diamond += "   B B\n"
        exp_diamond += "    A"
        self.assertEqual(diamond, exp_diamond)

    def test_make_diamond_h(self):
        section = ["A", "B", "C", "D", "E", "F", "G", "H"]
        diamond = make_diamond(section)
        exp_diamond = ""
        exp_diamond += "       A\n"
        exp_diamond += "      B B\n"
        exp_diamond += "     C   C\n"
        exp_diamond += "    D     D\n"
        exp_diamond += "   E       E\n"
        exp_diamond += "  F         F\n"
        exp_diamond += " G           G\n"
        exp_diamond += "H             H\n"
        exp_diamond += " G           G\n"
        exp_diamond += "  F         F\n"
        exp_diamond += "   E       E\n"
        exp_diamond += "    D     D\n"
        exp_diamond += "     C   C\n"
        exp_diamond += "      B B\n"
        exp_diamond += "       A"
        self.assertEqual(diamond, exp_diamond)

    def test_make_diamond_a(self):
        section = ["A"]
        diamond = make_diamond(section)
        exp_diamond = "A"
        self.assertEqual(diamond, exp_diamond)

    def test_run_functions_E(self):
        args = ["diamondKata.py", "E"]
        printer = PrinterMock()
        run_functions(args, printer)
        output = printer.text
        exp_diamond = ""
        exp_diamond += "    A\n"
        exp_diamond += "   B B\n"
        exp_diamond += "  C   C\n"
        exp_diamond += " D     D\n"
        exp_diamond += "E       E\n"
        exp_diamond += " D     D\n"
        exp_diamond += "  C   C\n"
        exp_diamond += "   B B\n"
        exp_diamond += "    A"
        self.assertEqual(output, exp_diamond)

    def test_run_functions_number(self):
        args = ["diamondKata.py", "0"]
        printer = PrinterMock()
        run_functions(args, printer)
        output = printer.text
        self.assertEqual(output, "AAAGHHHH")

    def test_run_functions_special_character(self):
        args = ["diamondKata.py", "?"]
        printer = PrinterMock()
        run_functions(args, printer)
        output = printer.text
        self.assertEqual(output, "AAAGHHHH")

    def test_run_functions_multiple_letters(self):
        args = ["diamondKata.py", "abcde"]
        printer = PrinterMock()
        run_functions(args, printer)
        output = printer.text
        self.assertEqual(output, "AAAGHHHH")

    def test_run_functions_multiple_args(self):
        args = ["diamondKata.py", "a", "b"]
        printer = PrinterMock()
        run_functions(args, printer)
        output = printer.text
        self.assertEqual(output, "Please provide one argument")

    def test_run_functions_no_args(self):
        args = ["diamondKata.py"]
        printer = PrinterMock()
        run_functions(args, printer)
        output = printer.text
        self.assertEqual(output, "Please provide one argument")





if __name__ == "__main__":
    unittest.main()
