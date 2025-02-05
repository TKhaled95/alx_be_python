# Define global conversion factors with the exact format
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9


# Function to convert Fahrenheit to Celsius
def fahrenheit_to_celsius(fahrenheit):
    """Converts temperature from Fahrenheit to Celsius using the global conversion factor."""
    celsius = (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR
    return celsius

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    """Converts temperature from Celsius to Fahrenheit using the global conversion factor."""
    fahrenheit = (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32
    return fahrenheit

# Main function to interact with the user
def main():
    try:
        # Prompt the user for the temperature value
        temperature = float(input("Enter the temperature to convert: "))
        
        # Prompt the user to specify whether the temperature is in Celsius or Fahrenheit
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()
        
        # Convert the temperature based on the user input
        if unit == 'C':
            # If the input temperature is in Celsius, convert to Fahrenheit
            fahrenheit = convert_to_fahrenheit(temperature)
            print(f"{temperature}°C is {fahrenheit}°F")
        
        elif unit == 'F':
            # If the input temperature is in Fahrenheit, convert to Celsius
            celsius = convert_to_celsius(temperature)
            print(f"{temperature}°F is {celsius}°C")
        
        else:
            # Handle invalid unit input
            print("Invalid input. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        # Handle non-numeric input
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()

