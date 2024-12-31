#Prompt User for Pattern Size:
size = int(input("Enter the size of the pattern: "))
# Initialize the row counter
row = 0
# Outer loop (while loop) to iterate through each row
while row < size:
    # Inner loop (for loop) to print the stars (*) for the current row
    for _ in range(size):
        print ("*", end="")    # Print stars on the same line
print()                        # Move to the next line after printing a row
row += 1                       # Increment the row counter