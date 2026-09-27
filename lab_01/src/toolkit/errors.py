class ToolkitError(Exception):
    pass

class VacuousExpression(ToolkitError):  # пустое выражение
    pass

class MissingOperand(ToolkitError):  # в конце оператор
    pass

class InvalidExpression(ToolkitError):  # недопустимое выражение
    pass

class UnknownUnit(ToolkitError):   #неизвестная еденица
    pass

class IncompatibleUnits(ToolkitError):   #несовместимые единицы
    pass

class BelowAbsoluteZero(ToolkitError):  # температура ниже абсолютного нуля
    pass

class DivisionByZeroError(ToolkitError):   #деление на 0
    pass