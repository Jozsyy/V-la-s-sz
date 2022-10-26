import math

def prim_function(a):
    if a<=1 or (a%2==0 and a!=2):
        return False
    for x in range(3,a,2): #optimized the 2nd argument:math.sqrt(a)+1
        if a%x==0:
            return False
    return True

for x in range (1000):
    if prim_function(x):
        print(x, end=" ")