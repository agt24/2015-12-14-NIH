import glob
import matplotlib.pyplot
import numpy
import sys

def print_usage():
    """ Print usage for this program """
    print("Usage: python plot.py filenames")


def analyze(filename):
    """ Plot mean, max and min of a given data file """
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
    save_figure(fig, filename)


def save_figure(fig, filename):
    matplotlib.pyplot.savefig(filename + ".jpg")
    return


def main():
    """ Main function that will call the analyze funtion """
    for fname in glob.glob("*.csv"):
        print(fname)
        analyze(fname)

main()
