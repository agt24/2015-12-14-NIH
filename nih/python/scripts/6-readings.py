with open("inflammation-01.csv", 'r') as filename:
    lines = filename.readlines()

line_number = 1
for line in lines:
    print("Line number:", line_number)
    print("  number of elements:", len(line))
    line_number = line_number + 1

print("Number of lines in inflammation-01.csv:", len(lines))
print("line_number is", line_number)
