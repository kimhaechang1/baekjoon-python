import sys

result = []
t = int(sys.stdin.readline().strip())

for i in range(t):
    x1, y1, r1, x2,y2,r2 = map(int, sys.stdin.readline().split())
    d = ((abs(x2-x1))**2 + (abs(y2-y1))**2)**(1/2)
    if d == 0 and r1 == r2:
        result.append(-1)
    elif r1+r2 == d or d+r2 == r1 or d+r1 == r2:
        result.append(1)
    elif r1+r2 > d > abs(r1 - r2):
        result.append(2)
    else:
        result.append(0)

for i in result:
    print(i)
