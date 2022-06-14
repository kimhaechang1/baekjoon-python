import sys
import copy
nums = list()
for _ in range(3):
    nums.append(tuple(map(int, sys.stdin.readline().split())))

nums = sorted(nums, key=lambda x : (x[0],x[1]))
temp = copy.deepcopy(nums)
dx, dy = 0,0
for xy in temp:
    x, y = xy
    x, y = x - temp[0][0], y - temp[0][1]
    if x == 0 and y>0:
        dy = y
    elif y == 0 and x > 0:
        dx = x
    else:
        dx, dy = x, y
nums = set(nums)
result = set()
result.add((temp[0][0],temp[0][1]))
result.add((temp[0][0]+dx,temp[0][1]))
result.add((temp[0][0],temp[0][1]+dy))
result.add((temp[0][0]+dx,temp[0][1]+dy))
r = result -nums

for i in r:
    x, y = i
    print(x, y)