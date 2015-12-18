import numpy

csvfile = "inflammation-01.csv"
data = numpy.loadtxt(fname=csvfile, delimiter=",")

print("average inflammation:", data.mean())
print("maximum inflammation:", data.max())
print("minimum inflammation:", data.min())
print("standard deviation:", data.std())

# we can combine methods instead of storing the data first
#patient_0 = data[0, :]
print("maximum inflammation for patient 0:", data[0, :].max())
