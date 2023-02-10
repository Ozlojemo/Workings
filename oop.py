
# Project
# Create a simple inventory management system. This project would cover several key concepts, such as object-oriented programming, file I/O, and data manipulation. Here are the requirements for the project:
# Create a class for the inventory item, with the following attributes: name, quantity, and price.
# Create a class for the inventory management system, with the following methods:
# add_item: allows the user to add a new item to the inventory
# remove_item: allows the user to remove an item from the inventory
# update_item: allows the user to update the quantity or price of an item
# display_inventory: displays the current inventory
# Allow the user to load and save the inventory from/to a CSV file


class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price
        
    def __repr__(self):
        return f"[{self.name}, {self.quantity}, {self.price}]"
        
class InventorySystem:
    def __init__(self):
        self.__inventory = []

    def add_item(self, inventory):
        self.__inventory.append(inventory)

    def remove_item(self, inventory):
        self.__inventory.remove(inventory)

    def update_item(self, inventory):
        for i,item in enumerate(self.__inventory):
            if item==inventory:
                self.__inventory[i].price = inventory.price
                self.__inventory[i].quantity = inventory.quantity
                break
                
    def display_inventory(self):
        print(f"Display Inventory: {self.__inventory}")
      
inventory_item_1 = InventoryItem("Item 1", 3, 35.8)
inventory_item_2 = InventoryItem("Item 2", 1, 52.12)
inventory_item_3 = InventoryItem("Item 3", 5, 63.12)
inventory_system = InventorySystem()
inventory_system.add_item(inventory_item_1)
inventory_system.add_item(inventory_item_2)
inventory_system.add_item(inventory_item_3)
inventory_system.display_inventory()
    