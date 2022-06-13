import sys
import collections

n = int(sys.stdin.readline().strip())
sl = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))

sd = collections.Counter(sl)

for num in nums:
    print(sd[num],end=" ")