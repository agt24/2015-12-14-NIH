with open("inflammation-01.csv", 'r') as filename:
    lines = filename.readlines()

print("lines is a", type(lines))
print("Number of lines in inflammation-01.csv:", len(lines))
