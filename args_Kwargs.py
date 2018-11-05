'''
Created on Oct 9, 2018
Discussion of *args and **kwargs
Here are args ar nothing but a tuple and kwargs are nothing but a dictionary.
@author: LAVIKAS
'''
'''We create a normal function which takes 2 inputs values and gives the sum of it'''
def sum_val(a,b):
    '''Sum takes only tuples where we have to pass values inserted in tuples'''
    return sum((a,b))

value=sum_val(4, 5);
print(value)
'''Here in the above function if we want to pass dynamic input values we will get and ArithmeticError
*args will resolve the issue'''
''' We are creating the same function using *args'''
def sum_val_args(*args):
    return sum((args))

value=sum_val_args(1,2,3,4,5,6,7)
print(value)

'''when you print args it looks like tuples'''
def args_type(*args):
    print(args)
    print(args[1])

args_type(1,2,3,4,5,6,7)
'''If you want to mention particular variables depends on the index you can use the index property in the tuple to pickup the vaue'''

def args_pick(*args):
    for arg_value in args:
        print(arg_value)

args_pick(1,2,3,4,5,6,7)
'''you can use any alternate name instead of args as args only is just a name mentioned
but for code you can use args without confusion'''
def just_args(*summing):
    print(summing)

just_args(1,2,3,4,5,6,)


'''now we are going to create a function with kwargs'''
def dimension(**kwargs):
    print(kwargs)

dimension(fruit=2,names='apples,oranges')
'''Here it is a dictionary'''
'''You can actually add keys and their values for the kwargs'''
def dimension_1(**fruits):
    fruits['Size']=45
    print(fruits)

dimension_1(fruitfff=2,names='Apples,Oranges')

'''You can use both args and kwargs in a single definition'''
def args_kwargs(*numbers,**name):
    for num in numbers:
        print('There are {} of {} with {} size'.format(num,name['animal'],name['size']))

args_kwargs(1,2,3,3,4,5,animal='dog',size='small')

def args_num_kwargs(*args,x,**kwargs):
    print(args)
    print(x)
    print(kwargs)

raise 'You cannot have args follwed by a variable as it will consider the variable value into args'
args_num_kwargs(1,2,3,4,5,6,'four',animal='Dog',size='Small')

'''you cannot pass a variable along with args because it will consider that variable value as args'''