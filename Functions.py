'''
Created on Oct 3, 2018
here we create different types of functions
@author: Lavikas
'''
from pip._vendor.distlib.resources import finder
def initial_function():
    '''Printing values'''
    print('Om Namah Sivaya!')
'''Calling the function'''
initial_function()
'''We can crate with input parameter also'''
def func_with_input(name):
    '''You can dynamically pass the parameter'''
    print('Welcome {}'.format(name))
func_with_input('Sivaya')
'''Functions which has input paramter and returns the value'''
def func_with_return(name):
    '''Here assign a variable and return it'''
    string='Om Namah '+ name+'!!'
    return string
stirng=func_with_return('Sivaya')
print(stirng)
'''giving default value to the input parameter'''
def func_with_default_value(name='Kasi'):
    func_with_input('Vasistaya')
    return 'Om Namah '+name+'!!'
string=func_with_default_value()
'''It won't throw error'''
print(string)

''' find a dog is present in the string or not'''
def dog_present(string=''):
    return 'DOG' in string.upper()
present=dog_present('The lazy Dog')
print(present)

string='sdsd'
print(string[0::])

'''Pig latin finder
When the word starts with vowel then add ay in the end else take the first letter and add ay along with that voewl'''
def pig_latin(string=''):
    vowels=['a','e','i','o','u']
    if string[0] in vowels:
        string +='ay'
    else:
        string=string[1::]+string[0]+'ay'
    return string
result=pig_latin('wolf')
print(result)
