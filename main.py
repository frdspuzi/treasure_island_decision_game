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

choice1= input('You\'re at a crossroad. Where do you want to go? Type "left" or "right"\n')

if (choice1 == "Left" or choice1 == "left"):

	choice2= input("You\'ve come to a lake. There is an island in the middle of the lake. Type \"wait\" to wait for a boat. Type \"swim\" to swim across.")

	if (choice2 == "Wait" or choice2 == "wait"):
		choice3= input('''
		
\nYou arrive at the island unharmed. There is a house with 3 doors. 
		
Red, 
Yellow,  
Blue. 
		
Which colour do you choose?\n''')

		if (choice3 == "Yellow" or choice3 == "yellow"):
			ans= input("\nYou found the treasure! You Win!\n")

		elif(choice3 == "Red" or choice3 == "red"):
			print("\nYou enter a room of beasts. Game Over.\n")

		elif(choice3 == "Blue" or choice3 == "blue"):
			print("\nYou enter a room of beasts. Game Over.\n")

		else:
			print("\nYou chose a door that doesn't exist. Game Over.\n")

	else:
		print("\nYou get attacked by an angry trout. Game Over.\n")

else:
	print("\nYou fell into a hole. Game Over.\n")
