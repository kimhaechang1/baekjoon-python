import sys

s = []
n = int(sys.stdin.readline())
for i in range(n):
    s.append(int(sys.stdin.readline()))

s = sorted(s)

for i in s:
    print(i)