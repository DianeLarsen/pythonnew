import unittest
from unittest.mock import patch
from manage import Inventory, InventoryItem

class TestInventoryManagement(unittest.TestCase):

    def setUp(self):
        """Set up a clean inventory for each test."""
        self.inventory = Inventory()
        self.inventory.items = {}  # Ensuring the inventory is empty at the start of each test

    def test_add_item(self):
        """Test adding an item to the inventory."""
        item = InventoryItem('Electronics', 'Resistor', 'Resistor 10K', 100, 'Warehouse A', 'Supplier XYZ', {'Resistance': '10KΩ', 'Tolerance': '5%', 'Power Rating': '0.25W'}, 'N/A')
        self.assertTrue(self.inventory.add_item(item))  # Verifies that add_item returns True for a successful addition
        key = self.inventory.item_key(item.part_type, item.part)
        self.assertIn(key, self.inventory.items)  # Check if the item is added to inventory
        self.assertEqual(self.inventory.items[key].to_dict(), item.to_dict())

    def test_delete_item(self):
        """Test deleting an item from the inventory."""
        item = InventoryItem('Electronics', 'Resistor', 'Resistor 10K', 100, 'Warehouse A', 'Supplier XYZ', {'Resistance': '10KΩ', 'Tolerance': '5%', 'Power Rating': '0.25W'}, 'N/A')
        self.inventory.add_item(item)  # Add an item before testing delete
        self.assertTrue(self.inventory.delete_item(item.part_type, item.part))  # Verify deletion was successful

        key = self.inventory.item_key(item.part_type, item.part)
        self.assertNotIn(key, self.inventory.items)  # Ensure the item is removed from the inventory

    @patch('builtins.input', side_effect=['SMT', '0805', '10KΩ', '5%', '0.25W'])
    def test_prompt_for_specs_resistors(self, mock_inputs):
        """Test prompting for specs for resistors."""
        expected_specs = {'mounting_type': 'SMT', 'package': '0805', 'resistance': '10KΩ', 'tolerance': '5%', 'power_rating': '0.25W'}
        specs = InventoryItem.prompt_for_specs('resistors')
        self.assertEqual(specs, expected_specs)

if __name__ == '__main__':
    unittest.main()
