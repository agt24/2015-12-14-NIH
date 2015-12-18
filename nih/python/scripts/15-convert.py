def fahr_to_kelvin(temp):
    kelvin = ((temp - 32) * (5/9)) + 273.15
    return kelvin

print("freezing point of water:", fahr_to_kelvin(32))
print("boiling point of water:", fahr_to_kelvin(212))
