xt = [int(i) for i in input().split()]

x = xt[0]
t = xt[1]

def work(sleepTime):
    if 0 <= sleepTime < t/6:
        return (t - sleepTime) * ((x * sleepTime) / (t / 6))
    elif t/6 <= sleepTime <= t/3:
        return (t - sleepTime) * (100 - ((100 - x) * (t/3 - sleepTime) / (t / 6)))
    else:
        return (t - sleepTime) * 100

if x == 100:
    print(work(t/6))
else:
    print(max(work(t/6), work((2*t/3) - (25 * t) / (3 * (100 - x))), work(t/3)))

