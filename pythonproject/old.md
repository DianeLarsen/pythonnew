# def main():
#     #  create an add part, update part, delete part
#     inventory = Inventory()
#     part_type = get_required_input("What is the type? ['R', 'D', 'C', 'U']: ")
#     measurment = ""
#     quantity = int(get_required_input("What is the quantity? ")) or 0
#     supplier = input("Who is the supplier? ") or "N/A"
#     location = get_required_input("Location: (i.e. EE Lab 1 right parts cabinet slot 2) ") or "N/A"
#     specs = {}
#     comments = input("Comments? ") or "N/A"

#     if part_type.upper() == "R":
#         ohms = get_required_input("Ohms (25k, or 25m): ")
        
#         watts = get_required_input("Power Rating: (1W) ")
#         tolerance = input("% tolarance: (1%) ") or "N/A"
#         if "W" not in watts:
#             watts += "W"
#         if "%" not in tolerance:
#             tolerance += "%"
#         measurment = ohms + "_ohm_" + watts
#         specs = {
#             "resistance": ohms + "ohm",
#             "tolerance": tolerance,
#             "power_rating": watts
#         }
        
#         if measurment not in inventory["resistors"]:
#             inventory["resistors"][measurment] = {
#                 "quantity": quantity,
#                 "location": location,
#                 "supplier": supplier,
#                 "specs": specs,
#                 "comments": comments
#             }
#         else:
#             print("That part is already in inventory, use update part to make changes:")
#     print(inventory["resistors"][measurment])
#     # part_num = input("What is the part number? ")
# #     if part_type.upper() == "D":
# #         diode_type = input("What is the type? (i.e. Zener Diode): ")
# # part_number = input("What is the type? (i.e. 1N4733A): ")
# # forward_voltage = input("What is the type? (i.e. Zener Diode): ") or "N/A"
# # reverse_voltage = input("What is the type? (i.e. Zener Diode): ")
# # maximum_current = input("What is the type? (i.e. Zener Diode): ")
# # reverse_current = input("What is the type? (i.e. Zener Diode): ")
# # junction_capacitance = input("What is the type? (i.e. Zener Diode): ")
# # package_type = input("What is the type? (i.e. Zener Diode): ")

# #         "part_number": "1N4733A",
# #         "forward_voltage": "N/A",
# #         "reverse_voltage": "5.1V (Zener Voltage)",
# #         "maximum_current": "49mA",
# #         "reverse_current": "N/A",
# #         "junction_capacitance": "N/A",
# #         "package_type": "DO-41",
    
    

#     inventory.add_item(InventoryItem("capacitors", "100uF_25V", 100, "Shelf A1", "ElectroParts Inc.", {"tolerance": "±5%", "temperature_coefficient": "-55 to +105°C"}))
#     inventory_json = inventory.to_json()
#     print(inventory_json)

#     # Re-create inventory from JSON
#     new_inventory = Inventory.from_json(inventory_json)
#     print(new_inventory.to_json())


 






    

# if __name__ == '__main__':
#     main()