#Mini Project
#Guess the number - Apna College
# The idea is to set a target and user have to guess the number
#if the number is too bigger, we will suggest them to think smaller nd vice-versa

import random

target = random.randint(1,100)

while True :
    user_choice = input("Guess the target or Quit(Q) : ")
    if (user_choice == "Q") :
        print("User Quitted")
        break

    user_choice = int(user_choice)
    if (user_choice == target) :
        print("Success : Correct Guess")
        break
    if (user_choice < target) :
        print("Guess something bigger....")
    if (user_choice > target) :
        print("Guess something smaller....")
print("----GAME OVER----")

