import numpy

csvfile = "inflammation-01.csv"
data = numpy.loadtxt(fname=csvfile, delimiter=",")

print("average inflammation:", data.mean())
print("maximum inflammation:", data.max())
print("minimum inflammation:", data.min())
print("standard deviation:", data.std())

patient_0 = data[0, :]
print("maximum inflammation for patient 0:", patient_0.max())


# verify manually with
# $ head -1 inflammation-01.csv 
# 0,0,1,3,1,2,4,7,8,3,3,3,10,5,7,4,7,7,12,18,6,13,11,11,7,7,4,6,8,8,4,4,5,7,3,4,2,3,0,0
