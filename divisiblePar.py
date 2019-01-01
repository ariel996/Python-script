import math
import descenteFermat
def divisiblepar(a,b):
    q,r = descenteFermat(a,b)
    if r == 0:
        return True
    return False