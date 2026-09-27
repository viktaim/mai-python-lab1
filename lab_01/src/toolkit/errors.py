class VacuousExpression(Exception):  # пустое выражение
    pass

class MissingOperand(Exception):  # в конце оператор
    pass

class TwoOperators(Exception):  # два оператора подряд
    pass