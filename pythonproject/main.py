from manage import Inventory, InventoryItem, InventoryManager

categories = {
    "components": ["capacitors", "resistors", "diodes", "inductors", "chips", "FETs"], 
    "tools": ["screwdrivers", "pliers", "soldering irons"], 
    "office equipment": ["printers", "computers", "monitors"], 
    "hardware": ["screws", "nails", "brackets"], 
    "device parts": ["screens", "batteries", "covers"]}


def get_required_input(prompt, allow_blank=False):
    """Prompt user until valid input is provided."""
    while True:
        user_input = input(prompt).strip()
        if user_input or allow_blank:
            return user_input
        print("This field is required. Please enter a value.")


def get_user_command():
    """Prompt for and return a user command."""
    command_map = {
        'v': 'view',
        'a': 'add',
        'd': 'delete',
        'u': 'update',
        's': 'search',
        'q': 'quit'
    }
    while True:
        user_input = get_required_input(
            "What would you like to do? (View, Add, Delete, Update, Search, Quit) choose first letter: ").lower()
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
    print(
        f"Select a sub-category from {category_name} by entering its number, or type 'quit' to exit: ")
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
            print(
                f"{e} Please enter a valid number from the list or type 'quit' to exit.")

def display_search_results(found_items):
    if not found_items:
        print("No items found matching criteria.")
        return

    while True:  # Keep showing the list until the user decides to exit to the main menu
        print("\nSearch Results:")
        # Display a concise list of found items
        for index, (category_name, part_type, part_name, item_details) in enumerate(found_items, start=1):
            print(f"{index}. {part_name} - Location: {item_details['location']}")

        print("\nEnter the number of an item to see more details, or type 'exit' to return to the main menu.")
        choice = input("Your choice: ").strip().lower()

        if choice == 'exit':
            break  # Exit to the main menu

        if choice.isdigit() and 1 <= int(choice) <= len(found_items):
            index = int(choice) - 1
            _, _, part_name, item_details = found_items[index]
            print(f"\nDetails for {part_name}:")
            for key, value in item_details.items():
                if key == 'specs':
                    print(f"  {key.capitalize()}:")
                    for spec_key, spec_value in value.items():
                        print(f"    {spec_key.capitalize()}: {spec_value}")
                else:
                    print(f"  {key.capitalize()}: {value}")
            input("\nPress Enter to return to the list...")  # Pause before showing the list again
        else:
            print("Invalid selection. Please enter a valid number or 'exit' to return to the main menu.")


def main():
    inventory = Inventory()  # Initialize your inventory right at the start
    InventoryManager.load_specs_from_file()
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
                part = input(
                    "Enter the item's part (or press Enter to return): ").strip()

            # Handle 'view' action
            if action == 'view':
                if part == "":
                    continue
                item_details = inventory.view_item(sub_category_name, part)
                print(item_details if item_details else "Item not found.")

            # Handle 'add' action
            elif action == 'add':
                part = get_required_input("Enter part # or classification (i.e., 100mF_10V): ")
                quantity = int(get_required_input("Enter quantity: "))
                location = get_required_input("Enter location: ")
                supplier = input("Enter supplier: ")
                specs = InventoryManager.prompt_for_specs(sub_category_name)
                
                # New section for additional specs
                add_more_specs = input("Would you like to add more specifications? (yes/no): ").lower()
                while add_more_specs == 'yes':
                    spec_key = input("Enter the specification name: ")
                    spec_value = input("Enter the specification value: ")
                    specs[spec_key] = spec_value
                    
                    InventoryManager.load_specs_from_file()
                    # Check if this is a new specification and update the master_specs accordingly
                    if spec_key not in InventoryManager.master_specs[sub_category_name]:
                        # Append the new spec name to the list for this sub-category
                        InventoryManager.master_specs[sub_category_name].append(spec_key)
                        # Save the updated specs to file
                        InventoryManager.save_specs_to_file()
                        print(f"Adding '{spec_key}' to master specifications for '{sub_category_name}'.")

                    add_more_specs = input("Add more specifications? (yes/no): ").lower()

                comments = get_required_input("Enter comments: ")
                item = InventoryItem(
                    category_name,
                    sub_category_name,
                    part,
                    quantity,
                    location,
                    supplier,
                    specs,
                    comments)
                
                item_add_success = inventory.add_item(item)
                if item_add_success is True:
                    print("Item added successfully.")
                else:
                    print("Failed to add item. It might already exist.")
                    user_choice = input("Choose an option: (1) Override, (2) Update current, (3) Change new: ")
                    
                    if user_choice == "1":
                        # Code to handle override option
                        inventory.override_item(item)
                        print("Item overridden successfully.")
                    elif user_choice == "2":
                        # Code to handle update current option
                        inventory.update_current_item(item)
                        print("Current item updated successfully.")
                    elif user_choice == "3":
                        # Code to gather new item changes and call update
                        # Assuming you have a method to update changes in an item
                        new_specs = InventoryManager.prompt_for_specs(sub_category_name)
                        item.update_specs(new_specs)
                        inventory.update_new_item(item)
                        print("New item updated with changes successfully.")


            # Handle 'delete' action
            elif action == 'delete':
                print("Item deleted successfully." if inventory.delete_item(
                    sub_category_name, part) else "Failed to delete item. It might not exist.")

            # Handle 'update' action
            elif action == 'update':
                new_quantity = int(get_required_input("Enter new quantity: "))
                new_location = get_required_input("Enter new location: ")
                new_comments = get_required_input("Enter new comments: ")
                # Prompt for new specs related to the type
                new_specs = InventoryItem.prompt_for_specs(sub_category_name)
                if inventory.update_item(
                        category_name,
                        sub_category_name,
                        part,
                        new_quantity,
                        new_location,
                        new_specs,
                        new_comments):
                    print("Item updated successfully.")
                else:
                    print("Failed to update item. It might not exist.")

            # Handle 'search' action
            # Handle 'search' action
            elif action == 'search':
                search_option = input("Press Enter for advanced search, or type a keyword for basic search: ").strip()

                if search_option == "":
                    # Advanced search mode
                    print("Advanced search mode.")
                    if sub_category_name == "capacitors":
                        print("Advanced search for capacitors.")
                        capacity = input("Enter capacity (e.g., 100uF): ").strip()
                        tolerance = input("Enter tolerance (e.g., ±5%): ").strip()
                        voltage = input("Enter voltage rating (e.g., 50V): ").strip()
                        search_criteria = {
                            'category_name': category_name,
                            'sub_category_name': sub_category_name,
                            'capacity': capacity,
                            'tolerance': tolerance,
                            'voltage': voltage
                        }
                    # Template for adding another subcategory with specific search criteria
                    # elif sub_category_name == "other_subcategory":
                    #     # Collect other specific criteria...
                    else:
                        print(f"No advanced search available for {sub_category_name}, switching to basic search.")
                        part = input("Enter search term: ").strip()
                        search_criteria = {
                            'part': part,
                            'category_name': category_name,
                            'sub_category_name': sub_category_name
                        }
                else:
                    # Basic search with a part keyword
                    search_criteria = {
                        'part': search_option,
                        'category_name': category_name,
                        'sub_category_name': sub_category_name
                    }

                # Perform the search with the criteria
                found_items = inventory.search_items(search_criteria)
                if found_items:
                    display_search_results(found_items)
                else:
                    print("No items found matching criteria.")


            else:
                print("Invalid action.")


if __name__ == "__main__":
    main()
