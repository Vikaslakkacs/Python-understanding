'''
Created on Sep 29, 2018
Stataements containing if, elif, For  and while
for this statements ':' is used after every statement declaration
eg: if true:
for row in matrix:
etc.
@author: LAVIKAS
'''
from _ast import Num
from pip._internal.cmdoptions import always_unzip
if True:
    print('If worked')

if 2<3:
    print('If worked for comparision operators')

boolean=False
if boolean:
    print('True worked if it is false')
else:
    print('Worked when it is false')

marks=46
if marks==36:
    print('Just pass')
elif marks==40:
    print('Second class')
else:
    print('First class!!')



''' For loops'''
my_list=[1,2,3,4,5,6,7,8,9]

for list_num in my_list:
    print(list_num)
    break
'''Now add If statements in for loops'''
for list_num in my_list:
    if list_num%2==0:
        print(list_num)
    else:
        print('Odd number')
tot=0
for num in my_list:
#tot=tot+ num
    tot += num
print(tot)
''' You can access with a string also'''
name='veera venkata satya narayana sharma santosh samrat'
name_list=[]
'''for letter in name:
    print(letter)'''
for letter in name[::2]:
    print(letter)
tup=(1,2,3,'Siva')
''' when the string is run in for loop then it takes as list'''
for letter in name[::2]:
    name_list+=[letter]
print(name_list)

tup=(1,2,3,'Siva')
for char in tup:
    print(char)

''' You can convert a tuple into a list and can edit them using for loop'''
for letter in tup:
    name_list+=[letter]
print(name_list)
name_list[-1]='Kasi'
print(name_list)
''' You can use dictionaries into for loops in different ways'''
dic={'Man':'Siva','Sup':'Kasi','Emp':'Vasi'}
for dic_num in dic:# or for dic_num in dic.keys():
    print(dic_num)#This returns keys
print('--'*10)
'''You can retrieve key values also'''
for dic_num in dic.values():
    print(dic_num)
print('--'*11)
''' Values can be retrieved in different way'''
for dic_num in dic:
    print(dic[dic_num])
print('--'*12)
'''you can retrieve keys and values from the dictionary item by following statements'''
for keys,values in dic.items():
    print(keys);
    print(values);

''' While Loop


'''


x=0
while x<10:
    x+=1
    print(x)
'''You can store the values into lists'''
x=0
list_while=[]
while x<10:
    x+=1
    if x%2==0:
        continue
    list_while+=[x]
print(list_while)

for letter in tup:
    print(letter)