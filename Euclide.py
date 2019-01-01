import math

def PGCD(a,b):
    while b != 0:
        a, b = b, a%b
    return a
print(PGCD(48,18))