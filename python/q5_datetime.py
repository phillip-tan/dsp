# Hint:  use Google to find python function

from datetime import date

####a)
date_start = '01-02-2013'
date_stop = '07-28-2015'

date_start = date(2013, 1, 2)
date_stop = date(2015, 7, 28)
delta_a = date_stop - date_start
print delta_a.days

####b)
date_start = '12312013'
date_stop = '05282015'

date_start = date(2013, 12, 31)
date_stop = date(2015, 5, 28)
delta_b = date_stop - date_start
print delta_b.days

####c)
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'

date_start = date(1994, 1, 15)
date_stop = date(2015, 7, 14)
delta_c = date_stop - date_start
print delta_c.days
