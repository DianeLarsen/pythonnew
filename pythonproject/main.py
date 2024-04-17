from manage import Inventory, InventoryItem, InventoryManager


def get_required_input(prompt, allow_blank=False):
    """Prompt user until valid input is provided."""
    while True:
        user_input = input(prompt).strip()
        if user_input or allow_blank:
            return user_input
        print("This field is required. Please enter a value.")

def handle_quit():
    quit_choice = input("Are you sure you want to quit?  (yes/no): ").strip()
    if quit_choice == 'yes' or quit_choice == 'y':
        print("Exiting program...")
        exit()
    else:
        return

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
    category = select_category(categories, action)
    if category == 'quit':
        handle_quit()

    subcategory = select_subcategory(category, categories, action)
    if subcategory == 'quit':
        handle_quit()

    # Proceed with action handling for the selected subcategory
    print(f"Handling {action} for {subcategory} in {category}.")
    print(category, subcategory)
    return category, subcategory

def select_category(categories, action = ""):
    print(action)
    while True:
        print("Select a category by entering its number, or type 'quit' to exit:")
        for index, category in enumerate(categories.keys(), start=1):
            print(f"{index}. {category}")
        if action == 'Add mode':
            print(f"{len(categories) + 1}. Add new category")
            print(f"{len(categories) + 2}. Edit a category")
        user_input = get_required_input("Your choice: ", allow_blank=True).lower()
        if user_input == 'quit':
            handle_quit()
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
    if action == 'Add mode':
        print(f"{len(subcategory) + 1}. Add new sub-category")
        print(f"{len(subcategory) + 2}. Edit a sub-category")
    print("Type 'quit' to exit or 'exit' to return to menu.")

    while True:
        choice = get_required_input("Your choice: ", allow_blank=True).lower()
        if choice == 'quit':
            handle_quit()
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

def display_results(inventory, found_items, category, subcategory, action = 'search'):
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
            part, location, item_details = found_items[index]['part'], found_items[index]['location'], found_items[index]['specs']
            if action == 'search' or action == 'update':
                print(f"{index + 1}. {part} - Location: {location}")
            if action == 'delete':
                print(f"{index + 1}. {part}")

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
                item_details = found_items[item_index]
                
                    
                print(f"\nDetails for {found_items[item_index]}:")
                for key, value in item_details.items():
                    if key == 'specs':
                        print(f"  {key.capitalize()}:")
                        for spec_key, spec_value in value.items():
                            print(f"    {spec_key.capitalize()}: {spec_value}")
                    else:
                        print(f"  {key.capitalize()}: {value}")
                if action == 'delete':
                    delete_input = input("Would you like to delete this item (yes/no): ").strip()
                    if delete_input == "yes" or delete_input == "y":
                        return found_items[item_index]
                if action == 'update':
                    update_input = input("Would you like to update this item (yes/no): ").strip()
                    if update_input == "yes" or update_input == "y":
                        handle_update(inventory, found_items[item_index], category, subcategory)
                input("\nPress Enter to return to the list...")  # Pause before showing the list again
            else:
                print("Invalid selection. Please enter a valid number within the page range or use 'next', 'prev', 'exit'.")
        else:
            print("Invalid selection. Please use 'next', 'prev', 'exit', or enter a valid item number.")

def display_item(item):
    for index, (k, v) in enumerate(item.items(), start=1):
        print(f"{index}. {k}: {v}")

def get_input_for_key(key, current_value):
    if isinstance(current_value, dict):  # Handle nested dictionaries
        for subkey, subvalue in current_value.items():
            new_subvalue = input(f"Update {subkey} [{subvalue}]: ")
            if new_subvalue.lower() == 'cancel':
                return 'cancel'
            elif new_subvalue == '':
                continue
            elif new_subvalue.lower() == 'clear':
                current_value[subkey] = ''
            else:
                current_value[subkey] = new_subvalue
    else:
        new_value = input(f"Update {key} [{current_value}]: ")
        if new_value.lower() == 'cancel':
            return 'cancel'
        elif new_value == '':
            pass
        elif new_value.lower() == 'clear':
            current_value = ''
        else:
            current_value = new_value
    return current_value

def handle_update(inventory, item, category, subcategory):
    print("Current item details:")
    display_item(item)
    print(item)
    updated_item = item.copy()
    # partdes = 
    keys_list = list(item.keys())

    while True:
        print("\nType the number of the field you wish to update, or type 'done' to finish:")
        user_choice = input("Your choice: ").strip().lower()
        if user_choice == 'done':
            break
        if user_choice.isdigit() and 1 <= int(user_choice) <= len(keys_list):
            key = keys_list[int(user_choice) - 1]
            current_value = updated_item[key]
            result = get_input_for_key(key, current_value)
            if result == 'cancel':
                return
            updated_item[key] = result if result != 'cancel' else updated_item[key]
        else:
            print("Invalid option, please try again.")

    print("\nReview changes:")
    print("Old item:")
    for k, v in item.items():
        print(f"{k}: {v}")
    print("Updated item:")
    for k, v in updated_item.items():
        print(f"{k}: {v}")
    confirm = input("Confirm changes (yes/no): ").strip().lower()
    if confirm.lower() == 'yes' or confirm.lower() == 'y':
        item.update(updated_item)
        if inventory.update_item(category, subcategory, item):
            print("Changes have been confirmed and applied.")
        else:
            print("Update not valid")
    elif confirm.lower() == 'no' or confirm.lower() == 'n':
        print("Changes not confirmed. You can modify the changes again.")
          # Recursive call to modify the item again
            
