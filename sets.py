'''
Created on Oct 11, 2018

@author: LAVIKAS
'''
my_set=set();
my_set.add(1)
my_set.add(2)
my_set.add(3)
my_set.add(4)
print(my_set)
my_set2=set()
my_set2.add(3)
my_set3=my_set & my_set2
print(my_set3)