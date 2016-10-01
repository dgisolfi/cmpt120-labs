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
        if any(c.isupper() for c in passkey):
            return True
        
    def checklowercase(passkey):
        if any(c.islower() for c in passkey):
            return True
        
    def checkdigit(passkey):
        if any(x.lower() for x in passkey):
            return True

    upper = checkupcase(passkey)
    lower = checklowercase(passkey)
    digit = checkdigit(passkey)

    if len(passkey) >= 8:
        length = True

    if upper == True and lower== True and digit == True and length == True:
        print("your password is strong")
        break
    else:
        print("Your password is to weak, add numbers, Capitilize letters \nand make it longer to make your pass word stronger")
        continue
