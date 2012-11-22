import unittest
from data import Character

class TestCharacter(unittest.TestCase):
    
    def setUp(self):
        self.chell = Character('Chell', {'HP': 10, 'AD': 5, 'DF': 3} )

    def test_inc_attr(self):
        base_health = self.chell.get_attr('HP')
        self.chell.inc_attr('HP', 5)

        self.assertEqual(self.chell.get_attr('HP'), base_health+5)

