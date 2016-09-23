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
        firstletter = guess
        firstletter = firstletter[0]
        
        
        if firstletter == "q":
            print("quitting")
            break
        elif guess == "dog":
            print()
            print("congrats, you have guesssed the right animal")
            like = input("do you like this animal, type Y for N: ")
            print()
            like = like.lower()
            if like == "y":
                print("Nice, I ike that one to")
            elif like == "n":
                print("Darn, I like that one")
            else:
                print("sorry that is not a valid response")
                continue
            break           
        else:
            print("sorry that is not the animal i am thinking of")
            print()
            continue
    

game() 

