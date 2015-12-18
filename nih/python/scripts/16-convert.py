def fahr_to_kelvin(temp):
    kelvin = ((temp - 32) * (5/9)) + 273.15
    return kelvin

def kelvin_to_celsius(temp):
    return temp - 273.15

print("freezing point of water:", fahr_to_kelvin(32))
print("boiling point of water:", fahr_to_kelvin(212))

print("absolute zero in Celsius:", kelvin_to_celsius(0.0))
