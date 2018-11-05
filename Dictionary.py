'''
Created on Sep 28, 2018
Dictionary
@author: Lavikas
'''
company={'Manager':'Siva', 'Supervisor':'Kasi','Employee':'Vasi'}
print(company)
print(company.keys())
print(company.values())
print('Items are {}'.format(company.items()))
print(company['Manager'])
print(company['Supervisor'])
'''Nested dictionaries
You can add Lists also inside disctionary along with dictionary'''
dictionary={'company':{'Manager':'siva','Supervisor':'Kasi'},'Number':[1,2,34]}
print(dictionary['company']['Manager'])
'''
You can add values with the dictionary with the lists it is not possible
'''
print(dictionary['company']['Manager']+'sista')
'''You can add extra values to the dictionary
Yo cannot add values to the list in the dictionary
dictionary['Number']=[5]; It will be replaced with the existing list.
But you can add the values in dictionary inside dictionary
'''
dictionary['company']['employee']='vikas'
print(dictionary)
