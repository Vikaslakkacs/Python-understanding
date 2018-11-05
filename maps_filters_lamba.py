'''
Created on Oct 9, 2018
here we will learn how to create map filters and lamba functions
@author: LAVIKAS
'''

'''Maps is a function which will take the function and input parameter LIST as arguments and execute it
which means if we want to execute the function for the values in the list we need to loop it. 
But the Map function will help elimionating the loop which is written below'''

def square_val(a):
    return a**2

''' We will test with normal case'''
value=square_val(5)
print(value)
'''giving the list of number'''
list_num=[1,2,3,4,5]
'''This wont give you any result'''
map(square_val,list_num)
'''To get the result you have to either loop the map fucntion or to store in the list'''
for item in map(square_val,list_num):
    print(item)

'''You can store it in a list'''

print(list(map(square_val,list_num)))







'''Filter is the function where the value is returned only when true(if it is returnig boolean)'''
def even_not(a):
    if a%2==0:
        return True
    else:
        return False
print(even_not(4))
'''Now we will use filter function to return the variables'''
list_num=[1,2,3,4,5]
for item in filter(even_not,list_num):
    print(item)
print(list(filter(even_not,list_num)))










'''We can use lamba function to insert the function directly into map or filter 
instead of creating a function and assigning it into map ot filter which will take more space'''
def sqre(a):
    returns=a**2
    return returns
'''instead of the above function we create a lamba function'''
#lambda a:a**2
list_result=list(map(lambda a:a**2,list_num))
print(list_result)