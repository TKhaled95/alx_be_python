import os

def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def check_file_exists_and_not_empty(filename):
    """Check if a file exists and is not empty."""
    if os.path.exists(filename):
        if os.stat(filename).st_size > 0:
            return True
        else:
            print(f"{filename} exists but is empty.")
            return False
    else:
        print(f"{filename} does not exist.")
        return False

def main():
    shopping_list = []  # Implementation of shopping_list array

    # Check if shopping_list.txt exists and is not empty
    if check_file_exists_and_not_empty('shopping_list.txt'):
        # Here you could load data from the file if necessary
        pass
    
    while True:
        display_menu()  # Calling display_menu function
        choice = input("Enter your choice (1-4): ")
        
        # Check if the input choice is a valid number
        if choice.isdigit():
            choice = int(choice)
            
            if choice == 1:
                # Prompt for and add an item
                item = input("Enter the item to add: ")
                shopping_list.append(item)
                print(f"'{item}' has been added to your shopping list.")
            
            elif choice == 2:
                # Prompt for and remove an item
                item = input("Enter the item to remove: ")
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f"'{item}' has been removed from your shopping list.")
                else:
                    print(f"'{item}' not found in the shopping list.")
            
            elif choice == 3:
                # Display the shopping list
                if shopping_list:
                    print("\nYour Shopping List:")
                    for index, item in enumerate(shopping_list, start=1):
                        print(f"{index}. {item}")
                else:
                    print("Your shopping list is empty.")
            
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please choose a number between 1 and 4.")
        else:
            print("Invalid input. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()

