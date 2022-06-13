import sys

n, m = map(int, sys.stdin.readline().split())

d = set()
b = set()
for i in range(n):
    d.add(sys.stdin.readline().strip())
for i in range(m):
    b.add(sys.stdin.readline().strip())
inter = sorted(d.intersection(b))
print(len(inter))
for k in inter:
    print(k)