'''
Module --- Module Contain Classes and Functions.
Package --- Package is colloection of simmilar module.
Library --- Collection of Package
Framework--- Collection of Libarary
'''

import datetime
# If you want to know all classes and Function in this module.

print(dir(datetime))
'''
['MAXYEAR', 'MINYEAR', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__',
 '__name__', '__package__','__spec__', 'date', 'datetime', 'datetime_CAPI', 
 'time', 'timedelta', 'timezone', 'tzinfo']
'''

print(datetime.datetime.now())     #module-->Class-->Function

# if you don't want to waste memory

from datetime import datetime
print(datetime.now())
