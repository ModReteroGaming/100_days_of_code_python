print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
choice1 = input("Do you want to look for the treasure? YES or NO?: ")
choice1 = choice1.upper()
if choice1 == 'YES':
  choice2 = input("\nYou chose to continue on with the quest for the treasure!\nYou have come to a fork in the road. Do you want to go LEFT or RIGHT?: ")
  choice2 = choice2.upper()

  if choice2 == "LEFT":
    choice3 = input(f"\nYou chose to go {choice2}.\nYou are now in front of a lake and see and island in the middle of it.\nYou can either wait for a boat or swim across to the island.\nDo you want to SWIM or WAIT: ")
    choice3 = choice3.upper() 

    if choice3 == "WAIT":
      choice4 = input(f"\nYou chose to {choice3}.\nYour patience has paid off and you safely made it to the island.\nYou now see a building with 3 doors.\nThe one on the left is red, the one in the middle is yellow, and the one on the right is blue.\nWhich door do you choose? RED, YELLOW, or BLUE?: ")
      choice4 = choice4.upper()
      
      if choice4 == "YELLOW":
        print(f"\nYou have chosen the {choice4} door.\nThe treasure is behind this door and you are now richer than your wildest dreams!\nYOU HAVE WON TREASURE ISLAND!")
      elif choice4 == "BLUE":
        print(f"\nYou chose the {choice4} door.\nThere was a bomb waiting behind it and you have been blown to bits.\nGAME OVER!!!")
      elif choice4 == "RED":
        print(f"\nYou chose the {choice4} door.\nThere was a giant monster waiting behind the door and he has beaten you to death.\nGAME OVER!!!")

    else:
      print(f"\nYou chose {choice3}.\nThe waters are filled with man eating sharks and you were eaten alive!\nGAME OVER!!!")

  else:
    print(f"\nYou chose to go {choice2}.\nYou fell into a pit with spikes and have died.\nGAME OVER!!!")

else:
  print("\nNO?!?! Well then, we will wait for a more brave soul to seek the treasure.\nGAME OVER!!!")
