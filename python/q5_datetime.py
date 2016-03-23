from datetime import date

# Hint:  use Google to find python function

####a) 
date_start = '01-02-2013'  
date_stop = '07-28-2015'   

####b)  
date_start = '12312013'  
date_stop = '05282015'  

####c)  
date_start = '15-Jan-1994'  
date_stop = '14-Jul-2015'


a_a = date(2013, 01, 02)
a_b = date(2015, 07, 28)
delta = a_b - a_a
print 'a = ', delta.days, 'days'

a_a = date(2013, 12, 31)
a_b = date(2015, 05, 28)
delta = a_b - a_a
print 'b = ', delta.days, 'days'

a_a = date(1994, 01, 15)
a_b = date(2015, 07, 14)
delta = a_b - a_a
print 'b = ', delta.days, 'days'
