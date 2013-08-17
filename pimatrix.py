#!/usr/bin/env python

"""
Analyze the relationships between digits in pi.
"""

from __future__ import print_function
import bigfloat
from bigfloat import precision
import numpy
from scipy import stats

str_pi = str(bigfloat.atan2(+0.0, -0.0, precision(100000)))

# remove the "3." at the beginning of pi
pi = list(str_pi)
pi.pop(0)
pi.pop(0)

m = numpy.zeros(100).reshape((10, 10))

for i in xrange(0, len(pi)):
    try:
        m[pi[i], pi[i+1]] += 1  # count adjacent digits of pi
    except IndexError:
        pass

print(m)
print("Min: " + str(m.min()))
print("Max: " + str(m.max()))
print("Mode: " + str(stats.mode(m)))
