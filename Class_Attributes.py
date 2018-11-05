'''
Created on Oct 11, 2018
Here we are going to create class along with attribute
Note: When you have to pass the input parameters for the init constructor you need to pass in the Class input parameter. not in the attribute call
@author: LAVIKAS
'''
'''We create a class of Solar system'''
class SolarSystem():
    '''A class object attribute is created just above the init and it is true for the whole class'''
    star_of_system='Sun'
    '''We create a constructor which will call everytime when you initiate the class'''
    def __init__(self,solarsystem_name,planets):
        '''Here you define attribute planet_count and assign the input parameter to the attribute.'''
        self.planet_count = 'There are '+ str(planets) +' planets in the solar system'
        self.name='The name of the solar system is '+solarsystem_name
        


'''We will call the class and the attribute below'''
solar_system = SolarSystem(solarsystem_name='Sun',planets=9)
'''You can either enter the attribute name and the value or simple enter the value as input parameters written below'''
solar_system=SolarSystem('Sun',9)
#print(type(solar_system))
name=solar_system.name
planet_num=solar_system.planet_count
star=solar_system.star_of_system
print(name)
print(planet_num)
print(star)
