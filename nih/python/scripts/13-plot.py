import matplotlib.pyplot
import numpy

csvfile = "inflammation-01.csv"
data = numpy.loadtxt(fname=csvfile, delimiter=",")

fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

axes1 = fig.add_subplot(1, 3, 1)
axes2 = fig.add_subplot(1, 3, 2)
axes3 = fig.add_subplot(1, 3, 3)

axes1.plot(data.mean(axis=0))
axes2.plot(data.max(axis=0))
axes3.plot(data.min(axis=0))

fig.tight_layout()

matplotlib.pyplot.show(fig)
