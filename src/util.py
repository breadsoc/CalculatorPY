"""
CalculatorPY  Copyright (C) 2021  nukestye, exdoth
    This program comes with ABSOLUTELY NO WARRANTY; for details type `show w'.
    This is free software, and you are welcome to redistribute it
    under certain conditions; type `show c' for details.

The hypothetical commands `show w' and `show c' should show the appropriate
parts of the General Public License.  Of course, your program's commands
might be different; for a GUI interface, you would use an "about box".

  You should also get your employer (if you work as a programmer) or school,
if any, to sign a "copyright disclaimer" for the program, if necessary.
For more information on this, and how to apply and follow the GNU GPL, see
<https://www.gnu.org/licenses/>.

  The GNU General Public License does not permit incorporating your program
into proprietary programs.  If your program is a subroutine library, you
may consider it more useful to permit linking proprietary applications with
the library.  If this is what you want to do, use the GNU Lesser General
Public License instead of this License.  But first, please read
<https://www.gnu.org/licenses/why-not-lgpl.html>.
"""

from src import Errors


def operationsFrom(string):
    """

    Takes in a String that may or may not contain operations such as "/, +, -, *" and returns in a
    list that determines the order they are supposed to go at.

    :param string: A piece of string that contains operations
    :return: A list that contains the operations found in the string
    """
    List = []

    for i in range(len(string)):
        if string[i] == "/":
            List.append("/")
    for i in range(len(string)):
        if string[i] == "*":
            List.append("*")
    for i in range(len(string)):
        if string[i] == "+":
            List.append("+")
    for i in range(len(string)):
        if string[i] == "-":
            List.append("-")

    return List


def findOperationAt(operation, stringOfOperations):
    """

    Looks for the operation that has to be carried out in the calculations

    :param operation: The operation that has to be carried out
    :param stringOfOperations: A list of operations that are inside the calculations
    :return: A int index of where the operation is at in the string
    """
    num = stringOfOperations.index(operation)

    return num


def toList(string):
    """

    Converts the string into a list

    :param string: A sentence that needs to be converted into a list
    :return: A list of the string without any spaces(" ")
    """
    List = []
    for i in range(len(string)):
        if string[i] != " ":
            if string[i] == "." and string[i + 1] != "" and string[i - 1] != "":
                List.append(string[i - 1] + string[i] + string[i + 1])
            else:
                # 0.0: 0. = i - 1; .0 = i + 1
                List.append(string[i])

    return List


def checksum(string):
    """
    Takes in a string that is checked to see if the calculation provided is in correct format

    :param string: The calculations needed to be parsed over
    """

    for i in range(len(string)):
        if (string[i] in ("/", "*", "+", "-")) and i <= 1:
            raise Errors.OperationError("cannot start with an operator")
        elif (string[i] in ("/", "*", "+", "-")) and i >= len(string) - 1:
            raise Errors.OperationError("cannot end with an operator")
        elif (string[i] in ("/", "*", "+", "-")) \
                and (string[i + 1] in ("/", "*", "+", "-")
                     or string[i - 1] in ("/", "*", "+", "-")):
            raise Errors.FormatError("an operator cannot be next to another operator")
