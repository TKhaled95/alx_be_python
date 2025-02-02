from datetime import datetime, timedelta

def display_current_datetime():
    """Displays the current date and time in a readable format."""
    # Get the current date and time
    current_date = datetime.now()
    
    # Format the current date and time in "YYYY-MM-DD HH:MM:SS" format
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """Calculates a future date after adding a specified number of days."""
    # Prompt the user to enter a number of days
    days_to_add = int(input("Enter the number of days to add to the current date: "))
    
    # Calculate the future date by adding the number of days
    current_date = datetime.now()
    future_date = current_date + timedelta(days=days_to_add)
    
    # Print the future date in "YYYY-MM-DD" format
    print("Future date:", future_date.strftime("%Y-%m-%d"))

def main():
    # Display the current date and time
    display_current_datetime()
    
    # Calculate and display the future date
    calculate_future_date()

if __name__ == "__main__":
    main()
