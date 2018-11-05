'''
Created on Oct 3, 2018
List of sample programs
@author: Lavikas
'''
for num in range(10):
   # print(num)
   continue

for num in range(0,11,2):
   # print(num)
   continue#print(list(range(10)))
'''Enumerate used to mention the index and the letter or number will be tuple'''
for num in enumerate(range(10)):
   # print(num)
   continue

for index,num in enumerate('a,b,c'):
   # print(num)
   continue
'''Zip will merge the lists and return the tuples'''
list1=[1,2,3,4]
list2=['s','b','cx']
list3=['!','@','#']
zip_tup=zip(list1,list2,list3)
for num in zip_tup:
    print(num)
'''you can change that into a list also.'''
'''list_tup=list(zip_tup)#If you use this you are not going to get the result'''
list_tup=list(zip(list1,list2,list3))
print(list_tup)

'''Methods of lists'''
list=[1,2,3,4,5,5,7,8,8,777,5,545,4];
print(list.__sizeof__())
list.append(3);
print(list);
list.pop()
print(list)
list.append(4)
list.insert(1, 2)
print(list)
list.insert(1,3)
print(list)
print(list.__sizeof__())
list.pop()
print(list.__sizeof__())
list.pop()
print(list.__sizeof__())
print(list)
list.pop()
print(list.__sizeof__())