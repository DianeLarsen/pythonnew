from manage import Inventory, InventoryItem

categories = {
    "components": ["capacitors", "resistors", "diodes", "inductors", "chips", "FETs"],
    "tools": ["screwdrivers", "pliers", "soldering irons"],
    "office equipment": ["printers", "computers", "monitors"],
    "hardware": ["screws", "nails", "brackets"],
    "device parts": ["screens", "batteries", "covers"]
}

def get_required_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input:
            return user_input
        else:
            print("This field is required. Please enter a value.")
            
def get_user_command():
    command_map = {
        'v': 'view',
        'a': 'add',
        'd': 'delete',
        'u': 'update',
        's': 'search',
        'q': 'quit'
    }
    while True:
        user_input = input("What would you like to do? (View, Add, Delete, Update, Search, Quit): ").lower()
        if user_input and user_input[0] in command_map:
            return command_map[user_input[0]]
        else:
            print("Invalid command. Please enter the first letter of one of the actions (View, Add, Delete, Update, Search, Quit).")

        
def handle_action(action):
    print(f"Handling {action}...")
    category = select_category(categories)
    if category == 'quit':
        return 'quit'
    
    subcategory = select_subcategory(category)
    if subcategory == 'quit':
        return 'quit'
    
    # Proceed with action handling for the selected subcategory
    print(f"Would handle {action} for {subcategory} in {category}.")

        
def select_category(categories):
    print("Select a category by entering its number, or type 'quit' to exit:")
    keys = list(categories.keys())
    for i, category in enumerate(keys, start=1):
        print(f"{i}. {category}")
    print("Type 'quit' to exit.")
    
    while True:
        user_input = input()
        if user_input.lower() == 'quit':
            return 'quit'
        try:
            category_num = int(user_input) - 1
            if category_num < 0 or category_num >= len(keys):
                raise ValueError("Invalid number.")
            category_name = keys[category_num]
            
            return category_name
        except ValueError as e:
            print(f"Your choice was not listed.  Please enter a valid number from the list or type 'quit' to exit: ")


def select_subcategory(category_name):
    sub_categories = categories[category_name]
    print(f"Select a sub-category from {category_name} by entering its number, or type 'quit' to exit: ")
    for i, sub_category in enumerate(sub_categories, start=1):
        print(f"{i}. {sub_category}")
    print("Type 'quit' to exit.")
    
    while True:
        user_input = input()
        if user_input.lower() == 'quit':
            return 'quit'
        try:
            sub_category_num = int(user_input) - 1
            if sub_category_num < 0 or sub_category_num >= len(sub_categories):
                raise ValueError("Invalid number.")
            sub_category_name = sub_categories[sub_category_num]
            return sub_category_name
        except ValueError as e:
            print(f"{e} Please enter a valid number from the list or type 'quit' to exit.")



def main():
    inventory = Inventory()  # Initialize your inventory right at the start

    while True:
        action = get_user_command()  # Get the user's chosen action
        if action == 'quit':
            print("Exiting program.")
            break

        # If the action is not 'quit', proceed to select category and part
        if action in ['view', 'add', 'delete', 'update', 'search']:
            category_name = select_category(categories)
            if category_name == 'quit':  # Allow user to quit during category selection
                continue
            sub_category_name = select_subcategory(category_name)
            if sub_category_name == 'quit':  # Allow user to quit during subcategory selection
                continue
            
            part = ""  # Initialize part variable
            if action in ['view', 'delete', 'update']:
                part = input("Enter the item's part (or press Enter to return): ").strip()
            
            # Handle 'view' action
            if action == 'view':
                if part == "":
                    continue
                item_details = inventory.view_item(sub_category_name, part)
                print(item_details if item_details else "Item not found.")

            # Handle 'add' action
            elif action == 'add':
                quantity = int(get_required_input("Enter quantity: "))
                location = get_required_input("Enter location: ")
                supplier = input("Enter supplier: ")
                specs = InventoryItem.prompt_for_specs(sub_category_name)
                comments = get_required_input("Enter comments: ")
                item = InventoryItem(sub_category_name, part, quantity, location, supplier, specs, comments)
                print("Item added successfully." if inventory.add_item(item) else "Failed to add item. It might already exist.")

            # Handle 'delete' action
            elif action == 'delete':
                print("Item deleted successfully." if inventory.delete_item(sub_category_name, part) else "Failed to delete item. It might not exist.")

            # Handle 'update' action
            elif action == 'update':
                new_quantity = int(get_required_input("Enter new quantity: "))
                new_location = get_required_input("Enter new location: ")
                new_comments = get_required_input("Enter new comments: ")
                # Prompt for new specs related to the type
                new_specs = InventoryItem.prompt_for_specs(sub_category_name)
                if inventory.update_item(sub_category_name, part, new_quantity, new_location, new_specs, new_comments):
                    print("Item updated successfully.")
                else:
                    print("Failed to update item. It might not exist.")
            
            # Handle 'search' action
            elif action == 'search':
                part = input("Enter search term (or press Enter to return): ").strip()
                if part == "":
                    continue
                search_criteria = {'part': part, 'category_name': category_name, 'sub_category_name': sub_category_name}
                found_items = inventory.search_items(search_criteria)
                if found_items:
                    for item_name, item_details in found_items:
                        print(f"Found {item_name}: {item_details}")
                else:
                    print("No items found matching criteria.")
            else:
                print("Invalid action.")

if __name__ == "__main__":
    main()