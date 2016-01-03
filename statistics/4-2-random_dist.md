[Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

>> The cdf of 1000 random numbers is uniform.


import numpy as np
import thinkplot, thinkstats2

rds = np.random.random(1000)
rd_pmf = thinkstats2.Pmf(rds, label='randos')

thinkplot.PrePlot(1)
thinkplot.Pmfs([rd_pmf])
thinkplot.Show()

rd_cdf = thinkstats2.Cdf(rds, label='randos')

thinkplot.PrePlot(1)
thinkplot.Cdfs([rd_cdf])
thinkplot.Show()

