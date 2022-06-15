import sys

n = int(sys.stdin.readline().strip())
t = []
for i in range(6):
    d, l = map(int, sys.stdin.readline().split())
    t.append(l)
big = 0
small = 0
idx = 0
for i in range(6):
    tmp = t[i]*t[(i+1)%6]
    if big < tmp:
        big = tmp
        idx = i

small = t[(idx+3)%6]*t[(idx+4)%6]

print(n*(big-small))