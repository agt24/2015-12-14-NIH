import matplotlib.pyplot
import numpy
import sys

def analyze(filename):
    data = numpy.loadtxt(fname=filename, delimiter=",")

    fig = matplotlib.pyplot.figure(figsize=(10.0, 3.0))

    axes1 = fig.add_subplot(1, 3, 1)
    axes2 = fig.add_subplot(1, 3, 2)
    axes3 = fig.add_subplot(1, 3, 3)

    axes1.set_ylabel('average')
    axes1.plot(data.mean(axis=0))

    axes2.set_ylabel('maximum')
    axes2.plot(data.max(axis=0))

    axes3.set_ylabel('minimum')
    axes3.plot(data.min(axis=0))

    fig.tight_layout()
    matplotlib.pyplot.show(fig)


# show list on interpreter, how to slice arguments and exclude sys.argv[0]
for fname in sys.argv[1:]:
    print(fname)
    analyze(fname)
