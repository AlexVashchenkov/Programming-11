t = int(input())
 
output = []
 
for i in range(t):
	n = int(input())
	l = [int(i) for i in input().split(' ')]
	output.append(l[(n//2):n][::-1] + [-i for i in l[0:(n//2)][::-1]])
 
for i in output:
	for j in i:
		print(j, end = " ")
	print()
