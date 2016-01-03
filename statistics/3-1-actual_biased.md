[Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

>> pmf = Pmf({0: 0.46617820227659301, 1: 0.21405207379301322, 2: 0.19625801386889966, 3: 0.087138558157791451, 4: 0.025644380478869556, 5: 0.010728771424833181})

>>> biased_pmf = Pmf({0: 0.0, 1: 0.20899335717935616, 2: 0.38323965252938175, 3: 0.25523760858456823, 4: 0.10015329586101177, 5: 0.052376085845682166})

>>> Avg actual pmf - avg biased pmf =
 1.02420515504 - 2.40367910066 = -1.37947394562

 #below is python code:

 %matplotlib inline

import chap01soln, thinkstats2
resp = chap01soln.ReadFemResp()

#hist = thinkstats2.Hist(resp.numkdhh)
pmf = thinkstats2.Pmf(resp.numkdhh, label='actual')

def BiasPmf(pmf, label=''):
    """Returns the Pmf with oversampling proportional to value.

    If pmf is the distribution of true values, the result is the
    distribution that would be seen if values are oversampled in
    proportion to their values; for example, if you ask students
    how big their classes are, large classes are oversampled in
    proportion to their size.

    Args:
      pmf: Pmf object.
      label: string label for the new Pmf.

     Returns:
       Pmf object
    """
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf



biased_pmf = BiasPmf(pmf, label='observed')

import thinkplot
thinkplot.PrePlot(2)
thinkplot.Pmfs([pmf, biased_pmf])
thinkplot.Show(xlabel='number of children per hh', ylabel='pmf')


mean1 = pmf.Mean()
mean2 = biased_pmf.Mean()
diff = mean1 - mean2
print("Actual pmf - biased pmf = \n", mean1, "-", mean2, "=", diff)

