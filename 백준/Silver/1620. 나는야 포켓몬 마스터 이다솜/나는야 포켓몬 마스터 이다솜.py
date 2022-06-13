import sys
import collections
n, m = map(int, sys.stdin.readline().split())

col = []
p = []
cold = collections.defaultdict(int)
result = []
for i in range(n):
    poke = sys.stdin.readline().strip()
    col.append(poke)
    cold[poke]=i+1
for i in range(m):
    p = sys.stdin.readline().strip()
    if p.isnumeric():
        result.append(col[int(p)-1])
    else:
        result.append(str(cold[p]))

for i in result:
    print(i)