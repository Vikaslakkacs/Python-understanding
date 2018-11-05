'''
Created on Oct 12, 2018
Inheritance: Meaning: Taking something from your ancestors or from your father's
Inhertance Definition: You can inherit classes and their method into the class which you are creating and use their methods.
when you create a method with the same name as that their in the inherited method then it will be overridden
@author: LAVIKAS
'''
''''Lets take the old class and paste it.'''
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





''' Now create the class of our own and inherit the class solarsystem'''
class Universe(SolarSystem):

   '''While creating init method you have to call the Solarsystem Init method also to inherit'''
   def __init__(self):
       SolarSystem.__init__(self,'Sun system',9)
       print('Welcome to the Universe!!')
   def galaxy(self,galaxy_name):
        galaxy_name='This is a '+ galaxy_name + ' galaxy.'
        return galaxy_name

'''Now we will call these class and let us see the result'''
universe=Universe()
'''Now you can call the object attribute of the solarsystem class'''
print(universe.planet_count)
print(universe.name)
'''Now you can call the method associated to Solarsystem class'''
universe.names('Sun')
galaxy_name=universe.galaxy('Milky Way')
print(galaxy_name)