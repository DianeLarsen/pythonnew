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
    prompt = "What would you like to do? (View, Add, Delete, Update, Search, Quit) choose first letter: "
    while True:
        user_input = get_required_input(prompt).lower()
        if user_input and user_input[0] in command_map:
            return command_map[user_input[0]]
        else:
            print("Invalid command. Please enter the first letter of one of the actions.")


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

def select_category(categories, action = ""):
    while True:
        print("Select a category by entering its number, or type 'quit' to exit:")
        for index, category in enumerate(categories.keys(), start=1):
            print(f"{index}. {category}")
        if action == 'add':
            print(f"{len(categories) + 1}. Add new category")
            print(f"{len(categories) + 2}. Edit a category")
        user_input = get_required_input("Your choice: ", allow_blank=True).lower()
        if user_input == 'quit':
            return 'quit'
        elif user_input == '':
            return ""
        try:
            choice_index = int(user_input) - 1
            if 0 <= choice_index < len(categories):
                return list(categories.keys())[choice_index]
            print("Invalid choice. Please select a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")


def select_subcategory(category, categories, action = ""):

    print(f"Select a subcategory from '{category}' (or 'exit' to exit or <enter> to return to main menu):")
    
    for i, subcategory in enumerate(categories[category], start=1):
        print(f"{i}. {subcategory}")
    if action == 'add':
        print(f"{len(subcategory) + 1}. Add new sub-category")
        print(f"{len(subcategory) + 2}. Edit a sub-category")
    print("Type 'quit' to exit or 'exit' to return to menu.")

    while True:
        choice = get_required_input("Your choice: ", allow_blank=True).lower()
        if choice == 'quit':
            return 'quit'
        elif choice == '':
            return ""
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

    items_per_page = 10
    start_index = 0

    while True:
        print("\nResults:")
        # Calculate the end index while maintaining the range within the list size
        end_index = min(start_index + items_per_page, len(found_items))

        # Display a concise list of found items within the page limit
        for index in range(start_index, end_index):
            part, item_details = found_items[index]
            print(f"{index + 1}. {part} - Location: {item_details['location']}")
        
            if index + 1 == len(found_items):
                print("End of List")

        # Handle pagination options
        print("\nEnter the number of an item to see more details, ", end="")

        if start_index > 0:
            print("type 'prev' to go back, ", end="")
        if end_index < len(found_items):
            print("type 'next' to see more items, ", end="")
        print("or 'exit' to return to the main menu.")

        choice = input("Your choice: ").strip().lower()

        if choice == 'exit':
            break # Exit to the main menu
        elif choice == 'next' and end_index < len(found_items):
            start_index = end_index  # Move to the next page
            
        elif choice == 'prev' and start_index > 0:
            start_index -= items_per_page  # Go to the previous page
        elif choice.isdigit():
            num_choice = int(choice)
            if start_index < num_choice <= end_index:
                item_index = num_choice - 1
                item_details = found_items[item_index][1]
                print(f"\nDetails for {found_items[item_index][0]}:")
                for key, value in item_details.items():
                    if key == 'specs':
                        print(f"  {key.capitalize()}:")
                        for spec_key, spec_value in value.items():
                            print(f"    {spec_key.capitalize()}: {spec_value}")
                    else:
                        print(f"  {key.capitalize()}: {value}")
                input("\nPress Enter to return to the list...")  # Pause before showing the list again
            else:
                print("Invalid selection. Please enter a valid number within the page range or use 'next', 'prev', 'exit'.")
        else:
            print("Invalid selection. Please use 'next', 'prev', 'exit', or enter a valid item number.")

            
def call_categories(inventory):
    
    return inventory.extract_categories_and_subcategories()

