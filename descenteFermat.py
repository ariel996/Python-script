import math
def fermat(a,b):
    q, r=0, a
    while r >= b:
        q += 1
        r -= b
    while r < 0:
        q -= 1
        r += b
    return q,r
print(fermat(78,12))