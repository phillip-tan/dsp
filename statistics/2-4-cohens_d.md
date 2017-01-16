# [Think Stats Chapter 2 Exercise 4](http://greenteapress.com/thinkstats2/html/thinkstats2003.html#toc24) (Cohen's d)

# Q1. Think Stats Chapter 2 Exercise 4 (effect size of Cohen's d)
#
# Cohen's D is an example of effect size. Other examples of effect size are:
# correlation between two variables, mean difference, regression coefficients
# and standardized test statistics such as: t, Z, F, etc. In this example,
# you will compute Cohen's D to quantify (or measure) the difference between
# two groups of data.

# # You will see effect size again and again in results of algorithms that are
# run in data science. For instance, in the bootcamp, when you run a
# # regression analysis, you will recognize the t-statistic as an example of
# # effect size.

import sys
import thinkstats2
import first

def CohenEffectSize(group1, group2): #from the book
    diff = group1.mean() - group2.mean() #diff in group means

    var1 = group1.var() #variance of group 1
    var2 = group2.var() #variance of group 2
    n1, n2 = len(group1), len(group2)

    pooled_var = (n1 * var1 + n2 * var2) / (n1 + n2)
    d = diff / math.sqrt(pooled_var) #pooled_var is S^2, so sqrt gives s
    return d

def WeightDifference(live, firsts, others):
    """Explore the difference in weight between first babies and others.

    live: DataFrame of all live births
    firsts: DataFrame of first babies
    others: DataFrame of others
    """
    mean0 = live.totalwgt_lb.mean()
    mean1 = firsts.totalwgt_lb.mean()
    mean2 = others.totalwgt_lb.mean()

    print '----------'
    print 'Mean:'
    print 'First babies: ' + str(mean1)
    print 'Others ' + str(mean2)

    var1 = firsts.totalwgt_lb.var()
    var2 = others.totalwgt_lb.var()

    print '----------'
    print 'Variance:'
    print 'First babies: ' + str(var1)
    print 'Others: ' + str(var2)

    print '----------'
    print 'Differences in group means:'
    print 'Difference in lbs: ' + str(mean1 - mean2)
    print 'Difference in oz: ' + str(((mean1 - mean2) * 16))

    print 'Difference relative to mean (%age points)', (mean1 - mean2) / mean0 * 100
    #this represents a probability, provided that mean0 is
    #all the live births, both firsts and others combined.
    #by dividing by this total amount, you can get the amount
    #that the differences in means represents of the whole.
    print '----------'
    print 'Effect Size: ' #bewteen the total weight of first
    #babies versus other babies.
    d = thinkstats2.CohenEffectSize(firsts.totalwgt_lb, others.totalwgt_lb)
    print 'Cohen d: ' + str(d) + ' standard deviation units'
    #reason it's negative is because of how the larger of the
    #two means are being subtracted. thus, the aboslute value
    #of the Cohen d represents the effect size of these two groups
    #in standard deviation units.
    print 'Compared to the 0.029 difference in pregnancy length, the 0.089' \
    ' difference from totalwgt_lb is about 3x, but still very small.'

def main(script):
    live, firsts, others = first.MakeFrames() #???
    # explore the weight difference between first babies and others
    WeightDifference(live, firsts, others)

if __name__ == '__main__':
    main(*sys.argv)
