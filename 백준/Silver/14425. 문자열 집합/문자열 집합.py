import sys
import collections
n, m = map(int,sys.stdin.readline().split())

s = list()
issub = list()


for i in range(n):
    s.append(sys.stdin.readline().strip())
for k in range(m):
    issub.append(sys.stdin.readline().strip())

i = collections.Counter(issub)
sum = 0

for sn in s:
    sum+=i[sn]
print(sum)