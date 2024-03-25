import json
from manage import Inventory, InventoryItem  # Assuming 'manage' is the module name containing the classes

def create_inventory_item(category, part_type, part, details):
    # print(f"Processing: {category}, {part_type}, {part}, {details}")
    if not isinstance(details, dict):
        raise TypeError(f"Expected 'details' to be a dict, got {type(details)} instead")
    details.setdefault('comments', '')
    # For tools, 'part' is not used, so we don't pass it for tools
    if category == 'tools':
        return InventoryItem(
            category=category,
            part_type=part_type,
            part='',  # Assuming 'part' is not applicable for tools
            **details  # Unpacks quantity, location, etc., from the details dict
        )
    else:
        return InventoryItem(
            category=category,
            part_type=part_type,
            part=part,
            **details  # Unpacks quantity, location, etc., from the details dict
        )


def build_and_save_inventory():
    raw_inventory_data = {
    "components": {
        "capacitors": {
            "100uF_25V": {
                "quantity": 100,
                "location": "Shelf A1",
                "supplier": "ElectroParts Inc.",
                "specs": {
                    "tolerance": "±5%",
                    "temperature_coefficient": "-55 to +105°C"
                }
            },
            "470uF_10V": {
                "quantity": 50,
                "location": "Shelf A2",
                "supplier": "Components Co.",
                "specs": {
                    "tolerance": "±10%",
                    "temperature_coefficient": "-55 to +105°C"
                }
            }
        },
        "resistors": {
            "220_ohm_1W": {
                "quantity": 200,
                "location": "Shelf B1",
                "supplier": "ResistAll",
                "specs": {
                    "resistance": "220 ohm",
                    "tolerance": "±1%",
                    "power_rating": "1W"
                }
            },
            "10K_ohm_0.5W": {
                "quantity": 150,
                "location": "Shelf B2",
                "supplier": "OhmSource",
                "specs": {
                    "resistance": "10K ohm",
                    "tolerance": "±5%",
                    "power_rating": "0.5W"
                }
            }
        }
        # Add the rest of the components here following the same structure.
    },
    "tools": {
        # Existing tools data plus tape, assuming it's used for electrical purposes and fits best here.
        "screwdriver_set": {
            "quantity": 4,
            "location": "Tool Rack",
            "supplier": "ToolMakers Inc.",
            "specs": {
                "pieces": "6",
                "handle_material": "rubber"
            }
        },
        "soldering_iron": {
            "quantity": 2,
            "location": "Tool Rack",
            "supplier": "HeatPro",
            "specs": {
                "wattage": "60W",
                "temperature_range": "200°C - 450°C"
            }
        },
        "electrical_tape": {
            "quantity": 10,
            "location": "Drawer 1",
            "supplier": "GeneralSupplies",
            "specs": {
                "width": "20mm",
                "length": "10m",
                "color": "black"
            }
        },
        "double_sided_tape": {
            "quantity": 5,
            "location": "Drawer 2",
            "supplier": "AdhesiveWorld",
            "specs": {
                "width": "10mm",
                "length": "5m",
                "adhesive_type": "permanent"
            }
        }
    },
    "office equipment": {
        "printers": {
            "laser_printer_3000": {
                "quantity": 3,
                "location": "Office Supply Room",
                "supplier": "PrintTech",
                "specs": {
                    "type": "Laser",
                    "color_capability": "Monochrome",
                    "connectivity": "USB, Ethernet"
                }
            },
            "inkjet_color_printer_X2": {
                "quantity": 2,
                "location": "Design Department",
                "supplier": "InkSolutions",
                "specs": {
                    "type": "Inkjet",
                    "color_capability": "Color",
                    "connectivity": "Wi-Fi, USB"
                }
            }
        },
        "computers": {
            "office_desktop_500": {
                "quantity": 10,
                "location": "IT Department",
                "supplier": "CompFast",
                "specs": {
                    "processor": "Intel i5",
                    "RAM": "8GB",
                    "storage": "256GB SSD"
                }
            }
        },
        "monitors": {
            "ultra_wide_monitor": {
                "quantity": 5,
                "location": "Design Department",
                "supplier": "ScreenTech",
                "specs": {
                    "size": "34 inches",
                    "resolution": "3440 x 1440",
                    "refresh_rate": "100Hz"
                }
            }
        }
    },
    "hardware": {
        "screws": {
            "m3_pan_head": {
                "quantity": 1000,
                "location": "Hardware Shelf 1",
                "supplier": "BuildRight",
                "specs": {
                    "length": "10mm",
                    "material": "Stainless steel",
                    "head_type": "Pan head"
                }
            }
        },
        "nails": {
            "steel_nail_2inch": {
                "quantity": 500,
                "location": "Hardware Shelf 2",
                "supplier": "FastenPro",
                "specs": {
                    "length": "2 inches",
                    "material": "Steel",
                    "type": "Common nail"
                }
            }
        },
        "brackets": {
            "angle_bracket": {
                "quantity": 100,
                "location": "Hardware Shelf 3",
                "supplier": "CornerStrong",
                "specs": {
                    "size": "50mm x 50mm x 40mm",
                    "material": "Aluminum",
                    "thickness": "3mm"
                }
            }
        }
    },
    "device parts": {
        "screens": {
            "smartphone_oled_screen_6inch": {
                "quantity": 20,
                "location": "Parts Room 1",
                "supplier": "ScreenMasters",
                "specs": {
                    "type": "OLED",
                    "size": "6 inches",
                    "resolution": "2340 x 1080"
                }
            }
        },
        "batteries": {
            "lithium_ion_3000mAh": {
                "quantity": 50,
                "location": "Parts Room 2",
                "supplier": "EnergyPlus",
                "specs": {
                    "type": "Lithium-ion",
                    "capacity": "3000mAh",
                    "voltage": "3.7V"
                }
            }
        },
        "covers": {
            "smartphone_cover_rugged": {
                "quantity": 30,
                "location": "Parts Room 3",
                "supplier": "CoverCraft",
                "specs": {
                    "material": "Silicone",
                    "compatibility": "Universal 6'' devices",
                    "features": "Shock-resistant, Water-resistant"
                }
            }
        }
    }

}


    inventory = Inventory()

    # Loop through the raw data to create and add inventory items
    for category, types in raw_inventory_data.items():
        for part_type, parts in types.items():
            if category == 'tools':
                # Initialize an empty dictionary to collect the tool's details
                tool_details = {}
                for attribute, value in parts.items():
                    # For tools, aggregate attributes into a single dictionary
                    tool_details[attribute] = value

                try:
                    item = create_inventory_item(category, part_type, 'specs', tool_details)
                    inventory.add_item(item)
                except KeyError as e:
                    print(f"Missing expected detail: {e}")
            else:
                # Process components as before
                for part, details in parts.items():

                    try:
                        item = create_inventory_item(category, part_type, part, details)
                        inventory.add_item(item)
                    except KeyError as e:
                        print(f"Missing expected detail: {e}")


    # Convert the inventory to JSON format and save
    inventory_json = inventory.to_json(inventory)
    with open('inventory.json', 'w') as file:
        file.write(inventory_json)

if __name__ == "__main__":
    build_and_save_inventory()