#Into to programing
#Author: Daniel Gisolfi
#Date: 9/16/16
#pi.py

import math

def main():
    n = int(input("What does n equal: "))

    total = 0
    sgn = 1.0   # used to alternate sign of terms
    for denom in range(1, 2*n, 2):
        total = total + sgn * 4.0/denom
        sgn = -sgn #flip the sign

    print("Approx to pi is:", total)

main()
        
