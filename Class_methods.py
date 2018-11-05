'''
Created on Oct 11, 2018
We are creating methods in the classes
Points:
     You can assign the attribute values in the method and can call through Classname.attribute but not methodname.attribute.
     We create a constructor which will call everytime when you initiate the class
@author: LAVIKAS
'''
class SolarSystem():
    '''A class object attribute is created just above the init and it is true for the whole class'''
    star_of_system='Sun'
    '''We create a constructor which will call everytime when you initiate the class'''
    def __init__(self,solarsystem_name,planets):
        '''Here you define attribute planet_count and assign the input parameter to the attribute.'''
        self.planet_count = 'There are '+ str(planets) +' planets in the solar system'
        self.name='The name of the solar system is '+solarsystem_name
        '''Method is not generic operation but a particular operation bounded it can manipulate and return objects'''
    def names(self,ss_name='Moon'):
        if ss_name.upper()=='SUN':
            planet_list=['Mer','Ven', 'Ear', 'Mar', 'Jup', 'Sat', 'Uran', 'Nep', 'Plu']
            print('Mer,Ven, Ear, Mar, Jup, Sat, Uran, Nep, Plu are the list of planets for the solar system {}'.format(self.name)); 
            '''If you want to add the class object attribute'''
            print(self.star_of_system) 
            ''' You can write in the following manner also'''
            print(SolarSystem.star_of_system)
            '''You can assign the attribute values in the method and can call through Classname.attribute but not methodname.attribute.'''
            self.small_planet='Pluto'
            return planet_list


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

'''Here we will call the method and expect the return value'''
planet_list=solar_system.names('Sun')
print(solar_system.small_planet)
print(planet_list)