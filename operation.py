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

import util


def check(operations, calculations):
    # print(calculations)
    print(calculations)
    while len(operations) > 1:
        if "/" in operations:
            div(operations[util.findOperationAt("/", calculations)], calculations)
            # operations[util.findOperationAt("/", calculations)] = ""
        elif "*" in operations:
            multiply(operations[util.findOperationAt("*", calculations)], calculations)
            # operations[util.findOperationAt("*", calculations)] = ""
        elif "+" in operations:
            add(operations[util.findOperationAt("+", calculations)], calculations)
            # operations[util.findOperationAt("+", calculations)] = ""
        elif "-" in operations:
            subtract(operations[util.findOperationAt("-", calculations)], calculations)
            # operations[util.findOperationAt("-", calculations)] = ""

    if len(calculations) == 1:
        print("The result is:", calculations[0])


def div(operation, calculations):
    print(calculations)
    operationAt = util.findOperationAt(operation, calculations)
    firstNumber = calculations[operationAt - 1]
    secondNumber = calculations[operationAt + 1]
    result = float(firstNumber) / float(secondNumber)
    print(result)

    calculations[operationAt] = result
    calculations.remove(firstNumber)
    calculations.remove(secondNumber)


def multiply(operation, calculations):
    print(calculations)
    operationAt = util.findOperationAt(operation, calculations)
    firstNumber = calculations[operationAt - 1]
    secondNumber = calculations[operationAt + 1]
    result = float(firstNumber) * float(secondNumber)
    print(result)

    calculations[operationAt] = result
    calculations.remove(firstNumber)
    calculations.remove(secondNumber)


def add(operation, calculations):
    print(calculations)
    operationAt = util.findOperationAt(operation, calculations)
    firstNumber = calculations[operationAt - 1]
    secondNumber = calculations[operationAt + 1]
    result = float(firstNumber) + float(secondNumber)
    print(result)

    calculations[operationAt] = result
    calculations.remove(firstNumber)
    calculations.remove(secondNumber)


def subtract(operation, calculations):
    print(calculations)
    operationAt = util.findOperationAt(operation, calculations)
    firstNumber = calculations[operationAt - 1]
    secondNumber = calculations[operationAt + 1]
    result = float(firstNumber) - float(secondNumber)
    print(result)

    calculations[operationAt] = result
    calculations.remove(firstNumber)
    calculations.remove(secondNumber)
