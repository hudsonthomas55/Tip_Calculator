    #Welcome and header of the project
print("Welcome to the tip calculator.")

    #Input total bill
total_bill = input("What is the total bill amount? \n$")
    #What percentage tip would you like to give? 10, 12, 15, or 20?
percentage_tip = input("What percentage tip would you like to give? (Do not include %) \n")
#How many people to split bill with
people = input("How many people would you like to split the bill with? \n")

    #Convert all data types to floats
total_bill_float = float(total_bill)
people_float = float(people)
percentage_tip_float = float(percentage_tip)

    #Calculating tip
total = round(total_bill_float + (total_bill_float * (percentage_tip_float/100)),2)
each_person = round(total/people_float, 2)

    #What each person should pay
message = (f"The bill total is ${total} and each person should pay: ${each_person}")
print(message)