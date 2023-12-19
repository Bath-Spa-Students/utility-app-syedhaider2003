# ASCII art representing the name of the application
print("""
██╗░░░██╗███████╗███╗░░██╗██████╗░██╗███╗░░██╗░██████╗░  ███╗░░░███╗░█████╗░░█████╗░██╗░░██╗██╗███╗░░██╗███████╗
██║░░░██║██╔════╝████╗░██║██╔══██╗██║████╗░██║██╔════╝░  ████╗░████║██╔══██╗██╔══██╗██║░░██║██║████╗░██║██╔════╝
╚██╗░██╔╝█████╗░░██╔██╗██║██║░░██║██║██╔██╗██║██║░░██╗░  ██╔████╔██║███████║██║░░╚═╝███████║██║██╔██╗██║█████╗░░
░╚████╔╝░██╔══╝░░██║╚████║██║░░██║██║██║╚████║██║░░╚██╗  ██║╚██╔╝██║██╔══██║██║░░██╗██╔══██║██║██║╚████║██╔══╝░░
░░╚██╔╝░░███████╗██║░╚███║██████╔╝██║██║░╚███║╚██████╔╝  ██║░╚═╝░██║██║░░██║╚█████╔╝██║░░██║██║██║░╚███║███████╗
░░░╚═╝░░░╚══════╝╚═╝░░╚══╝╚═════╝░╚═╝╚═╝░░╚══╝░╚═════╝░  ╚═╝░░░░░╚═╝╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═╝╚═╝░░╚══╝╚══════╝""")

# Vending Machine class
class VendingMachine:
    def __init__(self):
        # Predefined items in the vending machine with name, price, and quantity
        self.items = {
            '1': {'name': 'Soda', 'price': 1.50, 'quantity': 10},
            '2': {'name': 'Chips', 'price': 1.00, 'quantity': 8},
            '3': {'name': 'Candy', 'price': 0.75, 'quantity': 15}
        }
        self.balance = 0  # Initializing balance to zero

    # Displays available items with their details
    def display_items(self):
        print("Available items:")
        for code, item in self.items.items():
            print(f"{code}. {item['name']} - ${item['price']:.2f} - Quantity: {item['quantity']}")

    # Allows users to insert money into the vending machine
    def insert_money(self, amount):
        self.balance += amount
        print(f"Inserted: ${amount:.2f}, Total Balance: ${self.balance:.2f}")

    # Handles the purchase of an item by users
    def purchase_item(self, item_code):
        if item_code in self.items:
            item = self.items[item_code]
            if item['quantity'] > 0 and self.balance >= item['price']:
                self.balance -= item['price']
                item['quantity'] -= 1
                print(f"Purchased {item['name']} for ${item['price']:.2f}. Remaining Balance: ${self.balance:.2f}")
            else:
                print("Insufficient balance or item out of stock.")
        else:
            print("Invalid item code.")

    # Returns any remaining balance to the user
    def return_change(self):
        if self.balance > 0:
            print(f"Returning change: ${self.balance:.2f}")
            self.balance = 0

# Main function to run the vending machine program
def main():
    vending_machine = VendingMachine()  # Initialize the vending machine

    while True:
        # Display options for user interaction
        print("\nOptions:")
        print("1. Display Items")
        print("2. Insert Money")
        print("3. Purchase Item")
        print("4. Return Change")
        print("5. Exit")

        choice = input("Enter your choice: ")  # Get user choice

        # Perform actions based on user choice
        if choice == '1':
            vending_machine.display_items()
        elif choice == '2':
            amount = float(input("Enter the amount to insert: $"))
            vending_machine.insert_money(amount)
        elif choice == '3':
            item_code = input("Enter the item code: ")
            vending_machine.purchase_item(item_code)
        elif choice == '4':
            vending_machine.return_change()
        elif choice == '5':
            break  # Exit the program if the user chooses to exit
        else:
            print("Invalid choice. Please try again.")  # Display for invalid choices

if __name__ == "__main__":
    main()  # Run the main function if this script is executed
