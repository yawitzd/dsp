[Think Stats Chapter 8 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2009.html#toc77) (scoring)

>> Exercise 8.2

Suppose you draw a sample with size n=10 from a population 
with an exponential disrtribution with lamda=2.  Simulate
this experiment 1000 times and plot the sampling distribution of
the estimate L.  Compute the standard error of the estimate
and the 90% confidence interval.

Repeat the experiment with a few different values of n and make
a plot of standard error versus n.



1) With sample size 10:

    standard error 0.8143051321760896
    confidence interval (1.2833947662803724, 3.6030555525510546)
    <img src="https://github.com/yawitzd/dsp/blob/master/img/chap08ci.png" title="scatter hex" style="float: left"; />

2) As sample size increases:

    n        SE       90% ci
    10       0.8      (1.3, 3.6) 
    100      0.2      (1.7, 2.4)
    1000     0.06     (1.9, 2.1)
    
    As n increases, SE drops. 
