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

from src import util


def check(operations, calculations):
    """

    Coordinates the path the program should take. Looks at operations needed to be carried out
    and uses the format DMAS(Divide, Multiply, Add, Subtract) to get the result.

    :param operations: The operations in the string given by the user
    :param calculations: The raw string given by the user
    """
    print("Calculations at func check: " + str(calculations))
    for i in range(len(operations)):
        if operations[i] == "/":
            div(operations[i], calculations)
        if operations[i] == "*":
            multiply(operations[i], calculations)
        if operations[i] == "+":
            add(operations[i], calculations)
        if operations[i] == "-":
            subtract(operations[i], calculations)

    if len(calculations) == 1:
        print("The result is:", calculations[0])


def div(operation, calculations):
    """

    The Divide function; Divides the numerator by the denominator.

    :param operation: The operations in the string given by the user
    :param calculations: The raw string given by the user
    """
    # print("Calculations at func div: " + str(calculations))

    operationAt = util.findOperationAt(operation, calculations)
    firstNumber = calculations[operationAt - 1]
    secondNumber = calculations[operationAt + 1]

    # print("var operationAt in div: " + str(operationAt))
    # print("var firstNumber in div: " + str(firstNumber))
    # print("var secondNumber in div: " + str(secondNumber))

    result = float(firstNumber) / float(secondNumber)
    # print(result)

    calculations[operationAt] = result
    calculations.pop(operationAt - 1)
    calculations.pop(operationAt)


def multiply(operation, calculations):
    """

    The Multiply function; Multiplies the first number given by the second number.

    :param operation: The operations in the string given by the user
    :param calculations: The raw string given by the user
    """
    # print("Calculations at func multiply: " + str(calculations))

    operationAt = util.findOperationAt(operation, calculations)
    firstNumber = calculations[operationAt - 1]
    secondNumber = calculations[operationAt + 1]

    # print("var operationAt in multiply: " + str(operationAt))
    # print("var firstNumber in multiply: " + str(firstNumber))
    # print("var secondNumber in multiply: " + str(secondNumber))

    result = float(firstNumber) * float(secondNumber)
    # print(result)

    calculations[operationAt] = result
    calculations.pop(operationAt - 1)
    calculations.pop(operationAt)


def add(operation, calculations):
    """

    The Addition function; Adds the first number to the second number.

    :param operation: The operations in the string given by the user
    :param calculations: The raw string given by the user
    """
    # print("Calculations at func add: " + str(calculations))

    operationAt = util.findOperationAt(operation, calculations)
    firstNumber = calculations[operationAt - 1]
    secondNumber = calculations[operationAt + 1]

    # print("var operationAt in add: " + str(operationAt))
    # print("var firstNumber in add: " + str(firstNumber))
    # print("var secondNumber in add: " + str(secondNumber))

    result = float(firstNumber) + float(secondNumber)
    # print(result)

    calculations[operationAt] = result
    calculations.pop(operationAt - 1)
    calculations.pop(operationAt)


def subtract(operation, calculations):
    """

    The Subtraction function; Subtracts the second number from the first number.

    :param operation: The operations in the string given by the user
    :param calculations: The raw string given by the user
    """
    # print("Calculations at func subtract: " + str(calculations))

    operationAt = util.findOperationAt(operation, calculations)
    firstNumber = calculations[operationAt - 1]
    secondNumber = calculations[operationAt + 1]

    # print("var operationAt in subtract: " + str(operationAt))
    # print("var firstNumber in subtract: " + str(firstNumber))
    # print("var secondNumber in subtract: " + str(secondNumber))

    result = float(firstNumber) - float(secondNumber)
    # print(result)

    calculations[operationAt] = result
    calculations.pop(operationAt - 1)
    calculations.pop(operationAt)
