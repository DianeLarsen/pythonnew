import inventory_manager

def main():
    print("hello world")
    ref_des = input("What is the type? ['R', 'D', 'C', 'U']: ")
    measurment = ""
    if ref_des == "R":
        ohms = input("Ohms (25k, or 25m): ")
        watts = input("Watts: (1W) ")
        measurement = ohms+"_ohms"

    part_num = input("What is the part number? ")

    
    refdes = ["R", "D", "C", "U"]

    inventory = inventory_manager.load_inventory('inventory.json')



    inventory_manager.save_inventory('inventory.json', inventory)

if __name__ == '__main__':
    main()