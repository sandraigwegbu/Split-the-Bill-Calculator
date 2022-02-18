#TIP CALCULATOR
#This program calculates the amount each person should pay when a tip is applied to the bill

#Welcome note
print("Welcome to the tip calculator.")

#user inputs, define variables
bill = float(input("What was the total bill? £"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))

#Calculate the total payment, including tip
tip_amount = bill * (tip/100)
total_payment = bill + tip_amount

#Split total payment between people
bill_per_person = total_payment / people

#Final result
result = round(bill_per_person,2) # decimal format issue
result = "{:.2f}".format(bill_per_person) #decimal format resolved

print(f"Each person should pay: £{result}")