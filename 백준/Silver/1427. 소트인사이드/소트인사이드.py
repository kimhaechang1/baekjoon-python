import sys

n = sys.stdin.readline().strip()
l = list(n)
l = sorted(l, key=lambda x: int(x), reverse=True)
print("".join(l))