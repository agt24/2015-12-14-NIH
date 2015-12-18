import matplotlib.pyplot
import numpy

csvfile = "inflammation-01.csv"
data = numpy.loadtxt(fname=csvfile, delimiter=",")

image = matplotlib.pyplot.imshow(data)
matplotlib.pyplot.show(image)

# Blue regions in this heat map are low values, while red shows high values. As
# we can see, inflammation rises and falls over a 40-day period.
