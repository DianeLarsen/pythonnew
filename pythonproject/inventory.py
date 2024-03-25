import json

inventory = {
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
    },
    "tape": {
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
    "tools": {
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
        }
    }
}

with open('inventory.json', 'w') as file:
    json.dump(inventory, file, indent=4) 