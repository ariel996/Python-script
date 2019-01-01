import math
import divisiblePar

def listediviseur(a):
    a = -a if a < 0 else a
    for b in range(1, a+1):
        if divisiblePar(a,b):
            print(b,-b,end=' ')

print(listediviseur(12))