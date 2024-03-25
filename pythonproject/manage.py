import json

class InventoryItem:
    def __init__(self, category, part_type, part, quantity, location, supplier, specs, comments):
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
            "category": self.category,
            "part_type": self.part_type,
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
    
    @staticmethod
    def prompt_for_specs(item_type):
        # Specs prompt based on item type
        specs = {}
        common_specs = ['capacitors', 'resistors', 'diodes', 'inductors', 'chips', 'FETs']
        if item_type in common_specs:
            specs['mounting_type'] = input("Enter mounting type (e.g., through-hole, SMT): ")
            if specs['mounting_type'].lower() == 'smt':
                specs['package'] = input("Enter package type/number (e.g., 0805, SOT-23): ")
                
        if item_type in ["capacitors"]:
            specs['capacity'] = input("Enter capacity (e.g., 100uF): ")
            specs['voltage'] = input("Enter voltage rating (e.g., 10V): ")
            specs['type'] = input("Enter type (e.g., ceramic, electrolytic): ")
        elif item_type in ["resistors"]:
            specs['resistance'] = input("Enter resistance (e.g., 10KΩ): ")
            specs['tolerance'] = input("Enter tolerance (e.g., 5%): ")
            specs['power_rating'] = input("Enter power rating (e.g., 0.25W): ")
        elif item_type in ["diodes"]:
            specs['forward_voltage'] = input("Enter forward voltage (e.g., 1.2V): ")
            specs['current'] = input("Enter maximum current (e.g., 1A): ")
            specs['type'] = input("Enter type (e.g., Zener, Schottky): ")
        elif item_type in ["inductors"]:
            specs['inductance'] = input("Enter inductance (e.g., 10mH): ")
            specs['current_rating'] = input("Enter current rating (e.g., 2A): ")
            specs['tolerance'] = input("Enter tolerance (e.g., 10%): ")
        elif item_type in ["chips"]:
            specs['type'] = input("Enter type (e.g., microcontroller, amplifier): ")
            specs['pin_count'] = input("Enter pin count (e.g., 14): ")
            # Package prompt is already included above for SMT components
        elif item_type in ["FETs"]:
            specs['type'] = input("Enter type (N-channel, P-channel): ")
            specs['voltage_rating'] = input("Enter voltage rating (e.g., 30V): ")
            specs['current_rating'] = input("Enter current rating (e.g., 20A): ")
            # Additional package prompt can be included here if needed for non-SMT components
        elif item_type in ["screwdrivers"]:
            specs['type'] = input("Enter type (e.g., Phillips, flathead): ")
            specs['size'] = input("Enter size (e.g., #1, #2 for Phillips): ")
        elif item_type in ["pliers"]:
            specs['type'] = input("Enter type (e.g., needle-nose, wire-cutting): ")
            specs['length'] = input("Enter length (e.g., 6 inches): ")
        elif item_type in ["soldering irons"]:
            specs['wattage'] = input("Enter wattage (e.g., 60W): ")
            specs['type'] = input("Enter type (e.g., adjustable temperature, fixed): ")
        # Can add more item types and their respective specs here
        return specs

class Inventory:
    def __init__(self):
        self.items = {}
        self.load_items()
        
    def load_items(self):
        try:
            with open('inventory.json', 'r') as file:
                data = json.load(file)

            for category_name, subcategories in data.items():
                for subcategory_name, parts in subcategories.items():
                    for part, part_details in parts.items():
                        if isinstance(part_details, dict):  # Check if part_details is a dictionary
                            item_data = {
                                "category": category_name,
                                "part_type": subcategory_name,
                                "part": part,
                                "quantity": part_details.get("quantity"),
                                "location": part_details.get("location"),
                                "supplier": part_details.get("supplier"),
                                "specs": part_details.get("specs"),
                                "comments": part_details.get("comments", "")  # Assuming comments is optional
                            }
                            self.items[self.item_key(subcategory_name, part)] = InventoryItem.from_dict(item_data)
                        else:
                            # Handle the case where part_details is not a dictionary
                            print(f"Unexpected format for part details in {part}: {part_details}")
        except (FileNotFoundError, json.JSONDecodeError) as e:
            print(f"Failed to load items: {e}")
            self.items = {}

        
    def save_items(self):
        with open('inventory.json', 'w') as file:
            # Convert the inventory items to a serializable format
            json.dump({k: v.to_dict() for k, v in self.items.items()}, file, indent=4)
    
    def item_key(self, part_type, part):
        return f"{part_type}:{part}"
    
    def add_item(self, item):
        key = self.item_key(item.part_type, item.part)
        if key in self.items:
            return False
        self.items[key] = item
        return True
    
    def delete_item(self, part_type, part):
        key = self.item_key(part_type, part)
        return self.items.pop(key, False) is not False
    
    def update_item(self, part_type, part, **updates):
        key = self.item_key(part_type, part)
        item = self.items.get(key)
        if not item:
            return False
        for attr, value in updates.items():
            setattr(item, attr, value)
        return True
    
    
    def view_item(self, part_type, part):
        key = self.item_key(part_type, part)
        item = self.items.get(key)
        return item.to_dict() if item else None

    def search_items(self, search_criteria):
        found_items = []
        print(search_criteria)
        for item in self.items[search_criteria['category_name']][search_criteria['sub_category_name']]:
            print(item)

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