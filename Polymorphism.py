'''
Created on Oct 12, 2018
Polymorphism Meaning: The condition of the object occuring in different forms.
Polymorphism Defnition: you can use the same method name for different classes and that doesn't affect the code
@author: LAVIKAS
'''
class Animal():
    def __init__(self,name):
        self.name=name
    
    def speaks(self):
        pass

class Dog(Animal):
    '''Dont need to write the init as it will be inherited from he animal class'''
    def speaks(self):
        print(self.name+' says Woof!')

class Cat(Animal):
    '''Dont need to write the init as it will be inherited from he animal class'''
    def speaks(self):
        print(self.name+' says Meow!')
mydog=Dog('Pluto')
mycat=Cat('Tweety')
''' now we are going to call both the functions in for loop'''
for pet in [mydog,mycat]:
    pet.speaks()
'''the above code is calling with the individual class method and not confused with the same method name'''
