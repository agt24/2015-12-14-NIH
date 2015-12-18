import matplotlib.pyplot
import numpy

csvfile = "inflammation-01.csv"
data = numpy.loadtxt(fname=csvfile, delimiter=",")

#axis=0 average for each day
avg_plot = matplotlib.pyplot.plot(data.mean(axis=0))
matplotlib.pyplot.show(avg_plot)

max_plot = matplotlib.pyplot.plot(data.max(axis=0))
matplotlib.pyplot.show(max_plot)

min_plot = matplotlib.pyplot.plot(data.min(axis=0))
matplotlib.pyplot.show(min_plot)

# will open one first, then the other

# we have put the average per day across all patients in the variable
# ave_inflammation, then asked matplotlib.pyplot to create and display a line
# graph of those values. The result is roughly a linear rise and fall, which is
# suspicious: based on other studies, we expect a sharper rise and slower fall.
