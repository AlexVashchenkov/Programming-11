t = int(input())

def find_place(m, i):
    for l in m:
        for k in range(len(l)):
            if i == l[k]:
                return k

x = []
for j in range(t):
    nm = input().split(' ')
    n = int(nm[0])
    m = int(nm[1])
    some_strings = [[int(i) for i in input().split(' ')] for k in range(n)]
    some_columns = [[int(i) for i in input().split(' ')] for q in range(m)]
    output = [0 for i in range(n)]
    for i in range(len(some_strings)):
        output[i] = some_strings[find_place(some_columns, some_strings[i][0])]
    x += output

for l in x:
    print(l)

'''
2
2 3
6 5 4
1 2 3
1 6
2 5
3 4
3 1
2
3
1
3 1 2
'''
