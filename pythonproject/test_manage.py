import unittest
from unittest.mock import patch, mock_open
from manage import Inventory, InventoryItem


class TestInventoryManagement(unittest.TestCase):

    def setUp(self):
        """Set up a clean inventory for each test."""
        self.inventory = Inventory()
        self.inventory.items = {}  # Ensuring the inventory is empty at the start of each test

    def test_add_item(self):
        """Test adding an item to the inventory."""
        item = InventoryItem(
            'Electronics', 'Resistor', 'Resistor 10K', 100, 'Warehouse A', 'Supplier XYZ', 
            {'resistance': '10KΩ', 'tolerance': '5%', 'power_rating': '0.25W'}, 'N/A'
        )
        item_key = self.inventory.item_key('Resistor', 'Resistor 10K')
        self.inventory.add_item('Electronics', item_key, item.to_dict())  # Updated to reflect new method signature
        # Check if the item is added to inventory
        self.assertIn('Electronics', self.inventory.items)
        self.assertIn(item_key, self.inventory.items['Electronics'])
        self.assertEqual(self.inventory.items['Electronics'][item_key], item.to_dict())

    def test_delete_item(self):
        """Test deleting an item from the inventory."""
        item = InventoryItem(
            'Electronics', 'Resistor', 'Resistor 10K', 100, 'Warehouse A', 'Supplier XYZ', 
            {'resistance': '10KΩ', 'tolerance': '5%', 'power_rating': '0.25W'}, 'N/A'
        )
        item_key = self.inventory.item_key('Resistor', 'Resistor 10K')
        self.inventory.add_item('Electronics', item_key, item.to_dict())  # Add an item before testing delete
        self.assertTrue(self.inventory.delete_item('Electronics', item_key))  # Verify deletion was successful
        # Ensure the item is removed from the inventory
        self.assertNotIn(item_key, self.inventory.items.get('Electronics', {}))

    @patch('builtins.input', side_effect=['SMT', '0805', '10KΩ', '5%', '0.25W'])
    def test_prompt_for_specs_resistors(self, mock_inputs):
        """Test prompting for specs for resistors."""
        expected_specs = {
            'mounting_type': 'SMT',
            'package': '0805',
            'resistance': '10KΩ',
            'tolerance': '5%',
            'power_rating': '0.25W'
        }
        specs = InventoryItem.prompt_for_specs('resistors')
        self.assertEqual(specs, expected_specs)

    @patch("builtins.open", new_callable=mock_open,
           read_data='{"Electronics": {"Resistor:Resistor 10K": {"category": "Electronics", "part_type": "Resistor", "part": "Resistor 10K", "quantity": 100, "location": "Warehouse A", "supplier": "Supplier XYZ", "specs": {"resistance": "10KΩ", "tolerance": "5%", "power_rating": "0.25W"}, "comments": "N/A"}}}')
    def test_load_items(self, mock_file):
        """Test loading items from a file into the inventory."""
        self.inventory.load_items()  # Trigger the load_items method, which should read from the mocked file
        key = self.inventory.item_key('Resistor', 'Resistor 10K')
        # Check if the item was loaded correctly into the inventory
        self.assertIn('Electronics', self.inventory.items)
        self.assertIn(key, self.inventory.items['Electronics'])
        self.assertEqual(self.inventory.items['Electronics'][key]['quantity'], 100)
        self.assertEqual(self.inventory.items['Electronics'][key]['location'], 'Warehouse A')

if __name__ == '__main__':
    unittest.main()