def add_item_workflow(inventory, inventoryManager, categories, action = 'add'):
    category_name = ""

    while True:
        # category_choice = input("Select a category, 'exit' to exit program, <enter> to return to main menu: ").strip().lower()
        category_choice = select_category(categories, action) 

        if category_choice == '':
            print("Returning to Main Menu.")
            break
        if category_choice =='exit':
            print("Exiting program.")
            exit()
        if category_choice.isdigit():
            print(categories[category_choice])
            # Handle adding a new category
            if int(category_choice) == len(categories) + 1:
                new_category_name = input("Enter the name of the new category: ").strip()
                if new_category_name == "":
                    continue
                elif new_category_name:
                    if inventory.add_category(new_category_name):
                        # Assuming there's a method to add categories
                        categories = call_categories(inventory)
            elif int(category_choice) == len(categories) + 2:
                continue
            else:
                # Handling category selection
                try:
                    category_index = int(category_choice) - 1
                    category_name = categories[category_index]
                except (ValueError, IndexError):
                    print("Invalid selection. Please try again.")
                    continue

        # Subcategory selection or creation within the selected category
        subcategory_choice = select_subcategory(category_choice, categories, action = 'add')  # Assuming a method to get subcategories
        sub_category_name = ""
        print(subcategory_choice)
        # subcategory_choice = input("Select a subcategory: ").strip().lower()
        if subcategory_choice == '':
            print("Returning to Main Menu.")
            break
        if subcategory_choice =='exit':
            print("Exiting program.")
            exit()
  
            
        if subcategory_choice == "Add new sub-category":
            new_subcategory_name = input("Enter the name of the new subcategory: ").strip()
            if new_subcategory_name == "":
                continue
            elif new_subcategory_name:
                if inventory.add_subcategory(category_name, new_subcategory_name):
                    sub_category_name = new_subcategory_name
            else:
                print("Invalid subcategory name. Please try again.")
                continue
        elif subcategory_choice == "Edit a sub-category":
            continue


        
        # Proceed with adding an item to the chosen category and subcategory
        item_to_add = {}
        example = ""
        InventoryManager.load_parts_from_file()
        if subcategory_choice in InventoryManager.master_part:
            example = InventoryManager.master_part[subcategory_choice]
        item_to_add["part_num"] = input(f"Enter part number{example}: ").strip()
        item_to_add["quantity"] = input(f"Enter amount: ").strip()
        item_to_add["location"] = input(f"Enter location(EELab1 Cab2Bin14): ").strip()
        item_to_add["supplier"] = input(f"Enter supplier: ").strip()
        item_to_add["comments"] = input(f"Enter comments: ").strip()
        item_to_add["category"] = category_choice

        item_to_add["part_type"] = subcategory_choice
        item_to_add[item_to_add["part_num"]] = inventoryManager.prompt_for_specs(subcategory_choice)
        print(item_to_add)
        newitem = InventoryItem(category_choice, subcategory_choice, item_to_add["part_num"], item_to_add["quantity"], item_to_add["location"], item_to_add[item_to_add["part_num"]], item_to_add["supplier"], item_to_add["comments"] )
        inventory.add_item(item_to_add, newitem)
        
        break  # Exit after adding an item



def handle_adding_item_to_new_category(category_name):
    # Logic to add an item to the newly created category
    pass

def handle_adding_item_to_existing_category(category_name):
    # Logic to add an item to the specified existing category
    pass

def main():
    inventory = Inventory()  # Initialize your inventory right at the start
    InventoryManager.load_specs_from_file()
    inventoryManager = InventoryManager()
    # inventory_data = InventoryManager.load_inventory() 
    # categories = InventoryManager.extract_categories(inventory_data)
    categories = call_categories(inventory)

    while True:
        categories = call_categories(inventory)
        action = get_user_command()
        # Get the user's chosen action
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

                
                    listed_items = inventory.list_items(category_name, sub_category_name)
                    display_results(listed_items)
                    break    

                else:
                    item_details = inventory.view_item(category_name, sub_category_name, part)
                    
                    print(item_details)

        # Handle 'add' action
        elif action == 'add':
            
            categories = add_item_workflow(inventory, inventoryManager, categories, action)

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
