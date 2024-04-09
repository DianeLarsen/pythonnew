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
            
    def item_exists(self, category, part_type, part):
        item_details = self.items[category][part_type][part]
        return True, item_details
    
    def save_items(self):
        try:
            with open('inventory.json', 'w') as file:
                json.dump(self.items, file, indent=4)
        except Exception as e:
            print(f"An error occurred while saving: {e}")

    def item_key(self, part_type, part):
        return f"{part_type}:{part}"

    def add_item(self, item, force_add=False):

        exists, existing_item_details = self.item_exists(item.category, item.part_type, item.part)
        item_dict = item.to_dict()

        if exists:
            # existing_item = self.items[item.category][item.part_type][item.part]
            if self.items_are_equivalent(existing_item_details, item_dict):
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
            if item.category not in self.items:
                self.items[item.category] = {}
            if item.part_type not in self.items[item.category]:
                self.items[item.category][item.part_type] = {}
            self.items[item.category][item.part_type][item.part] = item_dict
            self.save_items()
            print(f"Item {item.part} added successfully in {item.category} > {item.part_type}.")
            return True
        
    def list_items(self, category_name, sub_category_name, start=0, limit=10):
        if category_name in self.items and sub_category_name in self.items[category_name]:
            sub_category_items = list(self.items[category_name][sub_category_name].items())
            end = start + limit
            next_start = end if end < len(sub_category_items) else None
            return sub_category_items[start:end], next_start
        return [], None    
    
    def extract_categories_and_subcategories(self):
        """
        Extracts categories and their subcategories from the items structure.

        Returns:
        - A dictionary where keys are category names and values are lists of subcategory names.
        """
        categories = {}
        for category, subcategories in self.items.items():
            # Initialize each category with an empty list for subcategories
            if isinstance(subcategories, dict):
                categories[category] = list(subcategories.keys())
            else:categories[category] = []
        # for subcategory in subcategories.keys():
        #     # Append each subcategory to the appropriate category
        #     categories[category].append(subcategory)
        return categories
    
    def add_category(self, category_name):
        if category_name in self.items:
            print(f"Category '{category_name}' already exists.")
            return False
        else:
            self.items[category_name] = {}
            self.save_items()
            print(f"Category '{category_name}' added successfully.")
            return True
        
    def add_subcategory(self, category_name, subcategory_name):
        if category_name not in self.items:
            print(f"Category '{category_name}' does not exist. Please add the category first.")
            return False
        elif subcategory_name in self.items[category_name]:
            print(f"Subcategory '{subcategory_name}' already exists in category '{category_name}'.")
            return False
        else:
            self.items[category_name][subcategory_name] = {}
            self.save_items()
            print(f"Subcategory '{subcategory_name}' added successfully to category '{category_name}'.")
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

    def view_item(self, category, subcategory, item_key):
        category_items = self.items.get(category)
        if category_items:
            subcategory_items = category_items.get(subcategory)
            if subcategory_items:
                item = subcategory_items.get(item_key)
                if item:
                # Formatting the details into a nicer format
                    item_details_formatted = (
                        f"Part: {item['part']}\n"
                        f"Quantity: {item['quantity']}\n"
                        f"Location: {item['location']}\n"
                        f"Supplier: {item['supplier']}\n"
                        f"Specifications:\n"
                        f"  Capacity: {item['specs']['capacity']}\n"
                        f"  Voltage: {item['specs']['voltage']}\n"
                        f"  Tolerance: {item['specs']['tolerance']}\n"
                        f"  Temperature Coefficient: {item['specs']['temperature_coefficient']}\n"
                        f"Comments: {item.get('comments', 'N/A')}"  # Using get to handle missing comments gracefully
                    )
                    return item_details_formatted
        return "Item not found."

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
                        print("Printing Items....")
                        print(category_name][part_type][part)
                        print(self.items[category_name][part_type][part])
                        found_items.append(self.items[category_name][part_type][part])
                        # found_items.append((category_name, part_type, part, item_details))

        return found_items

    def to_json(self):
        # Convert the inventory items to a serializable format
        return json.dumps({k: v.to_dict() for k, v in self.items.items()}, indent=4)

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        inventory = cls()  # Create a new inventory instance
        for k, v in data.items():
            inventory.items[k] = InventoryItem.from_dict(v)
        return inventory

    def update_current_item(self, item):
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
    def load_inventory(filename='inventory.json'):
        try:
            with open(filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("Error: The inventory file does not exist.")
            return {}
        except json.JSONDecodeError:
            print("Error: The inventory file could not be parsed.")
            return {}
        
    @staticmethod
    def extract_categories(inventory_data):
        return list(inventory_data.keys())
    
    @staticmethod
    def extract_subcat(inventory_data):
        return list(inventory_data.keys())
    
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

