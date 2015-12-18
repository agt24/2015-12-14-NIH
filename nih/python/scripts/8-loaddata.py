# go to interpreter first and run
# import numpy
#   make sure everybody can import the module
#
# numpy.loadtxt(fname="inflammation-01.csv", delimeter=",")
# print(type(data))
# print(data.shape)
#   output is rows, columns
#
# print("first value in data:", data[0, 0])
# show slicing
#   print(data[0:4, 0:10])
#   This will print first 4 patients (rows), and first 10 days (columns) of data
#
import numpy

data = numpy.loadtxt(fname="inflammation-01.csv", delimiter=",")

print("Printing first 4 patients, first 10 days:")
print(data[0:4, 0:10])
