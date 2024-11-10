

import unittest
from src.homework.i_dictionaries_and_sets.dictionary import add_inventory, remove_inventory_widget

class Test_Config(unittest.TestCase):

    def setUp(self):
        """Set up a sample inventory dictionary for testing."""
        self.inventory = {
            'Widget1': 10,
            'Widget2': 5
        }

    def test_add_inventory(self):
       
        add_inventory(self.inventory, 'Widget3', 20)
        self.assertEqual(self.inventory['Widget3'], 20)

       
        add_inventory(self.inventory, 'Widget1', 25)
        self.assertEqual(self.inventory['Widget1'], 35)


        add_inventory(self.inventory, 'Widget1', -10)
        self.assertEqual(self.inventory['Widget1'], 25)

    def test_remove_inventory_widget(self):
       
        result = remove_inventory_widget(self.inventory, 'Widget1')
        self.assertEqual(result, 'Record deleted')
        self.assertNotIn('Widget1', self.inventory)

       
        result = remove_inventory_widget(self.inventory, 'Widget3')
        self.assertEqual(result, 'Item not found')

       
        self.assertEqual(len(self.inventory), 1)  
        self.assertIn('Widget2', self.inventory)

if __name__ == '__main__':
    unittest.main()
