csvfile = "inflammation-01.csv"
with open(csvfile, 'r') as filename:
    lines = filename.readlines()

line_number = 1
for line in lines:
    print(type(line))
    print("Line number:", line_number)
    print("  number of elements:", len(line))
    line_number = line_number + 1

print("Number of lines in", csvfile,":", len(lines))
print("line_number is", line_number)
