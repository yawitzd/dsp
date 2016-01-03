[Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men)

>> about 34% of men are between 5'10 and 6'1

#python code:

from __future__ import print_function, division

import thinkstats2
import thinkplot

%matplotlib inline

import scipy.stats


mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

low = dist.cdf(177.8) #5'10
high = dist.cdf(185.42) #6'1
low, high, high-low
