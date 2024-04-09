from manage import Inventory, InventoryItem, InventoryManager


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


def handle_action(action, categories):
    print(f"Handling {action}...")
    category = select_category(categories)
    if category == 'quit':
        return 'quit'

    subcategory = select_subcategory(category, categories)
    if subcategory == 'quit':
        return 'quit'

    # Proceed with action handling for the selected subcategory
    print(f"Would handle {action} for {subcategory} in {category}.")
    return {category, subcategory}

def select_category(categories):
    print("Select a category by entering its number, or type 'quit' to exit:")
    keys = list(categories.keys())
    for i, category in enumerate(keys, start=1):
        print(f"{i}. {category}")
    print("Type 'quit' to exit or 'exit' to return to menu.")

    while True:
        user_input = get_required_input("Your choice: ", allow_blank=True).lower()
        if user_input == 'quit':
            return "quit"
        if user_input == 'exit':
            return 'exit'
        try:
 
            choice = int(user_input) - 1
            if choice in range(len(categories)):
                return list(categories.keys())[choice]
            raise ValueError
        except ValueError as e:
            print(f"Your choice was not listed.  Please enter a valid number from the list or type 'quit' to exit: ")


def select_subcategory(category, categories):
    
    if not category:
        return "quit"
    print(f"Select a subcategory from '{category}' (or 'quit' to exit or 'exit' to return to main menu):")
    
    for i, subcategory in enumerate(categories[category], start=1):
        print(f"{i}. {subcategory}")
    print("Type 'quit' to exit or 'exit' to return to menu.")

    while True:
        choice = get_required_input("Your choice: ", allow_blank=True).lower()
        if choice == 'quit':
            return 'quit'
        if choice == 'exit':
            return 'exit'
        try:
            choice = int(choice) - 1
            if choice in range(len(categories[category])):
                return categories[category][choice]
            raise ValueError
        except ValueError as e:
            print(
                f"{e} Please enter a valid number from the list or type 'quit' to exit or 'exit' to return to main menu.")

def display_results(found_items):
    if not found_items:
        print("No items found matching criteria.")
        return

    while True:  # Keep showing the list until the user decides to exit to the main menu
        print("\nResults:")
        # Display a concise list of found items
        for index, (part, item_details) in enumerate(found_items, start=1):
            print(f"{index}. {part} - Location: {item_details['location']}")

        print("\nEnter the number of an item to see more details, or type 'exit' to return to the main menu.")
        choice = input("Your choice: ").strip().lower()

        if choice == 'exit':
            break  # Exit to the main menu

        if choice.isdigit() and 1 <= int(choice) <= len(found_items):
            index = int(choice) - 1
            _, _, part, item_details = found_items[index]
            print(f"\nDetails for {part}:")
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
            
def call_categories(inventory):
    
    return inventory.extract_categories_and_subcategories()

def add_item_workflow(inventory, categories):

    while True:
        category_name = select_category(categories)
        if category_name == 'quit':  # Allow user to quit during category selection
            print("Exiting program.")
            break
        elif category_name == 'exit':
            print("Returning to Main Meu.")
            get_user_command()
        else:
            sub_category_name = select_subcategory(category_name, categories)
            if sub_category_name == 'quit':  # Allow user to quit during subcategory selection
                print("Exiting program.")
                break
            elif sub_category_name == 'exit':
                print("Returning to Main Meu.")
                get_user_command()
                break
            # Display existing categories with an option to add a new one
            # print("Select a category by number, 'n' to add a new category, or type 'quit' to exit:")
            for i, category in enumerate(categories, 1):
                print(f"{i}. {category}")
            print(f"{len(categories) + 1}. Add new category")

        choice = input("Your choice: ").lower()
        
        if choice == 'quit':
            print("Exiting program.")
            break  # Exit the add item workflow and go back to the main menu
        elif int(choice) == len(categories) + 1:  # Adjusted to handle dynamic category count
            new_category = input("Enter the name of the new category: ").strip()
            if new_category:  # Check if a new category name was actually provided
                inventory.add_category(new_category)
                categories = call_categories(inventory)
                # Add the new category to the list
                continue
            else:
                print("Invalid category name. Please try again.")
        else:
            try:
                choice_index = int(choice) - 1
                if choice_index in range(len(categories)):
                    category_name = categories[choice_index]
                    # Here, instead of directly handling item addition, ask if user wants to add an item or return to the category list
                    print(f"Selected category: {category_name}")
                    add_item = input("Do you want to add an item to this category? (yes/no): ").lower()
                    if add_item == 'yes':
                        # Assume we have a function to handle adding items to an existing category
                        handle_adding_item_to_existing_category(category_name)
                        break  # After adding an item, break the loop to go back to the main menu
                else:
                    raise ValueError
            except ValueError:
                print("Invalid selection. Please try again.")



