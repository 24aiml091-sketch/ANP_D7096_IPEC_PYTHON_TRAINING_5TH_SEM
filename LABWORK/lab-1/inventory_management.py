'''Problem Statement: Create a dictionary to maintain the stock of products in a shop.
 Example: { 'Laptop': 15, 'Mouse': 40, 'Keyboard': 25, 'Monitor': 10 } 
 Implement the following: 
 • Add a new product.  
 • Update the stock of an existing product.  
 • Remove a product from inventory. 
 • Display products having stock less than 20. 
 • Display the total number of items available in the inventory.
'''
#-----------------------coding-------------------------
# Initialize sample data :
inventory = {
    "Laptop": 15,
    "Mouse": 40,
    "Keyboard": 25,
    "Monitor": 10
}

# 1. Add a new product
print("--- Adding a New Product ---")
new_product = input("Enter the product name to add: ").strip()
inventory["CPU"] = 10
print(inventory)
# 2. Update the stock of an existing product
print("\n--- Updating Product Stock ---")
inventory["Mouse"] = 50
print(inventory)
# 3. Remove a product from inventory
print("\n--- Removing a Product ---")
del inventory["Keyboard"]
print(inventory)
# 4. Display products having stock less than 20
print("\n--- Products with Stock Less Than 20 ---")
for x in inventory:
    if(inventory[x] < 20):
        print(x, inventory[x])

# 5. Display the total number of items available in the inventory
print("\n--- Total Number of Items ---")
total_items = sum(inventory.values())
print(f"Total items in inventory: {total_items}")

#---------------------output---------------------