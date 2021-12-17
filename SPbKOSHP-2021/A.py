nmk = [int(i) for i in input().split()]

n = nmk[0]
m = nmk[1]
k = nmk[2]

board = [["." for i in range(m)] for j in range(n)]

if k <= min(n,m):
    print("Possible")
    for i in range(min(n,m)):
        board[i][i] = "*"
    for i in board:
        for j in i:
            print(j, end = "")
        print()
else:
    print("Impossible")
