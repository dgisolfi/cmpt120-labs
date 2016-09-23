#Into to programing
#Author: Daniel Gisolfi
#Date: 9/23/16
#guessing-game.py

def game():
    animalname = "dog"

    while True:
        print("I am thinking of an animal")
        guess = input("guess which animal it is: ")


        if guess == "dog":
            break
        else:
            print("sorry that is not the animal i am thinking of")
            print()
            continue
    print()
    print("congrats, you have guesssed the right animal")

game()
