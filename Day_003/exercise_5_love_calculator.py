# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

name1_lower = name1.lower()
name2_lower = name2.lower()
names = (f"{name1_lower} {name2_lower}")
true_count = 0
love_count = 0
total = 0

#Calculate true_count
if names.count("t") > 0:
    true_count += names.count("t")
if names.count("r") > 0:
    true_count += names.count("r")
if names.count("u") > 0:
    true_count += names.count("u")
if names.count("e") > 0:
    true_count += names.count("e")

#Calculate love_count
if names.count("l") > 0:
    love_count += names.count("l")
if names.count("o") > 0:
    love_count += names.count("o")
if names.count("v") > 0:
    love_count += names.count("v")
if names.count("e") > 0:
    love_count += names.count("e")

total = (f"{true_count}{love_count}")
total_int = int(total)

if total_int < 10 or total_int > 90:
    print(f"Your score is {total_int}, you go together like coke and mentos.")
elif total_int >= 40 and total_int <= 50:
    print(f"Your score is {total_int}, you are alright together.")
else:
    print(f"Your score is {total_int}.")
