#Into to programing
#Author: Daniel Gisolfi
#Date: 9/23/16
#guessing-game.py

def game():
    animalname = "dog"

    while True:
        print("I am thinking of an animal")
        guess = input("guess which animal it is: ")
        guess = guess.lower()


        if guess == "dog":
            print()
            print("congrats, you have guesssed the right animal")
            break
        elif guess == "quit":
            print("quitting")
            break
        else:
            print("sorry that is not the animal i am thinking of")
            print()
            continue
    

game() 
