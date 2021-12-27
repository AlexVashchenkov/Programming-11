from math import *

a = int(input())
b = int(input())

def aborygene(n):
    if n % 10 == 0:
        return -1
    else:
        return int(str(n)[::-1])

count = 0

for i in range(a, int(sqrt(b))+1):
    if i % 10 != 0:
        if i == int(sqrt(aborygene(i**2)) - (sqrt(aborygene(i**2)) % 1)) or i == aborygene(int(sqrt(aborygene(i**2)) - (sqrt(aborygene(i**2)) % 1))):
            #print(i)
            count += 1

print(count)
