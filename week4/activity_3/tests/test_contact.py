import unittest
from contact import Contact

class TestNameFunction(unittest.TestCase):

    def test_name_type(self):
        aContact = Contact("test", "email.com")
        self.assertIsInstance(aContact.name, str)