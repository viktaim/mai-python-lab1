from .converter import *
from .errors import *


def tokenize(lst):
    mainLst = []
    separateElem = ''

    for elem in range(len(lst)):
        if lst[elem] != ' ' and lst[elem] not in ["/", "*"]:
            if lst[elem] == '-':
                if elem == 0 or lst[elem-1] in ['-', '+', "/", "*"]:
                    separateElem += lst[elem]

            elif lst[elem] == "+":
                if elem == 0 or lst[elem-1] in ['-', '+', "/", "*"]:
                    separateElem += ''
            else:
                separateElem += lst[elem]

        if lst[elem] in ["-", '+', "/", "*"]:
            if lst[elem] == '-' or lst[elem] == "+":
                if elem != 0:

                    if lst[elem-1] not in ['-', '+', "/", "*"]:
                        mainLst.append(separateElem)
                        separateElem = ''
                        mainLst.append(lst[elem])

            else:
                mainLst.append(separateElem)
                separateElem = ''
                mainLst.append(lst[elem])

        if elem == len(lst) - 1:
            mainLst.append(separateElem)

    return mainLst


def check_token_sequence(tokens):
    expecting = "number"
    for token in tokens:
        if expecting == 'number':
            try:
                float(token)
            except ValueError:
                return False
        else:
            try:
                float(token)
            except ValueError:
                if token not in ['+', "-", "*", "/"]:
                    return False
            else:
                return False

        if expecting == 'number':
            expecting = 'operator'
        else:
            expecting = 'number'

    return True


def validate(lst):
    if len(lst) == 0:
        raise VacuousExpression("Выражение пустое")

    if lst[-1] in ["+", "-", "*", "/"]:
        raise MissingOperand("Оператор в конце выражение")

    if not check_token_sequence(lst):
        raise InvalidExpression("Недопустимое выражение")


def convert_to_numbers(tokens):
    result = []
    for token in tokens:
        if token in ["+", "-", "*", "/"]:
            result.append(token)
        else:
            result.append(float(token))
    return result


def evaluate(tokens):
    state = 0
    elem = 0

    while state == 0:
        if tokens[elem] == '*' or tokens[elem] == '/':
            if tokens[elem] == '*':
                num = tokens[elem-1] * tokens[elem+1]
                tokens[elem-1:elem+2] = [num]
                elem -= 2
            else:
                if tokens[elem + 1] == 0:
                    raise DivisionByZeroError("Деление на 0")
                else:
                    num = tokens[elem - 1] / tokens[elem + 1]
                    tokens[elem-1:elem+2] = [num]
                    elem -= 2
        else: elem += 1

        if '*' not in tokens and '/' not in tokens:
            state = 1
    elem = 0

    while state == 1:
        if tokens[elem] == '+' or tokens[elem] == '-':
            if tokens[elem] == '+':
                num = tokens[elem-1] + tokens[elem+1]
                tokens[elem-1:elem+2] = [num]
                elem -= 2
            else:
                num = tokens[elem - 1] - tokens[elem + 1]
                tokens[elem-1:elem+2] = [num]
                elem -= 2
        else: elem += 1

        if '+' not in tokens and '-' not in tokens:
            state = 2

    return tokens[0]



def calculate_expression(expression):
    tokens = tokenize(expression)
    validate(tokens)
    tokens = convert_to_numbers(tokens)
    result = evaluate(tokens)

    return result