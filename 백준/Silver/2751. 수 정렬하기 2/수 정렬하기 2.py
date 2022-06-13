import sys
import heapq

n = int(sys.stdin.readline())
h = []
result = []
for i in range(n):
    heapq.heappush(h, int(sys.stdin.readline()))

for i in range(n):
    print(heapq.heappop(h))