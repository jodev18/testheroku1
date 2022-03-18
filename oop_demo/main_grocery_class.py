from GroceryItem import GroceryItem

grocery_list = []

continuity = input("Press letter T to proceed.")

while continuity == "T":

    choice = input("A for add, V for view, X for total, R for remove:")
    print("Choice:",choice)
    
    if choice == 'V':

        if len(grocery_list) > 0:
            for x in range(len(grocery_list)):
                print(x,grocery_list[x].get_name(),grocery_list[x].get_price())
    
    elif choice == 'A':

        name = input("Enter name: ")
        price = input("Enter price: ")

        gi = GroceryItem(name,price)
        grocery_list.append(gi)

    elif choice == 'R':

        if len(grocery_list) > 0:
            for x in range(len(grocery_list)):
                print(x,grocery_list[x].get_name(),grocery_list[x].get_price())
        
        choice = input("Choose the index of the item you want to remove. Index:")
        num_choice = int(choice)
        grocery_list.remove(grocery_list[num_choice])