def call_categories(inventory):
    
    return inventory.extract_categories_and_subcategories()

def add_item_workflow(inventory, inventoryManager, categories, action = 'add'):

    while True:
        category_choice, subcategory_choice = handle_action("Add mode", categories)
        if subcategory_choice == "Add new sub-category":
            new_subcategory_name = input("Enter the name of the new subcategory: ").strip()
            if new_subcategory_name == "":
                continue
            elif new_subcategory_name:
                if inventory.add_subcategory(category_choice, new_subcategory_name):
                    subcategory_choice = new_subcategory_name
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
        while not item_to_add["part_num"]:
            item_to_add["part_num"] = input(f"Enter part number{example} - required: ").strip()
        item_to_add["quantity"] = input(f"Enter amount: ").strip()
        while not item_to_add["quantity"]:
            item_to_add["quantity"] = input(f"Enter amount - required: ").strip()
        item_to_add["location"] = input(f"Enter location(EELab1 Cab2Bin14): ").strip()
        while not item_to_add["location"]:
            item_to_add["location"] = input(f"Enter location (EELab1 Cab2Bin14) - required: ").strip()
        item_to_add["supplier"] = input(f"Enter supplier: ").strip()
        while not item_to_add["supplier"]:
            item_to_add["supplier"] = input(f"Enter supplier - required: ").strip()
        item_to_add["comments"] = input(f"Enter comments: ").strip()
        
        item_to_add["category"] = category_choice

        item_to_add["part_type"] = subcategory_choice
        item_to_add[item_to_add["part_num"]] = inventoryManager.prompt_for_specs(subcategory_choice)

        newitem = InventoryItem(category_choice, subcategory_choice, item_to_add["part_num"], item_to_add["quantity"], item_to_add["location"], item_to_add[item_to_add["part_num"]], item_to_add["supplier"], item_to_add["comments"] )
        inventory.add_item(item_to_add, newitem)
        
        break  # Exit after adding an item

def handle_search(inventory, categories, action = "search"):
    category, subcategory = handle_action("Search mode", categories)
    search_option = input("Press Enter for advanced search, or type a keyword for basic search: ").strip()
    
    print("cat, sub", category, subcategory)
    if search_option == "":
        specs = {}
        # Advanced search mode
        if subcategory in InventoryManager.master_specs:
            
            print("Advanced search for capacitors.")
            type_specs = InventoryManager.master_specs[subcategory]
            for spec in type_specs:
                user_input = input(f"Enter {spec}: ")  # Removed the example part for simplicity
                specs[spec] = user_input
                search_criteria = specs
                search_criteria["category"] = category
                search_criteria["subcategory"] = subcategory
            
        else:
            print(f"No advanced search available for {subcategory}, switching to basic search.")
            part = input("Enter search term: ").strip()
            search_criteria = {
                'part': part,
                'category': category,
                'subcategory': subcategory
            }
    else:
        # Basic search with a part keyword
        search_criteria = {
            'part': search_option,
            'category': category,
            'subcategory': subcategory
        }

    # Perform the search with the criteria
    found_items = inventory.search_items(search_criteria)
    if found_items:
        item_to_delete = display_results(inventory, found_items, category, subcategory, action )
        for item in found_items:
            print(item)

        if action == 'delete':
            print("action", action, True)
            return item_to_delete# ask if want to delete this item
    else:
        print("No items found matching criteria.")

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
            handle_quit()

        # Handle 'view' action
        if action == 'view':

            # categories = add_item_workflow(inventory, categories)
            category_name, sub_category_name = handle_action("View mode", categories)
            while True:
                part = input(
                "Enter the item's part or <list> for a list (or press Enter to return): ").strip()
                if part == "":
                    break
                elif part == "list":

                
                    listed_items = inventory.list_items(category_name, sub_category_name)
                    if None in listed_items:
                         print("No items found matching criteria.")
                    # dict_items = dict(listed_items)
                    # for item in listed_items:
                    #     print(f"Part: {item['part']}, Quantity: {item['quantity']}")
                    display_results(inventory, listed_items, category_name, sub_category_name)
                    break    

                else:
                    inventory.view_item(category_name, sub_category_name, part)
                    
                    # print(item_details)

        # Handle 'add' action
        elif action == 'add':
            
            categories = add_item_workflow(inventory, inventoryManager, categories, action)

        # Handle 'delete' action
        elif action == 'delete':
            item_details = handle_search(inventory, categories, action = 'delete')
            print(item_details)
            print("Item deleted successfully." if inventory.delete_item(item_details["category"],item_details["part_type"], item_details['part']) else "Failed to delete item. It might not exist.")

        # Handle 'update' action
        elif action == 'update':
            handle_search(inventory, categories, action = 'update')


        # Handle 'search' action
        elif action == 'search':
            handle_search(inventory, categories, action = 'search')


        else:
            print("Invalid action.")


if __name__ == "__main__":
    main()
