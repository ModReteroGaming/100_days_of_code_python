#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = input("Welcome to the tip calculator.\nWhat was the total bill? $")
tip = input("What percentage of tip would you like to give? 10, 12, 15, or 20? ")
people = input("How many people to split the bill? ")

bill = float(bill)
tip = float(tip)
tip_decimal = tip / 100 + 1
#tip_total = float(tip * bill / 100)
people = int(people)
total_with_tip = round(bill * tip_decimal, 2)
#total_each = round(total_with_tip / people, 2)

#To get a definite 2 decimals for the total_each variable, do as follows
#Better than what I had before which is commented out
total_each = "{:.2f}".format(total_with_tip / people)
tip_total = "{:.2f}".format(tip * bill / 100)

#I went an extra step to show tip amount, as that's a line item to fill out on the bill.
print(f"Tip Amount is: ${tip_total}")
print(f"Total Amount to pay: ${total_with_tip}")
print(f"Each person should pay: ${total_each}")
