#Q1



# Many of python 's time functions handle time as a tuple of 9 numbers , as shown below-
# Index field values
#0 4-digit year   2008
#1 month 1to 12
#2 day 1to 31
#3 hour   0 to 23
#4 minute 0 to 59
#5 second 0 to 61 (60 or 61 are leap-seconds)
#6 day of week 0to 6(0 is Monday )
#7 day of year 1to 366 (Julian day)
#8 daylight savings   -1, 0, ,1, -1 means library determines DST 



#Q2

import time 
print(time.asctime(time.localtime(time.time())))

#Q3

from datetime import datetime 
print  (datetime.now().strftime("%m"))

#Q4 

from datetime import datetime
print(datetime.now().strftime("%a")

#Q5



from datetime import datetime
print(datetime.now().strftime("%d"))


#Q6


import time
print(time.localtime())


#Q7


import math
print(math.factorial(int(input("enter any number"))))


#Q8

x=int(input("enter a number:"))
y=int(input("enter another number:"))
import math
print(math.gcd(x,y))

#Q9

import os
print(os.getcwd)


#2

import os
print(os.environ)







