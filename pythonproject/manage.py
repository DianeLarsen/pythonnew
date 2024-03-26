import json


class InventoryItem:
    def __init__(
            self,
            category,
            part_type,
            part,
            quantity,
            location,
            supplier,
            specs,
            comments):
        self.category = category
        self.part_type = part_type
        self.part = part
        self.quantity = quantity
        self.location = location
        self.supplier = supplier
        self.specs = specs
        self.comments = comments

    def to_dict(self):
        return {
            "part": self.part,
            "quantity": self.quantity,
            "location": self.location,
            "supplier": self.supplier,
            "specs": self.specs,
            "comments": self.comments
        }

    @classmethod
    def from_dict(cls, data):
        """Instantiate an InventoryItem from a dictionary."""
        return cls(**data)

   


class Inventory:
    def __init__(self):
        self.items = {}
        self.load_items()

    def load_items(self):
        try:
            with open('inventory.json', 'r') as file:
                self.items = json.load(file)
        except FileNotFoundError:
            print("The inventory file doesn't exist.")
        except json.JSONDecodeError:
            print("There was an error decoding the inventory file.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def save_items(self):
        try:
            with open('inventory.json', 'w') as file:
                json.dump(self.items, file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving: {e}")

    def item_key(self, part_type, part):
        return f"{part_type}:{part}"

    def add_item(self, item, force_add=False):
        """
        Adds an item to the inventory, updates an existing item, or overrides an existing item.
        
        Parameters:
        - item: InventoryItem instance to be added.
        - force_add: Boolean indicating whether to force addition of the item (True to override).
        
        Returns:
        - True if the item was successfully added or updated.
        - "exists_diff" if the item exists but is not equivalent, and force_add is False.
        - False if the item exists with the same supplier and specs.
        """
        item_dict = item.to_dict()
        category_exists = item.category in self.items
        part_type_exists = category_exists and item.part_type in self.items[item.category]
        item_exists = part_type_exists and item.part in self.items[item.category][item.part_type]

        if item_exists:
            existing_item = self.items[item.category][item.part_type][item.part]
            if self.items_are_equivalent(existing_item, item_dict):
                print(f"Item {item.part} already exists with the same supplier and specs.")
                return False
            else:
                if force_add:
                    # Override the existing item with the new one.
                    self.items[item.category][item.part_type][item.part] = item_dict
                    self.save_items()
                    print(f"Item {item.part} overridden successfully in {item.category} > {item.part_type}.")
                    return True
                else:
                    # Indicate that the item exists but is not equivalent, and no override was performed.
                    return "exists_diff"
        else:
            # Add new item if it doesn't exist.
            if not category_exists:
                self.items[item.category] = {}
            if not part_type_exists:
                self.items[item.category][item.part_type] = {}
            self.items[item.category][item.part_type][item.part] = item_dict
            self.save_items()
            print(f"Item {item.part} added successfully in {item.category} > {item.part_type}.")
            return True
        
    def items_are_equivalent(self, existing_item, new_item):
        # Compare suppliers
        if existing_item['supplier'] != new_item['supplier']:
            return False

        # Compare specs, ensuring all specs in existing_item are in new_item and are equivalent
        for spec_key, spec_value in existing_item['specs'].items():
            if spec_key not in new_item['specs'] or new_item['specs'][spec_key] != spec_value:
                return False

        # If we reach here, all compared specs are the same
        return True

    def delete_item(self, category, part_type, part):
        if category in self.items and part_type in self.items[category] and part in self.items[category][part_type]:
            del self.items[category][part_type][part]
            self.save_items()
            print(f"Item {part} deleted successfully from {category} > {part_type}.")
            return True
        else:
            print(f"Item {part} not found in {category} > {part_type}.")
            return False

    def update_item(self, category, item_key, **updates):
        category_items = self.items.get(category)
        if category_items and item_key in category_items:
            category_items[item_key].update(updates)
            return True
        return False

    def view_item(self, category, item_key):
        category_items = self.items.get(category)
        if category_items:
            return category_items.get(item_key)
        return None

    def search_items(self, search_criteria):
        found_items = []

        # Helper function to recursively search within item details (including nested dicts)
        def detail_matches_criteria(detail, value):
            if isinstance(detail, dict):
                return any(detail_matches_criteria(sub_detail, value) for sub_detail in detail.values())
            return str(detail).lower() == str(value).lower()

        for category_name, subcategories in self.items.items():
            # Category filter
            if 'category_name' in search_criteria and search_criteria['category_name'] != category_name:
                continue

            for part_type, parts in subcategories.items():
                # Sub-category filter
                if 'sub_category_name' in search_criteria and search_criteria['sub_category_name'] != part_type:
                    continue

                for part, item_details in parts.items():
                    # Part name filter
                    if 'part' in search_criteria and search_criteria['part'].lower() not in part.lower():
                        continue

                    # General search term filter
                    if 'general_search_term' in search_criteria:
                        general_search_term = search_criteria['general_search_term'].lower()
                        if not any(general_search_term in str(detail).lower() for detail in item_details.values()):
                            continue

                    # Specific criteria filter
                    match = True
                    for key, value in search_criteria.items():
                        if not value or key in ['category_name', 'sub_category_name', 'part', 'general_search_term']:
                            continue  # Skip non-specific criteria

                        # Adjusted to use helper function for potential nested detail matching
                        if key in item_details and isinstance(item_details[key], dict):
                            print("2")
                            nested_dict = item_details[key]
                            nested_match = False
                            for nested_key, nested_value in nested_dict.items():
                                if detail_matches_criteria(nested_value, value):
                                    nested_match = True
                                    break
                            if not nested_match:
                                match = False
                                break
                        elif key in item_details:
                            # Direct attribute match
                            if not detail_matches_criteria(item_details[key], value):
                                match = False
                                break
                        elif key in item_details["specs"]:
                            match = True
                        else:
                            # Key not found in either top-level or nested dictionary
                            match = False
                            break
                    if match:
                        found_items.append((category_name, part_type, part, item_details))

        return found_items





    def to_json(self):
        # Convert the inventory items to a serializable format
        return json.dumps({k: v.to_dict()
                          for k, v in self.items.items()}, indent=4)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        inventory = cls()  # Create a new inventory instance
        for k, v in data.items():
            inventory.items[k] = InventoryItem.from_dict(v)
        return inventory

    def update_current_item(self, item):
        """
        Updates the details of an existing item in the inventory.

        Parameters:
        - item: An InventoryItem instance with the updated details.

        Returns:
        - True if the item was successfully updated.
        - False if the item does not exist in the inventory.
        """
        item_dict = item.to_dict()
        # Check if the item exists
        if item.category in self.items and item.part_type in self.items[item.category] and item.part in self.items[item.category][item.part_type]:
            # Item exists, proceed with update
            # Assuming item_dict contains all the necessary fields to update the existing item
            self.items[item.category][item.part_type][item.part] = item_dict
            self.save_items()
            print(f"Item {item.part} in {item.category} > {item.part_type} has been updated successfully.")
            return True
        else:
            # Item does not exist, cannot update
            print(f"Cannot update {item.part} in {item.category} > {item.part_type} because it does not exist in the inventory.")
            return False

class InventoryManager:
    @staticmethod
    def load_specs_from_file(filename="master_specs.json"):
        try:
            with open(filename, 'r') as file:
                InventoryManager.master_specs = json.load(file)
                print("Master specs loaded from file.")
        except FileNotFoundError:
            print("Master specs file not found. Starting with empty specs.")
            InventoryManager.master_specs = {}

    @staticmethod
    def save_specs_to_file(filename="master_specs.json"):
        with open(filename, 'w') as file:
            json.dump(InventoryManager.master_specs, file, indent=4)
            print("Master specs saved to file.")

    @staticmethod
    def prompt_for_specs(item_type):
        specs = {}

        # Load the master specs to ensure we have the latest version
        InventoryManager.load_specs_from_file()

        # Check if item_type is already defined in master specs
        if item_type in InventoryManager.master_specs:
            type_specs = InventoryManager.master_specs[item_type]
            # Since type_specs is a list, we iterate directly over it
            for spec in type_specs:
                user_input = input(f"Enter {spec}: ")  # Removed the example part for simplicity
                specs[spec] = user_input
        else:
            # If the item type is not defined, ask for new specs dynamically
            print(f"New item type detected: {item_type}. Please define its specs.")
            new_specs = []
            while True:
                spec_name = input("Enter spec name (or type 'done' to finish): ")
                if spec_name.lower() == 'done':
                    break
                new_specs.append(spec_name)

            # Convert the list of new specs into a dictionary with placeholders for values
            for spec in new_specs:
                specs[spec] = "example value"  # You might want to prompt for actual example values here

            # Save the new item type and its specs to the master_specs
            InventoryManager.master_specs[item_type] = new_specs  # Store it as a list
            InventoryManager.save_specs_to_file()

        return specs

