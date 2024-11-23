import unittest
from models import PersonCRUD
from models import Person

class TestPersonCRUDE(unittest.TestCase):

    def setUp(self):
        self.crud = PersonCRUD()
        self.person1 = Person("Sebastián","Agredo","23","1006073732")
        self.person2 = Person("Fredy","Agredo","79","14445065")

    def test_create(self):
        self.crud.create(self.person1)

        self.assertEqual(len(self.crud.persons), 1)
        self.assertEqual(self.crud.persons[0].name, "Sebastián")

    def test_person_duplicate_dni(self):
        self.crud.create(self.person1)
        with self.assertRaises(ValueError):
            self.crud.create(self.person1)

if __name__ == "__main__":
    unittest.main()