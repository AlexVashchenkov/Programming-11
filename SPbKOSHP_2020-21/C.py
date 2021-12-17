kn = [int(i) for i in input().split()]
 
k = kn[0]
n = kn[1]
 
moves = [int(i) for i in input().split()]
 
rounds = 0
score = n
 
for i in range(len(moves)):
    if i == len(moves) - 1 and score == moves[i]:
        score = 0
        rounds += 1
    if score > moves[i]:
        score -= moves[i]
    elif score == moves[i]:
        score = n
        rounds += 1
 
 
print(rounds)
print(score)
