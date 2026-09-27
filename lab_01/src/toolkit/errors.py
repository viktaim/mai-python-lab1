class VacuousExpression(Exception):  # пустое выражение
    pass

class MissingOperand(Exception):  # в конце оператор
    pass

class TwoOperators(Exception):  # два оператора подряд
    pass

class InvalidNumber(Exception):  # не тот тип числа
    pass