#Into to programing
#Author: Daniel Gisolfi
#Date: 9/30/16
#Credentials.py

firstN = input("Enter your first name: \n")
lastN = input("Enter your last name: \n")

def username(first,last):
    first = firstN.capitalize()
    last = lastN.capitalize()
    username = (first + "." + last +"1")
    return username

makeuser = username(firstN, lastN)
print("Your Username is: "+makeuser)

while True:
    passkey = input("enter a strong password: \n")

    def checkupcase(passkey):
        if any(c.isupper() for c in pw):
            return True
        
    def checklowercase(pw):
        return any(c.islower() for c in pw)
    def checkdigit(pw):
        return any(x.lower() for x in pw)

    if len(passkey) >= 8:
        print("true")
    if checkupcase == True:
        print("it contains an upercase")
  
    else:
        print("that password is too short, it must be 8 characters or longer")
        continue
