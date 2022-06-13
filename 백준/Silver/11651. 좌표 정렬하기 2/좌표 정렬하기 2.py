import sys

n = int(sys.stdin.readline())
nums = list()
numd = dict()
keys = list()

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())
    nums.append((x,y))
    numd[y]= []

for x, y in nums:
    numd[y].append(x)
keys = sorted(numd)
for key in keys:
    numd[key] = sorted(numd[key])
    for value in numd[key]:
        print(value, key)