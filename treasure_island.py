print("Welcome to treasure island\nYour mission is to find the treasure.")

print(
'''
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
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************
''')

ques1 = input("You are at a crossroad. Where do you want to go? Left or Right").lower()

#ques1.lower()
if ques1=="left":
    ques2= input('You come to a lake. There is an island in the middle of the lake. Do you want to wait for a boat or swim? Type "wait" for a boat or "swim" to cross the lake.').lower()
    #   ques2.lower()
    if ques2=="wait":
        ques3= input("You arrived at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?").lower()
        #ques3.lower()
        if ques3=="red" and "blue":
            print("Game over! The room was full of monsters!")
        elif ques3=="yellow":
            print("You got your treasure! CONGRATULATION AND CELEBRATIONS!")
        else:
            print("You choose a door that does not exists! Game Over!")

    else:
        print("Game Over! You became crocodile's food!")
else:
    print("Game over! You got killed on the road!")

