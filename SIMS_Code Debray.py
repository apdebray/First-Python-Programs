import datetime

# Initialize the product catalog, I envisioned this being a sort of Apple product sales platform 
product_catalog = {
    'P1': {'Name': 'iphone_16', 'Price': 1500, 'Stock': 100, 'Units Sold': 0},
    'P2': {'Name': 'ipad_pro', 'Price': 2000, 'Stock': 50, 'Units Sold': 0},
    'P3': {'Name': 'macbook_air', 'Price': 1200, 'Stock': 10, 'Units Sold': 0},
    'P4': {'Name': 'airpods_gen2', 'Price': 130, 'Stock': 30, 'Units Sold': 0},
    'P5': {'Name': 'airpods_pro', 'Price': 220, 'Stock': 200, 'Units Sold': 0},
}

sales_history = []

# Function to display the catalog of the 5 electronic devices 
def view_catalog():
    print("\nProduct Catalog:")
    for product_id, details in product_catalog.items():
        print(f"Product ID: {product_id}")
        print(f"Name: {details['Name']}")
        print(f"Price: ${details['Price']}")
        print(f"Current stock quantity: {details['Stock']}")
        print("-" * 40)

# Function to make a sale
def make_sale():
    view_catalog()  # Show the catalog first
    print('Which product would you like to purchase? (Enter Product ID or Name)')
    answer = input()  # Capture user's product choice
    print('How many units would you like to purchase?')
    units_sold = int(input())

    # Find the product in the catalog by ID or name
    for product_id, details in product_catalog.items():
        if answer == product_id or answer == details['Name']:  # Match by ID or Name
            # Check if enough stock is available
            if details['Stock'] >= units_sold:
                # This is to update the stock 
                details['Stock'] -= units_sold 
                total_price = details['Price'] * units_sold 
                
                details['Units Sold'] += units_sold
                
                # Record the sale with a unique Sale ID
                sale_id = len(sales_history) + 1  # Incremental sale ID
                sale_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # Current date and time, had to google this function 
                
                # Creating a sale dictionary for record keeping
                sale_record = {
                    'Sale ID': sale_id,
                    'Date and Time': sale_time,
                    'Product ID': product_id,
                    'Quantity sold': units_sold,
                    'Total Sale Amount': total_price
                }
                
                # Append the sale record to sales history
                sales_history.append(sale_record)
                
                # Output of all of the sale information when the dictionary is called
                print(f'Sale ID: {sale_id}')
                print(f'Date and Time: {sale_time}')
                print(f'For {units_sold} unit(s) of {details["Name"]}, your total is: ${total_price}')
                print(f'Updated stock for {details["Name"]}: {details["Stock"]}')
                return
            else:
                print(f"Not enough stock available. Only {details['Stock']} units left.")
                return

    # If no valid product is found
    print('Not a valid input, please type an option from the catalog.')

#Top Seller function
def top_seller():
    if not sales_history:
        print('No sales have been made as of now!')
        return
    top_seller_id = max(product_catalog, key= lambda product_id: product_catalog[product_id]['Units Sold'])
    top_seller = product_catalog[top_seller_id]
    print("The Top SELLER is...")
    print(top_seller)

#Total Sales Revenue Function
def total_salesrev():
    if not sales_history:
        print('We not sold nothing yet. No money, no records...')
        return

    total_sales_revenue = sum(sale['Total Sale Amount'] for sale in sales_history)  
    print('The Total Sales Revenue is...')
    print(f"${total_sales_revenue}")  # Display the total sales revenue

# Individual Product Revenue
def product_rev():
    if not sales_history:
        print('Sadly... Noooo sales have been made, sooo a history could not be generated.')
        return
    
    # Initialize a dictionary to hold total revenue per product
    product_revenue = {}

    # Loop through the sales history and accumulate revenue for each product
    for sale in sales_history:
        product_id = sale['Product ID']
        total_sale_amount = sale['Total Sale Amount']

        # Add the sale amount to the respective product's revenue
        if product_id in product_revenue:
            product_revenue[product_id] += total_sale_amount
        else:
            product_revenue[product_id] = total_sale_amount

    # Display revenue for each product
    for product_id, revenue in product_revenue.items():
        product_name = product_catalog[product_id]['Name']
        print(f'For {product_name}, your total revenue is: ${revenue:.2f}')

# Updating Product Price/Quantity
def product_update():
    print("Which product would you like to update? (Enter Product ID or Name)")
    updated_id = input() 

    # Find the product in the catalog by ID or Name
    for product_id, details in product_catalog.items():
        if updated_id == product_id or updated_id == details['Name']:
            print("Update price or quantity?")
            update_focus = input("Enter 'Price' or 'Quantity': ").strip().lower()  # Case-insensitive check from the strip and lower functions

            # Update the price
            if update_focus == 'price':
                new_price = float(input(f"Enter the new price for {details['Name']}: "))
                details['Price'] = new_price  # Update the price
                print(f"Price for {details['Name']} has been updated to ${new_price:.2f}.")

            # Update the quantity (stock)
            elif update_focus == 'quantity':
                new_quantity = int(input(f"Enter the new stock quantity for {details['Name']}: "))
                details['Stock'] = new_quantity  # Update the stock quantity
                print(f"Stock quantity for {details['Name']} has been updated to {new_quantity} units.")

            else:
                print("Invalid option. Please choose 'Price' or 'Quantity'.")
            
            return

    print("Product not found. Please enter a valid Product ID or Name.")

# Main loop for the program
def main():
    while True:
        print("\nMain Menu:")
        print("1. View Catalog")
        print("2. Make a Sale")
        print("3. View Sales History")
        print("4. View Top Seller")
        print("5. View Total Sales Revenue")
        print("6. View Individual Product Sales Revenue")
        print("7. Update Product Price or Quantity")
        print("8. Exit")
        choice = input("Choose an option (1-8): ")
        
        #Main menu options are coded below
        if choice == '1':
            view_catalog()
        elif choice == '2':
            make_sale()
        elif choice == '3':
            print("\nSales History:")
            for sale in sales_history:
                print(sale)
        elif choice == '4':
            top_seller()
        elif choice == '5':    
            total_salesrev()
        elif choice == '6':   
            product_rev()     
        elif choice == '7':
            product_update()
        elif choice == '8':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice, please select a valid option.")

# Start the program
main()