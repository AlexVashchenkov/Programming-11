n = int(input())

def binary(l,r):
    if abs(l - r) <= 1:
        return [l,r]
    elif (((l+r)//2)*((l+r)//2)) > n:
        return binary(l, ((l+r)//2))
    else:
        return binary(((l + r) // 2), r)

def interval(r):
    if r*r > n >= (r//2)*(r//2):
        return [r // 2,r]
    else:
        return interval(r // 2)

q = interval(n)

print(binary(q[0], q[1])[0])
