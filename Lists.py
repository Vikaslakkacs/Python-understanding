'''
Created on Sep 28, 2018
Lists
@author: Lavikas
'''
my_list=[1,6,4,7,44,34,76,8]
print(my_list[1::])#Start from 2nd element
print(my_list[1::2])#Start from 2nd element and jump 2 values in the list
my_list.sort()
print(my_list)
my_list.sort(reverse=True)#reverse the sorting
print(my_list)
string_list=['siva','vasi',2,12]
print(string_list)
print(string_list[0]*10)
print(string_list[1]*10)
string_list=string_list+['Kasi']## Addding value into the list
print(string_list)
multi_list=string_list*2#Multiplying lists
print(multi_list)
print(my_list[::-1])#reversing the list values
#my_list.pop(3)#pop the 4th element in the list
#my_list.pop()#pop the last element
my_list.pop(-2)#pop the second last element
print(my_list)
''' Creating Matrix using lists
I.e, Nested lists
'''
column_1=[1,2,3]
column_2=['siva','vasi','Kasi']
column_3=['Rupee','Euro','Dollar']
matrix=[column_1,column_2,column_3]

print(matrix)#This is called nested list
print(matrix[1])##Picking the column
print(matrix[1][2])##Picking the 3rd value from the 1st column
''' List comprehension 
picking the first value in every matrix list'''
first_column=[column[2] for column in matrix]
print(first_column)
print(my_list.index(44))#Getting the index of the value in the list