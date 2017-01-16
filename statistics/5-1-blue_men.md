# <!-- [Think Stats Chapter 5 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2006.html#toc50) (blue men) -->

# Q4. Think Stats Chapter 5 Exercise 1 (normal distribution of blue men)
#
# This is a classic example of hypothesis testing using the normal distribution.
# The effect size used here is the Z-statistic.

import scipy.stats #contains objects that represent analytic distributions
#for example, scipy.stats.norm represents a normal distribution

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)
#this returns scipy.stats._distn_infrastructure.rv_frozen

#"frozen" random variable can be used to compute its mean and SD.
print "The normal distribution's mean: " + str(dist.mean())
print "The normal distribution's standard deviation " + str(dist.std())

#this function can also calculate CDF
#that is, how many people are more than one SD below the mean?
print "There are " + str(dist.cdf(mu-sigma)) + " converted to percentage of \
people that are more than one standard deviation below the mean."

#how many people are between 5'10" and 6'1"
low = dist.cdf(177.8) #convert american units to metric
high = dist.cdf(185.4) #unit conversion
print "Number of people below 5'10\": " + str(low)
print "Number of people below 6'1\": " + str(high)
print "Number of people between 5'10\" and 6'1\" :" + str(high - low)
