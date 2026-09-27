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