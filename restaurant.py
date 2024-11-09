def restaurant():
    # Predefined menu with items and their prices
    menu = {
        "Pizza": 8.50,
        "Burger": 5.00,
        "Pasta": 7.00,
        "Salad": 4.50,
        "Soda": 1.50
    }

    # Initialize the total cost to 0
    total_cost = 0

    print("Welcome to the restaurant!")
    print("Here is the menu:")
    
    # Display the menu
    for item, price in menu.items():
        print(f"{item}: £{price:.2f}")
    
    # Start the ordering loop
    while True:
        # Ask the user to enter an item they want to order
        order = input("Please enter your order (or press Enter to finish): ").strip().lower()
        
        # If the user presses Enter without typing anything, stop the loop
        if order == "":
            break
        
        # Check if the order is on the menu (case insensitive)
        # Convert both the menu items and input to lowercase for case-insensitive comparison
        matched_items = [item for item in menu if item.lower() == order]
        
        if matched_items:
            item = matched_items[0]  # Get the matched item (since we are doing a case-insensitive match)
            item_price = menu[item]
            total_cost += item_price
            print(f"Added {item} to your order. Price: £{item_price:.2f}")
            print(f"Your current total is: £{total_cost:.2f}")
        else:
            print(f"Sorry, '{order}' is not on the menu.")
    
    # Display the final total
    print(f"Your total cost is: £{total_cost:.2f}")
    print("Thank you for your order!")

# Call the restaurant function to run the program
restaurant()


