'''
Created on Sep 28, 2018
Tuples
@author: Lavikas
Tuples are like lists but you cannot change the values of tuples as they are immutable.
'''
week=('sun','mon','tue')
print(week)
print(week[0])
print(week[-1])
''' When you try to chagne the value it will throw the error
week[2]='Wen'
'''
print(week[::2])
''' you can check with the index also'''
print(week.index('mon'))