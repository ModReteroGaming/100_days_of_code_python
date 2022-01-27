# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)

days90 = int(365 * 90) 
weeks90 = int(52 * 90)
months90 = int(12 * 90)

daysage = int(365 * (age))
weeksage = int(52 * (age))
monthsage = int(12 * (age))

daysleft = days90 - daysage 
weeksleft = weeks90 - weeksage
monthsleft = months90 - monthsage

print(f"You have {daysleft} days, {weeksleft} weeks, and {monthsleft} months left.")
