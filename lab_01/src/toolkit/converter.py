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