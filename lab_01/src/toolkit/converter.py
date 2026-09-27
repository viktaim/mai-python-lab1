from .errors import BelowAbsoluteZero, IncompatibleUnits, UnknownUnit

length_units = {
    "m": 1,    # коэффициент 1
    "km": 1000,    # 1 км = 1000 метров
    "mm": 0.001,   # 1 мм = 0.001 метра
    "cm": 0.01,    # 1 см = 0.01 метра
}

mass_units = {
    "g": 1,    # коэффициент 1
    "kg": 1000,    #1 кг = 1000 г
}

def convert_linear(value, fromUnit, toUnit, unitsDict):
    coefFrom = unitsDict[fromUnit]
    coefTo = unitsDict[toUnit]
    value_in_base = value * coefFrom
    result = value_in_base / coefTo
    return result


def to_celsius(value, unit):
    if unit == 'f':
        num = (value - 32) * (5 / 9)
    if unit == 'k':
        num = value - 273.15
    if unit == 'c':
        num = value

    return num


def from_celsius(celsius_value, unit):
    if unit == 'c':
        num = celsius_value
    if unit == 'f':
        num = celsius_value * (9/5) + 32
    if unit == 'k':
        num = celsius_value + 273.15

    return num


def convert_temperature(value, from_unit, to_unit):
    celsius = to_celsius(value, from_unit)
    return from_celsius(celsius, to_unit)


def validate_temperature(value, unit):
    if unit not in ['c', 'f', 'k']:
        raise UnknownUnit("Неизвестная единица")
    
    if unit == 'c' and value < -273.15 or unit  == 'f' and value < -459.67 or unit  == 'k' and value < 0:
        raise BelowAbsoluteZero("Значение ниже абсолютного нуля")


def convert_temperature(value, from_unit, to_unit):
    validate_temperature(value, from_unit)

    if to_unit not in ['c', 'f', 'k']:
        raise UnknownUnit("Неизвестная единица")

    celsius = to_celsius(value, from_unit)
    return from_celsius(celsius, to_unit)


def get_group(unit):
    if unit in length_units:
        return "length"
    elif unit in mass_units:
        return "mass"
    elif unit in ['c', 'f', 'k']:
        return "temperature"
    else:
        raise UnknownUnit("Неизвестная единица")


def convert(value, from_unit, to_unit):
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    from_group = get_group(from_unit)
    to_group = get_group(to_unit)

    if from_group == to_group:
        if from_group == "length":
            return convert_linear(value, from_unit, to_unit, length_units)
        elif from_group == "mass":
            return convert_linear(value, from_unit, to_unit, mass_units)
        else:
            return convert_temperature(value, from_unit, to_unit)
    else:
        raise IncompatibleUnits("несовместимые единицы")