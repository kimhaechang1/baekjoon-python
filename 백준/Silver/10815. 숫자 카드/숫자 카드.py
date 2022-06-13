import sys
import collections
n = int(sys.stdin.readline())
sang = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
pre = list(map(int, sys.stdin.readline().split()))

result = collections.defaultdict(int)

for sn in sang:
    result[sn]=1

for p in pre:
    print(result[p],end=" ")