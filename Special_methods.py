'''
Created on Oct 12, 2018
Special methods are methods which are used like normal functions for an objcet
Eg: For a list we have Append method and that we cannot use it for the class method.
Special methods are used as methods of the objects.
@author: LAVIKAS
'''
class Book():
    
    def __init__(self,name):
        self.name=name

    def author(self,author):
        return 'Author name is '+ author
    
    def book_type(self):
        print('Type of the book is Hard cover.')
        '''To show the details of the book we use'''
    def __str__(self):
        return 'Name of the book is '+self.name
    def __del__(self):
       pass
    def __hello__(self):
        pass
'''We will call the class and method'''
mybook=Book('The beginning of Infinity!')

print(mybook.name)
print(mybook.author('David Deutsch'))
'''But the problem comes here what happens when you print the class itself'''
print(mybook)#This will show the location but not the details of it unless you have a __str__ calss
#del mybook#This will delete book class object
mybook.__hello__()
print(mybook.name)
