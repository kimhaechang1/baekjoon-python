import sys

n = int(sys.stdin.readline().strip())
nums=list()
numd = dict()
for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    nums.append((x,y))
    numd[x] = []
for x, y in nums:
    numd[x].append(y)
keys = sorted(numd)
for key in keys:
    numd[key]=sorted(numd[key])
    for value in numd[key]:
        print(key, value)