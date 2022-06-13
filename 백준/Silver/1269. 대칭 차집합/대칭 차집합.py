import sys
n, m = map(int, sys.stdin.readline().split())
s1 = set(map(int, sys.stdin.readline().split()))
s2 = set(map(int, sys.stdin.readline().split()))

c = len(s2-s1)+len(s1-s2)
print(c)