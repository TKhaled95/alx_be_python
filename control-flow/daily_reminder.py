#Prompt for a Single Task:
task = input("Enter Your Task : ")
priority = input("Priority (high, medium, low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()
#Process the Task Based on Priority and Time Sensitivity:
match priority:
    case "high":
         message = f"'{task}' is a high priority task."
    case "medium":
           message = f"'{task}' is a medium priority task."
    case "low":
           message = f"'{task}' is a low priority task."
    case _:
             message = f"'{task}' has an unknown priority. Please verify."

#Provide a Customized Reminder:
if time_bound == "yes":
      message += " It requires immediate attention today!"
else:
      message += " Consider completing it at your convenience."
print ("/nReminder", message)