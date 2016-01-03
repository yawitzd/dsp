[Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

>> The difference in the means is (d = 0.08867), or less than 0.1 standard deviations. Like with pregnancy length, there is no significant difference between the birthweight of first-born and all other children.


#Python code below
import numpy, scipy, thinkstats2, thinkplot, nsfg, math

#see p. 17, 20
#import pregnancy data from nsfg, create df's for first-born babies and all other babies
preg= nsfg.ReadFemPreg()
live=preg[preg.outcome==1]
firsts = live[live.birthord == 1]
others = live[live.birthord != 1]

#plot the total birthweight for both ('totalwgt_lb')
first_hist = thinkstats2.Hist(firsts.totalwgt_lb)
others_hist = thinkstats2.Hist(others.totalwgt_lb)

width = 0.45
thinkplot.PrePlot(2)
thinkplot.Hist(first_hist, align='right', width=width)
thinkplot.Hist(others_hist, align='left', width=width)
thinkplot.Show(xlabel='weight', ylabel='frequency')


#Compute effect size between the total weight of all first-born children to all other children using Cohen's d
#mean = live.totalwgt_lb.mean()
#var = live.totalwgt_lb.var()
#std = live.totalwgt_lb.std()

def CohenEffectSize(group1, group2):
    diff = group1.mean() - group2.mean()
    var1 = group1.var()
    var2 = group2.var()
    n1, n2 = len(group1), len(group2)
    pooled_var = (n1*var1 + n2*var2)/(n1 + n2)
    d = diff/math.sqrt(pooled.var)
    return d

d = CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
print d
