import unittest
from src.homework.i_dictionaries_and_sets.dictionary import (
    add_inventory,
    remove_inventory_widget,
)


class Test_Config(unittest.TestCase):

    def test_add_inventory(self):
        inventory_dictionary = {}

        # Add Widget1 with quantity 10
        add_inventory(inventory_dictionary, "Widget1", 10)
        self.assertIn("Widget1", inventory_dictionary)
        self.assertEqual(10, inventory_dictionary["Widget1"])

        # Add Widget1 with quantity 25 → total should be 35
        add_inventory(inventory_dictionary, "Widget1", 25)
        self.assertEqual(35, inventory_dictionary["Widget1"])

        # Add Widget1 with quantity -10 → total should be 25
        add_inventory(inventory_dictionary, "Widget1", -10)
        self.assertEqual(25, inventory_dictionary["Widget1"])

    def test_remove_inventory_widget(self):
        inventory_dictionary = {}

        # Add two widgets
        add_inventory(inventory_dictionary, "Widget1", 10)
        add_inventory(inventory_dictionary, "Widget2", 20)

        # Remove Widget1
        result = remove_inventory_widget(inventory_dictionary, "Widget1")
        self.assertEqual("Record deleted", result)
        self.assertEqual(1, len(inventory_dictionary))
        self.assertNotIn("Widget1", inventory_dictionary)
        self.assertIn("Widget2", inventory_dictionary)

        # Try to remove something that doesn't exist
        result2 = remove_inventory_widget(inventory_dictionary, "Widget3")
        self.assertEqual("Item not found", result2)
        self.assertEqual(1, len(inventory_dictionary))
