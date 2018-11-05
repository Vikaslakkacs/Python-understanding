'''
Created on Oct 12, 2018
here we are going to discuss modules and packages
When you are calling the other modules into the current module then below are the tips you have to follow
#1: When you are calling a function then you can directly call through from module name import function
#2: When you are calling  a class method then if you call ""        ""             ""           ""    . But the problem is when you execute the code all the methods in the class will be executed.
The thing you have to do is to use a condition If __name__=='__main__' then execute some methods. Which is means that you have
@author: LAVIKAS
'''
from Functions import randint

result=randint(1,2)
print(result)
