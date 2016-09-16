#Into to programing
#Author: Daniel Gisolfi
#Date: 9/16/16
#Fibonacci.py

def main():
    n = int(input("What does n equal: "))
    a, b = 1, 1
    for i in range(n-2):
        a, b = a+b, a
    print("The fibonacci number is", a)

main()
