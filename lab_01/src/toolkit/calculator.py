from .errors import *

def tokenize(lst):
    mainLst = []
    separateElem = ''

    for elem in range(len(lst)):
        if lst[elem] != ' ' and lst[elem] not in ["/", "*"]:
            if lst[elem] == '-':
                if elem == 0:
                    separateElem += lst[elem]
                elif lst[elem-1] in ['-', '+', "/", "*"]:
                    separateElem += lst[elem]

            elif lst[elem] == "+":
                if elem == 0:
                    separateElem += ''
                elif lst[elem-1] in ['-', '+', "/", "*"]:
                    separateElem += ''
            else:
                separateElem += lst[elem]

        if lst[elem] in ["-", '+', "/", "*"]:
            if lst[elem] == '-':
                if elem != 0:

                    if lst[elem-1] not in ['-', '+', "/", "*"]:
                        mainLst.append(separateElem)
                        separateElem = ''
                        mainLst.append(lst[elem])

            elif lst[elem] == "+":
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
        raise TwoOperators("Некорректная последовательность токенов")