n = int(input())

values = [0, 1, 3, 8, 24, 15, 4, 2, -8]


def root(values,x):
    l = 0
    r = len(values)
    while (r-l) > 1:
        m = (r + l) // 2
        if values[m] > x:
            r = m
        else:
            l = m
    if values[l] == x:
        return l
    else:
        return -1

values = [1, 3 ,5 ,7, 11, 13, 17, 19]

for i in range(20):
    print(i, root(values, i))

print(root(values, 1))
