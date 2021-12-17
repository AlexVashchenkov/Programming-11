n = int(input())
s = input()

out = "No"

for i in range(2, n-2):
    if s[i] == "o" and s[i+2] == "r":
        out = "Yes"
    elif s[i] == "o" and s[i-2] == "r":
        out = "Yes"
    elif s[i] == "r" and s[i+2] == "o":
        out = "Yes"
    elif s[i] == "r" and s[i-2] == "o":
        out = "Yes"
for i in range(1,n-1):
    if s[i:i+2] == "or":
        out = "Yes"
    elif s[i:i+2] == "ro":
        out = "Yes"

print(out)
