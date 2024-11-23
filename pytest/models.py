class Person:
    def __init__(self,name,lastName,age,dni):
        self.name = name 
        self.lastName = lastName
        self.age = age
        self.dni = dni


"""
CRUD

CREATE
READ
UPDATE
DELETE
"""

"""
This method provide information about the addition between 


"""
class PersonCRUD:
    def __init__(self):
        self.persons=[]

    # """ 
    # Es una función de busqueda por DNI

    # Params:
    # DNI: Es un atributo de la clase Person (string | number)

    # return:
    # Un objeto de tipo person

    # """

    def find_by_dni(self,dni):
        for person in self.persons:
            if person.dni == dni:
                return person
        
        return None

    def create(self,person):
        if self.find_by_dni(person.dni):
            raise ValueError("Person already exists")
        self.persons.append(person)

        #Optional
        return 

    def read(self,dni):
        person = self.find_by_dni(dni)
        if not person:
            raise ValueError("Person not fount")

        return person

    def update(self,dni,name,lastName,age):
        person = self.find_by_dni(dni)
        if not person:
            raise ValueError("Person not fount")
        
        if name is not None:
            person.name = name 
        
        if lastName is not None:
            person.lastName = lastName 

        if age is not None:
            person.age = age 

        if name is not None:
            person.name = name 

        #Optional
        return person
    
    # def _update (self,dni,**kwargs):
    #     person = self.find_by_dni(dni)

    #      if not person:
    #         raise ValueError("Person not fount")

    #     for key, value in kwargs.items():
    #         if hasattr(person, key):
    #             setattr(person, key, value)
    
    #     return person

    def delete(self,dni):
        person = self.find_by_dni(dni)
        if not person:
            raise ValueError("Person not fount")
        self.persons.remove(person)

        return f("Person deleted")
