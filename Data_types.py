'''
Created on Sep 20, 2018

@author: LAVIKAS
'''
print("hello Welcome to Data type file");
print('Hello \nNamaskaram')#Escape sequence
print('Hello \tNamaskaram')#Escape Tab
print('Hello \rNamaskaram')#Escape Tab
print(len('Namaskaram'));#Length of string

a=0.2+0.1;
b=type(a);
print(b);
#indexing and slicing
city="Nellore is my city";
print(city[5]);
print(city[-1]);#Reverse indexing
''' 
Slicing Syntax [Start:Stop:step]
'''
print(city[0::2]);
print(city[:3]);
print(city[::-1])
sliced=city[3];
sliced=sliced+'uck';
print(sliced);
newcity='Bangalore'+city[7:]
print(newcity)
uppercase=newcity.upper();
print(uppercase);
print(newcity.split());
'''
.format method
'''
print('{} is my city {}'.format('Bangalore','Cheers!!'));#dynamic assignment
print('{1} is my city {0}'.format('Bangalore','Cheers!!'));#Position assingment
print('{c} is my city {b}'.format(b='Bangalore',c='Cheers!!'));#Variable assignment

result=22/7;
print("the result is {r:0.2f}".format(r=result));
#fString
print(f'the result is {result:0.2f}');
print('the result is '+str(result)+'')#This can be done only for String not for the float values
a,b=0,1;
print(f'{a} {b}');
