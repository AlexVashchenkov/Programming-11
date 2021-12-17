ab = [int(i) for i in input().split()]
 
a = ab[0]
b = ab[1]
 
if b > a:
    print(min(b, a) + 1)
else:
    print(min(b, a))
