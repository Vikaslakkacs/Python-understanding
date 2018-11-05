'''
Created on Oct 11, 2018
Here we discuss about object oriented programming.
@author: LAVIKAS
'''
'''We create a simple class here '''
class Sample():
    '''You can directly add the print statement in the class'''
    print('Hi There!')

'''Now we will get the type of the class'''
my_sample=Sample()
print(type(my_sample))
'''the result is <class '__main__.Sample'>  '''

class Dog:
    def __init__(self,breed):
        self.breed = breed
        
sam = Dog(breed='Lab')
frank = Dog(breed='Huskie')
print(frank.breed)