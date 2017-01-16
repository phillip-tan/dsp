# [Think Stats Chapter 4 Exercise 2](http://greenteapress.com/thinkstats2/html/thinkstats2005.html#toc41) (a random distribution)

# Q3. Think Stats Chapter 4 Exercise 2 (random distribution)
#
# This questions asks you to examine the function that produces random numbers.
# Is it really random? A good way to test that is to examine the pmf and cdf of
# the list of random numbers and visualize the distribution.
# If you're not sure what pmf is, read more about it in Chapter 3.

import numpy as np
import thinkstats2
import nsfg
import thinkstats2
import thinkplot

random_1000 = np.random.random(1000) #uniform between 0 and 1, that is, every
#value should have the same probability

#plot these random 1000 numbers from random.random as PMF
pmf = thinkstats2.Pmf(random_1000)
thinkplot.Pmf(pmf, linewidth=0.1) #linewidth can be 0.01 too, for example.
thinkplot.Config(xlabel='1000 random numbers', ylabel='PMF')
#graph should cover entire area because there is a lot of 'noise' the larger
#the sample size and also because each value is equally probable by "density"
#or the area of the graph.

#now, plot these numbers as CDF
cdf = thinkstats2.Cdf(random_1000)
thinkplot.Cdf(cdf)
thinkplot.Config(xlabel='1000 random numbers', ylabel='CDF')
#graph should be a straight line, or a smoothed out step function, because
#CDFs are less affected by a larger sample size since it accounts for 'noise'
#and also a straight line represents a uniform distribution w/random sampling.
#it shows that 10% of sample is below 10th percentile, 20% of sample is below
#the 20th percentile, and so forth. It should look like a 'linear' line.