def handle_adding_item_to_new_category(category_name):
    # Logic to add an item to the newly created category
    pass

def handle_adding_item_to_existing_category(category_name):
    # Logic to add an item to the specified existing category
    pass

def main():
    inventory = Inventory()  # Initialize your inventory right at the start
    InventoryManager.load_specs_from_file()
    # inventory_data = InventoryManager.load_inventory() 
    # categories = InventoryManager.extract_categories(inventory_data)
    categories = call_categories(inventory)

    while True:
        action = get_user_command()  # Get the user's chosen action
        if action == 'quit':
            print("Exiting program.")
            break

        # Handle 'view' action
        if action == 'view':
            # categories = add_item_workflow(inventory, categories)
            category_name = select_category(categories)
            if category_name == 'quit':  # Allow user to quit during category selection
                print("Exiting program.")
                break
            sub_category_name = select_subcategory(category_name, categories)
            if sub_category_name == 'quit':  # Allow user to quit during subcategory selection
                print("Exiting program.")
                break
            while True:
                part = input(
                "Enter the item's part or <list> for a list (or press Enter to return): ").strip()
                if part == "":
                    break
                elif part == "list":
                    start = 0
                    while True:
                        listed_items, next_start = inventory.list_items(category_name, sub_category_name, start=start)
                        display_results(listed_items)
                        # for _, item in listed_items:
                        #     print(item['part'])  # Customize based on how you want the items displayed
                        if next_start is not None:
                            next_action = input("Press 'list' again for more items, 'back' to return, or 'quit' to exit: ").strip().lower()
                            if next_action == 'list':
                                start = next_start
                                continue
                            elif next_action == 'back':
                                break
                            elif next_action == 'quit':
                                exit()  # Or handle the quit action as per your program's flow
                        else:
                            print("End of list.")
                            break
                else:
                    item_details = inventory.view_item(category_name, sub_category_name, part)
                    
                    print(item_details)

        # Handle 'add' action
        elif action == 'add':
            
            categories = add_item_workflow(inventory, categories)

        # Handle 'delete' action
        elif action == 'delete':
            part = input(
                "Enter the item's part (or press Enter to return): ").strip()
            print("Item deleted successfully." if inventory.delete_item(
                sub_category_name, part) else "Failed to delete item. It might not exist.")

        # Handle 'update' action
        elif action == 'update':
            part = input(
                "Enter the item's part (or press Enter to return): ").strip()
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
        elif action == 'search':
            search_option = input("Press Enter for advanced search, or type a keyword for basic search: ").strip()
            subcategory, category = handle_action("Advanced search mode.", categories)
            print(category, subcategory)
            if search_option == "":
                # Advanced search mode
                if subcategory == "capacitors":
                    print("Advanced search for capacitors.")
                    capacity = input("Enter capacity (e.g., 100uF): ").strip()
                    tolerance = input("Enter tolerance (e.g., ±5%): ").strip()
                    voltage = input("Enter voltage rating (e.g., 50V): ").strip()
                    search_criteria = {
                        'category_name': category,
                        'sub_category_name': subcategory,
                        'capacity': capacity,
                        'tolerance': tolerance,
                        'voltage': voltage
                    }
                # Template for adding another subcategory with specific search criteria
                # elif sub_category_name == "other_subcategory":
                #     # Collect other specific criteria...
                else:
                    print(f"No advanced search available for {subcategory}, switching to basic search.")
                    part = input("Enter search term: ").strip()
                    search_criteria = {
                        'part': part,
                        'category_name': category,
                        'sub_category_name': subcategory
                    }
            else:
                # Basic search with a part keyword
                search_criteria = {
                    'part': search_option,
                    'category_name': category,
                    'sub_category_name': subcategory
                }

            # Perform the search with the criteria
            found_items = inventory.search_items(search_criteria)
            if found_items:
                display_results(found_items)
            else:
                print("No items found matching criteria.")


        else:
            print("Invalid action.")


if __name__ == "__main__":
    main()
