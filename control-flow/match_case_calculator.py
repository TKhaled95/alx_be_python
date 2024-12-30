#Ask the user to input two numbers (one at a time) using
num1 = float(input("Please Enter the first number: "))
num2 = float(input("Please Enter the second number: "))
#Ask for the type of operation they’d like to perform
operation= input("Choose the operation (+, -, *, /): ")
#Perform the Calculation Using Match Case:
match operation:
    case "+":
        result = num1 + num2
        print(f"The result is {result}")
    case "-":
        result = num1 - num2
        print(f"The result is {result}")
    case "*":
        result = num1 * num2
        print(f"The result is {result}")
    case "/":
        if result !=0:
            result = num1 / num2
            print(f"The result is {result}")
        else:
             print("Cannot divide by zero.")
    case _:
         print("Cannot divide by zero.")