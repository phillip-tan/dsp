# [Think Stats Chapter 3 Exercise 1](http://greenteapress.com/thinkstats2/html/thinkstats2004.html#toc31) (actual vs. biased)

# Q2. Think Stats Chapter 3 Exercise 1 (actual vs. biased)
#
# This problem presents a robust example of actual vs biased data.
# As a data scientist, it will be important to examine not only the data that
# is available, but also the data that may be missing but highly relevant.
# You will see how the absence of this relevant data will bias a dataset,
# its distribution, and ultimately, its statistical interpretation.

import thinkstats2
import nsfg
import thinkplot

def BiasPmf(pmf, label): #from the book to calculate BiasPmf from pmf
    new_pmf = pmf.Copy(label=label)

    for x, p in pmf.Items():
        new_pmf.Mult(x, x)

    new_pmf.Normalize()
    return new_pmf

respondents = nsfg.ReadFemResp() #returns data frame

pmf = thinkstats2.Pmf(respondents.numkdhh, label='numkdhh')
#numkdhh constructs actual distribution for number of children under 18 in
#respondent's households.

#Plot actual distribution using the numkdhh variable stored in pmf
thinkplot.Pmf(pmf)
thinkplot.Config(xlabel='Number of Children under 18', ylabel='PMF')

#construct biased distribution using the BiasPmf function that takes in pmf
biased = BiasPmf(pmf, label='biased')

#Plot the biased distribution using BiasPmf function stored in biased
thinkplot.PrePlot(2) #color scheme
thinkplot.Pmfs([pmf, biased]) #plots both graphs on one
thinkplot.Config(xlabel='Number of Children under 18', ylabel='PMF')

#Compute the means of both actual and biased
print 'The actual mean is: ' + str(pmf.Mean())
print 'The biased mean is: ' + str(biased.Mean())
