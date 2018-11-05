'''
Created on Sep 20, 2018
Fibanocci Series
@author: LAVIKAS
'''
n=100000000000
a, b=0, 1
siva=[];
while a < n:
   # print(a,end=' ')
    a,b=b, a+b
    print(a/b)