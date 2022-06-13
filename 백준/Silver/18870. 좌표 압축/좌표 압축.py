import sys
n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

copy = sorted(list(set(l)))
rank = dict()

for index, value in enumerate(copy):
    rank[value] = index

for num in l:
    print(rank[num],end=" ")