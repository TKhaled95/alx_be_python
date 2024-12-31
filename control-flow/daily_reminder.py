#Prompt for a Single Task:
Task = input("Enter Your Task : ")
Priority = input("Priority (high, medium, low): ").lower()
Time_Bound = input("Is it time-bound? (yes/no): ").lower()
#Process the Task Based on Priority and Time Sensitivity:
match Priority:
    case "high":
         message = f"'{Task}' is a high priority task."
    case "medium":
           message = f"'{Task}' is a medium priority task."
    case "low":
           message = f"'{Task}' is a low priority task."
    case _:
             message = f"'{Task}' has an unknown priority. Please verify."

#Provide a Customized Reminder:
if Time_Bound == "yes":
      message += " It requires immediate attention today!"
else:
      message += " Consider completing it at your convenience."
print ("/nReminder", message)